def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """ 
    b=[]
    for i in range(1,price):
        b+=[i*2.25]
    return b
print(main(4))