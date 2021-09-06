"""
Author: Nguyen Xuan Tung
Date: 09/08/2021
Program: project_10_page_165.py
Problem:
    Conversations often shift focus to earlier topics. Modify the therapist program to
    support this capability. Add each patient input to a history list. Then, occasionally
    choose an element at random from this list, change persons, and prepend (add
    at the beginning) the qualifier “Earlier you said that” to this reply. Make sure that
    this option is triggered only after several exchanges have occurred.
Solution:

"""
import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")
qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")
replacements = {"I": "you", "me": "you", "my": "your",
                "we": "you", "us": "you", "mine": "yours"}


def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)


def changePerson(sentence):
    """Replaces first person pronouns with second person
     pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)


def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()
