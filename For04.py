def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    b=[]
    for i in range(A,B+1):
        b.append(i)
    return b
print(main(2,5))