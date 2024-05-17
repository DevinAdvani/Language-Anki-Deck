import genanki
import random

my_deck = genanki.Deck(
  random.randrange(1 << 30, 1 << 31),
  'French Words')

my_model = genanki.Model(
  random.randrange(1 << 30, 1 << 31),
  'Audio of French Words',
  fields=[
    {'name': 'French Word'},
    {'name': 'Audio File'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{French Word}}',
      'afmt': '{{Audio File}}',
    },
  ])

my_note = genanki.Note(
  model=my_model,
  fields=['et',"[sound:et.mp3]"])


my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file('output.apkg')

my_package = genanki.Package(my_deck)
my_package.media_files = ['et.mp3']