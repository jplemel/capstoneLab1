print('This program turns a sentance into camel case')

userInputSentance = input("Enter a sentance to convert:")
#x = 0

#while x < len(userInputSentance):
    #if userInputSentance[x] == ' ':

#takes the string and capitalizes each word using title function
userInputSentance = userInputSentance.title()

#joining the words together and getting rid of spaces
# can also use replace() function
#list comprehention

# can also use replace() function
#no_space = test.replace(' ', '')
userInputSentance = ''.join(x for x in userInputSentance if not x.isspace())

#http://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string-in-python
userInputSentance = userInputSentance[0].lower() + userInputSentance[1:]

print(userInputSentance)
