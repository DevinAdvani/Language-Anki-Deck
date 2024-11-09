from gtts import gTTS
import genanki

# The text that you want to convert to audio
mytext = 'Bonjour'

# Language in which you want to convert
language = 'fr'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("Bonjour.mp3")

# Define a model
my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',  # Display the front and audio
            'afmt': '{{Audio}}',
        },
    ],
)

# Create a deck
my_deck = genanki.Deck(
    2059400110,
    'Sample Deck'
)

# Create a note with audio
my_note = genanki.Note(
    model=my_model,
    fields=['What is this?', f'[sound:{'Bonjour.mp3'}]'],  # Add audio here
)

# Add the note to the deck
my_deck.add_note(my_note)

# Generate the output file
genanki.Package(my_deck).write_to_file('output.apkg')
