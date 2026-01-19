# Debugging and Error Handling

"""
Dont:
Write enire programs
Test entire programs
Debug entire programs

Do:
write a function
Test a function
Debug a function
Do integration testing
Backup the code
"""

# 1. Glass box debugging
def abs(x):
    if x < -1:
        return -x
    else:
        return x
print(abs(-10))  # Output: 10
print(abs(10))   # Output: 10
print(abs(-1))   # Output: -1 (Incorrect output) This is the bug

# 2. Handing special exceptions
try:
#    a = int(input("Enter a number: "))
#    b = int(input("Enter another number: "))
    a = 10
    b = 0
    print("a/b = ", a / b)
    print("a + b = ", a + b)
except ValueError:
   print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except:
    print("You are cooked")

# 3. Raise an exception
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除數不能是 0")  # 丟錯誤
    return a / b
try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("處理錯誤：", e)  # 接錯誤

def get_ratios(L1, L2):
    """Assumes L1 and L2 are lists of equal length.
    Returns a list containing L1[i]/L2[i]"""
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i] / L2[i])
        except ZeroDivisionError:
            ratios.append(float('nan'))  # 除數是 0
        except:
            raise ValueError("get_ratios called with bad arg")
    return ratios

print(get_ratios([1, 2, 3], [4, 5, 0]))  # Output: [0.25, 0.4, nan]

def get_grades(class_list):
    new_stats = []
    for elt in class_list:
        # new_stats.append(elt[0], elt[1], avg(elt[1]))
        new_stats.append((elt[0], elt[1], avg(elt[1])))  # 包成 tuple
    return new_stats

def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('Warning: No grades data')
        return None

print(get_grades([('Tom', [90, 80, 70]), ('John', [])]))  # Output: Warning: No grades data [('Tom', [90, 80, 70], 80.0), ('John', [], None)]

# assert(斷言): Will terminate the program if the condition is False
def sqrt(x):
    assert x >= 0, "x 必須 >= 0"
    return x ** 0.5

print(sqrt(9))   # 3.0
print(sqrt(-1))  # AssertionError: x 必須 >= 0