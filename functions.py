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
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in text:
        if char in vowels:
            count += 1
    return count

def add_prefix(names, prefix="Mr. "):
    ans = []
    for name in names:
        ans.append(prefix + name)
    return ans

def initials(full_name):
    ans = ""
    words = full_name.split(' ')
    for i in words:
        ans = ans + i[0] + '.'
    return ans

def safe_divide(a, b):
    if b == 0:
        return None
    return a / b