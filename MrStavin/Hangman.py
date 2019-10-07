def hangman() :
    print("Welcome to hangman!")
    hangmanword = input("please input a word    : ")
    guessword = []



    for i in hangmanword:
        guessword.append("_")
    print(guessword)
    def lala():
        guess = input("Input a guess :")

        if guess in hangmanword :
            print("Correct")
            for a in range(0,len(hangmanword)):
                if hangmanword[a]==guess:
                    guessword[a] = guess
            print(guessword)
            if not '_' in guessword:
                print("You won!")
            else :
                lala()

        else :
            print("Incorrect,try again!")
            lala()
    lala()


hangman()