def find_max_sum(numbers):
    if not numbers:
        return 0
    if len(numbers) < 2:
        return numbers[0]
    if len(numbers) == 2:
        return sum(numbers)

    if numbers[0] > numbers[1]:
        first = numbers[0]
        second = numbers[1]
    else:
        first = numbers[1]
        second = numbers[0]

    for i in range(2, len(numbers)):
        if numbers[i] > first:
            second = first
            first = numbers[i]
        elif numbers[i] > second:# and numbers[i] != first:
            second = numbers[i]

    return first + second
    
if __name__ == "__main__":
    print(find_max_sum([30,5, 9, 7, 4, 20]))
    print(find_max_sum([1]))
