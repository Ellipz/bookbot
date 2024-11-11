def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(book_path)
    per_character_count = get_per_character_count(text)
    lod_per_character_count=dict_to_listofdict(per_character_count)
    
    #print(text)
    #print(word_count)
    #print(per_character_count)
    #print(lod_per_character_count)

    lod_per_character_count.sort(reverse=True, key=sort_on)

    #print(lod_per_character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for d in lod_per_character_count:
        print(f"The '{d["char"]}' character was found {d["count"]} times")
    print("--- End report ---")



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

def dict_to_listofdict(dict):
    listofdict=[]
    for c in dict:
        if c.isalpha():
            listofdict.append({"char":c ,"count":dict[c]})
    return listofdict

def sort_on(dict):
    return dict["count"]

#def sort_of_dicts(dict)
    
    #dict.sort(reverse=True, key=sort_on)

main()