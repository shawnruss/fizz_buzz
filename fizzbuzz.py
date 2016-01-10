n = 30

print("Fizz buzz counting up to {}".format(n))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 != 0:
        print("fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("buzz")
    elif i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    else:
        print(i)
