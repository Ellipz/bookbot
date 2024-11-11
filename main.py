def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    per_character_count = get_per_character_count(text)
    #print(text)
    #print(word_count)
    print(per_character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    with open(path) as f:
        return len(f.read().split())

def get_per_character_count(text):
    character_set={}
    for c in text.lower():
        if c in character_set:
            character_set[c] += 1
        else:
            character_set[c] = 1
    return character_set

main()