def add(a, b):
    return a + b

def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def is_even(number):
    return number % 2 == 0

def largest(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest


def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return len([char for char in text.lower() if char in vowels])
    

def add_prefix(names, prefix="Mr. "):
    return [prefix + name for name in names]

def initials(full_name):
    return "".join([f"{word[0]}." for word in full_name.split(' ')])

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b