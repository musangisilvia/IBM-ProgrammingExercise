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

def round_nearest(num, precision):
    return round(math.ceil(num / precision) - 0.05, 1) * precision

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
        res = exclude_items(prod)

        if prod.__contains__('imported'):
            if res is True:
                duty = import_duty * item['price']
                price = duty + item['price']
                total_sales_tax += duty
                total_price += price
                print(f"{prod}: {price}")
            else:
                sales_tax = (basic_tax * item['price'])/100
                duty = import_duty * item['price']
                price = duty + sales_tax + item['price']
                total_sales_tax += duty + sales_tax
                total_price += price
                print(f"{prod}: {price}")

        else:
                if res is True:
                    price = item['price']
                    total_price += price
                    print(f"{prod}: {price}")
                else:
                    sales_tax = (basic_tax * item['price'])/100
                    price = sales_tax + item['price']
                    total_price += price
                    total_sales_tax += sales_tax
                    print(f"{prod}: {price}")


        # res = exclude_items(item['prod'])
        # print(f"{prod}: {res}")
    print(f"Total Sales Tax: {total_sales_tax}")
    print(f"Total Price: {total_price}")
print_receipt(Baskets[2])