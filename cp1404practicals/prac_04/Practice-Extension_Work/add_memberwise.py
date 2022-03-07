def add_memberwise(l1: list[int], l2: list[int]) -> list[int]:
    """takes two lists, and returns the list that contains the sum of elements 
    that are in the same index in the two lists"""
    i = min(len(l1), len(l2))
    result = []
    while i > 0:
        result.append(l1.pop(0) + l2.pop(0))
        i -= 1
    return result + l1 if l1 else (result + l2 if l2 else result)
