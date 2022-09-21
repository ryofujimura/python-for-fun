'''
write a program that will ask for a positive integer and print all of the divisor of that number.
'''

number = int(input("Please enter a positive integer: "))
divisor = []
for i in range(1, number+1):
    if number % i == 0:
        divisor.append(i)
        
'''
print each divisor on a separate line'''
for i in divisor:
    print(i)