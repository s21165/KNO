import logging

from nltk.corpus import wordnet as wn


class WordHelperWordnet:
    def __init__(self, word):
        self.word = word
        self.syns = wn.synsets(self.word)

    def get_the_definition(self):
        logging.info("Word definitions")

        words_definitions = dict()
        for syn in self.syns:
            syn_name = syn.name()
            word = syn_name.split(sep=".")[0]

            definition = wn.synset(syn_name).definition() # używamy wbudowanych funkcji z wordnet aby uzyskac definicje

            words_definitions[word] = definition

        logging.info(words_definitions)
        return words_definitions

    def get_a_sentence_example(self):
        logging.info("Sentence examples")

        sentence_examples = dict()
        for syn in self.syns:
            syn_name = syn.name()
            word = syn_name.split(sep=".")[0]

            sentences = wn.synset(syn_name).examples()
            if not sentences:
                sentences = ["There is no example sentence for the word"]

            sentence_examples[word] = sentences

        logging.info(sentence_examples)
        return sentence_examples

    def get_the_parts_of_speech(self): # kolejne funckje z wordnet pozwalające określić jaką częścią mowy jest dane słowo
        logging.info("Parts of speech")
        parts_of_speech_examples = {
            "n": "Noun",
            "v": "Verb",
            "a": "Adjective",
            "s": "Adjective Satellite",
            "r": "Adverb",
        }

        parts_of_speech = dict()
        for syn in self.syns:
            syn_name = syn.name()
            word = syn_name.split(sep=".")[0]

            part_of_speech = syn_name.split(sep=".")[1] # rozdzielamy słowa i przypisujemy jej przykładowe użycie do zmiennej
            part_of_speech = parts_of_speech_examples.get(part_of_speech)
            parts_of_speech[word] = part_of_speech

        logging.info(parts_of_speech)
        return parts_of_speech

    def get_the_synonyms(self): # funkcja od synonimów, przypisujemy różne rodzaje synonimów aby dać użytkownikowi
        # większy wybór oraz rozjaśnić przykłady użycia
        logging.info("Synonyms")
        main_syn = self.syns[0]
        synonyms = dict()

        hypernyms = main_syn.hypernyms()
        hypernyms = [x.name().split(sep=".")[0] for x in hypernyms]
        logging.info(hypernyms)
        synonyms["hypernyms"] = hypernyms

        hyponyms = main_syn.hyponyms()
        hyponyms = [x.name().split(sep=".")[0] for x in hyponyms]
        logging.info(hyponyms)
        synonyms["hyponyms"] = hyponyms

        member_holonyms = main_syn.member_holonyms()
        member_holonyms = [x.name().split(sep=".")[0] for x in member_holonyms]
        logging.info(member_holonyms)
        synonyms["member_holonyms"] = member_holonyms

        root_hypernyms = main_syn.root_hypernyms()
        root_hypernyms = [x.name().split(sep=".")[0] for x in root_hypernyms]
        logging.info(root_hypernyms)
        synonyms["root_hypernyms"] = root_hypernyms

        logging.info(synonyms)
        return synonyms
