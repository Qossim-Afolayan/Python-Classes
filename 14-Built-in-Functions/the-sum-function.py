print(sum([1, 2, 5]))

def greater_sum(list1, list2):
    result =  []
    
    if sum(list1) > sum(list2):
        result = list1

    else:
        result = list2

    return result

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([1], [])) 


def sum_difference(lists1, lists2):
    return sum(lists1) - sum(lists2)

print(sum_difference([1], []))