from bs4 import BeautifulSoup
import requests
import random

url = 'https://meaningpedia.com/5-letter-words?show=all'
req = requests.get(url)
s = BeautifulSoup(req.content,'html.parser')
find = s.find_all('li',class_='float-sm-left col-lg-3 col-md-2')
words = [i.text for i in find]
random_num = random.randint(0,len(words)-1)
wordlist = words[random_num]

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
    word = wordlist  # takes random word in the word list
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
