# declares an integer variable and due to formatting it puts it inside another string x
types_of_people = 10
x = f"There are {types_of_people} types of people."  # the string is put in another string
# because all types are cast to string and then are put inside a string - 1

# declares two string variables and due to formatting puts them inside another string y
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."  # 2, 3

# prints some strings also with formatting
print(x)
print(y)
print(f"I said: {x}")           # 4
print(f"I also said: '{y}'")    # 5

# declares string and boolean variables and due to formatting puts boolean variable inside string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))    # 6

# prints the concatenation of two strings
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

# Explain why adding the two strings w and e with + makes a longer string
# Because the add operator for strings takes the first string and concatenates with the second one
