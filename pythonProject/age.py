import datetime
# Need to import datetime format in order for date and time calculations to work
n=input("Input your name")
d=input("Input your year of birth")
# Request name and date of birth from the user. Python uses year-month-day format
a=2024-int(d)
# Subtracting current year from the birth year
print("Hello", n ,", you are now", a ,"years old. Wow!!!")