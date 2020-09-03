import random
import string


def concatenate(list):
    string = ''
    for i in range(len(list)):
        string = string + list[i]
    return string

guess_list = ('python', 'java', 'kotlin', 'javascript')
guess = guess_list[random.randint(0, len(guess_list) - 1)]
guessed = list(len(guess) * '-')
typed_letters = ''
attempts = 0
play = ''

print('H A N G M A N')

while play != 'play' and play != 'exit':
    play = input('Type "play" to play the game, "exit" to quit:')

while play == 'play':

    while attempts < 8 and guess != concatenate(guessed):
        print()
        print(concatenate(guessed))
        letter = input('Input a letter:')

        if len(letter) > 1:
            print('You should input a single letter')

        elif letter not in string.ascii_lowercase:
            print('It is not an ASCII lowercase letter')

        elif letter in typed_letters:
            print('You already typed this letter')

        elif guess.find(letter) != -1:
            typed_letters = typed_letters + letter
            for n in range(len(guess)):
                if guess[n] == letter:
                    guessed[n] = letter
        else:
            typed_letters = typed_letters + letter
            print('No such letter in the word')
            attempts += 1

    if guess == concatenate(guessed):
        print('You guessed the word ' + guess + '!')
        print('You survived!')
        break
    else:
        print('You are hanged!')
        break
