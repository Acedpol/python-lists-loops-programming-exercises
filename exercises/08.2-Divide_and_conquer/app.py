list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def merge_list(list1, list2):
    # Your code here
    new_list = []
    for e in list1:
        new_list.append(e)
    for e in list2:
        new_list.append(e)
    return new_list

def sort_odd_even(list):
    odd_list = []   # sorted_list
    even_list = []  # even
    for e in list:
        if e % 2 != 0:
            odd_list.append(e)
        else:
            even_list.append(e)
    return merge_list(odd_list,even_list)

print(sort_odd_even(list_of_numbers))

