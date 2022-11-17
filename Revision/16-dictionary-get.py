translate = {"maça": "pomme", "cachorro": "chien", "gato": "chat", "dentro": "dans"}
s = int(0)
print("In our databank we have the translations, from portuguese to french, for the following words:")
for c in translate.keys():
    s += 1
    print(f"{s} - {c}")
word = str(input("Enter a word, in our databank to translate from portuguese to french: ")).lower()
print(f"{translate.get(word, f'The word {word} is not found')}")

