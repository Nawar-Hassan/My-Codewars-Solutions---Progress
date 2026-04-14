
# Mysolution for smash problem on Codewar (redundant as per Gemini)

"""

def smash(array):
    if len(array) == 0:
        return ''
    for word in array:
        if isinstance(word,str) or word !="":
            return " ".join(array[0:len(array)])
        else:
            print("Words should be strings")

print(f"'{smash(['hello', 'world', 'this', 'is', 'great'])}'")

#better use only return " ".join(array)

"""
#another solution by another warrior for smash problem (not a pythonic one but rather manual)

"""
def smash(words):
    
    i=0
    l=len(words)
    str1=""
    while i<l:
        if i<l-1: #-1 indicated except the last word
            str1+=words[i] + " "
        else: 
            str1+=words[i]
        i+=1 # end the loop
        
    return str1
print(f"'{smash(['hello', 'world', 'this', 'is', 'great'])}'")

"""
#another solution by another warrior for smash problem (very pythonic as per Gemini)

"""
smash = ' '.join  # here it is like we give an alias to the function it is very pythonic but not recommended in big programs 
print(f"'{smash(['hello', 'world', 'this', 'is', 'great'])}'")

"""
#another solution by another warrior for smash problem (using for loop instead of while which is favorable in Python)
"""
def smash(words):
    if not words:
        return ""
    
    result = ""
    # We loop through everything EXCEPT the last word which needs to be handled separately
    for word in words[:-1]:
        result += word + " "
    
    # Then we just tack the last word on at the end (no space!)
    result += words[-1]
    return result
print(f"'{smash(['hello', 'world', 'this', 'is', 'great'])}'")

"""
#another solution by another warrior for smash problem (using enumirate method)

"""
def smash(words):
    result = ""
    last_index = len(words) - 1
    
    for i, word in enumerate(words):
        if i < last_index:
            result += word + " "
        else:
            result += word
            
    return result

"""
#another solution by another warrior for smash problem (using list comprehension that also changed int to str)

"""
nums = ['hello', 'world', 'this', 'is', 'great']

print(f"'{' '.join([str(n) for n in nums])}'") # Convert each number to a string, then join them

"""

# my solution to returning a string of numbers into integers
"""
def string_to_number(s):
    
    return int(s)

print(string_to_number("703"))

"""
# my solution to returning a string of numbers into integers
"""
def string_to_number(s):
    
    return int(''.joint(s))

print(string_to_number("703"))

"""
# my solution to returning a count of 'True' in a list of boolean values list

"""
def count_sheep(present):

    return ''.join(str(present)).count('True')
    

print(count_sheep([True,  True,  True,  False,
                     True,  True,  True,  True ,
                     True,  False, True,  False, 
                       True,  False, False, True ,
                       True,  True,  True,  True , 
                         False, False, True, True]))

"""

# another solution from Codewar to returning a count of 'True' in a list of boolean values list

"""

def count_sheep(present):

    return present.count(True)
    

print(count_sheep([True,  True,  True,  False,
                     True,  True,  True,  True ,
                     True,  False, True,  False, 
                       True,  False, False, True ,
                       True,  True,  True,  True , 
                         False, False, True, True]))

"""
# another solution from Codewar to returning a count of 'True' in a list of boolean values list

"""

def count_sheeps(a):
    v = 0
    for i in a:
        if i == True:
            v += 1
    return v

print(count_sheeps([True,  True,  True,  False,
                     True,  True,  True,  True ,
                     True,  False, True,  False, 
                       True,  False, False, True ,
                       True,  True,  True,  True , 
                         False, False, True, True]))

"""
# Gemini way (since booeans are True=q, False= 0 we can just use sum) to returning a count of 'True' in a list of boolean values list

"""

def count_sheep(present):
    return sum(present)

print(count_sheep([True,  True,  True,  False,
                     True,  True,  True,  True ,
                     True,  False, True,  False, 
                       True,  False, False, True ,
                       True,  True,  True,  True , 
                         False, False, True, True]))

"""
# My solution for finding the opposite number excercise

"""
def opposite(number):
    
    if number == 0:
        return 0
    
    
    if number < 0:
        return abs(number)
    
    else:
        return -(number)

print(opposite(-5977764.896776721))

"""
# Gemini solution for finding the opposite number excercise

"""
def opposite(number):
    return -number

print(opposite(10))

"""
# other solution for finding the opposite number excercise
"""
def opposite(number):
  return abs(number) if number < 0 else 0 - number
print(opposite(0))

"""

# My solution for the hero and dragons excercise
"""
def hero(bullets, dragons):
        
        return bullets >= dragons * 2 

print(hero(107, 48))
"""
# another solution for the hero and dragons excercise using lambda method

"""
hero = lambda b,d: 2*d<=b
print(hero(107, 48))

"""
# My solution for the sum of square numbers excercise

"""

def square(n1, n2, n3):

    return (n1**2) + (n2**2) + (n3**2)

print(square(1, 1, 1))

"""

# another solution for the sum of square numbers excercise

"""

def square_sum(numbers):
    return sum(n**2 for n in numbers)
print(square_sum([1,2,2]))

"""

# another solution for the sum of square numbers excercise

"""
def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num * num
    return res 

print(square_sum([1, 2, 2]))

"""
# My solution for the string slicing excercise
"""
def remove_char(s):

    if len(s) > 2:
        return s[1:-1]
    elif len(s) == 2:
        return ''
    
print(remove_char('nawar'))
"""
# My solution for BMI calc excercise
"""
def bmi(weight ,height):
    calc = weight/(height ** 2)
    if calc <= 18.5:
        return "Underweight"

    if calc <= 25.0: 
        return "Normal"

    if calc <= 30.0: 
        return "Overweight"

    if calc > 30: 
        return "Obese"
    
print(bmi(64, 167))
"""
# another solution for BMI calc excercise
"""
def bmi(weight, height):

    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

print(bmi(64, 167))
"""
# My solution for even_multiplication excercise (more readable for others in the real world)
"""
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

print(simple_multiplication(9))
"""
# another solution /Bitwise Logic/ for even_multiplication excercise
"""
simple_multiplication = lambda a : a * (8 + (a & 1)) # a & 1 instead of n % 2
print(simple_multiplication(8))
"""
# Gemini solution /The "Ternary" Version/ for even_multiplication excercise
"""
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9
print(simple_multiplication(8))
"""
# Gemini solution /The "Mathematical" Trick (Advanced Logic)/ for even_multiplication excercise (most efficient)
"""
def simple_multiplication(number):
    return number * (8 + (number % 2)) # coz if the number is even it will return 0 else 1
print(simple_multiplication(8))
"""
# Gemini solution /The "Boolean Indexing" Trick/ for even_multiplication excercise
"""
def simple_multiplication(number):
    # [result_if_even, result_if_odd]
    return [number * 8, number * 9][number % 2] # coz if the number is even it will return 0 else 1
print(simple_multiplication(8))
"""
# My solution for reverse_seq excercise
"""
def reverse_seq(n):
   
    if n > 0:
       return sorted(list(range(1,n+1)),reverse = True)             
    
print(reverse_seq(10))
"""
# another solution for reverse_seq excercise (most effecient)
"""
def reverse_seq(n):
    return list(range(n, 0, -1))
print(reverse_seq(10))
"""
# another solution for reverse_seq excercise
"""
def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output
print(reverse_seq(10))
"""
# another solution for reverse_seq excercise

"""
def reverse_seq(n): return list(reversed(range(1,n+1)))
print(reverse_seq(10))
"""
# another solution for reverse_seq excercise

"""
def reverse_seq(n):
    return [i*-1 for i in range(-n,0)]
print(reverse_seq(10))
"""
# another solution for reverse_seq excercise / using slicing way

"""
reverse_seq = lambda n: list(range(1,n+1))[::-1]
print(reverse_seq(10))
"""
# My solution for the double integer excercise
"""
def double(num):

    if isinstance(num,int):
        return num * 2
    
print(double(4))

"""
# My solution for the make negative excercise
"""
def make_negative(i):
    return -i if i>0 else i
print(make_negative(10))

"""
# My solution for the make miliseconds excercise (very much like by Gemini)
"""
def make_milisec(h, m, s):
    return (h * 3_600_000) + (m * 60_000) + (s * 1_000) # use of _ is to make the large# more readable
print(make_milisec(0, 1, 1))
"""
# another solution suggested by Gemini for the make miliseconds excercise
"""
MILLIS_IN_SECOND = 1_000
MILLIS_IN_MINUTE = 60 * MILLIS_IN_SECOND
MILLIS_IN_HOUR = 60 * MILLIS_IN_MINUTE

def make_milisec(h, m, s):
    return (h * MILLIS_IN_HOUR) + (m * MILLIS_IN_MINUTE) + (s * MILLIS_IN_SECOND)

print(make_milisec(0, 1, 1))
"""
# another solution suggested by Gemini for the make miliseconds excercise

"""
from datetime import timedelta

def make_milisec(h, m, s):
    # This creates a time duration and asks for it in total seconds
    # then we just multiply by 1000 for milliseconds
    return int(timedelta(hours=h, minutes=m, seconds=s).total_seconds() * 1000)
print(make_milisec(0, 1, 1))
"""
# My solution for the max/min number in a list excercise (as per Gemini it is clean and pythonic and efficient)
"""
def maximum(arr):
    return max(arr)
            
def minimum(arr):
    return min(arr)
       
arr = [4,6,2,1,9,63,-134,566]

print(f'max = {maximum(arr)}, min = {minimum(arr)}')

"""
# another solution suggested by Gemini for the max/min number in a list excercise (just to show how the logic work behind the scenes)
"""
def manual_maximum(arr):
    # Start by assuming the first number is the biggest
    current_max = arr[0]
    
    # Check every other number
    for num in arr:
        if num > current_max:
            # If we find a bigger one, update our record
            current_max = num
            
    return current_max

def manual_mainimum(arr):
    # Start by assuming the first number is the samallest
    current_min = arr[0]
    
    # Check every other number
    for num in arr:
        if num < current_min:
            # If we find a smaller one, update our record
            current_min = num
            
    return current_min

arr = [4,6,2,1,9,63,-134,566]

print(f'max = {manual_maximum(arr)}, min = {manual_mainimum(arr)}')

"""
# another solution suggested by a worrior on Codewars for the max/min number in a list excercise (described by Gemini as clever but dagerous)
"""
def min(arr):
    arr.sort()
    return arr[0]

def max(arr):
    arr.sort(reverse=True)
    return arr[0]

arr = [4,6,2,1,9,63,-134,566]

print(f'max = {min(arr)}, min = {max(arr)}')

"""
# My solution for the repeat string excercise
"""
def repeat_str(repeat,string):
    if repeat >= 0 and isinstance(string,str):
        return repeat * string
print(f"'{repeat_str(10,'n')}'")
"""
# another solution for the repeat string excercise (Gemini evaluation that it is un-Pythonic and inefficient manual way)
"""
def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution
print(f"'{repeat_str(10,'n')}'")
"""
# another solution suggested by Gemini if i need to use loop-built in case '*' cannot be used is to 
# use the ''.join method for the repeat string excercise
"""
# The "Pro" way to loop-build a string

def repeat_str(repeat, string):
    parts = []
    for i in range(repeat):
        parts.append(string)
    return "".join(parts)
print(f"'{repeat_str(10,'n')}'")
"""
# My solution for the remove vowles from a string excercise (using set methods but not ordered!)
"""
def disemvowel(string_):
    vowels = {'a','o','u','e','i','y',' ','A','O','U','E','I','Y'}
    to_set = set(string_)
    return ''.join(to_set - vowels)

print(disemvowel("This website is for losers LOL!"))
"""
# My solution for the remove vowles from a string excercise
"""
def disemvowel(string_):
    vowels = "aeiouAEIOU " # 1. Simple string for comparison
    new_list = []
    for l in string_:
        if l not in vowels:
            new_list.append(l) # 2. Append the letter, not the sentence
    return ''.join(new_list)   # 3. Moved outside the loop

print(disemvowel("This website is for losers LOL!"))
"""
# My solution for the remove vowles from a string excercise
"""
def disemvowel(string_):
    vowels = ['a','o','u','e','i','y',' ','A','O','U','E','I','Y'] 
    new_list = []
    for l in list(string_):
        if l not in vowels:
            new_list.append(l) 
    return ''.join(new_list)   

print(disemvowel("This website is for losers LOL!"))
"""
# another solution by another warrior for the remove vowles from a string excercise

"""
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou ")
print(disemvowel("This website is for losers LOL!"))
"""
# another solution by another warrior for the remove vowles from a string excercise using Regular Expressions (often called Regex)
# the template here is like this: re.sub(pattern, replacement, string, ...)

"""
import re
def disemvowel(string):
    return re.sub('[aeiou ]', '', string, flags = re.IGNORECASE) # sub is like find & replace, pattern='vowles',replacement =''=delete, string=the original text
print(disemvowel("This website is for losers LOL!"))
"""
# another solution by another warrior for the remove vowles from a string excercise using translate
"""
def disemvowel(string):
    # Create a table that maps vowels to 'None' (meaning delete them)
    table = str.maketrans('', '', 'aeiouAEIOU ')
    return string.translate(table)

print(disemvowel("This website is for losers LOL!"))
"""
# My solution for the capitalize a string excercise using 

"""
from string import capwords

def to_jaden_case(string):
    
    return capwords(string)
  
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

"""
# another solution by another warrior for the capitalize a string excercise using capitalize & split methods
"""
def to_jaden_case(string):

    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
"""
# My solution for the sum a list of numbers excercise

"""
import numbers

def sum_array(a):

    if all(isinstance(x, numbers.Number) for x in a):
        return sum(a)
    else:
       print("List should contain only numbers")

print(sum_array([1, 5.2, 4, 0, -1]))
"""
# another solution (Gemini) for the sum a list of numbers excercise
"""
def sum_calc(n):
    try:
        return sum(n)
    except TypeError:
        return "List contains non-number items"

print(sum_calc([1, 5.2, 4, ' ', -1]))
"""

# My solution for the sort integrs in descending order excercise (wrong approach coz i used a list)
"""
def descending_order(a):
    
    if not all(isinstance(x, int) for x in a):
        return "Error: List must contain only integers"
        
   
    if any(x < 0 for x in a):
        return "Error: You should have only positive integers"

    return sorted(a, reverse=True)

print(descending_order([1, 8, 3, 4, 5, 6, 9, 5, 2]))
"""
# Gemini solution for the sort integrs in descending order excercise

"""
def descending_order(num):
    
    if num < 0:
        return "Error: Number must be positive"    
   
    str_num = str(num)                          # change to list
 
    sorted_list = sorted(str_num, reverse=True)    
    
    return int("".join(sorted_list))

print(descending_order(876954231))

"""
# another solution by a warrior for the sort integrs in descending order excercise (one liner onion type), very pythonic and efficeint
"""
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))  # change to list (we should the onio from the center out)
print(Descending_Order(876954231))
"""
# another solution by a warrior for the sort integrs in descending order excercise (same as the pervious one but a storybook way one by one) not recommended
"""
def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
print(Descending_Order(876954231))
"""
# another solution by a warrior for the sort integrs in descending order excercise (same as onion type but reverse method is different)
"""
def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))
print(Descending_Order(876954231))

"""
# another solution by a warrior for the sort integrs in descending order excercise (purely mathematical not pythonic)
"""
def Descending_Order(num):
    digits = []
    
    while num > 0:
        new_num = num // 10
        digits.append(num - new_num*10)
        num = new_num
        
    out = 0
    for i, digit in enumerate(sorted(digits)):
        out += digit * 10**i
        
    return out
print(Descending_Order(876954231))
"""
# My solution (1) for the squaring a dgiit in an integer excercise
"""
def square_digit(num):
    combined = []
    if isinstance(num,int):
        for x in str(num):
            combined.append(str(int(x) ** 2))
    return int(''.join(combined))

print(square_digit(9119))
"""
# My solution (2) for the squaring a dgiit in an integer excercise

"""
def square_digit(num):

    return int(''.join(str(int(x)**2) for x in str(num)))

print(square_digit(9119))

"""
# My solution for the in_love or not excercise

"""
def lovefunc(flower1, flower2):
    if (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0):
        return True
    else:
        return False

print(lovefunc(50,40))
"""
# another solution for the in_love or not excercise
"""
def lovefunc( flower1, flower2 ):

    return (flower1+flower2)%2

print(lovefunc(50,41))
"""
# another solution (by Gemini) for the in_love or not excercise

"""
def lovefunc(flower1, flower2):

    return flower1 % 2 != flower2 % 2

print(lovefunc(50,40))
"""
# my solution for the summation excercise
"""
def summation(num):
    if num > 0:
        return sum(range(0,num)) + num
    
print(summation(8))
"""
# another solution (Gemini) for the summation excercise (Pythonic way)
"""
def summation(num):
    return sum(range(1, num + 1))
print(summation(8))
"""
# another solution (Gemini) for the summation excercise (mathematical way)/most efficient o(1)
"""
def summation(num):
    return num * (num + 1) // 2
print(summation(8))

"""
# my solution for the compare grades excercise
"""
def better_than_average(your_points, class_points):   

    total_sum = sum(class_points) + your_points    
    
    total_students = len(class_points) + 1    
   
    true_avg = total_sum / total_students    
  
    return your_points > true_avg

print(better_than_average(59, [100, 40, 34, 57, 29, 72, 57, 88]))

"""
# my solution for the math operator excercise
"""
def operation(operator, value1, value2):

    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1/value2

print(operation('+', 1, 2))

"""
# Gemini solution for the math operator excercise (using dictionary method for profeciency and efficiency)
"""
def operation(operator, value1, value2):
    ops = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }
    return ops.get(operator)

print(operation('+', 1, 2))
"""
# Gemini solution for the math operator excercise (using dictionary method with operator module)/the cleanest way
"""
import operator

def operation(op_symbol, v1, v2):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    # Look up the function and then call it with (v1, v2)
    return ops[op_symbol](v1, v2)
print(operation('+', 1, 2))
"""
# another variation by a warrior of dictionary method to solve the math operator excercise /not recommended by Gemini
"""
def operation(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
print(operation('+', 1, 2))
"""
# another solution by a warrior for the math operator excercise (using eval method )/dangerous securitywise/not recommended
""""
def operation(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
print(operation('+', 1, 2))
# another eval variation
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')
# another eval variation
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

"""
# My solution for odd or even excercise
"""
def odd_or_even(arr):

    if abs(sum(arr) % 2) == 0:
        return 'even'
    else:
        return 'odd'
    
print(odd_or_even([0, -1, -5]))

"""
# My solution for a simple retunr a string with name varialbe
"""
def welcome(name):
    return f"Hello, {name} how are you doing today?"

print(welcome('Nawar'))

"""
# My solution for a joining two strings, sort, uinique
"""
def longest_distinct(s1, s2):
    return ''.join(sorted(set(s1+s2)))
print(longest_distinct("xyaabbbccccdefww","xxxxyyyyabklmopq"))

"""
# Gemini solution for the is_triangle excercise

"""
def surface(a, b, c):
    # This ensures the shape 'closes' and creates a surface
    return (a + b > c) and (a + c > b) and (b + c > a)
print(surface(7, 2, 2))
"""
# another solution by a warrior for the is_triangle excercise (clever and efficient/great use of math and geometry as per Gemini)
"""
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
print(is_triangle(7, 2, 2))
"""
# My solution for the get_middle excercise (logic & accuracy are good but too many brackets)
"""
def get_middle(s):

    if len(s) % 2 == 0:
        return s[(int(len(s) / 2 -1))] + s[(int(len(s) / 2))]
    else: 
        return s[int(len(s) // 2)]
    
print(get_middle('testing'))
"""
# Gemini solution for the get_middle excercise (same as mine but simpler)
"""
def get_middle(s):
    middle = len(s) // 2
    if len(s) % 2 == 0:
        return s[middle - 1 : middle + 1] # Using a "slice"
    else:
        return s[middle]
print(get_middle('test'))
"""
# another solution by a warrior for the get_middle excercise (extremly clever, mathematical & efficient as per Gemini)
"""
def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]
print(get_middle('test'))
"""
# My solution to count_positives_sum_negatives excercise
"""
def count_positives_sum_negatives(arr):
    
    if not arr: 
        return []
    
    positive_array = list(filter(lambda x: x > 0, arr))
    negative_array = list(filter(lambda x: x < 0, arr))
    new_array      = [len(positive_array),sum(negative_array)]
          
    return new_array
    
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
"""
# Gemini's solution to count_positives_sum_negatives excercise

"""
def count_positives_sum_negatives(arr):
    # 1. Check if the input is empty or None immediately
    if not arr: 
        return []    
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    
    return [len(pos), sum(neg)]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
"""
# another solution by a warrior to count_positives_sum_negatives excercise
"""
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
"""
# another solution by a warrior to count_positives_sum_negatives excercise
"""
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
"""
# another solution by a warrior to count_positives_sum_negatives excercise
"""
def count_positives_sum_negatives(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
"""
# My solution by a warrior to reverse string excercise
"""
def solution(string):
   if not string:
    return ''
   else:
    return ''.join(reversed(string))
     
print(solution('world'))
"""
# another solution by a warrior to reverse string excercise

"""
def solution(str):
  return str[::-1]

print(solution('world'))
"""
# My solution to endwith string excercise

"""
def solution(text, ending):
    
    return text.endswith(ending)
            
print(solution('nawarhassan','hassan'))
"""
# another solution to endwith string excercise (using slicing)
"""
def solution(string, ending):
    return ending in string[-len(ending):]
print(solution('nawarhassan','hassan'))
"""
# My solution to square of squares excercise
"""
import math

def is_square(n):
    if n >= 0:
        result = math.sqrt(n)
        if result * result == n:
            return True
        else:
            return False
    else:
        return False

print(is_square(3))
"""
# My solution to square of squares excercise
"""
import math

def is_square(n):
    if n < 0:
        return False
    
    sqrt_n = math.sqrt(n)
    
    return sqrt_n % 1 == 0
print(is_square(25))
"""
# My solution to boolean_to_string excercise (according to Gemini it is redundant/overengineering)
"""
def boolean_to_string(b):

    if b:
        if bool(b) == True:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'
print(boolean_to_string(0))
"""
# Gemini (1) solution to boolean_to_string excercise
"""
def boolean_to_string(b):
    if b:
        return "True"
    else:
        return "False"
print(boolean_to_string(0))
"""
# Gemini (2) solution to boolean_to_string excercise
"""
def boolean_to_string(b):
    return str(b)
print(boolean_to_string(0))
"""
# Gemini (3) solution to boolean_to_string excercise
"""
def boolean_to_string(b):
    return f"{b}"
print(boolean_to_string(0))
"""
# My solution to DNA_strand excercise (manual way, slow and long)
"""
def DNA_strand(dna):
    side2 = []
    if dna:
        for x in dna:
            if x == 'A':
                side2.append('T')
            elif x == 'T':
                side2.append('A')
            elif x == 'C':
                side2.append('G')
            elif x == 'G':
                side2.append('C')
    return ''.join(side2)

print(DNA_strand('ATTGC'))

"""
# Gemini (1) solution to DNA_strand excercise (intermediate dictionary way, simpler & faster)
"""
def DNA_strand(dna):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([pairs[x] for x in dna])
print(DNA_strand('ATTGC'))
"""
# Gemini (2) solution to DNA_strand excercise (professional translate way most efficient & incredibly fast & short)
"""
def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))
print(DNA_strand('ATTGC'))
"""
# another solution by a warrior to DNA_strand excercise (shorter dictionary way, simpler)
"""
def DNA_strand(dna):
  return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])
print(DNA_strand('ATTGC'))
"""
# My solution(logic)/supported by AI to reverse_words excercise (manual way, slow and long)
"""
def reverse_words(text):

    text += " "
    final_result = []

    while ' ' in text:
        pos = text.find(' ')
        # أخذ الجزء قبل المسافة
        part = text[:pos]
        # قلبه وإضافته
        final_result.append(part[::-1])
        # "طرح" الجزء المعالج من النص الأصلي (التحديث)
        text = text[pos+1:] 

    return " ".join(final_result)


print(reverse_words('This is an example!'))

"""
# Gemini and other warriors solution to reverse_words excercise (fast and efficient using the split built-in method)
"""
def reverse_words(text):
    
    return ' '.join(x[::-1] for x in text.split(' '))
print(reverse_words('This is an example!'))
"""
# another warriors solution/refined by Gemini to reverse_words excercise (manual not pythonic but very smart and reliable more like a C or Java way)
"""
def reverse_words(text):
    word = '' # this is the bucket
    result = ''
    for char in text:
        if char != ' ':
            word += char
        else:
            result += word[::-1] + char
            word = '' # to empty the word bucket
    return result + word[::-1]

print(reverse_words('This is an example!'))
"""
# My solution(logic) to bus_stops excercise (dictionay logic but failed all Codewar tests)
"""
def number(bus_stops):

    to_dic = dict(bus_stops)
    return sum(to_dic.keys()) - sum(to_dic.values())
    
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
"""
# My other solution(logic) to bus_stops excercise (passed all Codewar tests)

"""
def number(bus_stops):

    up = []
    down = []

    for i in bus_stops:
        up.append(i[0])
    for x in bus_stops:
        down.append(x[1])
    
    return sum(up) - sum(down)
    
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
"""
# Gemini solution to bus_stops excercise (using for loop in a simpler way to in one fater and more efficient)
"""
def number(bus_stops):
    total_people = 0
    for on, off in bus_stops:
        total_people += on
        total_people -= off
    return total_people
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
"""
# Gemini solution to bus_stops excercise (The Pythonic way, same my logic, but in a compact oneliner way/faster and more efficient)
"""
def number(bus_stops):
        return sum(stop[0] for stop in bus_stops) - sum(stop[1] for stop in bus_stops)
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
"""
# Another solution by a warrior to bus_stops excercise (The top Pythonic one,black belt, using automatic Tuple Unpacking/ on for first element and off for the second element in the pair)
"""
def number(bus_stops):
    return sum(on - off for on, off in bus_stops) # Uses almost zero extra memory, loops through the data once, one single mathematical expression.
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
"""
# My other solution to check_value_in_array excercise
"""
def find_value(a,x):
    if x in a:
        return True
    else:
        return False
    
print(find_value(('n', 'a', 'w', 'a', 'r','a'),('a')))
"""
# another solution by a warrior to check_value_in_array excercise
"""
def check(seq, elem):
    return elem in seq
print(check(('n', 'a', 'w', 'a', 'r','a'),('a')))
"""
# My other solution to the invert sign of a number excercise
"""
def invert(arr):
    opposit = []
    for x in arr:
        opposit.append(-x)
    return opposit
print(invert([1, -2, 3, -4, 5]))
"""
# another solution to the invert sign of a number excercise
"""
invert = lambda arr: [-x for x in arr]
print(invert([1, -2, 3, -4, 5]))
"""
# another solution to the invert sign of a number excercise
"""
def invert(arr):
    return [-x for x in arr]
print(invert([1, -2, 3, -4, 5]))
"""
# My solution to the like_string excercise
"""
def likes(names):
    if len(names) == 1:
        return(f'{names[0]} likes this')
    elif len(names) == 2:
        return(f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        return(f'{names[0]}, {names[1]} and {names[2]} like this')
    elif len(names) > 3:
        return(f'{names[0]}, {names[1]} and {len(names) - 2} others like this')
    else:
        return 'no one likes this'    
    
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

"""
# another solution to the like_string excercise
"""
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

print(likes(['Alex', 'Jacob', 'Mark', 'Max','Nawar','Ali']))
"""
# another solution to the like_string excercise (using the modern match mehtod which is a new one in Python)
"""
def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'
print(likes(['Alex', 'Jacob', 'Mark', 'Max','Nawar','Ali']))
"""
# My solution to the high_and_low excercise
"""
def high_and_low(num):
    high = []
    low = []
    
    to_list = num.split(' ')
    nums_as_ints = [int(x) for x in to_list]
    if num:
        high.append(str(max(nums_as_ints)))
        low.append(str(min(nums_as_ints)))
        comb = high + low
    return ' '.join(comb)
        
print(high_and_low("-93 -82 99 30 93 33"))
"""
# another solution to the high_and_low excercise
"""
def high_and_low(numbers):
    # Convert strings to actual numbers
    nums = [int(x) for x in numbers.split()]
    
    # Now max() and min() will work mathematically
    return f"{max(nums)} {min(nums)}"
print(high_and_low("-93 -82 99 30 93 33"))
"""
# another solution to the high_and_low excercise (using map)
"""
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"
print(high_and_low("-93 -82 99 30 93 33"))
"""
# another solution to the high_and_low excercise (using map)
"""
# another solution to the high_and_low excercise (one liner using map)
def high_and_low(numbers):
    return f'{max(map(int, numbers.split()))} {min(map(int, numbers.split()))}'
print(high_and_low("-93 -82 99 30 93 33"))
"""
# another solution to the high_and_low excercise (using format)
"""
def high_and_low(numbers):
    nmbrs = [int(n) for n in numbers.split()]
    return '{} {}'.format(max(nmbrs), min(nmbrs))
print(high_and_low("-93 -82 99 30 93 33"))
"""
# My solution to the row_sum_odd_numbers excercise
"""
def row_sum_odd_numbers(n):
    if n:
        return n ** 3
    
print(row_sum_odd_numbers(5))
"""
# another solution to the row_sum_odd_numbers excercise (lambda)
"""
row_sum_odd_numbers = lambda n: n ** 3
print(row_sum_odd_numbers(5))
"""
# My solution to the sum_of_positive excercise
"""
def sum_of_positive(arr):
    return sum(x for x in arr if x > 0)
print(sum_of_positive([1, -4, 7, 12, -10]))
"""
# another solution to the sum_of_positive excercise (lambda)
"""
def sum_of_positive(arr):
    return sum(filter(lambda x: x > 0,arr))
print(sum_of_positive([1, -4, 7, 12, -10]))
"""
# My solution to the find_uniq excercise
"""
def find_uniq(arr):

    short_list = arr[0:3]

    if len(arr) >= 3:
        if arr[0] != arr[1] and arr[1] == arr[2]:
            return arr[0]
        elif arr[0] != arr[1] and arr[0] == arr[2]:
            return arr[1]
        elif arr[0] == arr[1] and arr[1]!= arr[2]:
            return arr[2]
        else:
            for x in arr:
                if x not in short_list:
                    return x

            #return ([x for x in arr if x not in short_list])
    
print(find_uniq([ 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
"""
# another solution to the find_uniq excercise (using set to remove duplicates first)

"""
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
print(find_uniq([ 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
"""
# another solution to the find_uniq excercise (using sorted method)
"""
def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]
print(find_uniq([ 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
"""
# another solution to the find_uniq excercise (using Counter method which counts the values and turn it into dic and most_common method sorts from highest/left count to lowest/right)
"""
from collections import Counter

def find_uniq(a):
    return Counter(a).most_common()[-1][0]
print(find_uniq([ 1, 1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
"""
# My solution to the unique_in_order excercise (it is too heavy and not efficient)
"""
def unique_in_order(seq):
    if not seq:
        return []
    last_index = len(seq) - 1
    new=[]
    for i , x in enumerate(seq):
        if i < last_index:
         if x != seq[i + 1]:
            new.append(x)
    else:
        new.append(x)
        
    return ''.join(new)

print(unique_in_order('ABBCcAD'))
"""
# another solution by a warrior & Gemini to the unique_in_order excercise (shorter and very efficient/using the past(bucket building from previous) instead of the future(next))

"""
def unique_in_order(seq):
    new = []
    for item in seq:
        # If 'new' is empty OR the current item is different from the last one we added
        if len(new) == 0 or item != new[-1]:
            new.append(item)
    return new
print(unique_in_order('ABBCcAD'))
"""
# another solution by Gemini to the unique_in_order excercise (using indexing logic in list compreshension 
# by making it stop before the last charachter (using the Guardrail/range(len(seq) - 1)/ and adding the last one 
# manually to the bucket)
"""
def unique_in_order(seq):
    if not seq: return []    
    # Loop through everything except the last element
    new = [seq[i] for i in range(len(seq) - 1) if seq[i] != seq[i+1]]
    
    # Add the final element that we skipped
    new.append(seq[-1])
    return new
print(unique_in_order('ABBCcAD'))

"""
# another solution by a warrior to the unique_in_order excercise (using the blackbelt group by method which creats tupples(boxes)
# of every new element as the key and a small list of its likes as value, it is a very Pythonic and concise way)
"""
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
print(unique_in_order('ABBCcAD'))
"""
# My solution to the turn_binary excercise
"""
def turn_binary(a,b):

    return bin(a+b)[2:]

print(turn_binary(1,1))
"""
# another solution to the turn_binary excercise (using format)/function
"""
def turn_binary(a,b):

    return format(a + b, 'b')
print(turn_binary(1,1))
"""
# another solution to the turn_binary excercise (using format)
"""
def turn_binary(a,b):
    return f"{a + b:b}"
print(turn_binary(1,1))
"""
# another solution to the turn_binary excercise (using format)/string method
"""
def turn_binary(a,b):

    return '{:b}'.format(a+b)
print(turn_binary(1,1))
"""
# my solution to the DNA_to_RNA excercise (using dictionary)
"""
def dna_to_rna(dna):
    acids = {'A':'A','C':'C','G':'G','T':'U'}
    rna = []
    if not dna:
        return ''
    for a in dna:
        if a in acids :
            rna.append(acids.get(a))
    return ''.join(rna)
print(dna_to_rna('GCAT'))
"""
# my solution to the DNA_to_RNA excercise (using dictionary & list comprehension)
"""
def dna_to_rna(dna):
    if not dna:
        return ''
    acids = {'A':'A','C':'C','G':'G','T':'U'}
    rna = [acids[a] for a in dna if a in acids]
                
    return ''.join(rna)
print(dna_to_rna('GCAT'))
"""
# another solution to the DNA_to_RNA excercise (using replace, the most Pythonic and fast way)
"""
def dna_to_rna(dna):
    return dna.replace('T', 'U')
print(dna_to_rna('GCAT'))
"""
# my solution to the sum_two_smallest_numbers excercise
"""
def sum_two_smallest_numbers(arr):
    #temp_arr = arr[:] # This creates a shallow copy (a "stunt double") copy of the data to protect it without mutation as
    #suggested by Gemini
    if not arr:
        return []
    first = min(arr)
    arr.remove(first)
    second = min(arr)
    return first + second    

print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))
"""
# another solution to the sum_two_smallest_numbers excercise using sort function
"""
def sum_two_smallest_numbers(numbers):

    return sum(sorted(numbers)[:2])
    
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))
"""
# another solution to the sum_two_smallest_numbers excercise using smallest for the largest items we can use nlargest (best efficient one)
"""
from heapq import nsmallest
def sum_two_smallest_numbers(numbers):
    return sum(nsmallest(2,numbers))
    
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))
"""
# another solution to the sum_two_smallest_numbers excercise using pop and index (dangerous not recommended)
"""
def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))
"""
# my solution to the Growth_of_Population excercise (fixed by Gemini)
"""
def nb_year(p0,perc,aug,p):
   
    current = p0
    years = 0
 
    while current < p:
        
        growth = int(current * (perc/100)) + aug
        current = current + growth
        years += 1        
            
    return years

print(nb_year(1500000, 2.5, 10000, 2000000))
"""
# another solution (by Gemini) to the Growth_of_Population excercise
"""
def nb_year(p0, perc, aug, p):
    current = p0
    years = 0
    
    # Loop until 'current' population reaches or exceeds 'p'
    while current < p:
        # Calculate the new population for the next year
        # Note: Use int() to floor the value, as usually required in this problem
        current = int(current + (current * (perc / 100)) + aug)
        years += 1
            
    return years
print(nb_year(1500000, 2.5, 10000, 2000000))
"""
# another solution (by Gemini) to the Growth_of_Population excercise (The "Single Variable" Strategy)/efficient, no stale data, better readability
"""
def nb_year(p0, perc, aug, p):
    years = 0
    # We treat p0 as our "Live Population"
    while p0 < p:
        # We calculate the new value and IMMEDIATELY overwrite the old p0
        p0 = p0 + int(p0 * (perc / 100)) + aug
        # or we can write p0 += int(p0 * (perc / 100)) + aug (augemented assignment)
        years += 1
        
    return years
print(nb_year(1500000, 2.5, 10000, 2000000))
"""
# another solution (by Gemini) to the Growth_of_Population excercise (using a for loop but not quite suitable 
# for this specific probelm because a for loop needs to know how many times to loop)
"""
def nb_year(p0, perc, aug, p):
    # We pick a huge range (e.g., 0 to 1000 years)
    for year in range(1, 1001):
        
        # Calculate the new population
        p0 += int(p0 * (perc / 100)) + aug
        
        # The 'if' check is our exit door
        if p0 >= p:
            return year # This 'kills' the loop and sends the answer back
print(nb_year(1500000, 2.5, 10000, 2000000))
"""
# another solution (by Gemini) to the Growth_of_Population excercise (using the "infinite" for loop to solve 
# the # of loops issue with for, but still according to Gemini the while loop is the professional way for this problem)
""""
from itertools import count

def nb_year(p0, perc, aug, p):
    # This loop starts at 1 and goes to infinity... 1, 2, 3, 4...
    for year in count(1):
        p0 += int(p0 * (perc / 100)) + aug
        
        if p0 >= p:
            return year

print(nb_year(1500000, 2.5, 10000, 2000000))
"""
#solution (by Gemini) to the Take a Walk" challenge excercise 
"""
def take_walk(walk):

    if len(walk) != 10:
        return False
    return walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

print(take_walk(['n', 'n', 'w', 's', 'n', 's', 'n', 's', 'e', 's']))
"""
# My solution to the odd_times excersie
"""
def odd_times(arr):

    odd = next(x for x in arr if arr.count(x) % 2 != 0)

    return odd

print(odd_times([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
"""
# My solution for the Needle in the Haystack excercise
"""
def find_needle(arr):

    position = next(i for i, x in enumerate(arr) if x == 'needle')

    return f"found the needle at position {position}"

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
"""
# another solution for the Needle in the Haystack excercise
"""
def find_needle(arr):
    return f'found the needle at position {arr.index("needle")}'
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
"""
# My solution for the year_century excercise
"""
def century(year):
    if len(str(year)) < 3:
        return 1
    elif len(str(year)) == 3:
        return int(str(year)[0]) + 1
    elif int(str(year)[2:4]) in range(1,100):
        return int(str(year)[0:2]) + 1
    else:
        return int(str(year)[0:2])
print(century(100))        
"""
# another solution for the year_century excercise
"""
def century(year):
    return (year + 99) // 100
print(century(2189))
"""
# another solution for the year_century excercise
"""
import math

def century(year):
    return math.ceil(year / 100)
print(century(2189))
"""
# another solution for the year_century excercise
"""
def century(year):
    return -(-year//100)
print(century(2189))
"""
# My solution for the count_sheep excercise
"""
def count_sheep(num):

    to_list =list(range(1,num+1))
    text =list(['sheep...'] * num)
    zipped = dict(zip(to_list,text))
    concatenated_string = "".join(f"{key} {value}" for key, value in zipped.items())
    
    return concatenated_string
   
print(count_sheep(10))
"""
# another solution for the count_sheep excercise
"""
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))
print(count_sheep(10))
"""
# another solution for the count_sheep excercise
"""
def count_sheep(n):
    return "".join("{} sheep...".format(i) for i in range(1, n+1))
print(count_sheep(10))
"""
# My solution for the x_o exercise (True or false)
"""
def x_o(s):

    return s.casefold().count("x") == s.casefold().count("o")
       
print(x_o("ooxx"))
"""
# My solution for the valid_pin exercise (True or false)
"""
def valid_pin(s):

    if not s.isdigit():

        return False
    else:
       return len(s) == 4 or len(s) == 6

print(valid_pin('.234'))
"""
# another solution (Gemini) for the valid_pin exercise (True or false)
"""
def valid_pin(s):
    
    return s.isdigit() and (len(s) == 4 or len(s) == 6)

print(valid_pin('.234'))
"""
# another solution by a warrior for the valid_pin exercise (True or false), using Regex (spell) tools
# \d: This means "Digit." It looks for any number from 0 to 9.,
# {4}: This means "Exactly 4 times."
# |: This is the OR operator.
# \d{6}: This means "Exactly 6 digits."
"""
import re

def valid_pin(pin):
    
    return bool(re.fullmatch(r"\\d{4}|\\d{6}", pin")) # r and double backslash are added to prvent the parsing msg in the console

print(valid_pin('.234'))
"""
# My solution for the printer_error excercise
"""
def printer_error(s):

    colors = 'abcdefghijklm'
    cs = s.casefold()
    counter = 0

    if cs.isalpha() and len(cs) >= 1:
        for x in cs:
            if x not in colors:
                counter += 1
    
    return f'{counter}/{len(cs)}'    

print(printer_error('aaaabbbb'))
"""
# another solution (Gemini) for the printer_error excercise
"""
def printer_error(s):
    errors = 0
    for char in s:
        if char > 'm': # This catches n, o, p... all the way to z!
            errors += 1
    return f"{errors}/{len(s)}"
print(printer_error('aaaabbbbxx'))
"""
# another solution (Gemini) for the printer_error excercise The "One-Liner" (Generator Expression)
"""
def printer_error(s):
    # Count 1 for every character that is greater than 'm'
    errors = sum(1 for char in s if char > 'm')
    return f"{errors}/{len(s)}"
print(printer_error('aaaabbbbxx'))
"""
# My solution for the sum_without_min_max excercise (using sorted)
"""
def sum_array(arr):
        
    if len(arr) > 1:
        return sum(sorted(arr)[1:-1])
    
print(sum_array([6, 2, 1, 8, 10]))
"""
# another solution for the sum_without_min_max excercise (smae as mine but in one line)
"""
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0
print(sum_array([6, 2, 1, 8, 10]))
"""
# another solution for the sum_without_min_max excercise (using min and max)
"""
def sum_array(arr):
    return sum(arr) - max(arr) - min(arr) if arr and len(arr) > 1 else 0        
print(sum_array([6, 2, 1, 8, 10]))
"""
# My solution for the greeting message excercise
"""
def greeting(name,owner):

    return 'Hello boss' if name == owner else 'Hello guest'

print(greeting('nawar','ali'))
"""
# My solution for the make_upper_case excercise
"""
def make_upper_case(s):

    return s.upper()

print(make_upper_case('nawarhassan'))
"""
# My solution for the find_average excercise
"""
def find_average(arr):

    return sum(arr) / len(arr) if len(arr) > 0 else 0

print(find_average([10, 20, 30, 40]))
"""
# My solution of the is_isogram excercise
"""
def is_isogram(s):

    return True if len(set(s.lower())) == len(s.lower()) else False

print(is_isogram('nawar'))
"""
# A solution by a warrior for the delete_nth excercise (using counter module from collections)
"""
from collections import Counter

def delete_occurrences(arr,n):

    count = Counter()
    result = []
    
    for x in arr:
        if count[x] < n:
            result.append(x)
            count[x] += 1
    
    return result

print(delete_occurrences([1,2,3,1,2,1,2,3,5],2))
"""
# A solution by a warrior for the delete_nth excercise (according to Gemini although it is simple but it is a heavy weight
#  on the memory coz the computor has to make a lot of scans)
"""
def delete_nth(arr,n):
    result = []
    for x in arr:
        if result.count(x) < n: result.append(x)
    return result
print(delete_nth([1,2,3,1,2,1,2,3,5],2))
"""
# A solution by Gemini for the delete_nth excercise (using dictionary having a light weight o(1))
"""
def delete_nth(arr, n):
    result = []
    counts = {} # This is our "Scoreboard"
    
    for x in arr:
        # Get the current count from the scoreboard, or 0 if not there
        current_count = counts.get(x, 0)
        
        if current_count < n:
            result.append(x)
            counts[x] = current_count + 1 # Update the scoreboard
            
    return result
print(delete_nth([1,2,3,1,2,1,2,3,5],2))
"""
# My solution for the find_smallest_int excercise
"""
def find_smallest_int(arr):

    if len(arr) > 0:
         return sorted(arr)[0] 

print(find_smallest_int([34, -345, -1, 100]))
"""
# another solution for the find_smallest_int excercise
"""
def find_smallest_int(arr):
    return min(arr)
print(find_smallest_int([34, -345, -1, 100]))
"""
# another solution for the find_smallest_int excercise
"""
find_smallest_int=min   
print(find_smallest_int([34, -345, -1, 100]))
"""
# My solution for double_char excercise
"""
def double_char(s):

    double = [] # or return ''.join(x * 2 for x in s )
    return ''.join(double)

print(double_char("Hello World"))
"""
# My solution for count_smileys excercise
"""
def count_smileys(arr):
  
    eyes  = [':' , ';']
    nose  = ['-' , '~']
    mouth = [')' , 'D']
    count = []
    
    if not arr:
        return 0
    else:
        for x in arr:
    
            if len(x) == 3:
                if x[0] in eyes and x[1] in nose and x[2] in mouth:
                    count.append(x)
                    
            elif len(x) == 2:
                if x[0] in eyes and x[1] in mouth:
                    count.append(x) 
              
    return len(count)     
    
print(count_smileys([':oD', ';D', ';-D', ';(', ';-D', ':-D', ':-D', ':(', ';D', ':D', ';-(', ';(', ':(', ':oD', ';-(']))
"""
# Gemini's of my solution for count_smileys excercise (no need for if arr condition and append 1 instead to x)
"""
def count_smileys(arr):
    eyes = ":;"
    noses = "-~"
    mouths = ")D"
    count = 0

    for face in arr:
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouths:
                count += 1
        elif len(face) == 3:
            if face[0] in eyes and face[1] in noses and face[2] in mouths:
                count += 1
    return count
print(count_smileys([':oD', ';D', ';-D', ';(', ';-D', ':-D', ':-D', ':(', ';D', ':D', ';-(', ';(', ':(', ':oD', ';-(']))
"""
# Gemini one liner solution for count_smileys excercise (using Regex / findall)
"""
import re

def count_smileys(arr):
    # Pattern: [eyes] [optional nose] [mouth]
    # [;:]    -> find one of these
    # [-~]?   -> find one of these, but it's optional (?)
    # [)D]    -> find one of these
    return len(re.findall(r"[:;][-~]?[)D]", " ".join(arr)))
print(count_smileys([':oD', ';D', ';-D', ';(', ';-D', ':-D', ':-D', ':(', ';D', ':D', ';-(', ';(', ':(', ':oD', ';-(']))
"""
# another solution by a wrrior one liner solution for count_smileys excercise (he used set because the search is faster
# in sets 0(1) than lists 0(n)), he used '' in the nose list meaning if it was not available, he builds the pattern and
#  checks the list against it. It is very clever but not good for large # of items, but it is memory efficient and compact.
"""
def count_smileys(arr):
    smiles = set([a+b+c for a in ":;" for b in ['','-', '~'] for c in ")D"])
    return len([1 for s in arr if s in smiles])
print(count_smileys([':oD', ';D', ';-D', ';(', ';-D', ':-D', ':-D', ':(', ';D', ':D', ';-(', ';(', ':(', ':oD', ';-(']))
"""
# another solution by a wrrior one liner solution for count_smileys excercise (the winner/blackbelt for efficiency and "cool factor."). 
# using Boolean Algebra and Slicing to compress 10 lines of logic into a single mathematical expression. Using the lambda 
# (The Ghost Function), instead of def count_smileys(a):, they used lambda a:. Since this code return booleans so it used sum
# to claculate the 1s for the True & 0 for the False.
"""
count_smileys = lambda a : sum(s and s[0] in ':;' and s[-1] in ')D' and s[1:-1] in ('','-','~') for s in a)
print(count_smileys([':oD', ';D', ';-D', ';(', ';-D', ':-D', ':-D', ':(', ';D', ':D', ';-(', ';(', ':(', ':oD', ';-(']))
"""
# My solution for the count_characters in a string excercise
"""
def count(s):
    char = []
    count = []
    
    for x in s:
        char.append(x)
        count.append(s.count(x))
    return dict(zip(char,count))
    
print(count('lolo'))
"""
# another solution for the count_characters in a string excercise
"""
from collections import Counter

def count(string):
    return Counter(string)
print(count('lolo'))
"""
# another solution for the count_characters in a string excercise
"""
def count(s):
    return {x:s.count(x) for x in set(s)}
print(count('lolo'))
"""
# My solution to the Convert number to reversed array of digits excercise
"""
def digitize(num):

    return list(map(int,reversed(str(num))))

print(digitize(35231))
"""

"""
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
print(digitize(35231))
"""
# My solution for persistence excercise (refined by Gemini)
"""
def persistence(num):

    new = str(num)
    count = 0

    while len(new) > 1:
        product = 1
        for x in new:
            product *= int(x)         
            
        new = str(product) 
        count += 1

    return count       
        
print(persistence(999))
"""
# another solution by Gemini for persistence excercise (using math.prod and map)
"""
import math

def persistence(num):
    new = str(num)
    count = 0
    while len(new) > 1:
        # تحويل الحروف لأرقام وضربها مباشرة
        product = math.prod(map(int, new))
        new = str(product)
        count += 1
    return count
print(persistence(999))
"""
# My solution for fake_bin excercise
"""
def fake_bin(s):
  
    new = ''.join([d.replace(d,'1') if int(d) > 4 else d.replace(d,'0') for d in s ])
  
    return new

print(fake_bin('9483'))
"""
# another solution for fake_bin excercise
"""
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
print(fake_bin('9483'))
"""
# another solution for fake_bin excercise (using translate and maketrans)
"""
def fake_bin(s):
    return s.translate(s.maketrans('0123456789', '0000011111'))
print(fake_bin('9483'))
"""
# another solution for fake_bin excercise (using translate and maketrans)
"""
def fake_bin(x):
    map = str.maketrans('123456789', '000011111')
    return x.translate(map)
print(fake_bin('9483'))
"""
# another solution for fake_bin excercise (mathematical, Integer Division (floor division) for 1 and 0)
"""
def fake_bin(x):
    return ''.join([str(int(i) // 5) for i in x])
print(fake_bin('9483'))
"""
# My solution for the will_you_make_it exercise
"""
def zero_fuel(dist,gal,mpg):

    return (True if gal * mpg >= dist else False)

print(zero_fuel(50,1,25))
"""
# My solution for the convert a number to a list exercise
"""
def convert(arr):
    return f"'{str(arr)}'"
print(convert(-100))
"""
# My solution for the filter_list exercise
"""
def filter_list(arr):
    new_list = []
    for x in arr:
        if not isinstance(x,str):
            new_list.append(x)
    return new_list

print(filter_list([1,'a','b',0,15]))
"""
# My solution for the filter_list exercise
"""
def filter_list(arr):
    return [x for x in arr if not isinstance(x,str)]

print(filter_list([1,'a','b',0,15]))
"""
# My solution for the filter_list exercise
"""
def filter_list(l):  
  return [x for x in l if type(x) is not str]
print(filter_list([1,'a','b',0,15]))
"""
# my solution to the replace_alpha with numbers excercise (using dictionary, not recommended by Gemini
# coz it takes time to make the dictionary while there are other built in methods to do the job which are more efficient)
"""
def replace_alpha(s):

# This is the "Dictionary Comprehension" to create the same but automatically:
#mapping = {char: str(i + 1) + " " for i, char in enumerate(string.ascii_lowercase)}
#print(mapping) {'a': '1 ', 'b': '2 ', 'c': '3 ', 'd': '4 ', 'e': '5 ', 'f': '6 ', 'g': '7 ', 'h': '8 ', 'i': '9 ', 'j': '10 ', 'k': '11 ', 'l': '12 ', 'm': '13 ', 'n': '14 ', 'o': '15 ', 'p': '16 ', 'q': '17 ', 'r': '18 ', 's': '19 ', 't': '20 ', 'u': '21 ', 'v': '22 ', 'w': '23 ', 'x': '24 ', 'y': '25 ', 'z': '26 '}
    
    dic = {'a':1,'b':2,'c':3,'d':4,'e':5,
           'f':6,'g':7,'h':8,'i':9,'j':10,
           'k':11,'l':12,'m':13,'n':14,'o':15,
           'p':16,'q':17,'r':18,'s':19,'t':20,
           'u':21,'v':22,'w':23,'x':24,'y':25,
           'z':26,'A':1,'B':2,'C':3,'D':4,
           'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
           'K':11,'L':12,'M':13,'N':14,'O':15,
           'P':16,'Q':17,'R':18,'S':19,'T':20,
           'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    return ' '.join([str(dic.get(x,'')) for x in s if x in dic])
    # or return ' '.join(map(str,[dic.get(x,'') for x in s if x in dic]))  

print(replace_alpha("The sunset sets at twelve o' clock.")) # 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
"""
# Gemini solution to the replace_alpha with numbers excercise (using ord() - 96 /built-in ASCII math to replace
#  letters with numbers/ and isalpha(), whild chr() does the opposit by turning numbers to letters )
"""
def replace_alpha(s):
    # 1. We only care about letters
    # 2. We turn them lowercase
    # 3. We use ord() to get the position
    return ' '.join(str(ord(c) - 96) for c in s.lower() if c.isalpha())
print(replace_alpha("The sunset sets at twelve o' clock.")) # 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
"""
# another solution to the replace_alpha with numbers excercise (using maketrans and translation)
"""
import string

def replace_alpha(s):
    # 1. Create the mapping: {'a': '1 ', 'b': '2 ', ...}
    # We use a dictionary comprehension to build this map automatically
    alphabet = string.ascii_lowercase
    mapping = {char: str(i+1) + " " for i, char in enumerate(alphabet)}
    
    # 2. Build the translation table
    table = str.maketrans(mapping)
    
    # 3. Translate the lowercase version of the string
    # .strip() removes the very last trailing space
    return s.lower().translate(table).strip()
print(replace_alpha("The sunset sets at twelve o' clock.")) 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
"""
# My solution for the min_max excercise
"""
def min_max(arr):
    
    return [sorted(arr)[0],sorted(arr)[-1]]

print(min_max([2334454,5]))
"""
# another solution for the min_max excercise
"""
def min_max(lst):
  return [min(lst), max(lst)]
print(min_max([2334454,5]))
"""
# My solution for the find_short excercise (return shortest word)
"""
def find_short(s):      
   
    return min(list(s.split(' ')),key=len)

print(find_short('nawar is still a beginner in python'))
"""
# My solution for the find_short excercise (return shortest length)
"""
def find_short(s):      
   
    return  len(min(list(s.split(' ')),key=len))

print(find_short('nawar is still a beginner in python'))
"""
# another solution for the find_short excercise (return shortest length)/same as mine
"""
def find_short(s):
    return min(len(x) for x in s.split())
print(find_short('nawar is still a beginner in python'))
"""
# My solution for the Break camelCase excercise (fixed by Gemini)
"""
def solution(s):

    new = ''

    for x in s:
        if x.isupper():
            new += ' ' + x
        else:
            new += x
    return new

print(solution("long BigChildGreat"))
"""
# another solution by another player for the Break camelCase excercise 
"""
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
print(solution("long BigChildGreat"))
"""
# another solution by another player for the Break camelCase excercise
"""
import re
def solution(s):

    # (?<! ) is a "negative lookbehind" 
    # It says: "Match a capital letter ONLY if there isn't already a space before it"
    #([A-Z]): This is a capturing group that matches any single uppercase letter.
    #r' \1': The replacement string. The \1 is a backreference to whatever letter was captured in the
    #  first group. It essentially says: "Take that capital letter and put a space in front of it."
    
    return re.sub(r'(?<! )([A-Z])', r' \1', s)

print(solution("long BigChildGreat"))
"""
#---------------------------------------------------------------
# 5kyu
#---------------------------------------------------------------

# Gemini solution for the nested functions challange (manual one)
"""
def zero(operation=None):
    if operation is None:
        return 0
    return operation(0)

def one(operation=None):
    if operation is None:
        return 1
    return operation(1)

def two(operation=None):
    if operation is None:
        return 2
    return operation(2)

def three(operation=None):
    if operation is None:
        return 3
    return operation(3)

def four(operation=None):
    if operation is None:
        return 4
    return operation(4)

def five(operation=None):
    if operation is None:
        return 5
    return operation(5)

def six(operation=None):
    if operation is None:
        return 6
    return operation(6)

def seven(operation=None):
    if operation is None:
        return 7
    return operation(7)

def eight(operation=None):
    if operation is None:
        return 8
    return operation(8)

def nine(operation=None):
    if operation is None:
        return 9
    return operation(9)

def times(right_operand):
   
    return lambda left_operand: left_operand * right_operand
def plus(right_operand):
    
    return lambda left_operand: left_operand + right_operand
def minus(right_operand):
    
    return lambda left_operand: left_operand - right_operand
def divided_by(right_operand):
    
    return lambda left_operand: left_operand // right_operand

print(four(plus(nine())))
"""
# Gemini solution for the nested functions challange (using function factory method for a shorter code)
"""
def number_factory(n):
    return lambda op=None: n if op is None else op(n)

zero  = number_factory(0)
one   = number_factory(1)
two   = number_factory(2)
three = number_factory(3)
four = number_factory(4)
five = number_factory(5)
six = number_factory(6)
seven = number_factory(7)
eight = number_factory(8)
nine = number_factory(9)

def times(right_operand):   
    return lambda left_operand: left_operand * right_operand

def plus(right_operand):    
    return lambda left_operand: left_operand + right_operand

def minus(right_operand):    
    return lambda left_operand: left_operand - right_operand

def divided_by(right_operand):    
    return lambda left_operand: left_operand // right_operand

print(four(plus(nine())))
"""
# Gemini solution for the nested functions challange (using globals() method for even a more shorter code)
"""
def number_factory(n):
    return lambda op=None: n if op is None else op(n)

names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i, name in enumerate(names):
    globals()[name] = number_factory(i)

def times(right_operand):   
    return lambda left_operand: left_operand * right_operand

def plus(right_operand):    
    return lambda left_operand: left_operand + right_operand

def minus(right_operand):    
    return lambda left_operand: left_operand - right_operand

def divided_by(right_operand):    
    return lambda left_operand: left_operand // right_operand

print(four(plus(nine())))
"""
# another solution by a warrior for the nested functions challange (one line functions and lambda)
"""
def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

print(four(plus(nine())))
"""
# My solution for the compare lists excercise
"""
def comp(a,b):
    if a is None or b is None:
        return False
    result = list(map(lambda y: y**2, a))
    return True if sorted(result) == sorted(b) else False

print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 14641, 20736, 361, 25921, 361, 20736, 361])) # True
"""
# Gemini solution for the compare lists excercise
"""
def comp(a,b):
    if a is None or b is None:
        return False   
    return sorted([x*x for x in a]) == sorted(b)
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 14641, 20736, 361, 25921, 361, 20736, 361])) # True
"""
# another solution for the compare lists excercise (using try & except)
"""
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 14641, 20736, 361, 25921, 361, 20736, 361])) # True
"""
# another solution for the compare lists excercise (Short-Circuiting one-liner clever pythonic and efficeint one)
"""
def comp(a, b):
    return None not in (a,b) and [i*i for i in sorted(a)]==sorted(b)
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 14641, 20736, 361, 25921, 361, 20736, 361])) # True

# None not in (a, b) creates a small tuple (a, b). It then checks if the value None is inside that tuple. 
# The Result: If a1 is None or a2 is None, this part returns False. Because of the and, the rest of the code won't even run,
# and the whole function returns False
"""
# My solution for the friends =4letters excercise (using filter and lambda)
"""
def friend(arr):
    
        return list(filter(lambda y: len(y) == 4 if y.isalpha() else False, arr))
        
print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
"""
# Gmini's refinement of my solution for the friends =4letters excercise (using and instead of if/else)
"""
def friend(arr):    
    return list(filter(lambda y: y.isalpha() and len(y) == 4, arr))
print(friend(["Ryan", "Kieran", "Jason", "Yous"])) # ['Ryan']
"""
# Gmini's refinement of my solution for the friends =4letters excercise (using list comprehension)
"""
def friend(arr):
    return [name for name in arr if len(name) == 4 and name.isalpha()]
print(friend(["Ryan", "Kieran", "Jason", "Yous"])) # ['Ryan']
"""
# another simillar challange but from Gemini to use additional condition with .upper() / a sample on Tranforming data
"""
def friend(arr):
    return [name.upper() for name in arr if len(name) == 5 and name[0].upper() == 'R' and name.isalpha()] # we can use startswith(('R', 'r')) instead
print(friend(["Rhyan", "razan", "Kieran", "Jason", "Yous"])) # ['RHYAN', 'RAZAN']
"""
# another simillar challange but from Gemini to use additional condition with .upper() / a sample on agrigating data
"""
def friend(arr):
    friends = [name.upper() for name in arr if len(name) == 5 and name[0].upper() == 'R' and name.isalpha()]
    return len(friends)
print(friend(["Rhyan", "razan", "Kieran", "Jason", "Yous"])) # 2
"""
# another way of the count friend suggested by Gemini using the sum generator (we replace the sqare brackets 
# with normal ones and instead of name we put 1), coz in Python, True is equal to 1 and False is equal to 0, s
# um is the most memory-efficient way to count in Python
"""
def friend(arr):
    # This 'sums' up a 1 for every name that meets the criteria
    return sum(1 for name in arr if len(name) == 5 and name[0].upper() == 'R' and name.isalpha())
print(friend(["Rhyan", "razan", "Kieran", "Jason", "Yous"])) # 2
"""
# using the same example in Dictionary Comprehensions to show the name and its length in a search-friendly dictionary data structure
"""
def friend(arr):
    # This 'sums' up a 1 for every name that meets the criteria
    return {name: len(name) for name in arr if len(name) == 5 and name[0].upper() == 'R' and name.isalpha()}
print(friend(["Rhyan", "razan", "Kieran", "Jason", "Yous"])) # {'Rhyan': 5, 'razan': 5}
"""
# My solution for the turn a string into a list (simple 8kyu)
"""
def string_to_array(s):

    return list(s.split(" "))

print(string_to_array("I love arrays they are my favorite"))
"""
# My solution for the return difference in arrays excercise (using lambda)
"""
def array_diff(a,b):

    return list(filter(lambda i: str(i) if i not in b else '',a))

print(array_diff([10, 20, 19, 0, 4, 11, 1, -17, -19, 17, 12, -14, 19, 7, -13, 9],
 [-16, 7, -8, -10, -15, -3, -18, 17, -13, 14, 20, -13, 19, -7, -17, 8, 1, -7, -2, -2])) # [10, 0, 4, 11, -19, 12, -14, 9]
"""
# another solution for the return difference in arrays excercise (simple one liner)
"""
def array_diff(a, b):
    return [x for x in a if x not in b]
print(array_diff([10, 20, 19, 0, 4, 11, 1, -17, -19, 17, 12, -14, 19, 7, -13, 9],
 [-16, 7, -8, -10, -15, -3, -18, 17, -13, 14, 20, -13, 19, -7, -17, 8, 1, -7, -2, -2])) # [10, 0, 4, 11, -19, 12, -14, 9]
"""
# My solution for the rot13 excercise (used previous code on freeCodeCamp)
"""
def rot13(text):
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    next = -13    
    
    next_char = abc[next:] + abc[:next]
    table = str.maketrans(abc + abc.upper(), next_char + next_char.upper())
    coded_txt = text.translate(table)
    
    return coded_txt

print(rot13("@anjne71!")) # nawar
"""
# another solution for the rot13 excercise
"""
import string

def rot13(message):
    output = ''
    for l in message:
        if l.islower():
            output += string.ascii_lowercase[(ord(l) - ord('a') + 13) % 26]
        elif l.isupper():
            output += string.ascii_uppercase[(ord(l) - ord('A') + 13) % 26]
        else:
            output += l
            
    return output
print(rot13("@anjne71!")) # nawar
"""
# another solution for the rot13 excercise
"""
def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                               'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
print(rot13("@anjne71!")) # nawar
"""
# My solution for the the tower_builder (star identation is from the left, but did not pass all Codewar tests)
"""
def tower_builder(n):

    floors = list(range(0,n))                            
    
    draw = list(map(lambda x: f"{' ' * (n - x - 1)}{(x * 2 + 1) * '*'}",floors))
    
    return draw    
 
print(*tower_builder(10),sep="\n")
"""
# Gemini fix to my solution for the tower_builder (star identation is centered, passed all Codewar tests)
"""
def tower_builder(n):
    floors = range(n)

    draw = [f"{' ' * (n - x - 1)}{(x * 2 + 1) * '*'}{' ' * (n - x - 1)}" for x in floors]
    return draw
print(*tower_builder(10), sep="\n")
"""
# Gemini solution for the the tower_builder (star identation is centered, passed all Codewar tests)
"""
def tower_builder(n):
    floors = range(n)
    width = n * 2 - 1 # This is the max width of the bottom floor
    
    # 1. Calculate the stars: (x * 2 + 1)
    # 2. Use .center(width) to pad both sides with spaces
    draw = [((x * 2 + 1) * '*').center(width) for x in floors] # Cleanest way to center text in Python.
    
    return draw

# Now when you print it, it looks the same to us, 
# but Codewars sees the hidden spaces on the right!
print(*tower_builder(10), sep="\n")
"""
# another solution by a warrior for the the tower_builder (star identation is centered, passed all Codewar tests).
# as per Geminin this is the Gold Standard solution for this Kata! It’s elegant, readable, and highly efficient.
# The reason it feels "simpler" is that it uses natural numbering instead of zero-based indexing.
"""
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
print(*tower_builder(10), sep="\n")
"""
#To make a diamond using the same tower code + mirroring it to make the below opposite part
"""
def tower_builder(n):
    floors = range(n)

    draw = [f"{' ' * (n - x - 1)}{(x * 2 + 1) * '*'}{' ' * (n - x - 1)}" for x in floors]
    low = draw[:-1][::-1]  # this is the mirror part of the top part
    return draw + low      # important to use '+' not ','
print(*tower_builder(10), sep="\n")
"""
# This is another variation, a dimaond of letters using ASCII (65 for upper, 97 for lower, any starting letter we use: ord('Character'))
"""
import string
def tower_builder(n):
    floors = range(n)

    draw = [f"{' ' * (n - x - 1)}{(x * 2 + 1) * chr(65+x)}{' ' * (n - x - 1)}" for x in floors] # we used 65 for uppercase and 97 for lower case
    low = draw[:-1][::-1]
    return draw + low
print(*tower_builder(5), sep="\n")
"""
# My solution for the find_the_other_angle of a triangle excercise
"""
def other_angle(a,b):

    if a and b > 0:
        return 180-(a+b)

print(other_angle(60,60))
"""
# Another solution for the find_the_other_angle of a triangle excercise
"""
def other_angle(a,b):
    return 180 - a - b
print(other_angle(60,60))
"""
# My solution for the find_quarter for a month exercise
"""
def quarter_of(month):
    return (((month - 1) // 3) + 1, if 1 <= month <= 12))
print(quarter_of(12)) # 4
"""
# Another solution for the find_quarter for a month exercise
"""
def quarter_of(month):
    return (month + 2) // 3
print(quarter_of(12)) # 4
"""
# My solution for the find two_sum = target excercise
"""
def two_sum(arr,target):
    
    for x in arr:
        if target - x in arr and arr.index(target - x) != arr.index(x):
           return arr.index(x),arr.index(target-x)
        elif x == target - x and arr.count(x) > 1:
            return arr.index(x),arr.index(target-x)+1
        
print(two_sum([2, 2, 3], 4)) # Output: (0, 1)
"""
#Gemini solution for the find two_sum = target excercise using enumerate
"""
def two_sum(arr, target):
    # i is the index, x is the value
    for i, x in enumerate(arr):
        needed = target - x
        
        # Look for the 'needed' number in the REST of the list
        # starting from the next position (i + 1)
        if needed in arr[i+1:]:
            # Get the index of the 'needed' number, 
            # but only searching from i+1 onwards
            return i, arr.index(needed, i + 1)

print(two_sum([2, 2, 3], 4)) # Output: (0, 1)
"""
# another Gemini solution for the find two_sum = target excercise (using dictonary for remembering indexes)
"""
def two_sum(arr, target):
    seen = {} # Number : Index
    
    for i, x in enumerate(arr):
        needed = target - x
        if needed in seen:
            return seen[needed], i
        
        # Store the current number and its index for later
        seen[x] = i

print(two_sum([2, 2, 3], 4)) # Output: (0, 1)
"""
# Another solution by a warrior for the find two_sum = target excercise (but not recommended by Gemini due to o(n)2, due to several loops)
"""
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
print(two_sum([2, 2, 3], 4)) # Output: (0, 1)
"""
# My solution for the return even_or odd excercise
"""
def even_or_odd(arr):

    return ['Even' if x % 2 == 0 else 'Odd' for x in arr]

print(even_or_odd([1,2,3,5,6,4,8,7])) # ['Odd', 'Even', 'Odd', 'Odd', 'Even', 'Even', 'Even', 'Odd']
"""
# An excercise by Gemini to master the use of the bucket
# write a function called contains_nearby_duplicate(arr, k). It should return True if there are two same numbers
# in the list and the distance between their indices is less than or equal to k.
"""
def contains_nearby_duplicate(arr, k):
    memory = {} # Our Memory Bank (Number : Last seen Index)

    for i, x in enumerate(arr):
        if x in memory:
            # 1. Grab the PREVIOUS index from our bucket
            old_index = memory[x]
            
            # 2. Check the distance between current (i) and old
            if i - old_index <= k:
                return old_index, i
        
        # 3. ALWAYS update the memory with the latest position of x
        memory[x] = i
    
    return False # Return False if no nearby duplicates found

print(contains_nearby_duplicate([10, 20, 30, 20, 50, 10], 3)) # Output: (1, 3)
"""
# An excercise by Gemini to master the use of the bucket. The "First Non-Repeating Character" challenge (Common 5kyu/6kyu)
# Task: Find the first character in a string that appears only once and return its index.
# Hint: You might need two passes—one to count how many times each letter appears in the "Bucket", and a second to see 
# which one has a count of 1
"""
def first_non_repeating(arr):
    counts = {} # Our "Counter" Bucket
    
    # PASS 1: Fill the bucket with counts
    for x in arr:
        # If x is in counts, add 1. If not, start at 0 and add 1.
        counts[x] = counts.get(x, 0) + 1
    
    # counts now looks like: {10: 2, 20: 2, 30: 2, 50: 1}

    # PASS 2: Find the first one with a count of 1
    for i, x in enumerate(arr):
        if counts[x] == 1:
            return x, i # Found it!
            
    return None # Everyone repeats!

print(first_non_repeating([10, 20, 30, 20, 50, 10, 30])) # Output: (50, 4)
"""
# My solution for the Testing 1-2-3 excercise using dictionary key, value
"""
def number(arr):    
        
    lines = {i+1:x for i, x in enumerate(arr)}
    result = [f"{k}: {v}" for k, v in lines.items()]
        
    return result

print(number(["a", "b", "c"])) # ['1: a', '2: b', '3: c']
"""
# Another solution by another warrior for the Testing 1-2-3 excercise using dictionary key, value (but one liner/very Pythonic/new f-string school)
"""
def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
print(number(["a", "b", "c"])) # ['1: a', '2: b', '3: c']
"""
# Another solution by another warrior for the Testing 1-2-3 excercise text formatting tools (old school), it is not a Regex '%d: %s': This is the template.
# %d: A placeholder for a Decimal (integer). %s: A placeholder for a String. % v: The % here tells Python: "Take the data
# in the variable v and plug it into those placeholders." enumerate(lines, 1): This creates tuples like (1, "a").
# The 1 goes into %d.The "a" goes into %s.
"""
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
print(number(["a", "b", "c"])) # ['1: a', '2: b', '3: c']
"""
# Gemini solution for the direction reduction excercise (I could not solve it)
"""
def dir_reduc(arr):

    bad  = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    #good = []
    
    result = {arr[i]: arr[i+1] for i in range(len(arr) - 1)}
    
    return result
print(dir_reduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"])) # Output: ['WEST']
"""
# Gemini solution for the direction reduction excercise (another one using stack)
"""
def dir_reduc(arr):
    # 1. Your 'bad' dictionary is perfect for checking opposites
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    
    stack = []
    
    for direction in arr:
        # 2. Check if the stack has something AND if it's the opposite of current
        if stack and stack[-1] == opposites[direction]:
            # They cancel out! Remove the last one.
            stack.pop()
        else:
            # They don't cancel out, so save this direction
            stack.append(direction)
            
    return stack

print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) # Output: ['WEST']

"""
# Another solution by a warrior for the direction reduction excercise
"""
def dir_reduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dir_reduc(dir3) if len(dir3) < len(arr) else dir3
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) # Output: ['WEST']
"""
# My solution to the "Sum of the first nth term of Series" excercise (but did not pass/wrong apporach did not understand the requested)
"""
from fractions import Fraction

def series_sum(n):
    series = '1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16'
    return f"{sum([float(Fraction(x)) for x in series.split('+')][0:n]):,.2f}"    
print(series_sum(5))
"""
# Gemini's solution to the "Sum of the first nth term of Series" excercise
# Each denominator is exactly 3 more than the previous one. Mathematically, the $i$-th denominator is $1 + 3 \times i$.
"""
def series_sum(n):
    # Handle the '0' case immediately
    if n == 0:
        return "0.00"
    
    total = 0.0
    # We loop 'n' times to get 'n' terms
    for i in range(n):
        # Denominator starts at 1, then 4, then 7...
        # When i=0: 1 + (3*0) = 1
        # When i=1: 1 + (3*1) = 4
        # When i=2: 1 + (3*2) = 7
        denominator = 1 + (3 * i)
        total += 1 / denominator   # a standard float math
        
    # Formatting to 2 decimal places as a string
    return f"{total:.2f}"

print(series_sum(5)) # Output: 1.57
"""
# Gemini's solution to the "Sum of the first nth term of Series" excercise (one liner f-string)
"""
def series_sum(n):
    return f"{sum(1 / (1 + 3 * i) for i in range(n)):.2f}"
print(series_sum(5)) # Output: 1.57
"""
# Another warrior solution to the "Sum of the first nth term of Series" excercise
"""
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
print(series_sum(5)) # Output: 1.57
"""
# My solution for the simple find age in a string excercise
"""
def parse_char(s):
    
    return int(s[0])

print(parse_char("5 years old"))
"""
# My solution to the "Build a pile of Cubes" excercise (did not pass all Codewar tests)
"""
import math

def find_nb(m):
    if isinstance (m,int):
        return int((math.sqrt((math.sqrt(m)*2)*4+1)-1)/2)
    else:
        return -1
print(find_nb(1071225))
"""
# Gemini solution to the "Build a pile of Cubes" excercise (building block by blocck to reach the m volume)
"""
def find_nb(m):

    total_volume = 0
    n = 0

    # Keep adding cubes until we hit or pass 'm'
    while total_volume < m:
        n += 1
        total_volume += n**3
        
    # If we hit it exactly, return n. If we went past it, return -1.
    return n if total_volume == m else -1

print(find_nb(1071225)) # Output: 45
"""
# Another solution by a warrior to the "Build a pile of Cubes" excercise (using while loop/Incremental Loop and it is more concise and 
# pythonic as per Gemini) Multiple Assignment (i, sum = 1, 1): Instead of two lines, they initialized both variables at once.
# It’s a common Python shortcut that keeps the code "tight."
"""
def find_nb(m):
    i,sum = 1,1
    while sum < m:
        i+=1
        sum+=i**3
    return i if m==sum else -1
print(find_nb(1071225)) # Output: 45
"""
# My solution to the "Total amount of points" excercise (used split to unpack for x & y)
"""
def points(arr):
    
    total = 0
    if len(arr) >= 10:
        for x in arr:
            if (int(x.split(":")[0]) > int(x.split(":")[1])) and 0 <= int(x.split(":")[0]) <= 4:
                total += 3
            elif (int(x.split(":")[0]) == int(x.split(":")[1])) and 0 <= int(x.split(":")[0]) <= 4:
                total += 1            
            else:
                total += 0
    
    return total
print(points(["3:1", "4:1", "0:1","4:2","2:1","1:0","0:2","3:3","2:2","1:1"])) # 18
"""
# Gemini's solution (refined of mine) to the "Total amount of points" excercise (used split to unpack for x & y)
"""
def points(arr):
    total = 0
    # No need to check len(arr) unless the instructions strictly require it, 
    # as the loop simply won't run if the list is empty.
    
    for match in arr:
        # 1. Split once and unpack into two variables
        x, y = match.split(":")
        
        # 2. Convert to int once
        our_score = int(x)
        their_score = int(y)
        
        # 3. Simple logic
        if our_score > their_score:
            total += 3
        elif our_score == their_score:
            total += 1
            
    return total
print(points(["3:1", "4:1", "0:1","4:2","2:1","1:0","0:2","3:3","2:2","1:1"])) # 18
"""
# A warrior's solution (refined of mine) to the "Total amount of points" excercise
"""
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count
print(points(["3:1", "4:1", "0:1","4:2","2:1","1:0","0:2","3:3","2:2","1:1"])) # 18
"""
# My solution for the pangram excercise (did not pass all the tests in Codewar)
"""
def pangram(s):
    # abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = ''.join(set(s.lower())).replace(' ', '')
       
    return len(new) == 26
  
print(pangram("The quick brown fox jumps over the lazy dog" )) # True
"""
# the refined version of my solution by Copilot for the pangram excercise (passed all the tests in Codewar)
"""
import string
def is_pangram(s):

    new = set(s.lower())
    new = {ch for ch in new if ch in string.ascii_lowercase}
    
    return len(new) == 26
  
print(is_pangram("The quick brown fox jumps over the lazy dog" )) # True
"""
# another solution by a warrior for the pangram excercise
"""
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
print(is_pangram("The quick brown fox jumps over the lazy dog" )) # True
"""
# another solution by another warrior for the pangram excercise
"""
import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
print(is_pangram("The quick brown fox jumps over the lazy dog" )) # True
"""
# another solution by another warrior for the pangram excercise (very efficeint declaritive prgoramming telling the computer
# what is the result I want and not how to reach the result it is a short circuit), the use of 'all' is very powerfull tool, it will
# require that all letter should be present. (i in s.lower() for i in a) is a Generator. It doesn't create a new list in your 
# computer's RAM; it checks the letters one by one, on the fly.
"""
a = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(s):
    return all(i in s.lower() for i in a)
print(is_pangram("The quick brown fox jumps over the lazy dog" )) # True
"""
# My solution supported by Gemini to the Sort the odd in a string excercise
"""
def sort_array(arr):

        # Step 1: Extract and sort odd numbers
    odds = sorted([x for x in arr if x % 2 != 0])

    # Step 2: Reinsert sorted odds into original positions
    result = []
    odd_index = 0
    for x in arr:
        if x % 2 != 0:   # odd number
            result.append(odds[odd_index])
            odd_index += 1
        else:            # even number stays
            result.append(x)
    return result
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""
# Another solution by a warrior to the Sort the odd in a string excercise. we sort the odds by descending coz
# the .pop() if left not specified will delete the last figure, 
"""
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]     # .pop() without arguments removes from the end of the list.
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""
# My solution for the simple double the figures in a list excercise
"""
def doubled(arr):
    return [x * 2 for x in arr]
print(doubled([1, 2, 3]))
"""
# My solution for the simple bus capacity excercise
"""
def enough(cap,on,wait):
    return 0 if cap-(on+wait) >= 0 else abs(cap-(on+wait)) 
print(enough(100,60,50))
"""
# Another solution by a warrior for the simple bus capacity excercise
"""
def enough(cap, on, wait):
    return max(0, on + wait - cap) # The "Floor" Pattern: Use max(0, value) when you want to ensure a number never goes below zero. It effectively "clips" negative results and turns them into 0.
print(enough(100,60,50))
"""
"""
def consecutive(arr):

    return next(y for x in arr for y in arr if y != x + 1)

print(consecutive([1,2,3,4,6,7,8]))
"""
# My solution for the find the first none consecutive number
"""
def first_non_consecutive(arr):

    for i in range(len(arr)-1):
        if arr[i+1] != arr[i] + 1:
            return arr[i] + 2

print(first_non_consecutive([1,2,3,4,6,7,8])) 
"""
# Another solution by a warrior for the find the first none consecutive number
"""
def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]
print(first_non_consecutive([1,2,3,4,6,7,8]))        
"""
# Another solution by a warrior for the find the first none consecutive number
"""
def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None
print(first_non_consecutive([1,2,3,4,6,7,8]))
"""
# My solution for the count duplicates excercise
"""
def duplicate_count(text):
    counter = [x for x in text.lower() if text.lower().count(x) >1]
    return len(set(counter))
print(duplicate_count("F9kH7JA9fb0krCGgBhCRcikit0Lsa3Yrdc2EDFLtgK4hjc1DX95YrFT4b7HpScJ5nehjwN9F")) # 22
"""
# Gemini's solution for the count duplicates excercise. using counter as a faster method as it scans the list once
"""
def duplicate_count(text):
    # 1. Normalize to lowercase
    text = text.lower()
    
    # 2. Use our "Day 2" logic: count everything once
    from collections import Counter
    counts = Counter(text)
    
    # 3. Count how many characters appeared more than once
    duplicates = [char for char, count in counts.items() if count > 1]
    
    return len(duplicates)
print(duplicate_count("F9kH7JA9fb0krCGgBhCRcikit0Lsa3Yrdc2EDFLtgK4hjc1DX95YrFT4b7HpScJ5nehjwN9F")) # 22
"""
# Another solution by a warrior for the count duplicates excercise. (same like mine but a one liner)
"""
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
print(duplicate_count("F9kH7JA9fb0krCGgBhCRcikit0Lsa3Yrdc2EDFLtgK4hjc1DX95YrFT4b7HpScJ5nehjwN9F")) # 22
"""
# My solution for the Count by X excercise.
"""
def count_by(x,n):

    return list(range(x,n*x+x,x)) if x > 0 and n > 0 else []

print(count_by(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# Another solution by a warrior for the Count by X excercise.
"""
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
print(count_by(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# Gemini solution for finding the consecutive Fib numbers (Fibonacci sequence) for a given product

"""
def product_fib(prod):
    # 1. create the Fibonacci sequence, start from the true beginning: 0 and 1
    a, b = 0, 1
    
    # 2. Keep moving as long as the product is too small
    while a * b < prod:
        a, b = b, a + b
    
    # 3. Return as a LIST [a, b, boolean]
    return [a, b, a * b == prod]
print(product_fib(714)) # [21, 34, True]
"""
# Another solution by a warrior for finding the consecutive Fib numbers (Fibonacci sequence) for a given product, (using one liner lambda)
"""
def product_fib(prod):
    func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
    return func(0, 1)
print(product_fib(714)) # [21, 34, True]
"""
# Solution for Grasshopper - Grade Book/the find the grade of 3 given scores
"""
def get_grade(s1, s2, s3):
    
    score = (s1 + s2 + s3) / 3

    grades = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 0: 'F'}

    for threshold, letter in grades.items():
        if score >= threshold:
            return letter

print(get_grade(100, 95, 80)) # A
"""
# Another Solution for Grasshopper - Grade Book/the find the grade of 3 given scores
"""
def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) // 30, 'F')
print(get_grade(100, 95, 80)) # A
"""
# Solution for the Mexican wave in a string (supported by Copilot)
"""
def wave(s):
    wave_s = [s[:i] + s[i].upper() + s[i+1:] for i in range(len(s)) if s[i] != " "]
    return wave_s
print(wave(" s p a c e s ")) # [' S p a c e s ', ' s P a c e s ', ' s p A c e s ', ' s p a C e s ', ' s p a c E s ', ' s p a c e S ']

# s[:i] → everything from the start up to (but not including) position i.
# s[i] → the single character at position i.
# s[i+1:] → everything from position i+1 to the end.
# chars[:] → makes a shallow copy of the entire list/string.The : with no start or end means “take everything from beginning to end.
"""
# Another solution for the Mexican wave in a string (supported by Copilot)
"""
def wave(s):
    return [s[:i].lower() + s[i:].capitalize() for i in range(len(s)) if s[i] != " "]
print(wave(" s p a c e s ")) # [' S p a c e s ', ' s P a c e s ', ' s p A c e s ', ' s p a C e s ', ' s p a c E s ', ' s p a c e S ']
"""
# Another solution for the Mexican wave in a string (supported by Copilot)
"""
def wave(words):
    result = []
    chars = list(words)
    print(chars)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]         # This creates a shallow copy of the list. By making a fresh copy for every loop, the warrior ensures they are only changing one specific letter at a time while the others stay lowercase.
            copy[index] = copy[index].upper()   # The code goes to the specific position (index) in the copy and makes that one letter uppercase.
            result.append(''.join(copy))
    return result
print(wave(" s p a c e s ")) # [' S p a c e s ', ' s P a c e s ', ' s p A c e s ', ' s p a C e s ', ' s p a c E s ', ' s p a c e S ']
"""
# My solution for the simple creating a function to return "hello world!" excercise
"""
def greet():
    return "hello world!"
print(greet())
"""
# My solution to the find divisors for a num excercise
"""
def find_divisors(num):

    counter = 0

    for x in range(1,num+1):
        if num % x == 0:
            counter += 1

    return counter

print(find_divisors(30))    # 8
"""
# Or a one liner (same concept)
"""
def find_divisors(num): 
    return sum(1 for x in range(1, num+1) if num % x == 0)
print(find_divisors(30))    # 8
"""
# My solution for the Duplicate Encoder excercise
"""
def duplicate_encoder(s):

    encoded = ''.join([")" if s.lower().count(x) != 1 else "(" for x in s.lower()])

    return encoded

print(duplicate_encoder("v!RplTn(cMLXWb!hSVcW")) # ))(()((()()()()(()))
"""
# My solution to the sort a string of words by the numbers inside them
"""
def order(words):
    
    new=[]
    
    for x in list(words.split()):
        for y in x:
            if y.isdigit():     # to specify that y is a number not character
                new.append((int(y), x)) # put the number(y)/as integer and the word(x) in one tupple

    return ' '.join([word for _, word in sorted(new)]) # the use of _, here is to ignore anything else in the tupple except the word

print(order("4of Fo1r pe6ople g3ood th5e the2")) # Fo1r the2 g3ood 4of th5e pe6ople
"""
# Another solution of the above by CoPilot using a key for sorting (a lambda that sorts the word itself so the numbers
# becomes at the beggining of the words)
"""
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w))) # the key used for sorting here is the words sorted by their characters g3ood --> 3dgoo
print(order("4of Fo1r pe6ople g3ood th5e the2")) # Fo1r the2 g3ood 4of th5e pe6ople
"""
# Another solution of the above by CoPilot
"""
def order(words):
    # Split into words, sort by the digit inside each word
    return ' '.join(sorted(words.split(), key=lambda w: int(''.join(ch for ch in w if ch.isdigit()))))

print(order("4of Fo1r pe6ople g3ood th5e the2")) # Fo1r the2 g3ood 4of th5e pe6ople
"""
# My solution to find the stray number in arr
"""
def stray(arr):
    return [x for x in arr if len(arr) >=3 and arr.count(x) == 1][0]    # we usd [0] to return 3 not [3]
print(stray([17, 17, 3, 17, 17, 17, 17])) # 3
"""
# Another simple solution to find the stray number in arr (using min and key)
"""
def stray(arr):
    return min(arr, key=arr.count)
print(stray([17, 17, 3, 17, 17, 17, 17])) # 3
"""
# Another solution by a warrior to find the stray number in arr (the XORing tool '^')
"""
def stray(arr):
    s = 0
    for n in arr:
        s^=n        
    return s
print(stray([17, 17, 3, 17, 17, 17, 17])) # 3
# ---- XORing/'^' tool explanation
# s ^= n means “update s by XORing it with n.”
# x ^ x = 0 (a number cancels itself out), x ^ 0 = x (XOR with zero keeps the number),So if you XOR all numbers together,
# duplicates vanish, leaving only the unique one.
# Start s = 0.
# XOR with 17 repeatedly → they cancel out (17 ^ 17 ^ 17 ... = 0).
# XOR with 3 → s becomes 3.
# Final result = 3.
# This is much more efficient than using arr.count(x) because it only needs one pass through the list and no repeated counting.
"""
# Another solution by a warrior to find the stray number in arr (using indexing)
"""
def stray(arr):
    arr.sort()
    return arr[-1] if arr[0] == arr[1] else arr[0]
print(stray([17, 17, 3, 17, 17, 17, 17])) # 3
"""
# My solution for the Playing with Digits” (also known as dig_pow)
"""
def dig_pow(n,p):     

    # k = sum([digit ** (p + i) for i, digit in enumerate([int(d) for d in str(n)])]) # Instead of [int(d) for d in str(n)], we just use str(n). Python iterates through the string, and we turn each character into an int inside the calculation.
    k = total = sum(int(digit) ** (p + i) for i, digit in enumerate(str(n))) # more efficient than the previous which creates a list
    return k // n if k % n == 0 else -1   
                
print(dig_pow(46288,3))
 """
# My solution for the Terminal game move function
"""
# new_position = current_position + roll(*2)

def terminal_move(c,r):    
    return c + (r*2)
print(terminal_move(3,6))
"""
# My solution for the welcome excercise (using list data)
"""
def greet(l):

    greeting = [ ("english", "Welcome")
    , ("czech", "Vitejte")
    , ("danish", "Velkomst")
    , ("dutch", "Welkom")
    , ("estonian", "Tere tulemast")
    , ("finnish", "Tervetuloa")
    , ("flemish", "Welgekomen")
    , ("french", "Bienvenue")
    , ("german", "Willkommen")
    , ("irish", "Failte")
    , ("italian", "Benvenuto")
    , ("latvian", "Gaidits")
    , ("lithuanian", "Laukiamas")
    , ("polish", "Witamy")
    , ("spanish", "Bienvenido")
    , ("swedish", "Valkommen")
    , ("welsh", "Croeso")
    , ("arabic", "أهلا و سهلا")
    ]    
    
    matches = [x[1] for x in greeting if x[0] == l]
    return matches[0] if matches else "Welcome"    

print(greet("italian")) # Benvenuto
"""
# My solution for the welcome excercise (using dictionary data)
"""
def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

print(greet('italian')) # Benvenuto
"""
# My solution for the remove_exclamation_marks excercise
"""
def RemoveExclamationMarks(s):
    return s.replace('!','')
print(RemoveExclamationMarks("!Bien!venue!!"))
"""
# My solution for the keep hydrated excercise
"""
def litres(h):
    return h // 2
print(litres(11.8))
"""
# My solution for paperwork excercise
"""
def paperwork(n,m):
    return n * m if n > 0 and m > 0 else 0
print(paperwork(-5,5))
"""
# My solution for the powers_of_two excercise
"""
def powers_of_two(n):
    return [2 ** x  for x in range(n+1)]
print(powers_of_two(4))
"""
# My solution to the is_palindrome excercise
"""
def is_palindrome(s):
    return s.lower() == ''.join(reversed(s.lower()))
print(is_palindrome("racecar"))
"""
# My solution for the switch num to word excercise
"""
def switch_it_up(n):

    num_word = {0: 'Zero',
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'}

    return num_word.get(n,None)
print(switch_it_up(9))
"""
# Another solution for the switch num to word excercise (very cleve way to use n as the index or the word in the list)
"""
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
print(switch_it_up(9))
"""
# My solution for twice_age excercise
"""
def twice_age(f,s):
    return abs(f-(s*2))
print(twice_age(30,16))
"""
# My solution for the check_for_factor excercise
"""
def check_for_factor(f,b):
    return b % f == 0 if b > 0 and f > 0 else 0
print(check_for_factor(2,6))
"""
# My solution for list the number between a,b
"""
def between(a,b):
    return [x for x in range(a,b+1) if a < b]
print(between(1,4))
"""
# My solution for sum of Messi goals
"""
def sum_goals(a,b,c):
    return a+b+c if a >=0 and b>=0 and c >= 0 else 0
print(sum_goals(5, 10, 2))
"""
# Another way by a warrior
"""
def goals(*a):
    return sum(a)
print(goals(5, 10, 2))
"""
# My solution for the sum of powered digits of each number “Eureka numbers” excercise
"""
def sum_dig_pow(a, b):
   
    results = []
    for x in range(a, b+1):          
        total = sum(int(digit) ** (i+1) for i, digit in enumerate(str(x)))
        if total == x:
            results.append(total)
    return results 

print(sum_dig_pow(1, 1000)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598]
"""
# Another solution by a warrior for the sum of powered digits of each number “Eureka numbers” excercise (one liner)
"""
def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]
print(sum_dig_pow(1, 1000)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598]
"""
# The solution to the The Supermarket Queue excercise (done by Copilot)
"""
def queue_time(customers, n):
    tills = [0] * n
    for customer in customers:
        teller = tills.index(min(tills)) # .index() is a list method in Python.“find the position of this value inside the list tills.”
        tills[teller] += customer # tills[teller] += customer means send the customer to till index/#.
    return max(tills)
print(queue_time([2,3,10], 2)) # 12

# The trick is to always assign the next customer to the till that frees up first.
# That way, you simulate parallel checkout correctly.
# queue_time([10,2,3,3], 2)
# Start: tills = [0,0]
# Customer 10 → tills = [10,0]
# Customer 2 → tills = [10,2]
# Customer 3 → tills = [10,5]  (goes to till with 2)
# Customer 3 → tills = [10,8]  (goes to till with 5)
# Final result = max([10,8]) = 10
"""
# April 9th, 2026
# My solution to check if n is even excercise
"""
def is_even(n):

    return n % 2 == 0

print(is_even(0))
"""
# My solution for the find the sum in range a,b (regardless of order)
"""
def get_sum(a,b):

    if a == b:
        return a
    elif a < b:        
        return sum(x for x in range(a,b+1))
    elif a > b:
        return sum(x for x in range(b,a+1))    

print(get_sum(3141,2590)) # 1581756
"""
# Another solution by a warrior for the find the sum in range a,b (regardless of order), usig min and max
"""
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
print(get_sum(3141,2590)) # 1581756
"""
# Another solution by a warrior for the find the sum in range a,b (regardless of order), arethmatic way
"""
def get_sum(a, b):
    n = abs(a - b) + 1
    return (a + b) * n // 2
print(get_sum(3141,2590)) # 1581756
"""
# My solution for the say_hello excercise
""" 
def say_hello(name):
    return f"Hello, {name}"
print(say_hello('Mr. Nawar'))
"""
# My solution for the rental_car_cost excercise
"""
def rental_car_cost(d):
    base = d * 40
    if d >= 7:
        return base - 50
    elif d >= 3:
        return base - 20
    else:
        return base
print(rental_car_cost(2))
"""
# My solution for the remove the gees excercise
"""
def goose_filter(arr):
    gees = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"} # using a set is faster than the list
    return [x for x in arr if x not in gees]
print(goose_filter( ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])) # ['Mallard', 'Hook Bill', 'Crested', 'Blue Swedish']
"""
# Another solution by a warrior for the remove the gees excercise (using filter and lambda)
"""
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"] 
def goose_filter(birds):
    return list(filter(lambda x: x not in geese, birds))
print(goose_filter( ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])) # ['Mallard', 'Hook Bill', 'Crested', 'Blue Swedish']
"""
# My solution for the count vowels in a string excercise
"""
def count_vowels(text):
    return sum(1 for x in text if x in 'aeiou')
print(count_vowels('nawar hussain hassan'))
"""
# My solution for the tribonacci excercise
"""
def tribonacci(signature,n):

    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    else:
        new = signature
        while len(new) <n:
           new.append(sum(new[-3:]))
    return new
print(tribonacci([1,1,1],6)) # [1, 1, 1, 3, 5, 9]

"""
# Another solution by a warrior for the tribonacci excercise
"""
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
print(tribonacci([1,1,1],6))
"""
# My solution for the hula hoop excercise
"""
def keep_hoop(n):

    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

print(keep_hoop(11))
"""
# My solution for the remove every second element in a list
"""
def remove_second(arr):    
    return arr[::2]
print(remove_second(["Keep", "Remove", "Keep", "Remove", "Keep", "Remove", "Keep"])) # ['Keep', 'Keep', 'Keep', 'Keep']
"""
# My solution for sum & return str excercise
"""
def sum_str(s1, s2):
    return str((int(s1) if s1 else 0) + (int(s2) if s2 else 0))
print(sum_str('4','5')) # '9'
"""
# Another solution for sum & return str excercise
"""
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0)) # using or instead of if/else
print(sum_str('4','5')) # '9'
"""
# or another solution for sum & return str excercise
"""
def sum_str(*values):
    return str(sum(int(s or '0') for s in values))
print(sum_str('4','5')) # '9'
"""
# My solution for are_you_playing_banjo excercise
"""
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"
print(are_you_playing_banjo('Razan')) # Razan ' plays banjo'
"""
# My solution for the remove the smallest number (first occurence without mutating the original list) 
"""
def remove_smallest(arr):
    new_arr = arr[:]              # make a shallow copy so the original list is not mutated to pass all tests
    if new_arr:     
        removed = new_arr.pop(new_arr.index(min(new_arr)))
        return new_arr
print(remove_smallest([3, 1, 4, 1, 5])) # [3, 4, 1, 5]
"""
# Another solution by a warrior for the remove the smallest number (first occurence without mutating the original list)
"""
def remove_smallest(arr):
    new_arr = arr[:]              # make a shallow copy so the original list is not mutated to pass all tests
    if new_arr:
        new_arr.remove(min(new_arr))
        return new_arr
print(remove_smallest([3, 1, 4, 1, 5])) # [3, 4, 1, 5]
"""
# April 10th, 2026
# My solution for the L1: Set Alarm excercise
"""
def set_alarm(employed,vacation):
    return True if employed and not vacation else False
print(set_alarm(False, True))
"""
# or simply by another warrior
"""
def set_alarm(employed,vacation):
    return employed and not vacation
print(set_alarm(False, True))
"""
# My solution for the pipe problem excercise
"""
def pipes(arr):
   return [x for x in range(min(arr),max(arr)+1)]  
print(pipes([1,3,5,6,7,8]))
"""
# or simply by another warrior (same big O complexity but more readable and stylistic)
"""
def pipe_fix(nums):
	return list(range(nums[0], nums[-1] + 1))
print(pipe_fix([1,3,5,6,7,8]))
"""
# My solution for the Highest Scoring Word excercise
"""
def high(text):
    new = text.lower().split(' ')
    to_sum  = []     
    for x in new:       
        num = sum(ord(y) - 96 for y in x)
        to_sum.append(num)    
    return new[to_sum.index(max(to_sum))]
print(high('Nawar is amazing azaming'))
"""
# Another solution by a warrior for the Highest Scoring Word excercise (using max(,key) and lambda)
"""
def high(text):
    words = text.lower().split()
    return max(words, key=lambda w: sum(ord(c) - 96 for c in w))
print(high('Nawar is amazing azaming'))
"""
# My solution for the calculate_years excercise
"""
def calculate_years(p,i,t,d):
    if d <= p:
        return 0    
    accum = p + ((p * i)) - ((p * i) * t)
    years = 1
    while accum < d:
        accum += (accum * i) - (accum * i) * t
        years += 1      
    return years
print(calculate_years(1000, 0.05, 0.18, 1300))
"""
# Another solution by a warrior for the calculate_years excercise (simpler avoids redundance due to repeated formulas)
"""
def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
    return years
print(calculate_years(1000, 0.05, 0.18, 1300))
"""
# My solution for making initials out of two names excercise
"""
def abbrev_name(text):    
    return text.split()[0][0].capitalize() + '.' + text.split()[1][0].capitalize()
print(abbrev_name('nawar hassan'))  # N.H
"""
# Another solution by a warrior for making initials out of two names excercise
"""
def abbrev_name(name):
    return '.'.join(w[0].upper() for w in name.split())
print(abbrev_name('nawar hassan'))  # N.H
"""
# Another solution by a warrior for making initials out of two names excercise (this can accept more than two words)
"""
def abbrev_name(text):
    words = text.split()
    return f"{words[0][0].upper()}.{words[1][0].upper()}"
print(abbrev_name('nawar hassan'))  # N.H
"""
# Another solution by a warrior for making initials out of two names excercise
"""
def abbrev_name(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
print(abbrev_name('nawar hassan'))  # N.H
"""
# My solution for Write Number in Expanded Form excercise
"""
def expanded_form(num):
    digits = list(str(num))
    powers = [10**n for n in range(len(digits)-1, -1, -1)] # 10 ** [4, 3, 2, 1, 0] -> [10000, 1000, 100, 10, 0](using range(start,stop, step)), start = len(string)-1 = 4, stop = -1 (exclusive, so it stops at 0), step = -1 (count backwards)
    calc = [int(a)* b for a, b in zip(digits, powers)]
    return ' + '.join(str(x) for x in calc if x != 0)    
print(expanded_form(70304))     # 70000 + 300 + 4
"""
# Another solution by a warrior for Write Number in Expanded Form excercise
"""
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
print(expanded_form(70304))     # 70000 + 300 + 4
"""
# April 11th , 2026

# My solution for the beast & feast matching start and end letters excercise
"""
def feast(beast,dish):
    return dish.startswith(beast[0]) and dish.endswith(beast[-1])
print(feast('monkey funcky','meat sticky'))
"""
# This solution for the return the highest result of formulas excercise did not pass all the tests, will keep just to show that we can include formulas in lists and iterate over them
"""
def expressions(a,b,c):
    formulas = [lambda : a * (b + c),
                lambda : a * b * b,
                lambda : a + b * c,
                lambda : (a + b) * c
                ]
    
    results = [f() for f in formulas]   # evaluate each formula we use f() to envoke the functions
    return max(results)  
print(expressions(1, 2, 3))
"""
# This solution for the return the highest result of formulas excercise passed
"""
def expression_matter(a, b, c):
    return max(
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c)
    )
print(expression_matter(1, 2, 3))
"""
# Another solution by a warrior for the return the highest result of formulas excercise.
"""
def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))
print(expression_matter(1, 2, 3))
"""
# My solution for the find the index of an in between number excercise
""""
def gimme(arr):
    return [arr.index(x) for x in arr if x != max(arr) and x != min(arr)][0]
print(gimme([2, 3, 1]))
"""
# A refined solution by Gemini for the find the index of an in between number excercise
"""
def gimme(arr):
    # Calculate these once!
    mx, mn = max(arr), min(arr)
    return [arr.index(x) for x in arr if x != mx and x != mn][0]
print(gimme([2, 3, 1]))
"""
# Another solution by a warrior for the find the index of an in between number excercise
"""
def gimme(inputArray):
    return inputArray.index(sorted(inputArray)[1])
print(gimme([2, 3, 1]))
"""
# My solution for the find the next perfect square excercise
"""
import math

def perfect_square(num: int):
    root = int(math.sqrt(num))
    if root * root == num:        
        return (root + 1) ** 2   
    else:
        return -1
    return next
print(perfect_square(121))
"""
# My solution for the rock scissors paper excercise (using a dictionary)
"""
def rps(player1,player2):

    if (player1 == "rock" and player2 == "scissors") or \
        (player1 == "scissors" and player2 == "paper") or \
        (player1 == "paper" and player2 == "rock"):
        return "Player 1 won!"
    elif player1 == player2:
        return "Draw!"
    else:
        return "Player 2 won!"

print(rps("paper", "scissors"))
"""
# Another solution by a warrior for the rock scissors paper excercise (using a dictionary)
"""
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
print(rps("paper", "scissors"))
"""
# My solution for the get_volume_of_cuboid excercise
"""
def get_volume_of_cuboid(l,w,h):
    return l * w * h
print(get_volume_of_cuboid(20, 15, 12))
"""
# My solution to the string increment excercise (but failed as the middle zeros were not handled)
"""
def increase_string(s):

    to_list = list(str(s))    
    digit_list = []
    alpha_list = []
        
    if not s[-1].isdigit():
        s = s + '1'
    for x in to_list:
        if x.isdigit():
            digit_list.append(x)
        elif x.isalpha():
            alpha_list.append(x)        
    increment = list(str(int(''.join(digit_list))+1))        
    return ''.join(alpha_list + increment)

print(increase_string('foobar023'))
"""
# Gemini refienement of mysolution to the string increment excercise (but did not pass all tests) (used zfill to fill the missing zeros)
"""
def increase_string(s):
    if not s or not s[-1].isdigit():
        return s + '1'
    
    to_list = list(str(s))    
    digit_list = []
    alpha_list = []
        
    for x in to_list:
        if x.isdigit():
            digit_list.append(x)
        else:
            # Changed to 'else' to catch symbols/spaces too, not just alpha
            alpha_list.append(x) 
            
    # 1. Save the original length of the digit string
    original_len = len(digit_list)
    
    # 2. Increment the number
    incremented_value = int(''.join(digit_list)) + 1
    
    # 3. Convert back to string and PAD with zeros to match original length
    increment = str(incremented_value).zfill(original_len)
    
    return ''.join(alpha_list) + increment
print(increase_string('foobar023'))
"""
# Gemini's solution to the string increment excercise (passed using .rstrip() and zfill())
"""
def increase_string(s):

    head = s.rstrip('0123456789') # Strip digits from right to get the prefix
    tail = s[len(head):]           # Everything left is the trailing digits
    print(tail)
    if not tail:
        return s + "1"
        
    return head + str(int(tail) + 1).zfill(len(tail))
print(increase_string('foobar023')) # foobar024
"""
# April 12th, 2026

# My solution for the grow accumilation excercise
"""
def reduce_grow(arr):
    result = 1
    for n in arr:
        result *= n
    return result
print(reduce_grow([1, 2, 3, 4])) # 24
"""
# Gemini solution for the grow accumilation excercise (super efficient using prod accumilator)
"""
import math

def reduce_grow(arr):
    return math.prod(arr)
print(reduce_grow([1, 2, 3, 4])) # 24
"""
# My solution for the replace vowels
"""
def replace_exclamation(s):
    vowels = 'aeiouAEIOU'
    return ''.join([x.replace(x,'!') if x in vowels else x for x in s])
print(replace_exclamation("naeiou"))
"""
# My solution for the find duplicates with a limit
"""
def find_multiples(n,limit):
    return [x for x in range(n,limit+1) if (x % n) == 0]
print(find_multiples(2,9))  # [2, 4, 6, 8]
"""
# or simply us the range(start, stop, step)
"""
def find_multiples(n,limit):
    return list(range(n, limit+1, n))
print(find_multiples(2,9))  # [2, 4, 6, 8]
"""
# My solution for sorting a list of numbers
"""
def solution(arr):
    if arr:
        arr.sort()
        return arr
    else:
        return []
print(solution([1,2,3,10,5]))
"""
# or simply
"""
def solution(nums):
    return sorted(nums) if nums else []
print(solution([1,2,3,10,5]))
"""
# April 13th, 2026

# My solution for the change to alernated case excercise
"""
def to_alternating_case(text):
    return ''.join(c.upper() if c.islower() else c.lower() for c in text )
print(to_alternating_case("hello WORLD"))   # HELLO world
"""
# Another simple solution by a warrior for the change to alernated case excercise (using .swapce() tool)
"""
def to_alternating_case(text):
    return text.swapcase()
print(to_alternating_case("hello WORLD"))   # HELLO world
"""
# My solution for the nums smaller than limit excercise
"""
def small_enough(arr,limit):
    bucket = []
    for x in arr:
        if x <= limit:
            bucket.append(x)
            print(bucket)
    return len(bucket) == len(arr)
print(small_enough([1, 3, 10, 2, 5, 12, 8, 7], 11)) # False
"""
# Another simple solution by a warrior for the nums smaller than limit excercise using max()
"""
def small_enough(array, limit):
    return max(array)<=limit
print(small_enough([1, 3, 10, 2, 5, 12, 8, 7], 11)) # False
"""
# Another simple solution by a warrior for the nums smaller than limit excercise using all()
# The all() function is one of Python’s most powerful tools for "Boolean logic." It basically acts like a 
# strict inspector: it returns True only if every single item in the collection is true.
# all() logic: "I will only let the group in if ALL of them have an ID." (One person fails = Group fails).
# any() logic: "I will let the group in if AT LEAST ONE person has an ID."
"""
def small_enough(array, limit):
    return all(a <= limit for a in array)
print(small_enough([1, 3, 10, 2, 5, 12, 8, 7], 11)) # False
"""
# My solution for the bouning ball excercise
"""
def bouncing_ball(h, bounce, window):
    if h <= 0 or not (0 < bounce < 1) or window >= h:
        return -1
    
    count = 1  # first fall past the window
    while h * bounce > window:
        h *= bounce
        count += 2  # passes window going up and coming down
    
    return count

print(bouncing_ball(3, 0.66, 1.5))  # 3
"""
# April 14th, 2026
# My solution for the simple reverse words excercise
"""
def reverse_words(text):
    return ' '.join(text.split()[::-1])
print(reverse_words('Hello World')) # World Hello
"""
# My solution for the arethmatic calcs by operators name excercise
"""
def operator_name(a,b,operator):
    operators = {"add": a + b, "subtract": a - b, "divide": a / b, "multiply": a * b }
    return operators[operator]
print(operator_name(2, 7, 'add')) # 9

# or simply return {"add": a + b, "subtract": a - b, "divide": a / b, "multiply": a * b }[operator]
"""
# Gemini's solution for the arethmatic calcs by operators name excercise (use of labmda to store the logic/function in the dictionary, not the result)
"""
def operator_name(a, b, operator):
    # We store the functions (lambdas), not the results 
    ops = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "multiply": lambda: a * b,
        "divide": lambda: a / b if b != 0 else "Error: Division by zero"
    }    
    # Retrieve the function and then call it with ()
    return ops.get(operator, lambda: "Invalid Operator")()
print(operator_name(2, 7, 'add'))   # 9
"""
# Gemini's solution for the arethmatic calcs by operators name excercise (by use of the modern match which is very pythonic)
"""
def operator_name(a, b, operator):
    match operator:
        case "add": return a + b
        case "subtract": return a - b
        case "multiply": return a * b
        case "divide": return a / b if b != 0 else "Error"
        case _: return "Invalid Operator"
print(operator_name(2, 7, "add"))   # 9
"""
# My solution for the count a given char in a given string excercise
"""
def count_char(text,char):
    return text.lower().count(char)
print(count_char("Helloo", 'h'))
"""
# My solution fo the return indices of the captial letter in a text excercise (this kata moved me to 4kyu)
"""
def indeces_capital(text):
    return [i for i, x in enumerate(list(str(text))) if x.isupper()]
print(indeces_capital("CodEWaRs"))  # [0, 3, 4, 6]
"""
# On this day (April 14th, 2026) I became a 4kyu rank

# My solution for the club_member type excercise 
"""
def club_member(arr):  
        return ['Senior' if x[0] >= 55 and x[1] > 7 else 'Open' for x in arr]        
print(club_member([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])) # ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']
"""

def accum(text):

    return '-'.join([(x * i).title() for i, x in enumerate(text,1)])

print(accum("RqaEzty"))
# "RqaEzty" -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"