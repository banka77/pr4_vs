def process_input(input_str):
    numbers = list(map(int, input_str.split(')(')))
    last_digit = int(str(numbers[-1])[-1])
    tens_first = int(str(numbers[0])[-2]) if len(str(numbers[0])) > 1 else 0
    is_valid_number = lambda num: (num % last_digit == 0) and (
        int(str(num)[-2]) if len(str(num)) > 1 else 0 > tens_first)
    result = list(map(str, filter(is_valid_number, numbers[1:-1])))

    return " ".join(result)


input_str = input().strip()
print(process_input(input_str))
