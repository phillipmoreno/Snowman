from random_word import RandomWords

# API object created
r = RandomWords()

# Random word is retrieved from API with certain conditions
word = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb"))

# Built in function is used to set all characters to lowercase
word = word.lower()

# Character array is declared to contain missing/found letters
wordArray = []

# Character dictionary is created to hold letter key and value(index) pairs
letterDictionary = {}

# Initialized boolean variable to check whether the user has won the game or not
gameWon = False

# Character array is declared to contain the letters entered
lettersUsed = []

# Initialized integer variable to check how many attempts the user has left at guessing letters
lives = 5


# for loop used to iterate through indices of word
for x in range(len(word)):
    # if the character at index x is a letter, append an underline to serve as a letter guessing slot
    if word[x].isalpha():
        wordArray.append("_")
        if letterDictionary.get(word[x]) is not None:
            letterDictionary[word[x]].append(x)
        else:
            letterDictionary[word[x]] = [x]
    else:
        wordArray.append("-")

print(word)

while lives >= 0 and gameWon is False:
    print(str(lives) + " lives left!")
    for x in wordArray:
        print(x, end=" ")
    letterPicked = input("Choose a letter: ")
    if letterDictionary.get(letterPicked) is not None:
        for j in letterDictionary[letterPicked]:
            wordArray[j] = letterPicked
        if "".join(wordArray) == word:
            gameWon = True
    else:
        lives -= 1
    print("\n")


if gameWon:
    print("Congrats! You solved the entire word")
else:
    print("Oops! The word you didn't solve was " + word)

