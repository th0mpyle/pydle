from random import *


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
        print("Welcome to Pydle!")
        words = open("Pydle/pydle/wordfiles/words.txt", "r")
        targets = open("Pydle/pydle/wordfiles/targets.txt", "r")
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
                print("You win!")
                break
            else:
                correct_letters_arr = []

                g_array = list(guess)
                t_array = list(target)
                for i in range(len(guess)):
                    if g_array[i] == t_array[i]:
                        correct_letters_arr.append(g_array[i])
                    else:
                        continue
                contained_letters_arr = []
                for i in range(len(guess)):
                    if g_array[i] in t_array:
                        if g_array[i] in contained_letters_arr:
                            pass
                        elif g_array[i] in correct_letters_arr:
                            pass
                        elif g_array[i] not in contained_letters_arr:
                            contained_letters_arr.append(g_array[i])
                    else:
                        continue
                if len(correct_letters_arr) > 0:
                    correct_letters = ", ".join(correct_letters_arr)
                    print(f"Correctly placed letters: {correct_letters}")
                if len(contained_letters_arr) > 0:
                    contained_letters = ", ".join(contained_letters_arr)
                    print(f"Contained letters: {contained_letters}")
                else:
                    print("There are no correct letters in your word.\n")
                tries += 1
            if tries == 6:
                print("You lose!")
                print(f"The answer was {target.upper()}.")
        


        
