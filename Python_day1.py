# Created on iPad.
#Day 1 - Ques1: Print string
print("Twinkle twinkle little star \n How i wonder what you are \n Up the sky oh so high \n Like a wonder in the sky")


#Day 1 - Ques2: Swap 2 numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The two numbers you want to swap are {a} and {b}")

#method 1: Use 3rd variable Temp
Temp = 0
Temp = a
a = b
b = Temp 
print(f"Method 1: The two numbers swapped using 3rd variable {a} and {b}")

#method 2: Using addition and subtraction operators
a = a + b
b = a - b
a = a - b
print(f"Method 2: The two numbers swapped using addition and subtraction {a} and {b}")

#method 3: Using multiplication and division
a = a*b
b = int(a/b)
a = int(a/b)
print(f"Method 3: The two numbers swapped using multiplication and division are {a} and {b}")

#method 4: Using BITWISE XOR operator
a = a ^ b
b = a ^ b
a = a ^ b
print(f"Method 4: The two numbers are swapped using BITWISE XOR operator are {a} and {b}")

#method 5: Using tuple packing and unpacking (Built in for python)
a,b = b,a
print(f"Method 5: The two numbers are swapped using Tuple packing and unpacking are {a} and {b}")

#Day 1 - Ques 3: Find largest of three numbers
#method 1: Using 'and' operator and relational operators
d = int(input("Enter the first number you want to compare: "))
e = int(input("Enter the second number you want to compare: "))
f = int(input("Enter the third number you want to compare: "))
print(f"The 3 numbers which which you want to compare are : {d}, {e}, {f}")

if((d>e) and (e>f)):
    print(f"Method 1: The max number out of {d},{e},{f} is {d}")
if((e>d) and (d>f)):
    print(f"Method 1: The max number out of {d},{e},{f} is {e}")
if((f>d) and (d>e)):
    print(f"Method 1: The max number out of {d},{e},{f} is {f}")

#method 2: Using for loop
def getLargestNum(nums):
    largestNum = nums[0]
    for num in nums:
        if largestNum < num:
            largestNum = num
        return largestNum
    
maximum = getLargestNum([d,e,f])
print(f"Method 2: Largest number out of these are {maximum}")

#method 3: Using built in function in Python - max(), sorted(), nlargest()
largest_using_max = max(d,e,f)
print(f"Method 3: a) The largest out of {d},{e},{f} using max() function is {largest_using_max}")

largest_using_sorted = sorted([d,e,f], reverse = True)[0]
print(f"Method 3: b) The largest out of {d}, {e}, {f} using sorted() function is {largest_using_sorted}")

import heapq
largest_using_heapq = heapq.nlargest(1,[d,e,f])[0]
print(f"Method 3: c) The largest out of {d}, {e}, {f} using heapq.nargest() function is {largest_using_heapq}")

#Method 4: Place numbers in a list and use max()
numbers = [d,e,f]
largest_using_list = max(numbers)
print(f"Method 4: The largest out of {d},{e},{f} is {largest_using_list}")

#Method 5: Use conditional (Ternary operator)
largest_using_ternary = d if(d>=e and d>=f) else (e if e>=f else f)
print(f"Method 5: The largest out of {d},{e},{f} is {largest_using_ternary}")


#Day 1 - Ques4=: Check whether a number is even or odd
def checkNum(g):
    if(g % 2 == 0):
        print(f"The entered number {g} is even since it is divisible by 2")
    else:
        print(f"The number entered {g} is odd since it is not divisible by 2")
        
g = int(input("Enter the number for which you want to verify whether it is even or odd: "))
checkNum(g)

#Method 2: use list and for loop
list_a = [1,2,3,4,5]
for num in list_a:
    if (num % 2 == 0):
        print(f"Method 2: {num} is even")
    else:
        print(f"Method 2: {num} is odd")

#Method 3: Use lamba with map (memory efficient)
res = map(lambda num:str(num) + "even" if num % 2 == 0 else str(num) + "odd",list_a)
print("Method 3: \n")
print("\n".join(res))

#Method 4: Generator expression (Best option but readability is not good)
print("Method 4: \n")
print("\n".join(f"{num} even" if num % 2 == 0 else f"{num} odd" for num in list_a))

#Method 5: Check the last digit of the number
print("Method 5: \n")
list_b = [11, -20, 60, 39, 47]
for num in list_b:
    last_digit_abs = abs(num)%10
    if(last_digit_abs in (0,2,4,6,8)):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    



#Method 6: Use Bitwise operators (&, ^, |)
print("Method 6: After using Bitwise AND (&)\n")
for num_bitwise_and in list_b:
    if((num_bitwise_and & 1) == 0):
        print(f"{num_bitwise_and} is even")
    if((num_bitwise_and & 1) == 1):
        print(f"{num_bitwise_and} is odd")
    
print("Method 6: After using Bitwise XOR(^)\n")
for num_bitwise_xor in list_b:
    if(num_bitwise_xor ^ 1 == num_bitwise_xor + 1):
        print(f"{num_bitwise_xor} is even")
    if(num_bitwise_xor ^ 1 == num_bitwise_xor - 1):
        print(f"{num_bitwise_xor} is odd")
        
print("Method 6: After using Bitwise OR (|)\n")
for num_bitwise_or in list_b:
    if(num_bitwise_or | 1 == (num_bitwise_or + 1)):
        print(f"{num_bitwise_or} is even")
    if(num_bitwise_or | 1 == num_bitwise_or):
        print(f"{num_bitwise_or} is odd")

#Method 7: Use Bitwise left shift (<<) and right shift(>>) operators
print("Method 7: Apply bitwise shift right on the number and then apply shift left on result \n")
for num_bitwise_shift in list_b:
    if(((num_bitwise_shift >> 1) << 1) == num_bitwise_shift):
        print(f"{num_bitwise_shift} is even")
    else:
        print(f"{num_bitwise_shift} is odd")
    

#Method 8: Use floor division and multiplication
print("Method 8: Apply floor division and multiplication\n")
for num_floor_div in list_b:
    if(((num_floor_div // 2) * 2) == num_floor_div):
        print(f"{num_floor_div} is even")
    else:
        print(f"{num_floor_div} is odd")


#Day 1 - Ques 5: Factorial of a number using loops
#method 1: Using for loop
def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
factorial_iteration_for = factorial_for(5)
print(f"Method 1 using for loops: Factoral is {factorial_iteration_for}")

#Method 2: using while loop
def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
factorial_iteration_while = factorial_while(6)
print(f"Method 2 using while loops: Factorial is {factorial_iteration_while}")


#Method 3: Recursive Approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)
factorial_recursive_approach = factorial_recursive(10)
print(f"Method 3: using recursion: Factorial is {factorial_recursive_approach}")

#Method 4: Using built-in math function in python
import math
factorial_built_in_math = math.factorial(12)
print(f"Method 4: Using built in function math in python, the factorial is {factorial_built_in_math}")

#Method 5: Using Reduce + lambda (functional approach)
from functools import reduce
def factorial_reduce(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1,n+1))
factorial_lambda = factorial_reduce(81)
print(f"Using method 5: the factorial is {factorial_lambda}")
    

#Method 6: Calculating factorial with memoization (caching)
memo = {0:1,1:1}
def factorial_memo(n):
    if n not in memo:
        memo[n] = n * factorial_memo(n-1)
    return memo[n]
call_1_fact = factorial_memo(5)
call_2_fact = factorial_memo(6)
print(f"Method 6: call 1 using memoization {call_1_fact}")
print(f"Method 6: call 2 using memoization {call_2_fact}")


#Day 1 - Ques 6: Find Fibonacci of a number
#method 1: take last 2 numbers in the last and append the result at the end of the list
def fibonacci_list(nterms):
    if (nterms < 0):
        return []
    elif (nterms == 1):
        return [1]
    seq = [0,1]
    while len(seq) < nterms:
        seq.append(seq[-1] + seq[-2])
    return seq
fibonacci_list_return = fibonacci_list(5)
print(f"Method 1: Using list return {fibonacci_list_return}")

#Method 2: Generator version

print("Method 2: Using generator function, the fibonacci series is \n")
def fibonacci_generator(nterms):
    n1, n2 = 0, 1
    for _ in range(nterms):
        yield n1
        n1, n2 = n2, n1 + n2
for num in fibonacci_generator(10):
        print(num,'\n',end = "")

        
#Method 3: Iterative tuple update (no list, constant space)
print("Method 3: Using iterative tuple update, the fibonacci series is: ")
def fib_n(n):
    a1, b1 = 0,1
    for _ in range(n):
        a1, b1 = b1, a1 + b1
    return a1
print([fib_n(i) for i in range(12)])


#Method 4: Using while loop upto a maximum threshold (not by count)
print("Method 4: Using while loop print all fibonacci numbers upto a threshhold: ")
def fib_upto(limit):
    a2, b2 = 0,1
    while a2 <= limit:
        yield a2
        a2, b2 = b2, a2 + b2
print(list(fib_upto(50)))

#Method 5: Naive recursion (Time = 2^n which is very slow for large values of n)
print("Method 5: Using naive recursion: ")
def naive_rec(n):
    if n < 2:
        return n
    return naive_rec(n-1) + naive_rec(n-2)
print(naive_rec(15))


#Method 6: Recursion with Memoization 
print("Method 6: Using recursion with memoization: ")
from functools import lru_cache
@lru_cache(maxsize = None)
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n-1) + fib_memo(n-2)
print([fib_memo(i) for i in range(15)])
    

#Method 7: Recursion with Dynamic programming
print("Method 7: Using recursion with Dynamic Programming: ")
def fib_dp(n):
    if n < 2:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fib_dp(10))




#Day 1 - Ques 7: reverse a string
#Method 1: Use 2 pointer swap
print("Method 1: using a pointer swap: \n")
def reverse_in_place(s):
	s_list = list(s)
	i,j = 0, len(s_list) - 1
	while i < j:
		s_list[i],s_list[j] = s_list[j],s_list[i]
		i += 1
		j -= 1
	return "".join(s_list)
print(reverse_in_place("Hello"))
	


#method 2: Using for loop (list + join)
print("Method 2: using for loop, the new string is : \n")
s = "race"
rev_list = []
for ch in s:
	rev_list.append(ch)
rev = "".join(rev_list[::-1])
print(rev)


#Method 3: using reversed() function in python
print("Method 3: using reverse function, the new string is : \n")
s1 = "trello"
rev1 = "".join(reversed(s1))
print(rev1)


#Method 4: Using slicing [::-1] 
print("Method 4: using slicing, the new string is : \n")
s2 = "Gayatri"
rev2 = s2[::-1]
print(rev2)



#Day 1 - Ques 7: Check whether a string is palindrome

#Method 1: Using slicing
print("Using slicing: \n")
def is_palindrome_slice(s3):
	return s3 == s3[::-1]
print(is_palindrome_slice("racecar"))
print(is_palindrome_slice("hello"))

#Method 2: Two pointer technique
print("Using two pointer technique: \n")
def is_palindrome_pointer(s4):
	i3, j3 = 0, len(s4) - 1
	while i3 < j3:
		if (s4[i3] != s4[j3]):
			return False
		i3 += 1
		j3 -= 1
	return True
print(is_palindrome_pointer("madam"))
print(is_palindrome_pointer("hello"))
			

#Method 3: Using reversed() function in python
print("Using reversed function in python: \n")
def is_palindrome_reverse(s5):
	return list(s5) == list(reversed(s5))
print(is_palindrome_reverse("level"))
print(is_palindrome_reverse("hurray"))


#Method 4: Using all() with generator
print("Using all() with generator: \n")
def is_palindrome_all(s6):
	return all(s6[i] == s6[~i] for i in range(len(s6) // 2))
print(is_palindrome_all("level"))
print(is_palindrome_all("parlour"))

#Method 5: Ignoring case and aplhanumeric & convert to lower for comparison
print("Ignoring case and alphanumeric: \n")
import re
def is_palindrome_re(s7):
	s7 = re.sub(r'[^a-zA-Z0-9]', '', s7).lower()
	return s == s[::-1]
print(is_palindrome_re("A man, a plan, a Canal: Panama"))
