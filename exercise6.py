'''Create a function named is_triangle_possible() that accepts three positive numbers. It should return True when it is possible to create a triangle from the line segments of given lengths and False otherwise.
'''

def is_triangle_possible(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(is_triangle_possible(1, 2, 3))
print(is_triangle_possible(1, 1, 1))


'''
Create two functions: print_five_times() and speak(). The function print_five_times() should accept one parameter (called sentence) and print it five times.
'''

def print_five_times(sentence):
    for i in range(5):
        print(sentence)