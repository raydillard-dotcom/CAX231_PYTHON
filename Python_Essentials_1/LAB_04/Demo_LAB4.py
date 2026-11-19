def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None

def wishes():
    return "Happy Birthday!"
 
w = wishes()
 
print(w) # outputs: Happy Birthday!

# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))

def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))

def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)



def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
my_numbers = [10, 20, 30, 40, 50]

for i in range(4):
    my_numbers.insert(i, my_numbers[-1])

print(my_numbers)

x = 5
y = 2
print(x // y, x % y)

for i in range(1, 10, 2):
    pass

