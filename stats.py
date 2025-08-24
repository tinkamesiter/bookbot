def word_number(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(char_count):
    char_sorted_list = []
    for char in char_count:
        char_sorted_list.append((char, char_count[char]))
    char_sorted_list.sort()
    return char_sorted_list