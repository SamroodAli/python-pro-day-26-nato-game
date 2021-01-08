""" Main file """
import pandas

# reading data from the nato phonetic alphabet csv file
csv_file_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary from the dataframe csv_file_data using dictionary comprehension
nato_dictionary = {
    row.letter: row.code for (index, row) in csv_file_data.iterrows()
}

# saving the user input
game_is_on = True
while game_is_on:
    user_word = input("Enter the word: ")
    if user_word.lower() == "exit":
        game_is_on = False
        break

    # user nato in dictionary
    try:
        user_word_nato = {
            letter: nato_dictionary[letter.title()] for letter in user_word
        }
        print("\nHere is your NATO code\n", user_word_nato)
        # user nato in list form
        user_word_nato_list = [code for (letter, code) in user_word_nato.items()]
        print("\n", user_word_nato_list)
    except KeyError:
        print("Sorry, only letters in the Alphabet please.")
