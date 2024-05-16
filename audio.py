class audio:
    def __init__(self, filename):
        self.filename = filename

    def make_list(self):
        my_file = open(self.filename, "r", encoding = "utf-8")
        data = my_file.read()
        self.word_list = data.split("\n")
        print(self.word_list[5])
        