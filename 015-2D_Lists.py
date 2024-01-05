# food="ahvbi"
# print(f"{food:0^100}")

fruits=["apple", "mango", "bananna", "grapes"]
vegetables=["potato", "gourd", "capsicum"]

grocery=[fruits, ["sugar", "salt", "chilli"], vegetables]

for item in grocery:
    for food in item:
        print(food, end=" ")
    print()                                   # to initiate a new line






############## Practice program to print the keypads of button phones

buttons=[["1", "2", "3"],["4","5","6"],["7","8","9"],["*","0","#"]]

for row in buttons:
    for button in row:
        print(button, end=" ")
    print()

######  SHOULD have used TUPLES as we are not changing the data and it is faster and could have directly used the INTEGER  for numerals