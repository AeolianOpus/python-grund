city = "Stockholm"
print (city)

Age = 25
age = 30
print(Age)
print(age)

x = 42
print (x)
x = "Now Im a string"
print (x)

a, b, c = 10, 20, "Thirty"
print (a, b, c)

num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print (num_str, type(int))
print (num_float, type(float))

x = 5
y = x
x = 10
print("x:", x)
print("y:", y)

a, b = 5, 10
a, b = b, a
print("a:", a)
print("b:", b)

word = 'Guitars'
length = len(word)
print('Length of string: ', length)

x = "global"
def my_func():
    x = "local"
    print("In function:", x)

my_func()
print("Outside function:", x)