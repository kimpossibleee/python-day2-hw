'''
Exercise 1:
Given a list as a parameter,write a function that returns a list of numbers that are less than ten
For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
'''

def less_than_ten(lst):
    my_list = [number for number in lst if number < 10]
    return my_list

my_list = [1, 11, 14, 5, 8, 9]
print(less_than_ten(my_list))

'''
Exercise 2
Write a function that takes in two lists and returns the two lists merged together and sorted
'''

def merge_2_lists(list1, list2):
    joined_list = list1 + list2
    joined_list.sort()
    return joined_list

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
print(merge_2_lists(l_1, l_2))
