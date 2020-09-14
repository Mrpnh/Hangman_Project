import random
import time



word_list=["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants",'buffalo','buzz','cycle','funny','gossip','icebox','injury','jackpot','keyhole','joke','lucky','khaki','oxygen','quiz','wax','wizard','cat','dog','elephant','tiger','lion','mango','apple','cherry']

def printHangman(count):
    if count==3:
        print('''
                 
                |      
                |       
                |    
                |   
                |
              __|__
              ''')
    elif count==2:
        print('''
                 _____
                |      
                |       
                |    
                |  
                |
              __|__
              ''')
    elif count==1:
        print('''
                 _____
                |     | 
                |       
                |    
                |   
                |
              __|__
              ''')
    elif count==0:
        print('''
                 _____
                |     | 
                |     O  
                |    /|\\
                |    / \\
                |
              __|__
              ''')


def word_print(word_list):
    word=random.choice(word_list)
    if len(word)<=5:
         print(word[0]+' _'*len(word[1:-1])+' '+word[-1])
    else:
        middle=len(word)//2
        print(word[0]+(' _'*len(word[1:middle])+' '+word[middle]+' _'*len(word[middle+1:])))
    return word

def checkGuess(guessWord,word):
    if guessWord.lower()==word:
        return True
    return False

def main_game(word_list):
    print("Welcome to Hangman Game...\nYou have 3 chances to guess the word.")
    count=3
    word=word_print(word_list)
    for i in range(3):
        guess_word=input("Input your guess...\n")
        if checkGuess(guess_word,word):
            print(f"Congratulations! You guessed it right and saved Hangman.\n{word} is the word.\n")
            break 
        else:
            count-=1
            print(f"Not right! {count} guess left.\n")
            printHangman(count)
            
    else:
        print(f"Sorry ! Hangman is dead. The word was {word}\n")

def playLoop():
    print("Wait...Your game is loading.\n")
    time.sleep(2)
    main_game(word_list)
    choice=input("Do you want to play Hangman again\nInput 'y' to play and 'Enter' to exit??\n").lower()
    if choice=='y':
        playLoop()

if __name__=='__main__':
    playLoop()
        
