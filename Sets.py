'''Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).
Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.'''

s1 = input()
s2 = input()

set1 = set(list(s1.split(' ')))
set2 = set(list(s2.split(' ')))
print(set1)
print(set2)
print(len(set1&set2))