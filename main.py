
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
    
def generate_report(path):
    def sort_on(dict):
        return dict["count"]

    book_text = get_book_text(path)
    words_count = get_words_count(book_text)
    chars = char_occurrence(book_text)
    list_of_chars = []
    for ch in chars:
        if ch.isalpha():
            list_of_chars.append({"char": ch, "count": chars[ch]})
    list_of_chars.sort(reverse=True, key=sort_on)

    report = f"--- report of {path}"
    report += f"\n{words_count} word found"
    for ch in list_of_chars:
        report += f"\nThe '{ch['char']}' was found {ch['count']} times"

    report += "\n--- End of report ---"

    return report

def main():
    book_path = r"books/frankenstein.txt"
    report = generate_report(book_path)
    print(report)
main()