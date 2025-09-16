def square(n):
    n = n * n
    return n

def is_even(num):
    if num % 2 == 0:
        return "Yes it is even"
    else:
        return "No it is odd"

def string_len(s):
    return len(s)
    

print(square(3))
print(is_even(13))
print(string_len("This is a String"))