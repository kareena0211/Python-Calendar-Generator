# import calendar

# year = 2022
# month = 3
# x = calendar.month(year, month)
# print(x)


# .......................   Or ...........................

import calendar

year = 2022
month = 2

# Using the calendar module
x = calendar.month(year, month)
print(x)

print(f"Calendar for {calendar.month_name[month]} {year}:")
print()
print("Mo Tu We Th Fr Sa Su")
for week in calendar.monthcalendar(year, month):
    week_str = " ".join([str(day) if day != 0 else "  " for day in week])
    print(week_str)
