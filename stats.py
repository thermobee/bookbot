def count_words(text):
    count = len(text.split())

    return count

def count_characters(text):
    character_dict = {}

    for i in text:
        lowerchar = i.lower()
        if lowerchar in character_dict:
            character_dict[lowerchar] += 1
        else:
            character_dict[lowerchar] = 1

    return character_dict