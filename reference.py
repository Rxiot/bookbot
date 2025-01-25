




def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file = f.read()
        file = file.lower()

    def letters():
        char_dict = {}
        for char in file:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        return char_dict

    # Format the output
    char_dict = letters()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file.split())} words found in the document")
    print("\n")
    
    # Sort characters by count (most frequent first)
    for char in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        # For spaces, we'll show "space" instead of empty quotes
        char_name = "space" if char[0] == " " else f"'{char[0]}'"
        print(f"The {char_name} character was found {char[1]} times")

    print("--- End report ---")

main()