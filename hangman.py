print('Welcome to hangman')
print('User 1: Please enter a word/phrase')
i=0
n=0
counter=1
test='a'
# j=0
x=input()
length =len(x)
dash = '_'
for i in range(0,(length-1)):
    dash += '_'
new =list(dash)
print(new)
for i in range(0,length):#printing the empty spaces to let user 2 know length of the word
    print('_',end=' ')

# go until the hangman limit but break out if word is guessed
#change to length of word+tally of hangman
for i in range(0,10):#########

    print('\nUser 2, Please enter a letter')
    guess=input()#user 2 guess
    n=0

    # for i in range(0,length):#loop to loop through multiple guesses of user 2
    for j in range(0,length):#loop to loop through letters in word to find any matches

            if guess != x[j]:
                test=' '.join(new)
                n=n+1
                continue 
            if guess == x[j]:
                counter+=1
                new[n]= guess
                test=' '.join(new)
                
                
            print(n)
            n=n+1
              
    print(test)

    if counter>length:
        break

print('congraulations you have won')        