from gtts import gTTS
import os
import genanki


my_file = open("frequency.txt", "r", encoding = "utf-8")
data = my_file.read()
list = data.split("\n")

for i in range(0,5):#len(self.word_list)):
    output = gTTS(text = list[i], lang = "fr")
    output.save(list[i] + ".mp3")




my_deck = genanki.Deck(
  2059400110,
  'Country Capitals')

my_model = genanki.Model(
  1091735104,
  'Simple Model with Media',
  fields=[
    {'name': 'Question'},
    {'name': 'MyMedia'},                                  # ADD THIS
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',              # AND THIS
      'afmt': '{{MyMedia}}',
    },
  ])

my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', '[sound:et.mp3]'])



my_deck.add_note(my_note)
my_package = genanki.Package(my_deck)
my_package.media_files = ['et.mp3']


my_package.write_to_file('output.apkg')










#for i in range(0,5):
#    os.remove(list[i] + ".mp3")