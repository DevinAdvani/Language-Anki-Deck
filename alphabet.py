from gtts import gTTS
import os
import genanki

start = 0   
number_of_words = 26
end = start + number_of_words

my_file = open("alphabet.txt", "r", encoding = "utf-8")
data = my_file.read()
list = data.split("\n")

for i in range(start,end):
    output = gTTS(text = list[i], lang = "fr")
    output.save(list[i] + ".mp3")

my_deck = genanki.Deck(
  2059400110,
  "French Words::Alphabet")

my_model = genanki.Model(
  1091735104,
  "French Words::Alphabet",
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
my_package = genanki.Package(my_deck)
my_package.media_files = []

for i in range(start,end):
    my_note = genanki.Note(
    model=my_model,
    fields=[list[i], '[sound:' + list[i] + '.mp3]'])

    my_deck.add_note(my_note)
    my_package.media_files.append(list[i] + ".mp3")

filename = "Alphabet.apkg"

my_package.write_to_file(filename)

for i in range(start,end):
    os.remove(list[i] + ".mp3")