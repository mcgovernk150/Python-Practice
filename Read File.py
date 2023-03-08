#Receive a filename from the user (module6.txt), open the text file for reading, and read the file
#Count the sentences in the text file
#Count the number of words in the text file
#Print these two values with appropriate labels as a result of running the program
sentences = 0

f = open("C:/Users/kerri/OneDrive/Documents/IT 697 Python/module6.txt", "r")

print(f.read())

for line in f:
 
  lines += 1
  
  if line.startswith('\n'):
    blanklines += 1
  else:
      sentences += line.count('.') + line.count('!') + line.count('?')
   
    
print ("Number of sentences: ", sentences)
with open ("C:/Users/kerri/OneDrive/Documents/IT 697 Python/module6.txt", "r") as f:
    data = f.read()
words = data.split()
   


print ("Number of words: ",(len(words)))

