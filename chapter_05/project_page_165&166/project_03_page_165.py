"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: project_03_page_165.py
Problem:
    Modify the sentence-generator program of Case Study 5.3 so that it inputs its
    vocabulary from a set of text files at startup. The filenames are nouns.txt, verbs.
    txt, articles.txt, and prepositions.txt. (Hint: Define a single new function,
    getWords. This function should expect a filename as an argument. The function
    should open an input file with this name, define a temporary list, read words
    from the file, and add them to the list. The function should then convert the list
    to a tuple and return this tuple. Call the function with an actual filename to initialize
    each of the four variables for the vocabulary.)
Solution:

"""
import random

from case_study.case_study_page_150 import articles, nouns, verbs, prepositions


def getWords():
    openFile = open('x', 'r')
    readFile = openFile.read()
    listWords = []  # declaring a list
    listWords = [readFile]
    tupleList = tuple(listWords)  # Converting to tuple
    readFile.close()
    return tupleList

    def sentence():
        return nounPhrase() + " " + verbPhrase()

    def nounPhrase():
        return random.choice(getWords(articles)) + " " + random.choice(nouns)

    def verbPhrase():
        return random.choice(verbs) + "  " + nounPhrase() + " " + \
               prepositionalPhrase()

    def prepositionalPhrase():
        return random.choice(prepositions) + " " + nounPhrase()

    def main():
        nouns = input("Enter the noun file name: ")
        verbs = input("Enter verb file name: ")
        prepositions = input("Enter the preposition file name: ")
        articles = input("Enter the article file name: ")

        prepositions = getWords(prepositions)
        nouns = getWords(nouns)
        verbs = getWords(verbs)
        articles = getWords(articles)

        number = int(input("Enter the number of sentences: "))

        for count in range(number):
            print(sentence())
