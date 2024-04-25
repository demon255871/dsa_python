def sqrt_binary_search(num):
    if num < 0:
        return None

    if num == 0 or num == 1:
        return num

    left = 1
    right = num

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return mid
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return right

# Example usage
number = 16
result = sqrt_binary_search(number)
print(f"The square root of {number} is {result}")