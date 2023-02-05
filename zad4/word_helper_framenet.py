import logging

from nltk.corpus import framenet as fn


class WordHelperFramenet:
    def __init__(self, word):
        self.word = word
        self.f = fn.frames(self.word)

    def get_the_frame_of_word(self, num):
        try:
            frame = self.f[num]
        except IndexError:
            frame = None
            "There is no frame for the word"

        logging.info(frame)
        if not frame:
            msg = "There is no frame for the word"
            return msg
        else:
            return frame
