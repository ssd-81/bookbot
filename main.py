def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    generate_report(file_contents)    


def count_words(book):
    return len(book.split())


def count_character(text):
    count = {}
    for i in text.lower():
        if i in count:
            count[i] += 1
        else:
            if(i.isalpha()):
                count[i] = 1
    mod_count = []
    for i in count:
        # i is the char
        mod_count.append({'char':i,'count':count[i]})    
    return mod_count


def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    char_report = count_character(text)
    char_report.sort(reverse=True, key=sort_on)
    for i in char_report:
        print(f"The '{i['char']}' character was found {i['count']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict['count']

main()
