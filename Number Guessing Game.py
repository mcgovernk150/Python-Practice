import random

random_number = random.randint(-100,100)

attempts = 0
tries_allowed = 10
print("Hello, welcome to the game. You will be choosing a number between 1 and 100")

print("You only get " + str(tries_allowed) + " tries.")

my_list = []

while attempts < tries_allowed:
    guess = int(input("Please guess a number: "))
    if guess in my_list:
        print("You have already guessed " + str(guess))
        continue
    attempts += 1
    my_list.append(guess)
    if guess > random_number:
            print("Guess is too high, try a smaller number")
    elif guess < random_number:
            print("Guess is too low, try a higher number")
    elif guess == random_number:
            print("Correct- you win in", str(attempts), "guesses")
            break
else:
    if attempts == 10:
       print("You failed to guess in time")

for item in my_list:
    print(item)
