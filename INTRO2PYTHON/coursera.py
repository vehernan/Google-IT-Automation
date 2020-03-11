def greeting(name, department):
    print("Welcome, " + name)

    greeting("Blake", "It support")
    Welcome, Blake
    


    def area_traingle(base, height):
        return base*height/2

        area_a = area_triangle(5,4)
        area_b = area_triangle(7,3)
        sum = area_a + area_b
        print("The sum of both areas is: " + str(sum))

    def get_second(hours, minutes, seconds):
        return 3600*hours + 60*minutes + seconds

        amount_a = get_seconds(2,30,0)
        amount_b = get_seconds(0,45,15)
        result = amount_a + amount_b
        print(result)
        11715

#RETURN VALUE
""" // = floor division, divides a number
and takes the integer part of the division as the result.
We may want a function to manipulate data 
we passed it and then return the result to us.
 This is where the concept of return values comes in handy
"""

    def convert_seconds(seconds):
        hours = seconds // 3600
        minutes = (seconds - hours * 3600) // 60
        remaining_seconds = seconds - hours ** 3600 - minutes * 60
        return hours, minutes, remaining_seconds
    hours, minutes, seconds = convert_seconds(5000)
    print(hours, minutes, seconds)
   
   
    def greeting(name):
        print("Welcome, " + name)

    result = greeting("Christine")
    Welcome, Christine
    >>print (result)
    None #NULL-is empty
    #up^ wont return anything


#code reuse

    name = "Kay"
    number = len(name) * 9

    print("Hello " + name + ". Your lucky number is " + str(number))

    name = "Cameron"
    number = len(name) * 9

    print("Hello " + name + ". Your lucky number is " + str(number))

    #instead reause code to seem cleaner

    def lucky_number(name):
        number = len(name) * 9
        print("Hello " + name + ". Your lucky number is " + str(number))

        lucky_number("Kay")
        lucky_number("Cameron")

#wrong 
    def print_monthly_expense(month, hours):
        month_cost = hours * 0.65 
        print("In " + month "we spent: " + str(month_cost))

#correct, their system might be wrong?

def print_monthly_expense(month, hours):
    month_cost = hours * 0.65 
    print("In " + month + "we spent: " + str(month_cost))
    
    print_monthly_expense("June",243)
    print_monthly_expense("July",325)
    print_monthly_expense("August",298)

#TEST 
#1st question
""" 1.Complete the function to return the result of the conversion
    2.Call the function to convert the trip distance from miles to kilometers
    3.Fill in the blank to print the result of the conversion
    4.Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

"""

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = ___

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + ___)

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + ___)


#answer maybe

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km

my_trip_miles = convert_distance(55)

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = my_trip_miles

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_miles))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_miles*2))


#2nd question: Fill in the blanks, so the print statement displays the result of the function call in order.
# # This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99) #filled in smaller,bigger <-
print(smaller, bigger)


#COMPARING THINGS


"""
<,>,==,
(&&, ||, !)
Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.

Comparison operators
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.
"""
#IF/ELSE/ELIF & modulos

def hint_username(username): #colon ':' can be persieved as a {} like in C to begin a block
    if len(username) < 3: #if follow by condition we want to chech for
        print("Invalid username. Must be at least 3 characters long")
    elif #statement is like else if
    else:
        print("valid username")

def is_positive(number):
      if (number) > 0:
    return True
def is_even(number):
    if number % 2 == 0:
        return True
    return False

def number_group(number):
      if (number) > 0:
    return "Positive"
  elif (number) < -1:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

#WEEK 2 TEST
 #1

"""
Complete the function by filling in the missing parts.
The color_translator function receives the name of a color,
then prints its hexadecimal value. 
Currently, it only supports the three additive primary colors (red, green, blue), 
so it returns "unknown" for all other colors. 
"""
#correct
def color_translator(color):
    	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

#4
"""
Students in a class receive their grades as Pass/Fail.
Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail".
In addition,scores above 95 (not included) are graded as "Top Score".
Fill in this function so that it returns the proper grade. 
"""
#correct
def exam_grade(score):
    	if (score) > 95:
		grade = "Top Score"
	elif (score) > 59:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

#6
"""
If both the last_name and the first_name parameters are supplied, the function should return like so:
print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella

If only one name parameter is supplied (either the first name or the last name) , the function should return like so:
print(format_name("Adele", ""))
Name: Adele

Finally, if both names are blank, the function should return the empty string
print(format_name("", ""))

"""
#alltries
def format_name(first_name, last_name):
    if first_name == 1 and last_name == 1
        return format_name();
    elif first_name == 1 or last_name == 1
        return format_name();
    else 
        return ("");

def format_name(first_name, last_name):
    if len(first_name) < 1 or len(last_name) < 1:
    else len(first_name) == 0 and len(last_name) == 0:
        return ("")

    if first_name != "" and last_name != "";
        string = "Name: " + first_name, last_name:
    else
        string = "":

def format_name(first_name, last_name):
      if first_name != "" and last_name != "":
    string = "Name: " + first_name, last_name
  elif first_name == "":
    string = "Name: " + last_name
  elif last_name == "":
    string = "Name: " + first_name
  else:
    string = ""
  return string 
else first_name == "" and last_name == "":
    string = ""


def format_name(first_name, last_name):
    if first_name == "" and last_name == "":
        string = ""
    elif first_name == "":
        string = "Name: " + last_name
    elif last_name == "":
        string = "Name: " + first_name
    else first_name != "" and last_name != "":
        string = "Name: " + first_name + "," + last_name
    return string
#CORRECT
def format_name(first_name, last_name):
      if first_name == "" and last_name == "":
    string = ""
  elif first_name != "" and last_name != "":
    string = "Name: " + last_name + ", " + first_name
  else:
    string = "Name: " + last_name + first_name
  return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

#7
"""
The longest_word function is used to compare 3 words.
It should return the word with the most number of characters
(and the first in the list when they have the same length). Fill in the blank to make this happen.

"""
#tries
def longest_word(word1, word2, word3):
    	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1) <= :
		word = word2
	else:
		word = word3
	return(word)

def longest_word(word1, word2, word3):
    	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1) < len(word2) and len(word2) > len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

def sum(x, y):
      return(x+y)
    print 3, 7 10

#10
"""
 The fractional_part function divides the numerator by the denominator,
 and returns just the fractional part (a number between 0 and 1).
 Complete the body of the function so that it returns the right number.
 Note: Since division by 0 produces an error, if the denominator is 0,
 the function should return 0 instead of attempting the division.
"""

def fractional_part(numerator, denominator):
    	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0



#WEEK 3
#LOOPS


  attempts(100)

  #output
  Attempt 1
  Attempt 2
  Attempt 3... until 100

  #
