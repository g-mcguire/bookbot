path = "books/frankenstein.txt"

def main():
    with open(path) as f:
        contents = f.read()
        # print(content)
        # print(count_words(contents))
        # print(count_chars(contents))
        print(compose_report(contents))

def count_words(string):
    return len(string.split())

def count_chars(string):
    full_counts = {}
    lowercase_string = string.lower()

    for char in lowercase_string:
        if char in full_counts:
            full_counts[char] += 1
        else:
            full_counts[char] = 1
    
    return full_counts

def sort_on(dict):
    return dict["num"]

def compose_report(string):
    print(f"\n--- Begin report on {path} ---\n")
    counts = count_chars(string)

    char_counts = [{"letter": x, "num": y} for x,y in counts.items() if x.isalpha()]
    char_counts.sort(reverse=True, key=sort_on)

    for char_count in char_counts:
        letter = char_count["letter"]
        num = char_count["num"]
        print(f"The letter {letter} was found {num} times in the text.")
    print("\n--- End of report ---\n")
    
    pass


main()