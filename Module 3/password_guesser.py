#Nick Wendel
#IT - 75
#9/20/19
#Extra Credit - Password Challange


ltrs = 'abcdefghijklmnopqrstuvwxyz'
pw = 'nick'
x = 0
guess = ''


for i in range(26):
    for j in range(26):
        for k in range(26):
            for l in range(26):
                guess = ltrs[i] + ltrs[j] + ltrs[k] + ltrs[l]
                x = x + 1
                if guess == pw:
                    print('Password found after ', x, ' guesses')
                    break

