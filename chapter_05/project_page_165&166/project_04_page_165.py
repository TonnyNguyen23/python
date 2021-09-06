"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: project_04_page_165.py
Problem:
    Make the following modifications to the original sentence-generator program:
    a. The prepositional phrase is optional. (It can appear with a certain
    probability.)
    b. A conjunction and a second independent clause are optional: The boy took a
    drink and the girl played baseball.
    c. An adjective is optional: The girl kicked the red ball with a sore foot.
    You should add new variables for the sets of adjectives and conjunctions.
Solution:

"""
import random

# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()


def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences
 to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


# The entry point for program execution
if __name__ == "__main__":
    main()
