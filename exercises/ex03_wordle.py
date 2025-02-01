__author__ = "730761368"




def input_guess(word_length: int) -> str:
    word = input(f"Enter a {word_length} character word:")

    while len(word) != word_length:
        word = input(f"That wasn't {word_length} chars! Try again:")

    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """This takes in a word and then checks the word to see if the second parameter is in the given word"""
    assert len(char_guess) == 1
    index = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False

def emojified(word: str, secret_word: str)-> str:
    """to compare two strings of equal length and return a string of emojies"""
    assert len(word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index = 0
    emoji = ""

    while index < len(word):
        if secret_word[index] == word[index]:
            emoji += GREEN_BOX
        elif contains_char(secret_word, word[index]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
        
    return(emoji)
    


def main(secret:str)-> None:
    """The entrypoint of the program and main game loop."""
    turn:int = 1
    while turn <= 6:
        guess = input_guess(len(secret))
        print(f"=== Turn {turn}/6 ===")
        print(emojified(word = guess, secret_word = secret))

        """Here it took some time to figure out why the program wasnt working and i finally figured out that the guess needs to be inside the while loop"""
        

        if secret == guess:
            print(f"You won in {turn}/6 turns!")
            turn = 7
            """This stop the loop without using break"""
        elif turn != 6:
            turn += 1
            """Here also it took me a while to figure out that i need an elif statement to make all this run smoothly"""
        else:
            print("X/6 - Sorry, try again tomorrow!")
            turn += 1
            


if __name__ == "__main__":
        main(secret="codes")








