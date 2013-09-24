from random import randint

random_number = randint(1, 100)
print "Hi!"
name = raw_input("What's your name? >")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
tries = 0

while True:
    guess = int(raw_input("Your guess?"))
    tries = tries + 1
    if guess < random_number:
        print "Your guess is too low, try again."
    elif guess > random_number:
        print "Your guess is too high, try again."
    else:
        print "Well done, %s! You found my number in %d tries!" % (name, tries)
        break