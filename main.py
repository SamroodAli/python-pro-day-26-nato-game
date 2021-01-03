"Main file"
import pandas

# reading data from the nato phonetic alphabet csv file
csv_file_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Creating a dictionary from the dataframe csv_file_data using dictionary comprehension
nato_dictionary = {
    row.letter: row.code for (index, row) in csv_file_data.iterrows()
}
