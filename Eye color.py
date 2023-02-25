'''You are given a 2D matrix, which represents the number of people in a room, grouped by their eye color and gender.
The first row represents the male gender, while the second row represents females.
The columns are the eye colors, in the following order: brown, blue, green, black
data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
PY
The data shows that, for example, there are 20 green eyed females in the room (2nd row, 3rd column).

Our program needs to take eye color as input and output the percentage of people with that eye color in the room.

Sample Input:
blue

Sample Output:
36
Explanation: There are 11+32=43 people with blue eyes, which is 36% of the total.'''

data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]

color = input("Enter the eye color from brown,blue,green,black")
sum = 0

for i in data:
    for j in i:
        sum+=j

if color=="brown":
    brown = int(((data[0][0]+data[1][0])/sum)*100)
    print("Percentage of brown eyed persons",brown)
elif color == "blue":
    blue = int(((data[0][1]+data[1][1])/sum)*100)
    print("Percentage of blue eyed persons",blue)
elif color == "green":
    green = int(((data[0][2] + data[1][2]) / sum) * 100)
    print("Percentage of green eyed persons", green)
elif color == "black":
    black = int(((data[0][3] + data[1][3]) / sum) * 100)
    print("Percentage of black eyed persons", black)
