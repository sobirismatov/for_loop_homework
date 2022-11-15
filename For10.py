def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    ism=[]
    for i in list1:
        ism.append(i.capitalize())
    return ism
print(main(["husan ","alisher","asadbek", "sanjar"]))