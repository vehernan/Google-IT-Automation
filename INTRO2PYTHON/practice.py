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

""" // = floor division, divides a number
and takes the integer part of the division as the result."""

    def convert_seconds(seconds):
        hours = seconds // 3600
        minutes = (seconds - hours * 3600) // 60
        remaining_seconds = seconds - hours ** 3600 - minutes * 60
        return hours, minutes, remaining_seconds
    hours, minutes, seconds = convert_seconds(5000)
    print(hours, minutes, seconds)

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

#correct, their systam might be wrong?

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
"""

def hint_username(username): #colon ':' can be persieved as a {} like in C to begin a block
    if len(username) < 3: #if follow by condition we want to chech for
        print("Invalid username. Must be at least 3 characters long")
    elif #statement is like else if
    else:
        print("valid username")

def is_positive(number):
      if (number) > 0:
    return True



#LOOPS 