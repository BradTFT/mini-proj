
# i didnt know what to make today so i made this super basic script
input = input('Month(abbrv) example: jan = January. >>> ')


if input == 'jan' or input == 'Jan' or input == 'mar' or input == 'Mar' or input == 'may' or input == 'May' or input == 'jul' or input == 'Jul' or input == 'aug' or input == 'Aug' or input == 'oct' or input == 'Oct' or input == 'dec' or input == 'Dec':
    print(f'The month of {input} has 31 days')
elif input == 'apr' or input == "Apr" or input == 'jun' or input == 'Jun' or input == 'sept' or input == 'Sept' or input == 'sep' or input == 'Sep' or input == 'nov' or input == "Nov":
    print(f'The month of {input} has 30 days')
elif input == 'feb' or input == 'Feb':
    print(f'The month of {input} has 28 days, but every fourth year, known as leap year, it has 29 days')
