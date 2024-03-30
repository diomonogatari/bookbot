def sort_on(dict):
    """
    A function that takes a dictionary and returns the value of the "num" key
    This is how the `.sort()` method knows how to sort the list of dictionaries
    """
    return dict["num"]

def sort_results(lst):
    lst.sort(reverse=True,key=sort_on)
    return lst

def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    text = text.lower()
    char_result = {}
    
    for c in text:
        if char_result.get(c) == None:
            char_result[c] = 1
            continue
        char_result[c] += 1
    
    lst = []
    for key in char_result:
        if key.isalpha():
            lst.append({"letter":key, "num":char_result[key]})
    return lst

def main():
    path_to_file = "./books/frankenstein.txt"
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    total_words = word_counter(file_contents)
    sorted_characters = sort_results(char_counter(file_contents))

    print(f"--- Begin report of {path_to_file} ---")
    print(total_words, "words found in the document\r\n")

    for dict in sorted_characters:
            print(f"The '{dict["letter"]}' character was found {dict["num"]} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
