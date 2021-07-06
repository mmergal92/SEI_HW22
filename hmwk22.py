# Exercise 1
# Create a list named students containing some student names (strings).
students = ['Maria', 'Hayley', 'Peiyi']

# Print out the second student's name.
print(students[1])

# Print out the last student's name.
print(students[-1])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
foods =('bananas','kiwis','apples')
# Use a for loop to print out the string "food goes here is a good food".
for foods in (foods):
  print (f"{foods} are a good food")

# Exercise 3
# Using a for loop, print just the last two food strings from foods.
foods =('bananas','kiwis','apples')
print(foods[1:])

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
home_town ={
  'city':'New York',
  'state':'NY',
  'population':'8 million'
}
# Print a string with this format:
# "I was born in city, state - population of population"
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for key, val in home_town.items():
  print(f'{key} = {val}')

# Exercise 6
# Create an empty list named cohort.
cohort=[]
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
#  {
#  	'student': 'Tina',
#  	'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.
j = 0
for student in (students):
  cohort.extend([{
    'student': student,
    'fav_food': foods[j]
  }])
  j += 1
for cohort in cohort:
  print(cohort)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
awesome_students = [f" {student} is awesome!" for student in students]
print(awesome_students)
# Iterate over awesome_students printing out each string.
for val in awesome_students:
  print(val)
# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
afoods = [food for food in foods if 'a' in food]
print(afoods)