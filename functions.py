last_id = 0
ordered_items = ""
final_id = ""


def generate_order_id():
    last_line = 0
    file = open("order_details.txt", "r")
    for last_line in file:
        pass
    last_ln = str(last_line)
    globals()['last_id'] = int(last_ln[1:4])
    globals()['last_id'] += 1
    globals()["final_id"] = "O{}".format(globals()['last_id'])
    file.close()

    return globals()["final_id"]


def calculate_bill(food_price, food_list, quantity_list):
    ordered_item = {food_list[i]: quantity_list[i] for i in range(len(food_list))}
    # print(ordered_item)
    globals()["ordered_items"] = ordered_item
    bill_amount = 0
    for key, value in ordered_item.items():
        if key in food_price:
            amount = food_price[key]
            bill_amount += amount * value

    return bill_amount
