from language_class import language

folder_name = input("CHECK WHICH DECK: ")
paragraph = input("CHECK WHICH PARAGRAPH: ")

edited_folder_name = ""
for i in range(0,len(folder_name)):    
    if (folder_name[i] == " "):
        edited_folder_name += '_'
    else:
        edited_folder_name += folder_name[i]

language_deck = language(int(paragraph), edited_folder_name)
language_deck.check_deck_translations()