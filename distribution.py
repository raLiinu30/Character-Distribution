"""
distribution.py
Author: Rain Liu
Credit: Mr. Dennison, Mr. Healy, Miriam, https://pymotw.com/2/collections/counter.html, 

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
import collections 
from collections import Counter

sentence = input('Please enter a string of text (the bigger the better): ')
print('The distribution of characters in "'+str(sentence)+'" is: ')


Y=sentence.lower()
c = collections.Counter(Y)

list(string.ascii_lowercase)

mylist=[]
for x in c:
    if x in string.ascii_lowercase:
        n=c[x]
        mylist.append(x*n)

E = mylist[:]


for j in range(0, len(E)):
    for i in range(0, len(E)-1):
        if len(E[i]) == len(E[i+1]):
            if E[i] > E[i+1]:
                E[i], E[i+1] = E[i+1], E[i]
        elif len(E[i]) < len(E[i+1]):
            E[i], E[i+1] = E[i+1], E[i]

R='\n'.join(E)
print(R)

'''for x in E:
    print(x)'''

 

    
            
