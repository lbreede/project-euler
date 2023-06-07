# Counting Sundays

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

month_dict = {}
for m in MONTHS:
    if m in ("September", "April", "June", "November"):
        month_dict[m] = 30
    else:
        month_dict[m] = 31
month_dict["February"] = 28

curr_weekday = WEEKDAYS[0]
curr_day = 1
curr_month = MONTHS[0]
curr_year = 1900

# for i in range(31):
# 	curr_day = i
# 	print(f"{curr_day}. {curr_month} {curr_year}")

for year in range(1900, 2001):
    if year % 4 == 0:
        days = 29
    else:
        days = 28

    print(f"{year} has {days} days!")
