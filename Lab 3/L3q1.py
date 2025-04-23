#This program count how many vowels are there in a string. Accept the string from the user
a=str(input('enter a string: '))
count=0
for i in a:
    if i in 'aeiou':
        count+=1
print('number of vowels in string: ',count)
