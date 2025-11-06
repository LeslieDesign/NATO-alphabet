import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def nato_phonetic():
    answer = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in answer]
    except KeyError:
        print("Sorry, only letters are allowed.")
        nato_phonetic()
    else:
        print(f"Your phonetic library for spelling this word is: {output_list}")

nato_phonetic()