from language_class import language

folder = input("CHECK WHICH DECK: ")
paragraph = input("CHECK WHICH PARAGRAPH: ")

language_deck = language(int(paragraph))
language_deck.check_deck_translations()