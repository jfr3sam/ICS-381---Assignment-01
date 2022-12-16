
    
# This function takes a list as an input and return it as a sorted list (Return a sorted list)
def bubble_sort(number_list):
    sorted_number_list = number_list.copy()
    N = len(number_list)
    
    for j in range(1, N):
        for i in range(0, N - j):
            if sorted_number_list[i] > sorted_number_list[i + 1]: 
                temp = sorted_number_list[i]
                sorted_number_list[i] = sorted_number_list[i+1]
                sorted_number_list[i + 1] = temp
                
    return sorted_number_list



# This function implements the third element (smallest number) in a soetrd number list.
def third_min(number_list):
    number_list = bubble_sort(number_list)
    return number_list[2]



# This function implements the second largest element (second last number) in a soetrd number list using negative indexing.
def second_max(number_list):
    number_list = bubble_sort(number_list)
    return number_list[-2]
    
