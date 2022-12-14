import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
word = response.content.splitlines()

random_num = random.randint(0,10000)

word_list = str(word[random_num].decode())


while len(word_list) != 5:
    random_num = random.randint(0, 10000)
    word_list = str(word[random_num].decode())

print('Welcome to Wordle!')
# list of words

def word_len_checker():
    word_input = input(f"\u001b[0m{'-> '}").lower()
    while len(word_input) != 5:
        print(f'\u001b[31m{"Enter a 5 letter word"}')
        word_input = input(f"\u001b[0m{'-> '}").lower()
    return word_input

wins = 0
def wordle():
    print()
    word = word_list
    num_of_guesses = 6

    print(f'\033[0m{"Enter a 5 letter word"}')

    word_guess = word_len_checker()

    while num_of_guesses > 1:

        if word_guess == word:
            global wins
            wins+=1
            print(f"\u001b[34m{':-)'}")
            break

        for i in range(len(word_guess)):
            if word_guess[i] == word[i]:
                print("\033[0;32;48m{}".format(word_guess[i]), end='')

            if word_guess[i] != word[i] and word_guess[i] in word:
                print("\033[0;33;48m{}".format(word_guess[i]), end='')

            if word_guess[i] not in word:
                print("\033[0;30;48m{}".format(word_guess[i]), end='')

        num_of_guesses -= 1
        print()
        word_guess = word_len_checker()


num_of_games = 0
while True:
    num_of_games += 1
    wordle()
    print("\033[0m{}".format('\nDo you want to play again? Yes/No'))
    play_again = input(':').lower()
    if play_again == 'no':
        break

print('\nThanks for playing!')
print(f'Your score is {(wins/num_of_games)*100} %\n Total played = {num_of_games}\n Total won = {wins}')
