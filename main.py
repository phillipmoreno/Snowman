from random_word import RandomWords

# API object created
r = RandomWords()


# Function created to notify the user whether they have won the game or not
def game_result(result, word):
    if result:
        print("Congrats! You guessed the word " + word + ". You win!")
    else:
        print("Oops! The mystery word was " + word + ". Better luck next time.")


# Function created to ask the user whether they want to play again or not
def play_again():
    print("Do you want to play Again? Y or N")
    res = input()
    if res == 'Y':
        start_game()


# Function created to start the game of Snowman
def start_game():
    # Random word is retrieved from API under certain conditions
    word = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb"))

    # Built in function is used to set all characters to lowercase
    word = word.lower()

    # Character array is declared to contain missing/found letters
    word_array = []

    # Character/list dictionary is created to hold letter key and value(index) pairs
    letter_dictionary = {}

    # Character/integer dictionary is declared to contain the letters entered
    letters_used = {}

    # Initialized boolean variable to check whether the user has won the game or not
    game_won = False

    # Initialized integer variable to check how many attempts the user has left at guessing letters
    lives = 5

    # For loop used to iterate through indices of word
    for x in range(len(word)):
        # if the character at index x is a letter, append an underline to serve as a letter guessing slot
        if word[x].isalpha():
            word_array.append("_")
            # if a key is found, the list value is appended with the next index
            if letter_dictionary.get(word[x]) is not None:
                letter_dictionary[word[x]].append(x)
            # if a key is not found, a key(letter)/value(indices) pair is stored
            else:
                letter_dictionary[word[x]] = [x]
        else:
            # if the character at index x is not a letter, a dash is appended to represent a space or hyphen
            word_array.append("-")

    print(word)

    # while loop used to continue game until player is out of lives or the player wins the game
    while lives >= 0 and game_won is False:
        print(str(lives) + " lives left!")
        for x in word_array:
            print(x, end=" ")
        letter_picked = input("Choose a letter: ")
        if letter_dictionary.get(letter_picked) is not None:
            if letters_used.get(letter_picked) is None:
                letters_used[letter_picked] = 1
                for j in letter_dictionary[letter_picked]:
                    word_array[j] = letter_picked
                    # if statement used to verify whether the current progress matches the complete word
                    if "".join(word_array) == word:
                        game_won = True
            else:
                print("You have already used character " + letter_picked + ". Pick a different one.")
        else:
            lives -= 1
        print("\n")

    game_result(game_won, word)
    play_again()


start_game()
