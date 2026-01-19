# MIT OCW 6.001 2016 Fall (Lecture 11)

# Bisection Search 1 Example (切片法，會建立新列表)
def bisect_search1(L, target):
    if L == []:
        # return False
        raise ValueError("List is empty")
    elif len(L) == 1:
        # return L[0] == target
        if L[0] == target:
            return True
        else:
            raise ValueError(f"{target} not found in list")
    else:
        half = len(L) // 2
        if L[half] > target:
            return bisect_search1(L[:half], target) # ← 這裡!切片建立新列表
        else:
            return bisect_search1(L[half:], target) # ← 這裡!切片建立新列表
        
# print(bisect_search([1, 3, 5, 7, 9], 7))  # Output: True
# print(bisect_search([1, 3, 5, 7, 9], 8))  # Output: False
# 測試範例
try:
    print(bisect_search1([1, 3, 5, 7, 9], 7))  # Output: True
    print(bisect_search1([1, 3, 5, 7, 9], 8))  # 會拋出 ValueError
except ValueError as e:
    print(f"錯誤: {e}")

# Bisection Search 2 Example (索引法，不會建立新列表)
def bisect_search2(L, target):
    def bisect_search_helper(L, target, low, high):
        if high == low:
            return L[low] == target
        mid = (low + high) // 2
        if L[mid] == target:
            return True
        elif L[mid] > target:
            if low == mid: # Nothing left to search
                return False
            else:
                return bisect_search_helper(L, target, low, mid) # 不會建立新列表
        else:
            return bisect_search_helper(L, target, mid + 1, high) 
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, target, 0, len(L) - 1)
    
# Logarithmic time complexity: O(log n) 對數時間複雜度

def inttostr(i):
    """Converts an integer to its string representation."""
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i //= 10
    return result

print(inttostr(12345))  # Output: '12345'
print(inttostr(0))      # Output: '0'

# Recursive function example O(n) 階層
def fact_recur(n):
    """Assumes n is an int >= 0"""
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n - 1)
print(fact_recur(5))  # Output: 120
print(fact_recur(0))  # Output: 1

# polynomial evaluation O(n) 多項式求值
def poly_eval(poly, x):
    """Assumes poly is a list of numbers and x a number
    Evaluates polynomial at x.
    For example, if poly is [3, 2, 0, 5] and x is 2,
    this function returns 3*2^3 + 2*2^2 + 0*2^1 + 5*2^0"""
    total = 0
    for power in range(len(poly)):
        total += poly[power] * (x ** power)
    return total
print(poly_eval([3, 2, 0, 5], 2))  # Output: 43

# Exponentiation complexity example O(log n) 指數
def hanoi(n, source, target, auxiliary):
    """Assumes n is a positive int
    Prints moves required to move n disks from source to target using auxiliary"""
    if n == 1:
        print(f"Move disk from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)

# Test the hanoi function
""" Output:
 Move disk from A to C
 Move disk from A to B
 Move disk from C to B
 Move disk from A to C
 Move disk from B to A
 Move disk from B to C
 Move disk from A to C
"""
hanoi(3, 'A', 'C', 'B') 

#----------------------------------------------------------------------------------

# Exponentiation complexity example O(log n) 指數
def genSubsets(L): # L is a list 
    res = []
    if len(L) == 0:
        return [[]] # list of the empty set
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # last element
    new = []
    for small in smaller:
        new.append(small + extra) # add last element to each of the smaller subsets
    return smaller + new # combine subsets without last element and with last element
print(genSubsets([1, 2, 3])) # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(genSubsets([])) # Output: [[]]
#----------------------------------------------------------------------------------
import time
# Expotential time complexity O(2^n) 指數
class fibonacci(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
f = fibonacci()
time_start = time.time()
print(f.fib(6))  # Output: 8
time_end = time.time()
print(f"執行時間: {time_end - time_start} 秒")  #


# Dynamic Programming example O(n) 線性
def fib_list(n):
    if n <= 1:
        return 1
    fib = [0] * (n + 1)   # 建立長度 n+1 的清單
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
time_start = time.time()
print(fib_list(6))  # Output: 13
time_end = time.time()
print(f"執行時間: {time_end - time_start} 秒")  