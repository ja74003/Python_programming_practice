#Question 1: Calculate LCM of 2 numbers


#Method 1: Using LCM/GCD relationship
print("LCM method 1 result: ")
import math
def lcm(a,b):
	return abs(a*b)//math.gcd(a,b)
print(lcm(12,18))


#Method 2: Using python built-in function
print("LCM method 2 result: ")
print(math.lcm(12,18))


#Method 3: Using reduce function
print("LCM method 3 result: ")
from functools import reduce
def lcm_two(a,b):
	return abs(a*b)//math.gcd(a,b)
def lcm_multiple(numbers):
	return reduce(lcm_two,numbers)
print(lcm_multiple([12,18,24]))

#Question 2: Convert decimal to binary

#Method 1: Using python built in functions - bin() and format()
print("Decimal to binary method 1 result: ")
n = 13
binary_one = bin(n)[2:]
print(binary_one)
binary_two = format(n,"b")
print(binary_two)
binary_two = f"{n:b}"
print(binary_two)

#Method 2: Using recursion
print("Decimal to binary method 2 result: ")
def dec_to_binary_rec(n):
	if n == 0:
		return ""
	return dec_to_binary_rec(n//2) + str(n%2)
binary_three = dec_to_binary_rec(n)
print(binary_three)

#Method 3: Using iterative division
print("Decimal to binary method 3 result: ")
def dec_to_binary_iter(n):
	if n == 0:
		return 0
	bits = []
	while n > 0:
		bits.append(str(n%2))
		n //= 2
	return "".join(reversed(bits))
binary_four = dec_to_binary_iter(n)
print(binary_four)

#Method 4: Using BITWISE operations (AND, Shift right)
print("Decimal to binary method 4 result: ")
"""
def dec_to_binary_bitwise(n):
	bits = []
	while n > 0:
		bits.append(str(n&1))
		n >> 1
	return "".join(reversed(bits))
binary_five = dec_to_binary_bitwise(n)
print(binary_five)
"""

#Question 3: Convert binary number to decimal

#Method 1: Use built-in python function
print("Method 1 binary to decimal result: ")
binary_str = "1101"
decimal_one = int(binary_str,2) # converts to decimal value of base 2
print(decimal_one)

#Method 2: Manual iteration (positional value method)
print("Method 2 binary to decimal result: ")
def binary_to_decimal(binary_str):
	decimal = 0
	power = len(binary_str) - 1
	for digit in binary_str:
		decimal += int(digit)*(2**power)
		power -= 1
	return decimal
decimal_two = binary_to_decimal(binary_str)
print(decimal_two)

#Method 3: Iterative accumulation
print("Method 3 binary to decimal result: ")
def binary_to_decimal_accumulation(binary_str):
	decimal = 0
	for digit in binary_str:
		decimal = decimal*2 + int(digit) #shift the current decimal value left by one binary digit and add the current binary digit
	return decimal
decimal_three = binary_to_decimal_accumulation(binary_str)
print(decimal_three)

#Method 4: Using sum() and enumerate()
print("Method 4 binary to decimal result: ")
def binary_to_decimal_sum(binary_str):
	return sum(int(digit)*(2**idx) for idx,digit in enumerate(reversed(binary_str)))
decimal_four = binary_to_decimal_sum(binary_str)
print(decimal_four)

#Method 5: Using reduce()
print("Method 5 binary to decimal result: ")
def binary_to_decimal_reduce(binary_str):
	return reduce(lambda acc,d: acc*2 + int(d),binary_str,0)
decimal_five = binary_to_decimal_reduce(binary_str)
print(decimal_five)

#Question 4: Create a random number generator in python

#Method 1: using random.randint()
print("Random number generator Method 1 result: ")
import random
rand_one = random.randint(1,10)
print(rand_one)

#Method 2: Using random.randrange()
print("Random number generator Method 2 result: ")
rand_two = random.randrange(1,11) #11 is excluded due to range()
print(rand_two)

#Method 3: Using random.choice()
print("Random number generator Method 3 result: ")
rand_three = random.choice(list(range(1,11))) #List [1,2....10] is generated from which choice() picks a random element
print(rand_three)

#Method 4: Using random.random() with scaling
print("Random number generator Method 4 result: ")
rand_four = int(random.random()*10)+1
print(rand_four)

#Method 5: Using secrets module (cryptographically secure)
print("Random number generator Method 5 result: ")
import secrets
rand_five = secrets.randbelow(10) + 1
print(rand_five)

#Method 6: Using numpy.random.randint()
print("Random number generator Method 6 result: ")
import numpy as np
rand_six = np.random.randint(1,11)
print(rand_six)

#Question 5: Find maximum and minimum in a list

#Method 1: using built in functions - max(),min()
print("Find maximum and minimum in a list Method 1 result: ")
list_one = [3,1,7,9,2,5]
minimum_one = min(list_one)
maximum_one = max(list_one)
print(minimum_one,maximum_one)

#Method 2: Single pass iteration
print("Find maximum and minimum in a list Method 2 result: ")
minimum_two = maximum_two = list_one[0]
for num in list_one[1:]:
	if num < minimum_two:
		minimum_two = num
	elif num > maximum_two:
		maximum_two = num
print(minimum_two,maximum_two) 

#Method 3: Using max() and min() with unpacking
print("Find maximum and minimum in a list Method 3 result: ")
minimum_three, maximum_three = min(list_one),max(list_one)
print(minimum_three,maximum_three)

#Method 4: Using reduce()
print("Find maximum and minimum in a list Method 4 result: ")
minimum_four = reduce(lambda x,y: x if x<y else y,list_one)
maximum_four = reduce(lambda x,y: x if x>y else y,list_one)
print(minimum_four,maximum_four)

#Method 5: Using sort()
print("Find maximum and minimum in a list Method 5 result: ")
list_two = [67, 98, 2, 0, -8, 100]
print(f"Before sorting: {list_two}")
list_two.sort()
minimum_five = list_two[0]
maximum_five = list_two[-1]
print(f"After sort(): {list_two}")
print(minimum_five,maximum_five)

#Method 6: using sorted()
print("Find maximum and minimum in a list Method 6 result: ")
list_sorted = sorted(list_one)
minimum_six = list_sorted[0]
maximum_six = list_sorted[-1]
print(minimum_six,maximum_six)

#Method 7: Using numpy (vectorized)
print("Find maximum and minimum in a list Method 7 result: ")
list_numpy = np.array(list_one)
minimum_seven = list_numpy.min()
maximum_seven = list_numpy.max()
print(minimum_seven,maximum_seven)


#Question 6: Calculate sum of all elements in a list

#Method 1: Using sum()
print("Sum of all elements in a list Method 1 result: ")
list_three = [1,2,3,4,5]
result_one = sum(list_three)
print(result_one)


#Method 2: using for loop
print("Sum of all elements in a list Method 2 result: ")
total_one = 0
for item in list_three:
	total_one += item
print(total_one)

#Method 3: Using while loop with index
print("Sum of all elements in a list Method 3 result: ")
total_two = 0
index_two = 0
while index_two < len(list_three):
	total_two += list_three[index_two]
	index_two += 1
print(total_two)


#Method 4: using reduce()
print("Sum of all elements in a list Method 4 result: ")
total_three = reduce(lambda x,y: x+y,list_three)
print(total_three)


#Method 5: Using recursion
print("Sum of all elements in a list Method 5 result: ")
def rec_sum(list):
	if not list:
		return 0
	else:
		return list[0] + rec_sum(list[1:])
total_four = rec_sum(list_three)
print(total_four)


#Method 6: Using sum()
print("Sum of all elements in a list Method 6 result: ")
numpy_arr_1 = np.array(list_three)
total_five = np.sum(numpy_arr_1)
print(total_five)


#Question 7: Remove duplicates from a list

#Method 1: using set() - only keeps unique elements, but does not preserve the original order
print("Removes duplicates in a list Method 1 result: ")
num_one = [1,2,3,2,1,4,5,3,1,9,0]
unique_one = list(set(num_one))
print(unique_one)

#Method 2: using dict.fromkeys()
print("Removes duplicates in a list Method 2 result: ")
unique_two = list(dict.fromkeys(num_one))
print(unique_two)


#Method 3: Using loop + set
print("Removes duplicates in a list Method 3 result: ")
unique_three = []
seen = set()
for num in num_one:
	if num not in seen:
		unique_three.append(num)
		seen.add(num)
print(unique_three)


#Method 4: Using list comprehension + list
print("Removes duplicates in a list Method 4 result: ")
seen_one = set()
unique_four = [x for x in num_one if not (x in seen_one or seen_one.add(x))]
print(unique_four)


#Method 5: using collections.orderedDict
print("Removes duplicates in a list Method 5 result: ")
from collections import OrderedDict
unique_five = list(OrderedDict.fromkeys(num_one))
print(unique_five)


#Method 6: Using new list to store elements, without built-in functions (Time complexity: O(n^2), Space complexity: O(n))
print("Removes duplicates in a list Method 6 result: ")
def remove_duplicates(list):
	result = []
	for item in list:
		found = False
		for r in result:
			if r == item:
				found = True
				break
		if not found:
			result.append(item)
	return result
print(remove_duplicates(num_one))


#Method 7: Using same list to store elements (in-place), without built-in functions (Time complexity: O(n^2), Space complexity: O(1))
print("Removes duplicates in a list Method 7 result: ")
def remove_duplicates_inplace(list):
	i = 0
	while i<len(list):
		j = i + 1
		while j < len(list):
			if list[i] == list[j]:
				list.pop(j)
			else:
				j += 1
		i += 1
	return list
list_in = [1,2,3,2,4,1,5,3]
print(remove_duplicates_inplace(list_in))

#Question 8: Merge two lists

#Method 1: Using + operator (creates a new list, does not modify original lists)
print("Merge two lists Method 1 result: ")
m3 = [1,2,3]
m4 = [4,5,6]
merged_one = m3 + m4
print(merged_one)


#Method 2: in-place: Using list.extend() (does not create a new list, modifies m1 permanently)
print("Merge two lists Method 2 result: ")
m3.extend(m4)
print(m3)


#Method 3: using unpacking (creates a new list, less efficient due to unpacking overhead)
print("Merge two lists Method 3 result: ")
m1 = [1,2,3]
m2 = [4,5,6]
merged_three = [*m1,*m2]
print(merged_three)

#Method 4: using for loop
print("Merge two lists Method 4 result: ")
merged_four = []
for item in m1:
	merged_four.append(item)
for item in m2:
	merged_four.append(item)
print(merged_four)


#Method 5: using itertools.chain()
print("Merge two lists Method 5 result: ")
from itertools import chain
merged_five = list(chain(m1,m2))
print(merged_five)


#Method 6: using numpy.concatenate() - superfast for large numeric lists, but not memory efficient for small lists
print("Merge two lists Method 6 result: ")
import numpy as np
merged_six = np.concatenate((m1,m2))
print(merged_six)

#Question 9: List comprehension for squares
n=10

print("List comprehension for squares Method 1 result: ")
square_one = [x*x for x in range(1,n+1)]
print(square_one)

print("List comprehension for squares Method 2 result: ")
square_two = [pow(x,2) for x in range(1,n+1)]
print(square_two)

print("List comprehension for squares Method 3 result: ")
square_three = [x*x for x in range(1,n+1) if x%2 == 0]
print(square_three)

print("List comprehension for squares Method 4 result: ")
square_four = [[x*x for x in range(1,n+1)]for _ in range(5)]
print(square_four)

print("List comprehension for squares Method 5 result: ")
square_five = (x*x for x in range(1,n+1))
for num_five in square_five:
	print(num_five)

print("List comprehension for squares Method 6 result: ")
square_six_dict = {x:x*x for x in range(1,n+1)}
print(square_six_dict)




#Question 10: calculate the frequency of elements in a list

#Method 1: Naive nested loop
print("Calculate the frequency of elements in a list Method 1 result: ")
arr_freq = [1,2,2,3,1,4,2,3,1,5]
def bruteforce_freq(arr):
	freq_count = {}
	for num in arr:
		count = 0
		for ele in arr:
			if ele == num:
				count += 1
		freq_count[num] = count
	return freq_count
res_1 = bruteforce_freq(arr_freq)
print(res_1)				

#Method 2: Manual dictionary
print("Calculate the frequency of elements in a list Method 2 result: ")
def manual_dict(arr):
	freq_count = {}
	for num in arr:
		if num in freq_count:
			freq_count[num] += 1
		else:
			freq_count[num] = 1
	return freq_count
res_2 = manual_dict(arr_freq)
print(res_2)

#Method 3: dict.get()
print("Calculate the frequency of elements in a list Method 3 result: ")
def freq_dict_get(arr):
	freq_count = {}
	for num in arr:
		freq_count[num] = freq_count.get(num,0) + 1
	return freq_count
res_3 = freq_dict_get(arr_freq)
print(res_3)


#Method 4: using defaultdict(int)
print("Calculate the frequency of elements in a list Method 4 result: ")
from collections import defaultdict
def df_dict(arr):
	freq_count = defaultdict(int)
	for num in arr:
		freq_count[num] += 1
	return freq_count
res_4 = df_dict(arr_freq)
print(res_4)
		
	
#Method 5: Using counter
print("Calculate the frequency of elements in a list Method 5 result: ")
from collections import Counter
res_5 = Counter(arr_freq)
print(res_5)


#Method 6: Using pandas.value_counts()
print("Calculate the frequency of elements in a list Method 6 result: ")
import pandas as pd
res_6 = pd.Series(arr_freq).value_counts()
print(res_6)
