def function1(length):
    if length > 0:
        print(length)
        function1(length - 1)
length = 3
print(function1(length))