#Practice problem
#print only odd numbers from 0 to 100
for num in range(101):
    if num%2!=0:
        print(num, end=" ")

# Convert string to upper and lower case
string = "I Love my India"
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

# Reverse a string
string = "Janarthanan"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string  
print("Reversed string:", reversed_string)


# Fibonacci series up to n terms
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
n = 10 
for i in range(n):
    print(fibonacci_recursive(i), end=" ")


# Check if a number is Armstrong number
def is_armstrong(num):
    order = len(str(num))
    sum_of_digits = sum(int(digit) ** order for digit in str(num))
    return num == sum_of_digits
num = 153 
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")


# Check if a letter is a vowel or consonant
def check_vowel_consonant(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return f"{letter} is a vowel"
    else:
        return f"{letter} is a consonant"
letter = 'A'
print(check_vowel_consonant(letter))
letter = 'J'
print(check_vowel_consonant(letter))
letter = 'e'
print(check_vowel_consonant(letter))
letter = 'g'
print(check_vowel_consonant(letter))


# Check if a number is odd or even
def check_odd_even(num):
    if num % 2 == 0:
        return f"{num} is an even number"
    else:
        return f"{num} is an odd number"
num = 25
print(check_odd_even(num))
num = 40
print(check_odd_even(num))
num = 1010234124
print(check_odd_even(num))


# Check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
year = 2024
print(is_leap_year(year))
year = 2020
print(is_leap_year(year))
year = 1947
print(is_leap_year(year))
year = 2050
print(is_leap_year(year))


