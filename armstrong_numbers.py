# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    new_numbers = []
    for n in numbers:
       if helper(n) == n:
        new_numbers.append(n)
    return new_numbers
    
def helper(num):
    digits = [int(d) for d in str(num)]
    product = 0
    for d in digits:
        product += d ** len(digits)
    return product

print(find_armstrong_numbers(list(range(0,100)))) #== [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# def helper(num):
#     digits = [int(x) for x in str(num)]
#     length = len(digits)

#     return functools.reduce(lambda product, d : product + (d ** length), digits, 0)
