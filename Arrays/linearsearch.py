def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
my_list = [4, 2, 7, 1, 9, 5]
target_value = 7

result = linear_search(my_list, target_value)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")