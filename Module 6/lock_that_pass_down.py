#Nick Wendel
#IT - 75

#! python3
# lock_that_pass_down.py

##This is a basic password locker program.
##The program begins by asking the user to create a master passcode.
##Then the user will be able to login to the program using their passcode.
##If the master passcode does not match it will return the user to the login page.
##Once the user is logged in it will bring them to the main menu.
##From the main menu the user can choose to: create a new credential, view all saved accounts,
##copy the passcode to their clipboard, or log out.
##When a user chooses to add a credential they will be asked for the account name, and then
##it will give them the option to use an existing passcode or generate a random one that
##is 'strong' according to the XKCD comic strip.
##Once the user enters a passcode or generates one the program will encrypt the passcode and
##store it in the dictionary 'credentials'.
##When the user chooses to copy an accounts passcode the program will pull the passcode from
##the given account, decrypts it, and then using pyperclip copies it to their clipboard.
##
##In the future I would like to make this program able to:
##    - Save the information after the program is closed
##    - Improve the master passcode creation and login functions
##    - Improve the encryption practices
##
##Thank you for using my program and I hope you enjoy it!


import pyperclip
import random

nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']
words = nouns + verbs + adjs
length = 4
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'qwertyuiop0192asdfghjklMNBVCXZ8374LKJHGFDSAzxcvbnmPOIUYTREWQ65'
credentials = {}

def header():           # Function to print the 'Lock That Pass Down!' header
    print('='*80)
    print(' Lock That Pass Down! '.center(80, '='))
    print('='*80)
    print('\n'*2)

def add_cred():         # Function used to add a new credential
    ciphertext = ''
    print('\n'*35)
    header()
    print('Enter account name')
    account = str(input())
    if account in credentials:
        print(credentials[account] + ' has already been saved!')
    else:
        print('\n'*2)
        print('Passcode preference:')
        print('\n'*2)       # Sub-menu to choose if you want to use existing passcode or generate one
        print('[1] Existing passcode \n[2] Random generated passcode \n')
        print()
        pref = str(input('Which would you like to use? '))
        if pref == '1':
            print('\n'*2)
            print('Enter passcode for ' + account)
            pc = str(input())
            for character in pc:        # Encrypts the existing passcode
                if character in characters:
                    num = characters.find(character)
                    ciphertext += key[num]
            credentials[account] = ciphertext
            print('\n'*2)
            print('Saved credentials list has been updated!')
            print('\n'*4)
            header()
        elif pref == '2':
            pc = ''.join(random.sample(words,length))       # Generates a 'strong' passcode
            for character in pc:            # Encrypts the new generated passcode
                if character in characters:
                    num = characters.find(character)
                    ciphertext += key[num]
            credentials[account] = ciphertext
            print('\n'*2)
            print('Saved credentials list has been updated!')
            print('\n'*4)
            header()
        else:
            print('\n'*2)
            print('Invalid input! Please make your choice using the numbers 1 or 2.')
            print('\n'*5)
    
def view_all():         # Function to print all saved accounts
    print('\n'*35)
    header()
    print('Here are all of your saved accounts:')
    print('\n'*2)
    for k in credentials.keys():        # Searches the credentials dictionary and prints only the keys (accounts)
        print('- ' + str(k) + '\n' + '\n')
    print('\n'*2)
    header()

def copy_pc():          # Function to copy an accounts passcode to the clipboard
    plaintext = ''
    print('\n'*35)
    header()
    print('Which account would you like to get the passcode for?')
    account = str(input())
    if account in credentials:      # Decrypts the saved encrypted passcode
        for character in credentials[account]:
            if character in key:
                num = key.find(character)
                plaintext += characters[num]
        pyperclip.copy(plaintext)       # Copies the passcode to the clipboard
        print('\n'*2)
        print('The passcode for ' + account + ' has been copied to your clipboard!')
    else:
        print('Sorry, there are no credentials for ' + account)
    print('\n'*4)
    header()

def login():        # Function to login to the program
    print('Enter your Master Passcode to login:')
    passchk = input()
    if passchk == mpass:
        print('\n'*35)
        header()
        menu()
        
    else:           # Alerts user that passcode is incorrect and returns them to the login screen
        print('\n'*3)
        print('Sorry that passcode is incorrect!')
        print('Try Again')
        print('\n'*10)
        header()
        login()

def menu():         # Function to create a main menu for the program
    while True:
        print(' Main Menu '.center(80, '='))
        print('\n'*2)           # Gives users a menu of features they can use within the program
        print('[1] Add Credential \n[2] View All Credentials \n[3] Copy Passcode \n[4] Log Out \n')
        print()
        choice = str(input('What would you like to do? '))
        if choice == '4':       # Returns user to the login screen
            print('\n'*35)
            header()
            login()

        elif choice == '1':     # Brings the user to the add credential screen
            print('\n'*35)
            header()
            add_cred()

        elif choice == '2':     # Prints a list of all saved accounts
            print('\n'*35)
            header
            view_all()

        elif choice == '3':     # Asks the user which account they want the passcode for and then copies it to the clipboard
            print('\n'*35)
            header()
            copy_pc()

        else:                   # Alerts the user they entered an invalid respose and restarts the menu function
            print('\n'*5)
            print('Invalid input! Please make your choice using the numbers 1, 2, 3, or 4.')
            print('\n'*5)
            menu()



header()
print('Create Your Master Passcode: ')
mpass = str(input())
print('\n'*35)
header()
login()
    
