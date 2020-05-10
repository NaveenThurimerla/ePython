

def getNumberOfAttempts():
    while True:
        num_attempts = int(input("Enter how many attempts you want (1-25)?: " ))
        if (1 <= num_attempts <= 25):
            return num_attempts;
        else:
            print("Please enter valid number")
            getNumberOfAttempts()
            
            


def getNumberOfWords():
    while True:
        num_words = int (input("Enter maximum word length you want to play(1-10)?: "))
        if (1 <= num_words <= 10):
            return num_words;
        else:
            print("Please enter valid number")
            getNumberOfWords()
    
getNumberOfAttempts()
getNumberOfWords()    