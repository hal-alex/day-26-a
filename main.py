# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import csv


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_from_csv = {}

with open('nato_phonetic_alphabet.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

print(dict_from_csv)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Type in a word: ").upper()

decoded_word = {letter:dict_from_csv[letter] for letter in user_input}

print(decoded_word)