def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element : "))
    arr.append(num)

sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)












# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


# user_input = input("Enter numbers separated by spaces: ")
# input_list = user_input.strip().split()  # split input into strings


# arr = []  # empty list for storing integers
# for item in input_list:
#     arr.append(int(item))  # convert each to int and add to list


# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)
