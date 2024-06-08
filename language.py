from gtts import gTTS
import os
import genanki

class language:
  def __init__(self, name, language):
    self.language = language
    self.name = name
    self.filename = self.name + ".txt"
    self.english = []
    self.translation = []
    self.sentence_list = []
    self.my_genanki_deck = 0
    self.my_genanki_model = 0

  def read_files_and_put_into_list(self):
    my_file = open(self.filename, "r", encoding = "utf-8")
    self.sentence_list = my_file.read().split("\n")

  def create_english_and_translation_list(self):
    try:
      for i in range(0,len(self.sentence_list),3):
          self.english.append(self.sentence_list[i])
          self.translation.append(self.sentence_list[i+1])
    except:
      for i in range(0,len(self.sentence_list)-3,3):
          self.english.append(self.sentence_list[i])
          self.translation.append(self.sentence_list[i+1])

  def make_my_genanki_deck(self):
    self.my_genanki_deck = genanki.Deck(
      2059400110,
      "Languages::" + self.name + " Sentences")
    
  def make_my_genanki_model(self):
    self.my_genanki_model = genanki.Model(
    1607392319,
    "Basic",
    fields=[
      {'name': 'English'},
      {'name': 'Translation'},
    ],
    templates=[
      {
        'name': 'Card 1',
        'qfmt': '{{English}}',
        'afmt': '{{Translation}}',
      },
    ])

  def add_cards_to_deck(self):
    for i in range(0,len(self.english)):
        my_note = genanki.Note(
        model=self.my_genanki_model,    
        fields=[self.english[i], self.translation[i]])
        self.my_genanki_deck.add_note(my_note)   
  
  def print_cards(self):
    for i in range(0,len(self.english)):
        print("ENGLISH   : " + self.english[i])
        print("TRANSLATED:  " + self.translation[i])
        print("")

  def check_deck_translations(self):
    self.read_files_and_put_into_list()
    self.create_english_and_translation_list()
    self.print_cards()

  def make_sentences_deck(self):
    self.read_files_and_put_into_list()
    self.create_english_and_translation_list()
    self.make_my_genanki_deck()
    self.make_my_genanki_model()
    self.add_cards_to_deck()
    genanki.Package(self.my_genanki_deck).write_to_file(self.name + ' Sentences.apkg')










"""
  def make_audio_deck(self):
    translated_words = []

    stuff_to_remove = ['.',',','(',')',':','"','','«','»','?']

    for i in range(0,len(self.translation)):
        temp = self.translation[i].split(" ")
        for j in range(0,len(temp)):
            for k in range(0,len(stuff_to_remove)):
                temp[j] = temp[j].replace(stuff_to_remove[k], "")
            translated_words.append(temp[j].lower())

    tempOne = set(translated_words)
    tempTwo = []
    for x in tempOne:
        if (x != '' and x != '1' and x != '2'):
          tempTwo.append(x)
    tempTwo.sort()

    translated_words = tempTwo

    print(translated_words)

    for i in range(0,len(translated_words)):
        output = gTTS(text = translated_words[i], lang = language)
        output.save(translated_words[i] + ".mp3")


    my_deck = genanki.Deck(
      2059400110,
      "Languages::" + self.name + " Audio")

    my_model = genanki.Model(
      1091735104,
      "Basic",
      fields=[
        {'name': 'Word'},
        {'name': 'Audio'},
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': '{{Word}}',
          'afmt': '{{Audio}}',
        },
      ])

    my_audio = genanki.Package(my_deck)
    my_audio.media_files = []

    for i in range(0, len(translated_words)):
        my_note = genanki.Note(
        model=my_model,
        fields=[translated_words[i], '[sound:' + translated_words[i] + '.mp3]'])

        my_deck.add_note(my_note)
        my_audio.media_files.append(translated_words[i] + ".mp3")


    my_audio.write_to_file(self.name + " Audio.apkg")


    for i in range(0, len(translated_words)):
        try:
            os.remove(translated_words[i] + ".mp3")
        except:
            pass
"""