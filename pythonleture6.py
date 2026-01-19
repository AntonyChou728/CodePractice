# Lecture Topic : Recursion and Dictionary

# iteration version

def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial_iter(5))  # Output: 120

# recursive version
def factorial_recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recur(n - 1)
print(factorial_recur(5))  # Output: 120

# hanoi tower
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')

# Fibonacci sequence
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))  # Output: 8

# is_palindrome function
def is_palindrome(s):
    def tochars(s):
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    def isPalindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPalindrome(s[1:-1])
    return isPalindrome(s)
print(is_palindrome("A man a plan a canal Panama"))  # Output: True


# list: using index numbers
list_a = [1, 2, 3]
print(list_a)        # Output: [1, 2, 3]
print(list_a[0])     # Output: 1 
print(list_a[-1])    # Output: 3
print(list_a[0:2])   # Output: [1, 2]
list_a.append(4)
print(list_a)        # Output: [1, 2, 3, 4]

# dictionary: using key-value pairs
dic_a = {'name': 'Alice', 'age': 25}
print(dic_a)        # Output: {'name': 'Alice', 'age': 25}
print(dic_a['name']) # Output: Alice
print(dic_a['age'])  # Output: 25
dic_a['grade'] = 'A'
print(dic_a)        # Output: {'name': 'Alice', 'age': 25, 'grade': 'A'}
print(dic_a.keys())   # Output: dict_keys(['name', 'age', 'grade'])
print(dic_a.values()) # Output: dict_values(['Alice', 25, 'A'])

def count_letters(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d
print(count_letters("hello world"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def count_words(s):
    mydict = {}
    for word in s.lower().split():
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    return mydict
print(count_words("Hello world hello"))  # Output: {'hello': 2, 'world': 1}

def most_common_word(s):
    values = freq.values()
    best = max(values)
    words = []
    for k in freq:
        if freq[k] == best:
            words.append(k)
    return (', '.join(words), best)

def words_often(freq, min_times):
    result = []
    done = False
    while not done:
        temp = most_common_word(freq)
        if temp[1] >= min_times:
            result.append(temp)
            for w in temp[0].split():
                del freq[w]
        else:
            done = True
    return result
freq = count_words("hello world hello")
print(words_often(freq, 2))  # Output: [('hello', 3)]

def fib_efficient(n, d):
    if n in d:
        return d[n]
    if n == 0 or n == 1:
        result = 1
    else:
        result = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = result
    return result

d = {1:1, 2:2}
print(fib_efficient(6, d))  # Output: 8