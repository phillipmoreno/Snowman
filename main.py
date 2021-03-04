from random_word import RandomWords

# API object created
r = RandomWords()

# Random word is retrieved from API with certain conditions
word = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb"))

# Built in function is used to set all characters to lowercase
word = word.lower()

# Character array is declared to contain missing/found letters
wordArray = []

# Character/list dictionary is created to hold letter key and value(index) pairs
letterDictionary = {}

# Character/integer dictionary is declared to contain the letters entered
lettersUsed = {}

# Initialized boolean variable to check whether the user has won the game or not
gameWon = False

# Initialized integer variable to check how many attempts the user has left at guessing letters
lives = 5


# for loop used to iterate through indices of word
for x in range(len(word)):
    # if the character at index x is a letter, append an underline to serve as a letter guessing slot
    if word[x].isalpha():
        wordArray.append("_")
        # if a key is found, the list value is appended with the next index
        if letterDictionary.get(word[x]) is not None:
            letterDictionary[word[x]].append(x)
        # if a key is not found, a key(letter)/value(indices) pair is stored
        else:
            letterDictionary[word[x]] = [x]
    else:
        # if the character at index x is not a letter, a dash is appended to represent a space or hyphen
        wordArray.append("-")

print(word)

# while loop used to continue game until player is out of lives or the player wins the game
while lives >= 0 and gameWon is False:
    print(str(lives) + " lives left!")
    for x in wordArray:
        print(x, end=" ")
    letterPicked = input("Choose a letter: ")
    if letterDictionary.get(letterPicked) is not None:
        if lettersUsed.get(letterPicked) is None:
            lettersUsed[letterPicked] = 1
            for j in letterDictionary[letterPicked]:
                wordArray[j] = letterPicked
                # if statement used to verify whether the current progress matches the complete word
                if "".join(wordArray) == word:
                    gameWon = True
        else:
            print("You have already used character " + letterPicked + ". Pick a different one.")
    else:
        lives -= 1
    print("\n")


# Check if the user has won the game or not
if gameWon:
    print("Congrats! You guessed the word " + word + ". You win!")
else:
    print("Oops! The mystery word was " + word + ". Do you want to play again?")