"""EX02 - Chardle - A cute step toward Wordle."""
 
__author__ = "730761368"


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print ("Error: Word must contain 5 characters.")
        exit()
    else:
        return (word)

#here i didnt understand why we had to return instead of print and then i later understood that in the instructions that the things in quotes are what needs to be returned no printed
def input_letter() -> str:
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print ("Error: Character must be a single character.")
        exit()
    else:
        return(letter)
#Below I had not used the f to concatinate the variable and string properly so i had go bakc and figure out that only one f is needed

#here i had made a mistake by def contains_char(word=input_word(), letter=input_letter()), and this had caused the program to ask for the input twice before outputting and it took me a while to figure why it wasnt working properly
def contains_char( word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")
    count = 0
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"{count} instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")

def main() -> None:
    contains_char(word=input_word(), letter=input_letter())

if __name__ == "__main__":
    main()
