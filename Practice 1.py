#Print numbers 1 through 5
for x in range (6):

            if x >= 0: print (x) 



#Print sum of 3 and 4
print (3 + 4) 

#Print sum of constant pi and square root of 2
import math 
print (math.pi)
print (math.sqrt (2))
print(math.pi + math.sqrt(2))


#Print sum of cos30 + sin30
math.radians
print (math.cos(30) + math.sin(30))

#Write code to print values of integers x, y, and z in a single line such that each value is left-justified in 6 columns
x,y,z = 1,2,3
print ("%-6d %-6d %-6d" %(x,y,z))

#Write code to print area of a circle given the value of the radius of the circle
r = (2)
print (math.pi * (r * r))


#Write code to print the greater of two given numbers x and y
print (max(x,y))

#Write code to print the result of negation of AND of two Boolean variables A and B
a = 83
b = 274

print(not(b > 90 and a < 90))

#Write a for-loop to sum the first 10 non-zero integers
print(sum(range(11)))

#Write a while-loop to sum the first 10 non-zero integers
sum = 0
i = 1
while i < 11:
  sum += i
  i += 1
print(sum)
