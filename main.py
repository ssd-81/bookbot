def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # generate_report(file_contents)
    print(convert_to_list(count_character(file_contents)))


def count_words(book):
    return len(book.split())

def convert_to_list(dict):
    temp = []
    for i in dict:
        temp.append({i:dict[i]})
    return temp

def count_character(text):
    count = {}
    for i in text.lower():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    char_report = count_character(text)
    for i in char_report:
        print(f"The '{i}' character was found {char_report[i]} times")
    print("--- End report ---")


main()
