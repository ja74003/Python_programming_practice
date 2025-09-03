#This file contains 2 search alogorithms and 8 sorting alogorithms

#Search 1: Linear search(can be applied on both sorted and unsorted arrays) - Time Complexity: O(n)[W.C, A.C],O(1)[B.C], Space Complexity: O(1)

#Method 1: Iteratuve linear search using for loop
def linear_search(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i
	return -1
arr = [5,3,8,6,7]
ele1 = linear_search(arr,8)
print(f"Linear search method 1, in {arr} the element is found at index: {ele1}")

#Method 2: Linear search using string enumerate
def linear_search_enumerate(arr,target):
	for index,value in enumerate(arr):
		if value == target:
			return index
	return -1
ele2 = linear_search_enumerate(arr,7)
print(f"Linear search method 2, in {arr} the element is found at index: {ele2}")

#Method 3: Linear search using recursion (should not use in real life as space complexity is O(n) due to recursion stack)
def linear_search_recursion(arr,target,index=0):
	if index >= len(arr):
		return -1
	if arr[index] == target:
		return index
	return linear_search_recursion(arr,target,index+1)
ele3 = linear_search_recursion(arr,3)
print(f"Linear search method 3, in {arr} the element is found at index: {ele3}")

#Search 2: Binary Search(Can be applied on sorted arrays only) - Time complexity : O(logn) [A.C, W.C], O(1) [B.C], Space Complexity: O(1) [iterative version], O(logn) [recursive stack version]

#Method 1: Iterative binary search
def binary_search_iterative(arr1,target):
	left, right = 0, len(arr1)-1
	while left <= right:
		mid = (left + right)//2
		if arr1[mid] == target:
			return mid
		elif arr1[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1
arr1 = [1,3,5,7,9,11]
ele4 = binary_search_iterative(arr1,9)
print(f"Binary search method 1: in {arr1} the target is found at {ele4}")



#Method 2: Recursive Binary search
def binary_search_recursive(arr1,target,left = 0, right = None):
	if right is None:
		right = len(arr1) - 1
	if left > right:
		return -1
	mid = (left + right) // 2
	if arr1[mid] == target:
		return mid
	elif arr1[mid] < target:
		return binary_search_recursive(arr1,target,mid+1,right)
	else:
		return binary_search_recursive(arr1,target,left,mid-1)
ele5 = binary_search_recursive(arr1,3)
print(f"Binary search method 2: in {arr1} the target is found at {ele5}")



#Method 3: Using bisect module
import bisect
index = bisect.bisect_left(arr1,11)
if index < len(arr1) and arr1[index] == 11:
	print("Binary search method 3: element found at index", index)
else:
	print("Binary search method 3: element not found")
	
#Sorting 1: Bubble sort (the largest element bubbles up to the last position in each pass by adjacent swaps), Time complexity: O(n) [B.C.], O(n^2) [A.C/W.C], Space complexity: O(1) [basic/optimized bubble sort], O(n) [recursive bubble sort]

#Method 1: Basic Bubble Sort
def basic_bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
ele9 = basic_bubble_sort(arr1)
print(f"Basic bubble sort method 1 result is: {ele9}")


#Method 2: Optimized Bubble Sort (In this case, if array is already sorted then time complexity = O(n) [B.C])
def optimised_bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1],arr[j]
				swapped = True
		if not swapped:
			break
	return arr
ele10 = optimised_bubble_sort(arr1)
print(f"Optimised bubble sort method result is: {ele10}")


#Method 3: Recursive Bubble Sort (In this case space complexity will be O(n) due to recursion stack)
def recursion_bubble_sort(arr,n = None):
	if n is None:
		n = len(arr)
	if n == 1:
		return arr
	for i in range(n-1):
		if arr[i]>arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
	return recursion_bubble_sort(arr,n-1)
ele11 = recursion_bubble_sort(arr1)
print(f"Recursive bubble sort method result is: {ele11}")
	

#Sorting 2: Selection Sort (The minimum element is put at the 1st position in each pass), Time Complexity : O(n^2) [B.C, A.C, W.C] Space complexity: O(1)[iterative selection sort], O(n) [recursive selection sort]


#Method 1: Iterative Selection Sort
def selection_iterative(arr):
	n = len(arr)
	for i in range(n):
		min_index = i
		for j in range(i+1,n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i],arr[min_index] = arr[min_index], arr[i]
	return arr
ele6 = selection_iterative(arr1)
print(f"Selection sort iterative method 1 result: {ele6}") 
 

#Method 2: Recursive Selection Sort
def selection_recursive(arr,start=0):
	if start >= len(arr) - 1:
		return arr
	min_index = start
	for i in range(start+1,len(arr)):
		if(arr[i]<arr[min_index]):
			min_index = i
	arr[start],arr[min_index] = arr[min_index],arr[start]
	return selection_recursive(arr,start+1)
ele7 = selection_recursive(arr1)
print(f"Selection sort recursive method 2 result: {ele7}")
	


#Method 3: Descending Selection Sort
def selection_sort_desc(arr):
	n = len(arr)
	for i in range(n):
		max_index = i
		for j in range(i+1,n):
			if(arr[j] > arr[max_index]):
				max_index = j
		arr[i],arr[max_index] = arr[max_index],arr[i]
	return arr
ele8 = selection_sort_desc(arr1)
print(f"Selection sort descending sort method 3 result: {ele8}")


#Sorting 3: Insertion sort (Time complexity: O(n^2) [A.C/W.C], O(n) [B.C], Space Complexity: O(1))

#Method 1: Iterative insertion sort
def insertion_sort_iter(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i-1
		while j>=0 and arr[j]>key:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr
ele12 = insertion_sort_iter(arr1)
print(f"Insertion sort iterative method result is: {ele12}")

#Sorting 4: Merge Sort (Time complexity: O(nlogn) [B.C, W.C, A.C], Space complexity: O(n))
def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result

def merge_sort(arr):
	if(len(arr)<=1):
		return arr
	mid = len(arr)//2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left,right)

ele13 = merge_sort(arr1)
print(f"Merge sort recursive approach method result is: {ele13}")



#Sorting 5: Quick Sort - A pivot is choosen and placed at it's correct position using partition. The elements at left are smaller and right is greater. The same process is repeated untill the array is sorted (Time complexity: O(nlogn) [B.C/A.C], O(n^2):  W.C], Space complexity: O(logn) due to stack)

#Method 1: Quick sort using Lomuto partition style (first element is choosen as the pivot)
def partition(arr,low,high):
	pivot = arr[low]
	i = low+1
	j = high
	while True:
		while i<=j and arr[i] <= pivot:
			i += 1
		while i<=j and arr[j] > pivot:
			j -= 1
		if i<=j:
			arr[i],arr[j] = arr[j], arr[i]
		else:
			break
	arr[low], arr[j] = arr[j],arr[low]
	return j

def quick_sort_basic(arr, low=0, high=None):
	if high is None:
		high = len(arr) - 1
	if low < high:
		p = partition(arr,low,high)
		quick_sort_basic(arr,low,p-1)
		quick_sort_basic(arr,p+1,high)
	return arr
arr2 = [10,7,8,9,1,5]
ele14 = quick_sort_basic(arr2)
print(f"Quick sort basic lomuto method result is: {ele14}")
	



#Method 2: Quick sort using Hoare's partition (Random element is choosen as pivot)
import random
def hoare_partition(arr,low,high):
	pivot_index = random.randint(low,high)
	pivot = arr[pivot_index]
	arr[low],arr[pivot_index] = arr[pivot_index],arr[low]
	i = low - 1
	j = high + 1
	while True:
		i += 1
		while arr[i]<pivot:
			i += 1
		j -= 1
		while arr[j]>pivot:
			j -= 1
		if i>=j:
			return j
		arr[i],arr[j] = arr[j],arr[i]
	

def quick_sort_randomized(arr,low=0,high=None):
	if high is None:
		high = len(arr) - 1
	while low < high:
		p = hoare_partition(arr,low,high)
		if p - low < high - p:
			quick_sort_randomized(arr,low,p)
			low = p+1
		else:
			quick_sort_randomized(arr,p+1,high)
			high = p
	return arr
arr3 = [10,7,8,9,5]
ele15 = quick_sort_randomized(arr3)
print(f"Quick sort randomized sorting result is: {ele15}")

#Sorting 6: Counting Sort
def counting_sort(arr):
	min_value = min(arr)
	max_value = max(arr)
	range_val = max_value - min_value + 1
	count = [0]*range_val
	output = [0]*len(arr)
	
	#count the frequency of each element and add it in count array 1 by 1
	for num in arr:
		count[num - min_value] += 1
	
	#calculative the cumulative sums and update the count array
	for i in range(1,len(count)):
		count[i] += count[i-1]
		
	#Build the output array
	for num in reversed(arr):
		output[count[num - min_value] - 1] = num
		count [num - min_value] -= 1
		
	#copy the output array into original array
	for i in range(len(arr)):
		arr[i] = output[i]
		
	return arr
ele16 = counting_sort(arr3)
print(f"The counting sort result is: {ele16}")
	
	
#Sorting 7: Radix Sort (Performs counting sort digit by digit upto 'd' passes where d = #digits in the maximum number in the array), Time complexity: O(d*(n+k)), Space complexity: O(n+k)
def counting_sort_for_radix(arr,exp):
	n = len(arr)
	output = [0]*n
	count = [0]*10
	
	for num in arr:
		digit = (num//exp)%10 #extract the digits at a given place (1,10,100.....) from num i.e num//exp removes the ones place if exp = 10, 10's place if exp = 100 etc. and (num//exp)%10 gives the last digit of that result(num//exp)
		count[digit] += 1
		
	for i in range(1,10):
		count[i] += count[i-1]
	
	for i in range(n-1,-1,-1):
		digit = (arr[i]//exp)%10
		output[count[digit] - 1] = arr[i]
		count[digit] -= 1
		
	for i in range(n):
		arr[i] = output[i]
		

def radix_sort(arr):
	max_val = max(arr)
	exp = 1
	while max_val//exp > 0:
		counting_sort_for_radix(arr,exp)
		exp *= 10
	return arr
arr4 = [170,45,75,90,802,24,2,66]
ele17 = radix_sort(arr4)
print(f"The radix sort result is : {ele17}")



#Sorting 8: Heap Sort (Time complexity: O(nlogn) [B.C, A.C, W.C], Space Complexity: O(1))
def heapify(arr,n,i):
	largest = i
	left = 2*i + 1
	right = 2*i + 2
	if left < n and arr[left] > arr[largest]:
		largest = left
	if right < n and arr[right] > arr[largest]:
		largest = right
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr,n,largest)
	
	
def heap_sort(arr):
	n = len(arr)
	
	for i in range(n//2-1,-1,-1):
		heapify(arr,n,i) #Build the heap using heapify in O(n)
		
	for i in range(n-1,0,-1):
		arr[i],arr[0] = arr[0],arr[i] #Move maximum element to the end
		heapify(arr,i,0) #reheapify the reduced heap in O(nlogn)
	return arr
	
ele18 = heap_sort(arr4)
print(f"The heap sort using heapify method result is: {ele18}")

