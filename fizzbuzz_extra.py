import sys

passedCheck = False

if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
        passedCheck = True
    except ValueError:
        print("Must be a number.")

while not passedCheck:
    try:
        n = int(input("Enter upper limit: "))
        passedCheck = True
    except ValueError:
        print("Must be a number.")

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
