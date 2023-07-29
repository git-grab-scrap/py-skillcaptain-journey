def set_to_list(s1):
    l1 = list(s1)
    return l1


def list_to_set(l1):
    s1 = set(l1)
    return s1


list1 = [1,2,1,3,4,4,5,1,6,7,3,8]
print(f"Look at the contents: {list1}")
print(f"Too Many duplicates and copies of the same thing!! Time to clean-up the list and eliminate copies... non-redundant values belong to the set type: \n {type(list_to_set(list1))}: {list_to_set(list1)}")
print(f"So now the set can become a list too... check this out \n {type(set_to_list(list1))}: {set_to_list(list_to_set(list1))} ")
