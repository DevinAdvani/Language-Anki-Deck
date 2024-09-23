from language_class import language

folder = input("MAKE WHICH DECK: ")
paragraph = input("MAKE WHICH PARAGRAPH: ")

language_deck = language(int(paragraph))
language_deck.make_sentences_deck()