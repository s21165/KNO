import logging
import os

from word_helper_framenet import WordHelperFramenet  # framenet używamy do frame
from word_helper_wordnet import WordHelperWordnet  # wordnet używamy do definicji, synonimów itp.


class MainApp:
    @staticmethod
    def display_title_bar():

        print("Let me help you with any english word :) ")

    @staticmethod
    def get_user_choice():  # Lista dostępnych opcji
        print("\n[1] Get the definition of the word")
        print("[2] Get sample sentences")
        print("[3] Get the parts of speech")
        print("[4] Get the synonyms")
        print("[5] Check frames")
        print("[6] Enter new word")
        print("[q] Exit the program")

        return input("How can I help u today?: ")

    @staticmethod
    def get_user_choice_frame():
        print("\n[1] Next frame")
        print("[2] Previous frame")
        print("[3] Quit frames")

        return input("What would you like to do ?: ")

    def menu(self):
        choice = ""
        self.display_title_bar()  # wyświetlany pierwotny ekran
        user_word = input("Your word: ").strip()  # usuwamy niepotrzebne znaki gdy user wybierze słowo
        while not user_word:  # jeżeli nie mamy słowa od użytkownika, poproś o słowo
            user_word = input("Please enter a word: ").strip()

        while choice != "q":  # jeżeli użytkownik nie zdecydował się wyłączyć aplikacji będziemy używać innych funkcji i wykorzystywać wpsiane
            word_helper_wordnet = WordHelperWordnet(word=user_word)
            word_helper_framenet = WordHelperFramenet(word=user_word)
            choice = self.get_user_choice()

            if choice == "1":
                words_definitions = word_helper_wordnet.get_the_definition()
                for k, v in words_definitions.items():  # dla każdego słowa k daj definicje v, pętle są podobnie wykonane dla innych przykładów
                    print(f"\n===Word===\n{k}\n=====Definition=====\n{v}\n")

            elif choice == "2":
                sentence_examples = word_helper_wordnet.get_a_sentence_example()
                for k, v in sentence_examples.items():
                    print(f"\n===Word===\n{k}\n=====Sentence Examples=====")
                    for sen in range(len(v)):
                        print(f"{sen + 1}. {v[sen]}")

            elif choice == "3":
                parts_of_speech = word_helper_wordnet.get_the_parts_of_speech()
                for k, v in parts_of_speech.items():
                    print(f"\n===Word===\n{k}\n=====Part of speech=====\n{v}\n")

            elif choice == "4":
                try:
                    synonyms = word_helper_wordnet.get_the_synonyms()
                    for k, v in synonyms.items():
                        print(f"\n===Synonyms - {k}===\n")
                        for syn in range(len(v)):
                            print(f"{syn + 1}. {v[syn]}")
                except IndexError:
                    print("There are no synonyms for this word")

            elif choice == "5":
                frame_choice = ""
                num = 0
                frame = word_helper_framenet.get_the_frame_of_word(num)
                print(frame)
                if frame == "There is no frame for the word":
                    frame_choice = "3"

                while frame_choice != "3":
                    frame_choice = self.get_user_choice_frame()

                    if frame_choice == "1":
                        try:
                            num += 1
                            frame = word_helper_framenet.get_the_frame_of_word(num)
                            print(frame)
                        except IndexError:
                            num = 0
                            print("No more frames for a given word")

                    elif frame_choice == "2":
                        if num <= 0:
                            num = 0
                            print("There is no previous example before the first")
                        else:
                            num -= 1
                        frame = word_helper_framenet.get_the_frame_of_word(num)
                        print(frame)

                    elif frame_choice == "3":
                        pass
                    else:
                        print("\nI did not understand that choice.\n")

            elif choice == "6":
                user_word = "".strip()
                while not user_word:
                    user_word = input("Please enter a word: ").strip()

            elif choice == "q":
                print("I hope u are satisfied with our cooperation :)")
            else:
                print("\nI did not understand that choice.\n")
