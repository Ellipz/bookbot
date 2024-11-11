def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    #print(text)
    print(word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    with open(path) as f:
        return len(f.read().split())


main()