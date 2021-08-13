from collections import defaultdict

import math

class Marathi:

    def __init__(self): #initializes the alphabet, and generates the dictionaries.

        swar = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", "अं", "अः"]

        vyanjan = [["क", "ख", "ग", "घ", "ङ"],
                   ["च", "छ", "ज", "झ", "ञ"],
                   ["ट", "ठ", "ड", "ढ", "ण"],
                   ["त", "थ", "द", "ध", "न"],
                   ["प", "फ", "ब", "भ", "म"],
                   ["य", "र", "ल", "व", "श"],
                   ["ष", "स", "ह", "क्ष", "ज्ञ"]]

        dictME = {}
        with open(eng_dict.txt) as eng:
            
        dictEM = defaultdict(list)
        marathi_list = []


    def update_dictEM(self): #updates English to Marathi Dictionary

        {self.dictEM[v].append(k) for k, v in self.dictME.items()}


    def jodakshar(self):
        return


    def add_word(self, word, definition, dict):
        if dict == "Marathi":
            self.dictME[word] = definition

        elif dict == "English":
            self.dictEM = definition


    def check_if_word_exists(self, word, lang):

        if lang == "Marathi":
            for i in self.dictME:
                if i == word:
                    return True

        elif lang == "English":
            for i in self.dictEM:
                if i == word:
                    return True

        return False


    def translate(self, lang1, lang2, word): #translates between the dictionaries

        tword = ""

        if lang1 != "English" and lang2 != "English":
            return "Bad input"

        if lang1 != "Marathi" and lang2 != "Marathi":
            return "Bad input"

        if lang1 == "Marathi":

            if not self.check_if_word_exists(word, "Marathi"):
                return

            for i in self.dictME:
                if i == word:
                    tword = self.dictME[i]

        elif lang2 == "Marathi":

            if not self.check_if_word_exists(word, "English"):
                return

            for i in self.dictEM:
                if i == word:
                    tword = self.dictEM[i]

        return tword


    def print_Alphabet(self):
        out = "Swar: \n\n"

        for i in self.swar:
            out += i + " "

        out+="\n\n Vyanjan: \n\n"

        for i in self.vyanjan:
            for j in i:
                out+=j + " "
            out+="\n"

        return out

    def infinite_word_game(self):

        print("Welcome to Infinite Word Game!\n\n")

        print("Instructions: \n")

        print("You have 5 lives. Type as many words  in Marathi as you can. " +
              "\nEach time you make a typo or a make up a word, you'll lose a life. "
              + "\nEach time you exceed 1 minute without answering, you lose a life\n" +
              "Try to get as many as you can!!!!!")

        score = 0

        lives = 5

        while True:
            word = input("Enter Marathi Word: ")

            if self.dictME[word] != None:
                score+=10

            else:
                lives-=1

            if lives == 0:
                print("GAME OVER!" + " Your Score was: " + score + "!!!")
                play_again = input("Do you want to play again? Y/N")

                if play_again == "Y":
                    score = 0
                    continue
                else:
                    break

    def translation_game(self):

        print("Welcome to Translation Game! \n")

        print("Instructions: \n" +
              "You have 5 lives. A random word from Marathi will be given to you\n, " +
              "and your goal is to write down the translation for it in English.\n" +
              "Every wrong guess will result in the loss of a life." +
              " Every right guess will result in an increase in you score\n" +
              "Try to get as many right as you can!!!")

        score = 0
        lives = 5

        while True:

            r = math.randint(0, len(self.marathi_list)-1)

            w = self.marathi_list[r]

            mword = input("Translate " + w + " to Marathi: ")

            if self.dictEM[w] == mword:
                score+=1

            else:
                lives-=1

            if lives == 0:
                print("GAME OVER!!!\n")
                cont = input("Continues? Y/N")

                if cont == "Y":
                    score = 0
                    continue

                else:
                    break


m = Marathi()









