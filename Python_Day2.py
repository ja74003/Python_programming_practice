#Ques 1: Check whether a number is prime or composite

#Ques 1 - method 1: check divisibility from 2 to (n-1) 
print("Ques 1- Method 1: ")
def is_prime_naive(n):
	if n <= 1:
		return false
	for i in range(2,n):
		if n%i == 0:
			return False
	return True
print(is_prime_naive(23))
print(is_prime_naive(80))

#Ques 1 - method 2: square root optimization( if n has a factor, at least one should be less than square_root(n))
print("Ques 1- Method 2: ")
import math
def is_prime_sqrt(n):
	if n <= 1:
		return False
	for i in range(2,int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True
print(is_prime_sqrt(23))
print(is_prime_sqrt(80))

#Ques 1 - Method3: skip even numbers (Even numbers > 2 are never prime, so only run the check for odd numbers)
print("Ques 1- Method 3: ")
def is_prime_even_skip(n):
	if n <= 1:
		return False
	if n <=2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True
print(is_prime_even_skip(19))
print(is_prime_even_skip(20))


#Ques 1 - method 4: using 6k+1 Or 6K-1 optimization(all primes>3 are form of 6k + 1 or 6K-1)
print("Ques 1- Method 4: ")
def is_prime_6k(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % (i+2) == 0:
			return False
		i += 6
	return True
print(is_prime_6k(7))
print(is_prime_6k(8))


#Ques 1 - Method 5: sieve of erothosthenes (Precomputes primes upto N once, then lookup in O(1))
print("Ques 1- Method 5: ")
def is_prime_sieve(n):
	primes = [True]*(n+1)
	primes[0] = primes[1] = False
	p = 2
	while p*p <= n:
		for i in range(p*p, n+1, p):
			primes[i] = False
		p += 1
	return primes
print(is_prime_sieve(23))
print(is_prime_sieve(600))

#---------------------------------------------------------------------------------#
#Ques 2: Find the sum of digits of a given number

#Ques 2 - Method 1: String conversion + Map() + sum()
n1 = 123456
digit_sum1 = sum(map(int,str(n1)))
print("Ques 2- Method 1: ")
print(digit_sum1)


#Ques 2 - Method 2: String conversion + List comprehension
print("Ques 2- Method 2: ")
digit_sum2 = sum([int(d) for d in str(n1)])
print(digit_sum2)


#Ques 2 - Method 3: String conversion + Generator expression (memory efficient)
print("Ques 2- Method 3: ")
digit_sum3 = sum(int(d) for d in str(n1))
print(digit_sum3)


#Ques 2 - Method 4: Modulo and division loop
print("Ques 2- Method 4: ")
digit_sum4 = 0
while n1 > 0:
	digit_sum4 += n1%10
	n1 //= 10
print(digit_sum4)

#Ques 2 - Method 5: Recursive Approach
print("Ques 2- Method 5: ")
def digit_sum5(n):
	if n == 0:
		return 0
	return n % 10 + digit_sum5(n//10)
	
print(digit_sum5(7678686))


#Ques 2 - Method 6: using functools.reduce
print("Ques 2- Method 6: ")
from functools import reduce
n3 = 76868
digit_sum6 = reduce(lambda x,y : x + int(y), str(n3),0)
print(digit_sum6)


#Ques 2 - Method 7: Using abs() to handle negative numbers
print("Ques 2- Method 7: ")
n2 = -123456
digit_sum7 = sum(map(int, str(abs(n2))))
print(digit_sum7)

#---------------------------------------------------------------------------------#

#Ques 3: Check if a number is Armstrong number or not

#Ques 3 - Method 1: String conversion + for loop
print("Ques 3- Method 1: ")
def is_armstrong_for(n):
	digits = str(n)
	power = len(digits)
	total = 0
	for d in digits:
		total += int(d)**power
	return total == n
	
print(is_armstrong_for(153))
print(is_armstrong_for(123))


#Ques 3 - Method 2: Pure Math (modulo + Division)
print("Ques 3- Method 2: ")
def is_armstrong_math(n):
	num = n
	power = len(str(n))
	total = 0
	while num > 0:
		digit = num % 10
		total += digit**power
		num //= 10
	return total == n
	
print(is_armstrong_math(153))
print(is_armstrong_math(123))


#Ques 3 - Method 3: String + Sum() + generator expression
print("Ques 3- Method 3: ")
def is_armstrong_meth3(n):
	power = len(str(n))
	return n == sum(int(d)**power for d in str(n))
print(is_armstrong_meth3(9474))
print(is_armstrong_meth3(123))


#Ques 3 - Method 4: Using map() + sum()
print("Ques 3- Method 4: ")
def is_armstrong_meth4(n):
	power = len(str(n))
	return n == sum(map(lambda d: int(d)**power, str(n)))
print(is_armstrong_meth4(370))
print(is_armstrong_meth4(123))


#Ques 3 - Method 5: Using recursion
print("Ques 3- Method 5: ")
def armstrong_recursive(n, power = None):
	if power is None:
		power = len(str(n))
	if n == 0:
		return 0
	return (n % 10)**power + armstrong_recursive(n // 10, power)

def is_armstrong(n):
	return n == armstrong_recursive(n)
	
print(is_armstrong(9474))
print(is_armstrong(123))

#Ques 3 - Method 6: Using reduce() function
print("Ques 3- Method 6: ")
def is_armstrong_reduce(n):
	power = len(str(n))
	return n == reduce(lambda acc,d: acc + int(d)**power, str(n),0)
print(is_armstrong_reduce(9474))

#---------------------------------------------------------------------------------#

#Ques 4: Create a simple calculator (+, -, *, /)
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
op = input("Please enter the operation you want to perform: '+' or '-' or '*' or '/': ")

#Ques 4 - Method 1: Using basic elif conditions
print("Ques 4- Method 1: ")
def calculator_elif(a,b,op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	elif op == '/':
		if b!=0:
			return a/b
		else:
			return "Division by 0 error"
	else:
		return "Please select valid operator"

print(calculator_elif(a,b,op))


#Ques 4 - Method 2: using a dictionary of functions
print("Ques 4- Method 2: ")
def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y if y != 0 else "Division by zero error"
operations = {'+':add, '-':sub, '*':mul, '/':div}
print(operations[op](a,b))

#Ques 4 - Method 3: using eval()
print("Ques 4- Method 3: ")
expr = "10+5*2-1"
result = eval(expr)
print(result)

#Ques 4 - Method 4: Using lambda + dictionary
print("Ques 4- Method 4: ")
calc = {
	'+': lambda x,y: x+y,
	'-': lambda x,y: x-y,
	'*': lambda x,y: x*y,
	'/': lambda x,y: x/y if y != 0 else "Division by zero error"
}
print(calc[op](a,b))

#Ques 4 - Method 5: Using interactive command line calculator
print("Ques 4- Method 5: ")
while True:
	expr1 = input("Enter expression or 'q' to quit: ")
	if expr1.lower() == 'q':
		break
	try:
		result1 = eval(expr1)
		print(f"The calculated value of the expression you have entered is {result1}")
	except Exception as e:
		print("Error: ", e)



#Ques 4 - Method 6: Using OOPs approach
print("Ques 4- Method 6: ")
class Calculator:
	def add(self,a,b):
		return a + b
	def sub(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b if b != 0 else "Division by zero"
	
calc = Calculator()
print(calc.mul(a,b))
 
  
   
#Ques 4 - Method 7: using operator module
print("Ques 4- Method 7: ")
import operator
ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv
}
print(ops[op](a,b))
#---------------------------------------------------------------------------------#

#Ques 5: Create a multiplication table 

num = int(input("Enter which number's table you want to print: "))
k = int(input("Enter the range till you want to print: "))

#Ques 5 - Method 1: Using for loop
print("Ques 5- Method 1: ")
def table_for_loop(num,k):
	for i in range(1,k+1):
		print(num*i)
table_for_loop(num,k)

#Ques 5- Method 2: Using while loop
print("Ques 5- Method 2: ")
def table_while_loop(num,k):
	i = 1
	while i <= k:
		print(num*i)
		i += 1
table_while_loop(num,k)

#Ques 5 - Method 3: Using list comprehension
print("Ques 5- Method 3: ")
def table_list_comp(num,k):
	return [num*i for i in range(1, k+1)]
print(table_list_comp(num,k))


#Ques 5 - Method 4: using map() and lambda()
print("Ques 5- Method 4: ")
def table_map(num,k):
	return list(map(lambda i: num*i, range(1, k+1)))
print(table_map(num,k))
  
   
#Ques 5 - Method 5: using string multiplication formatting
print("Ques 5- Method 5: ")
def table_string_format(num,k):
	return [f"{num}*{i} = {num*i}" for i in range(1, k+1)]
print(table_string_format(num,k)) 
  
#Ques 5 - Method 6: Using generators (yield)
print("Ques 5- Method 6: ")
def table_generator(num,k):
	for i in range(1,k+1):
		yield num*i
print(list(table_generator(num,k)))

#Ques 5 - Method 7: Generate table in matrix style
print("Ques 5- Method 7: ")
def full_table(num):
	return [[i*j for j in range (1,num+1)] for i in range(1, num+1)]
print(full_table(num))
 
  
#---------------------------------------------------------------------------------#

#Ques 6: Count and return vowels in a string
s = "Hello World"
vowels = "aeiouAEIOU"

#Ques 6 - Method 1: Using for loop
print("Ques 6- Method 1: ")
def vowels_for_loop(s):
	result = []
	for ch in s:
		if ch in vowels:
			result.append(ch)
	return result, len(result)
print(vowels_for_loop(s))
 
  
#Ques 6 - Method 2: Using list comprehension
print("Ques 6- Method 2: ")
def vowels_list_comp(s):
	result = [ch for ch in s if ch in vowels]
	return result, len(result)
print(vowels_list_comp(s))

  
#Ques 6 - Method 3: using filter() + lambda function
print("Ques 6- Method 3: ")
def vowels_filter(s):
	result = list(filter(lambda ch: ch in vowels,s))
	return result, len(result)
print(vowels_filter(s))
 
  
#Ques 6 - Method 4: Using regex
print("Ques 6- Method 4: ")
import re
def vowels_regex(s):
	result = re.findall(r"[aeiouAEIOU]",s)
	return result, len(result)
print(vowels_regex(s))
 
  
#Ques 6 - Method 5: Using set for efficiency
print("Ques 6- Method 5: ")
def vowels_set(s):
	vowels1 = set("aeiouAEIOU")
	result = [ch for ch in s if ch in vowels1]
	return result, len(result)
print(vowels_set(s))
 
  
#Ques 6 - method 6: Count + Extract together
print("Ques 6- Method 6: ")
def vowels_count_extract(s):
	vowels1 = set("aeiouAEIOU")
	result = [ch for ch in s if ch in vowels1]
	count = sum(1 for ch in s if ch in vowels1)
	return result, count
print(vowels_count_extract(s))
	
  
#Ques 6 - Method 7: Dictionary frequency
print("Ques 6- Method 7: ")
def dictionary_frequency(s):
	freq = {}
	result = []
	for ch in s:
		if ch in vowels:
			result.append(ch)
			freq[ch] = freq.get(ch,0) + 1
	return result, sum(freq.values()),freq
print(dictionary_frequency(s))
  

#---------------------------------------------------------------------------------#

#Ques 7: Calculate GCD (Greatest common divisor) of two numbers
c = int(input("Enter the first number out of two numbers for which you want to find GCD"))
d = int(input("Enter the second number out of two numbers for which you want to find GCD"))
    
#Ques 7 - Method 1: Naive (check all divisors)
print("Ques 7- Method 1: ")
def gcd_naive(c,d):
	gcd = 1
	for i in range(1,min(c,d)+1):
		if c % i == 0 and d % i == 0:
			gcd = i
	return gcd
print(gcd_naive(c,d))
    
#Ques 7 - Method 2: Euclidean algorithm (subtraction method)
print("Ques 7- Method 2: ")
def gcd_euc_sub(c,d):
	while c != d:
		if c > d:
			c -= d
		else:
			d -= c
	return c
print(gcd_euc_sub(c,d))

  
#Ques 7 - Method 3: Euclidean algorithm (Modulus method)
print("Ques 7- Method 3: ")
def gcd_euc_mod(c,d):
	while d != 0:
		c,d = d, c % d
	return c 
print(gcd_euc_mod(c,d)) 
    
#Ques 7 - Method 4: using built-in function in python - math.gcd()
print("Ques 7- Method 4: ")
print(math.gcd(c,d))
  
    
#Ques 7 - Method 5: Using recursion
print("Ques 7- Method 5: ")
def gcd_recursive(c,d):
	if d == 0:
		return c
	return gcd_recursive(d, c % d)
print(gcd_recursive(c,d))
#---------------------------------------------------------------------------------#  
