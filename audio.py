from gtts import gTTS
import os

class audio:
    def __init__(self, filename):
        self.filename = filename

    def make_list(self):
        my_file = open(self.filename, "r", encoding = "utf-8")
        data = my_file.read()
        self.word_list = data.split("\n")

    def make_audio(self):
        for i in range(0,5):#len(self.word_list)):
            output = gTTS(text = self.word_list[i], lang = "fr")
            output.save(self.word_list[i] + ".mp3")

    def delete_audio(self):
        for i in range(0,5):
            os.remove(self.word_list[i] + ".mp3")