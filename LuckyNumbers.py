lucky_numbers = [ 5, 23, 45 , 12, 33]
count = 0
guess_list = []
while lucky_numbers != []:
    guess = int(input("Guess a number (1-50): "))
    if guess in guess_list:
        print("you already guessed it!")
        break
    elif guess in lucky_numbers:
        lucky_numbers.remove(guess)
        count = count + 1
    elif guess > 50 or guess < 1:
        print("number outside range")
    else:
        count = count + 1
    guess_list.append(guess)
    if len(guess_list) == 20:
        guess_list = []
        print("start over!")
        count = 0
        
print("you had " + str(count) + " guesses within range")
print(guess_list)
