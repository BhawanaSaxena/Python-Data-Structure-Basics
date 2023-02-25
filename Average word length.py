'''Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5'''

#taking input from user
sentence = input("Enter a sentence")

#split the sentence to form a list
split_sentence = sentence.split(' ')

#cal. length of the list split_sentence
length_sentence = len(split_sentence)

#variable used as a counter
count_letter = 0

for i in sentence:
    if i==" ":
        continue
    count_letter += 1 #letter count increment by 1 , skipped when letter is " "(space)

#calculating average length by the formula
avg_word = count_letter/length_sentence

#printing the average word length
print("average word length",avg_word)
