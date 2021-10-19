from easy_food_online import functions as f


class EasyFood:

    def order_food(self):
        food_price_dict = {
            "biriyani": 120, "veg-pizza": 90, "nonveg-pizza": 120, "meals": 100
        }
        user_name = []
        foods = 1
        flag = True
        try:
            while flag:
                name = input("Enter your username: ")
                if all(x.isalpha() or x.isspace() for x in name):
                    user_name.append(name)
                    print("Welcome %s!" % name)
                    flag = False
                else:
                    print("Enter correct Username and try again")

            if not flag:
                print("See the Food Details below:")
                for key, value in food_price_dict.items():
                    print("{} : Rs.{}".format(key, value))

                ordered_food_name = []
                ordered_quantity = []
                new_flag = True
                while new_flag:
                    food = input("Order food\nEnter a food name: ")
                    if food.lower() in food_price_dict:
                        print("Food is available")
                        ordered_food_name.append(food)
                        qty_flag = True
                        while qty_flag:
                            qty = int(input("Enter a Quantity: "))
                            if qty > 0:
                                ordered_quantity.append(qty)
                                qty_flag = False
                            else:
                                print("Enter correct quantity")
                                continue

                        need_more = input("To add more type Y for Yes or N for No: ")
                        if need_more.lower().strip() == "y":
                            continue
                        else:
                            new_flag = False
                    else:
                        print("Food is not Available or check spelling and try again")
                        continue

                # calling Functions
                total_amount = f.calculate_bill(food_price_dict, ordered_food_name,
                                                ordered_quantity)  # calling bill method
                # discount method
                if total_amount > 299:
                    total_amount -= int(total_amount * 0.1)  # For 10% Discount

                # for creating ID
                ids = f.generate_order_id()

                fl = open("order_details.txt", "a")

                net_items = f.ordered_items
                before_val = ""
                length = 1
                for key, value in net_items.items():
                    final = f"{key}:food{foods}#{value}"
                    foods += 1
                    before_val += final

                    if length < len(net_items):
                        before_val += ","
                        length += 1
                order_details = f'\n{ids}:{user_name[0]}:{before_val}:{total_amount}'
                print(f'{ids}:{user_name[0]}:{before_val}:{total_amount}')
                fl.write(order_details)
                fl.close()
        except RuntimeError as r:
            print("some error", r)
        except ZeroDivisionError as z:
            print("Number not divided by Zero", z)
        except ValueError as v:
            print("Check the type of data", v)
        except IndexError as i:
            print("Index out of range", i)
        except Exception as e:
            print(e)
        finally:
            pass


food = EasyFood()
food.order_food()
