
def generate_sales_order_str(num:int) -> str:
    no = "SO"

    str_num = str(num)
    digits = len(str_num)

    for i in range(0,20-digits):
        no += "0"

    for i in range(0, digits):
        no += str_num[i]

    return no
