
def char_occurrence(text):
    lower_text = text.lower()
    chars = {}
    for ch in lower_text:
        if not(ch in chars):
            chars[ch] = 1
            continue

        chars[ch] += 1
    
    return chars


def get_words_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content

def main():
    book_path = r"books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words_count = get_words_count(book_text)
    print(char_occurrence(book_text))
main()