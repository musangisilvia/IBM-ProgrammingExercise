import math

# test input
Baskets = {
    1:[{
        
        "qty": 1,
        "prod": "book",
        "price": 12.49
    },{
        
        "qty": 1,
        "prod": "music CD",
        "price": 14.99
    },{
        
        "qty": 1,
        "prod": "chocolate bar",
        "price": 0.85
    }],
    2: [{
        "qty": 1,
        "prod": "imported box of chocolates",
        "price": 10.00
    }, {
        "qty": 1,
        "prod": "imported bottle of perfume",
        "price": 47.50
    }],
    3: [{
        "qty": 1,
        "prod": "imported bottle of perfume",
        "price": 27.99
    },{
        "qty": 1,
        "prod": "bottle of perfume",
        "price": 18.99
    },{
        "qty": 1,
        "prod": "packet of headache pills",
        "price": 9.75
    },{
        "qty": 1,
        "prod": "box of imported chocolates",
        "price": 11.25
    }]
}

def round_nearest(num):
    return math.ceil(num * 100) / 100

def exclude_items(item):
    excluded = ['book', 'chocolate', 'headache pills']
    return any(it in item for it in excluded)


def print_receipt(basket):
    """
        Prints the Receipt in the format:
            Item Price
            Sales Tax
            Total Price
    """
    total_sales_tax = 0
    total_price = 0
    basic_tax = 10 # 10%
    import_duty = 0.05 # 5%

    
    for item in basket:
        #  Check the kind of item
        prod = item['prod']
        qty = item['qty']
        res = exclude_items(prod) # true or false

        if prod.__contains__('imported'):
            if res is True: #if item is imported food/book/medicine
                duty = import_duty * item['price']
                price = round_nearest(duty) + item['price']
                total_sales_tax += round_nearest(duty)
                total_price += round_nearest(price)
                total_price += round_nearest(price)
                print(f"{qty} {prod}: {round_nearest(price)}")
            else:
                sales_tax = (basic_tax * item['price'])/100
                duty = import_duty * item['price']
                price = round_nearest(duty) + round_nearest(sales_tax) + item['price']
                total_sales_tax += round_nearest(duty) + round_nearest(sales_tax)
                total_price += round_nearest(price)
                print(f"{qty} {prod}: {round_nearest(price)}")

        else:
                if res is True:
                    price = item['price']
                    total_price += round_nearest(price)
                    print(f"{qty} {prod}: {round_nearest(price)}")
                else:
                    sales_tax = (basic_tax * item['price'])/100
                    price = round_nearest(sales_tax) + item['price']
                    total_price += round_nearest(price)
                    total_sales_tax += round_nearest(sales_tax)
                    print(f"{qty} {prod}: {round_nearest(price)}")

        print(total_price)

    print(f"Sales Tax: {round_nearest(total_sales_tax)}")
    print(f"Price: {round_nearest(total_price)}")

# print_receipt(Baskets[1])
# print_receipt(Baskets[2])
print_receipt(Baskets[3])