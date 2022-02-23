from random import *
from colorama import Fore, Style

def word_list_check(guess, arr):
    flag = 0
    index = 0
    for line in arr:
        # if flag returns 1 then the program should run
        # this is messy but the order is hard to change
        index += 1
        if guess == "":
            flag = 3
        elif guess in line:
            flag = 1
        elif len(guess) != 5:
            flag = 2
        else:
            continue
    return flag

if __name__ == "__main__":
    while True:
        print("\nWelcome to Pydle!")
        words = open("pydle/wordfiles/words.txt", "r")
        targets = open("pydle/wordfiles/targets.txt", "r")
        target_list = targets.readlines()
        word_list = words.readlines()
        lines = 0
        tries = 0
        for i in range(len(target_list)):
            lines += 1
        index = target_list[randint(0, len(target_list) - 1)]
        target = index[3:8]
        word = "NaN"
        while True:
            while True:
                guess = input("\nGuess: \n").lower()
                test = word_list_check(guess, word_list)
                if test == 0:
                    print("Not in word list!")
                elif test == 2:
                    print("Word must be 5 letters long!")
                elif test == 3:
                    print("Please enter something...")
                else:
                    break
            
            if guess == target:
                print(Fore.GREEN + guess.upper())
                print(Style.RESET_ALL)
                print('You win!!')
                yn = input("Another game? (press Y to continue): ")
                break
            else:
                response_blocks = []
                guess_arr = list(guess)
                target_arr = list(target)
                for index in range(len(guess)):
                    if guess_arr[index] == target_arr[index]:
                        greenletter = Fore.GREEN + guess_arr[index].upper()
                        response_blocks.append(greenletter)
                    elif guess_arr[index] in target_arr:
                        yellowletter = Fore.YELLOW + guess_arr[index].upper()
                        response_blocks.append(yellowletter)
                    else:
                        whiteletter = Fore.WHITE + guess_arr[index].upper()
                        response_blocks.append(whiteletter)
                print(''.join(response_blocks))
                print(Style.RESET_ALL)
                tries += 1
            if tries == 6:
                print("You lose!")
                print(f"The answer was {target.upper()}.")
                yn = input("Another game? (press Y to continue): ")
        if yn.lower() == 'y':
            continue
        else:
            print("Thank you for playing my game! I spent ages making this.")
            break


        
