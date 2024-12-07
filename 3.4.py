

def sum_digits(number):
    number = abs(number)
    number_str = str(number)
    digit_sum = sum(int(digit) for digit in number_str)
    return digit_sum

any_number = int(input('Enter an integer number: '))
result = sum_digits(any_number)

print(f'The sum of the digits in the number {any_number} is {result}')
