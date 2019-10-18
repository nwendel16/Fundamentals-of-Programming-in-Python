# Challenge #1: String Slicing

# Assign sub_lyric by slicing rhyme_lyric from start_index to end_index which are given as inputs.
    # Sample output with inputs: 4 7
    # cow

##start_index = int(input())
##end_index = int(input())
##rhyme_lyric = 'The cow jumped over the moon.'
##sub_lyric = rhyme_lyric[20:28]
##print(sub_lyric)

# Challenge #2: Format Temperature Output

# Print air_temperature with 1 decimal point followed by C.
    # Sample output with input: 36.4158102
    # 36.4C

#air_temperature = float(input())

#print('The temperature is: %.1fC' % air_temperature)

# Challege #3: Find Abbreviations

# Complete the if-else statement to print 'LOL means laughing out loud' if user_tweet contains 'LOL'.
    # Sample output with input: 'I was LOL during the whole movie!'
    # LOL means laughing out loud.

##user_tweet = input()
##
##if user_tweet.find('LOL') != -1:
##    print('LOL means laughing out loud.')
##else:
##    print('No abbreviation.')

## Challenge #4: Replace Abbreviations
##
## Assign decoded_tweet with user_tweet, replacing any occurrence of 'TTYL' with 'talk to you later'.
##    # Sample output with input: 'Gotta go. I will TTYL.'
##
##user_tweet = input()
##
##decoded_tweet = user_tweet.replace('TTYL', 'Talk to you later')
##print(decoded_tweet)

# Challenge 5: Extract Area Code

# Assign number_segments with phone_number split by the hyphens.
    # Sample output with input: '977-555-3221'
    # Area code: 977

##phone_number = input('Enter your phone number:    ex. 555-555-5555 \n')
##number_segments = phone_number.split('-')
##area_code = number_segments[0]
##print('Area code:', area_code)

# Challenge 6: Check for integer in string

# Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input,
# and outputs yes if every character is a digit 0-9.

# Ex: If the input is:
    # 1995
    # the output is:
        # yes
# Ex: If the input is:
    # 42,000
    # # or any string with a non-integer character, the output is:
        # no

##user_string = input()
##
##if user_string.isdigit():
##    print('yes')
##else:
##    print('no')

# Challenge 7: Name Format

# Many documents use a specific format for a person's name. Write a program whose input is: firstName middleName lastName,
# and whose output is: lastName, firstName middleInitial.

# Ex: If the input is:
    # Pat Silly Doe
    # the output is:
        # Doe, Pat S.

# If the input has the form firstName lastName, the output is lastName, firstName.

# Ex: If the input is:
    # Julia Clark
    # the output is:
        # Clark, Julia

##names = input('Enter your First, Middle, and Last names: \n')
##tokens = names.split(' ')
##print()
##
##if len(tokens) == 3:
##    print('%s, %s %s.' % (tokens[2], tokens[0], tokens[1][0]))
##          
##if len(tokens) == 2:
##    print('%s, %s' % (tokens[1], tokens[0]))


# Challenge 8: Palindrome

# A palindrome is a word or a phrase that is the same when read both forward and backward.
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

# Ex: If the input is:
    # bob
    # the output is:
        # bob is a palindrome
# Ex: If the input is:
    # bobby
    # the output is:
        # bobby is not a palindrome
# Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

##word = input('Enter a word to see if it is a palindrome: \n')
##word = word.replace(' ', '')
##
##if word == word[::-1]:
##    print(word[::-1])
##    print('Yes,', word, 'is a palindrome!')
##else:
##    print(word[::-1])
##    print('No,', word, 'is not a palindrome')
