
def main():
    with open("books/frankenstein.txt") as f:

        file_contents = f.read()
        words = file_contents.split()
        count = 0
        letter_count = {}
        for word in words:
            count += 1
            for letter in word.lower():
                if letter not in letter_count.keys():
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1
        
        letters = []
        
        letters = letter_count.items()

        letters = list(letters)

        letters.sort()
        print(f"{count} words found in the document")
        for item in letters:
            if item[0].isalpha():
                
                print(f"The '{item[0]}' character was found {item[1]} times")

        


main()