word = input("gimme a word: ")
#newWord;

def pluralize(word):
    if (word == "moose"):
        return word
    elif (word == "automaton"):
        return "automata"
    elif (word == "mouse"):
        return "mice"
    else:
        word += "s"
        return word

newWord = pluralize(word)
print(newWord)