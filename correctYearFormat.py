# Readable Time Durations
# Given a string input seconds, return a readable string of time featuring years, days, hours, minutes, and seconds.

# Example:
# Input: "31600000"
# Output:  "1 year, 0 days, 17 hours, 46 minutes, and 40 seconds"
# Note: Correct pluralization matters (1 year not 1 years)


sec = 31600000

def correctYearFormat(input):
    input = int(input)

    seconds = input % 36

    print(seconds)

print(correctYearFormat("31600000"))


year = sec // 31536000

sec_remaining = sec - (year * 31536000)

days = 31536000 - (31536000 * year)

sec_remaining = sec_remaining - (86400 * days)

hours = 86400 - (86400 * days)

# print(year, days, hours)


# print(year)

# days = sec // 86400
# print(f'{days}')

# # print(year, days)

# days_floor = days // 365 - year

# print(days_floor)

# hours = sec // 3600

# print(hours)

# hours_floor = (hours - (year *8760) - (days_floor * 24))
# print(f"{hours_floor} = ({hours} - ({year}*8760) - (24 * {days_floor}")

# hours_total = hours_floor % 24
# print(hours_total)

# minutes = sec // 60

# minutes_floor = (minutes)
 

# if year == 1:
#     year_string = "1 year"
# else:
#     year_string = f"{year} years"

# sec_minus_year = sec - year * 31536000

# days = sec_minus_year // 86400

# sec_minus_days = sec_minus_year - days * 86400

# print(year, days)


