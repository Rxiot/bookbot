def main():
    def count(file_contents):
        doc = file_contents.split()
        return len(doc)  # Return the word count
    
    # Step 1: Read from the file
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    
    # Step 2: Count the words using the nested count() function
    word_count = count(file_contents)
    
    # Step 3: Print the result
    print(word_count)
   
main()  # Entry point: Only one function exists at the top level