def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count(text)
    report_content = ""
    for item in score_keeping(text):
        report_content = f"The {item['char']} character was found {item['num']} times \n" + report_content 
    print(f"--- Begin report of {book_path} --- \n{num_words} words found in the document \n{report_content} \n --- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def score_keeping(text):
    container, letters = [], {}
    characters = "abcdefghijklmnopqrstuvwxyz"
    for char in characters: 
        letters[char] = 0
    for char in list(str(text.lower())):
        if char in characters: 
            letters[char] += 1
    for key in letters:
        container.append(dict([('char', key), ('num', letters[key])]))
    container = sorted(container, key=sort_on)
    return container

main()

    
