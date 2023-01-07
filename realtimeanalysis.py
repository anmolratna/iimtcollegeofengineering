import time
timestamp = time.strftime('%A:%x:%I:%M:%S:%p')
print(timestamp)
timestamp = time.strftime('%I')
print(timestamp)
H=int(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
M=int(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
S=int(timestamp)
if (H == 5):
    print("GOOD MORNING")
elif (H == 12):
    print("GOOD AFTERNOON")
elif(H == 17):
    print("GOOD EVENING")
elif(H==21):
    print("good night")
elif(H==00):
    print("IT IS MIDNIGHT TIME PLEASE SLEEP")
else:
    print("thankyou have a nice day")

# NOTE below all the point related to the time

"""  %a    Locale’s abbreviated weekday name.

     %A    Locale’s full weekday name.

     %b    Locale’s abbreviated month name.

     %B    Locale’s full month name.

     %c    Locale’s appropriate date and time representation.

     %d    Day of the month as a decimal number [01,31].

     %H    Hour (24-hour clock) as a decimal number [00,23].

     %I    Hour (12-hour clock) as a decimal number [01,12].

     %j    Day of the year as a decimal number [001,366].

     %m    Month as a decimal number [01,12].

     %M    Minute as a decimal number [00,59].

     %p    Locale’s equivalent of either AM or PM. (1)

     %S    Second as a decimal number [00,61].(2)

     %U    Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year 
           preceding the first Sunday are considered to be in week 0. (3)

     %w    Weekday as a decimal number [0(Sunday),6].

     %W    Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year 
           preceding the first Monday are considered to be in week 0 (3)
     
     %x    Locale’s appropriate date representation.

     %X    Locale’s appropriate time representation.

     %y    Year without century as a decimal number [00,99].

     %Y    Year with century as a decimal number.

     %z    Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H 
           represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59]. 1

     %Z    Time zone name (no characters if no time zone exists). Deprecated. 1

     %%    A literal '%' character."""