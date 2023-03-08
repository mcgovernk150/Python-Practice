#Write a loop that accumulates the sum of all the numbers in a list (given below) and prints the sum in the end
data = [0, -1, 2, -3, 4, -5, 6, -7, 8]
def sum (data):
    total = 0
    for x in data:
        total += x
    return total
print (sum(data))

#Write a loop that accumulates the sum of absolute value of all the numbers in a list (given below) and prints the sum in the end
import math

output = sum ([abs(number) for number in data])

print (output)
