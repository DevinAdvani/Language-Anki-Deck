from gtts import gTTS
import os
import genanki

name = "Anne Frank's Diary"
language = "du"
make_audio = False

filename = name + ".txt"

my_file = open(filename, "r", encoding = "utf-8")
data = my_file.read()
list = data.split("\n")

english = []
translation = []
try:
  for i in range(0,len(list),3):
      english.append(list[i])
      translation.append(list[i+1])
except:
  for i in range(0,len(list)-3,3):
      english.append(list[i])
      translation.append(list[i+1])

my_deck = genanki.Deck(
  2059400110,
  "Languages::" + name + " Sentences")

my_model = genanki.Model(
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

for i in range(0,len(english)):
    my_note = genanki.Note(
    model=my_model,    
    fields=[english[i], translation[i]])
    print("ENGLISH   : " + english[i])
    print("TRANSLATED:  " + translation[i])
    print("")

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file(name + ' Sentences.apkg')



##AUDIO


if (make_audio):
  translated_words = []

  stuff_to_remove = ['.',',','(',')',':','"','','«','»','?']

  for i in range(0,len(translation)):
      temp = translation[i].split(" ")
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
    "Languages::" + name + " Audio")

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


  my_audio.write_to_file(name + " Audio.apkg")


  for i in range(0, len(translated_words)):
      try:
          os.remove(translated_words[i] + ".mp3")
      except:
          pass
