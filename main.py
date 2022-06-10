'''# 1 player game
import random as rn
import cv2
from tkinter import *
import tkinter.messagebox as tkm
from string import ascii_lowercase
root = Tk()
koot = Tk()
root.geometry('400x200')
def hangman() :
    words = ["college", "school", "basket", "python", "coding", "formula", "project", "physics", "navigate", "zombie",
             "luxury", "rickshaw", "zipper", "chemistry", "rhythm"]
    word = rn.choice(words)  # selecting a random word
    wrong_letters = ''  # to display the wrong letters
    w_count = 7  # wrongly guesses letters count
    guessed_word = ""  # comes from user inputs and merging alphabets at random
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    p = ''
    Label(koot, text="Player name: ",font=('Arial Black',10)).grid(row=0,column=0)
    Label(koot, text=e1.get(),font =('Georgia', 15)).grid(row=0, column=1)

    def variable(l):
        nonlocal guessed_word
        nonlocal w_count
        nonlocal wrong_letters
        letter = StringVar()
        letter.set(l)
        p = letter.get()

        final_word = ""  # arranging the letters in ordered way

        user = p  # input alphabet from user
        user.lower()


        if len(user) == 1:
            if user in alphabets:  # check if the entered letter is the alphabets
                if user not in guessed_word:
                    guessed_word += user
                else:
                    print(user, 'is already entered')
            else:
                print("Enter a valid character: ")
        else:
            print('')


        for letter in word:
            if letter in guessed_word:
                final_word += letter
            else:
                final_word += " _ "
        lb=Label(koot,text=final_word,font=("Arial,50"),height=5,width=30)
        lb.config(text=final_word)
        lb.grid(row=17,column=10,columnspan=15)


        if final_word == word:
            cv2.destroyAllWindows()
            tkm.showinfo("Game","Congrats!! You have guessed the word correctly!!")
            def again():
                play = tkm.askyesno('Game', 'Do you wanna play again!!! ')  # input from user to restart or not
                if play == 1:
                    hangman()
                if play == 0:
                    exit()
            again()



        if user not in word and len(user) == 1 and user in alphabets:  # this is for letter not in word
            if user not in wrong_letters:
                wrong_letters = wrong_letters + ' ' + user
                w_count -= 1
                c = 1
                if True:
                    #img = PhotoImage(file="D:\hangman project\hangman 2\%d.png"% (6 - w_count))
                    #Label(koot, image=img).grid(column=12,row=2)
                    img = cv2.imread("C:/Users/shara/OneDrive/Desktop/PES Projects/%d.jpeg" % (6 - w_count))
                    cv2.imshow("Img%d" % c, img)
                    cv2.waitKey(250)

                    print("Number of wrong attempts left: ", w_count)
                    print("The letters wrongly guessed are: ", wrong_letters)
                    c += 1
                    if w_count == 0:
                        cv2.destroyAllWindows()
                        tkm.showerror('Game', "The innocent man lost his life!!!")
                        exit()

    ro = 20
    col = 6
    count = 1
    for c in ascii_lowercase:
        Button(koot, text=c, command=lambda c=c: variable(c)).grid(columnspan=5, row=ro, column=col, padx=10, pady=10,
                                                                   ipadx=10)
        count += 1
        col += 5
        if count % 9 == 0:
            ro += 1
            col = 6
    variable('')


e1 = Entry(root)
e1.insert(0,"Enter your Name: ")
e1.grid(column=200,row=4)
b1=Button(root,text = "Start Game",font =("Comic Sans MS", 20, "bold"),command = hangman).grid(column = 200,row=10)
l1 = Label(root,text="Welcome to Hangman!!!!",font = ("Arial,50")).grid(column=200,row=0)
l2=Label(root,text = "Rules of the game:\n"
      "1. Don't let the innocent guy die.\n"
      "2. You will have 7 wrong guesses.\n"
      "3. Insert alphabet inputs only (no special character or numbers allowed).\n"
      "4. If you lose you discontinue.",fg = 'green').grid(column=200,row=1)

koot.mainloop()
root.mainloop()'''

# 2 player game
import random as rn
import cv2
from tkinter import *
import tkinter.messagebox as tkm
from string import ascii_lowercase
#from PIL import ImageTk,Image
root = Tk()
root.title("HaNgMaN")
koot = Tk()
koot.title("HaNgMaN")
root.geometry('400x220')
variable_count=0
def hangman() :
    global variable_count
    #words = ["college", "school", "basket", "python", "coding", "formula", "project", "physics", "navigate", "zombie",
    #        "luxury", "rickshaw", "zipper", "chemistry", "rhythm"]
    #word = rn.choice(words)  # selecting a random word
    #word = input("Enter word secretly: ")
    wrong_letters = ''  # to display the wrong letters
    w_count = 7  # wrongly guesses letters count
    guessed_word = ""  # comes from user inputs and merging alphabets at random
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    p = ''
    word=''
    turn=''
    turn_count=1
    score_1=0
    score_2=0
    def variable(l):
        global variable_count
        nonlocal score_1
        nonlocal score_2
        nonlocal turn
        nonlocal turn_count
        nonlocal word
        nonlocal guessed_word
        nonlocal w_count
        nonlocal wrong_letters
        if type(l) == int:
            if turn_count % 2 != 0:
                turn = e1.get() + "'s turn to play"
                tkm.showinfo('Chance', message=turn)
                word = input("Enter word secretly: ")
                for i in range(50):
                    print(' ')
            else:
                if turn_count==10:
                    exit()
                turn = e2.get() + "'s turn to play"
                tkm.showinfo('Chance', message=turn)
                word = input("Enter word secretly: ")
                for i in range(50):
                    print(' ')

        if word=="":
            def exit1():
                root.quit()
                koot.quit()

            Button(koot, text='Exit', command=exit1).grid(columnspan=20, row=25, column=10, padx=10, pady=10,ipadx=10)

        elif word != '':
            letter = StringVar()
            letter.set(l)
            p = letter.get()

            final_word = ""  # arranging the letters in ordered way

            user = p  # input alphabet from user
            user.lower()

            def exit1():
                root.quit()
                koot.quit()

            Button(koot, text='Exit', command=exit1).grid(columnspan=20, row=25, column=10, padx=10, pady=10,ipadx=10)

            if len(user) == 1 and user in alphabets:  # check if the entered letter is the alphabets
                if user not in guessed_word:
                    guessed_word += user
                else:
                    print(user, 'is already entered')

            for letter in word:
                if letter in guessed_word:
                    final_word += letter
                else:
                    final_word += " _ "
            lb = Label(koot, text=final_word, font=("Arial,50"), height=5, width=30)
            lb.config(text=final_word)
            lb.grid(row=17, column=10, columnspan=15)

            if final_word == word:
                cv2.destroyAllWindows()
                word=''
                w_count = 7
                wrong_letters = ''
                tkm.showinfo("Game", "Congrats!! You have guessed the word correctly!!")
                guessed_word = ""
                variable_count += 1
                if turn_count % 2 != 0:
                    score_1 += 1
                    l1.config(text=e1.get() + " score:" + " %d" % score_1)
                elif turn_count % 2 == 0:
                    score_2 += 1
                    l2.config(text=e2.get() + " score:" + " %d" % score_2)
                turn_count += 1

            if user not in word and len(user) == 1 and user in alphabets and word!='':  # this is for letter not in word
                if user not in wrong_letters:
                    wrong_letters = wrong_letters + ' ' + user
                    w_count -= 1
                    c = 1
                    if True:
                        # img = PhotoImage(file="D:\hangman project\hangman 2\%d.png" % (6 - w_count))
                        # Label(koot, image=img).grid(column=12,row=2)
                        img = cv2.imread("C:/Users/shara/OneDrive/Desktop/PES Projects/%d.jpeg" % (6 - w_count))
                        cv2.imshow("Img%d" % c, img)
                        cv2.waitKey(250)
                        print("Number of wrong attempts left: ", w_count)
                        print("The letters wrongly guessed are: ", wrong_letters)
                        c += 1
                        if w_count == 0:
                            w_count = 7
                            guessed_word = ""
                            wrong_letters = ''
                            cv2.destroyAllWindows()
                            turn_count += 1
                            tkm.showerror('Game', "The innocent man lost his life!!!")
            if w_count == 0:
                word=""
                final_word=""

    l1 = Label(koot, text=e1.get() + " score:" + " %d" % score_1, font=('Arial Black', 10))
    l1.grid(row=0, column=0)
    l2 = Label(koot, text=e2.get() + " score:" + " %d" % score_2, font=('Arial Black', 10))
    l2.grid(row=1, column=0)

    ro = 20
    col = 6
    count = 1
    for c in ascii_lowercase:
        Button(koot, text=c, command=lambda c=c: variable(c)).grid(columnspan=5, row=ro, column=col, padx=10, pady=10,
                                                                   ipadx=10)
        count += 1
        col += 5
        if count % 9 == 0:
            ro += 1
            col = 6

    Button(koot, text='Word', command=lambda: variable(variable_count)).grid(columnspan=20, row=24, column=10, padx=10, pady=10,ipadx=10)


e1 = Entry(root)
e1.insert(0,"Enter Player 1 Name: ")
e1.grid(column=200,row=4)
e2 = Entry(root)
e2.insert(0,"Enter Player 2 Name: ")
e2.grid(column=200,row=5)
b1=Button(root,text = "Enter Game",font =("Comic Sans MS", 20, "bold"),command = hangman).grid(column = 200,row=10)
l1 = Label(root,text="Welcome to Hangman!!!!",font = ("Arial,50")).grid(column=200,row=0)
l2=Label(root,text = "Rules of the game:\n"
      "1. Don't let the innocent guy die.\n"
      "2. You will have 7 wrong guesses.\n"
      "3. Insert alphabet inputs only (no special character or numbers allowed).\n"
      "4. If you lose you discontinue.",fg = 'green').grid(column=200,row=1)

koot.mainloop()
root.mainloop()
