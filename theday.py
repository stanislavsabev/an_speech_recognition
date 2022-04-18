import calendar

from siri import speak
from siri import speak_and_take_command

day_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero' : 0,
    'ten' : 10,
    'eleven' : 11,
    'twelve' : 12,
}

month_dict = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october' : 10,
    'november' : 11,
    'december' : 12,
}

def weekday():
    year = speak_and_take_command("Enter Year")
    month = speak_and_take_command("Enter Month")
    date = speak_and_take_command("Enter date")

    if month:
        month = month.lower()

    if month in day_dict:
        month = day_dict[month]

    if month in month_dict:
        month = month_dict[month]

    if date in day_dict:
        date = day[date]


    try:
        year, month, date = int(year), int(month), int(date)
        day = calendar.weekday(year, month, date)
    except Exception as e:
        print(e)
        return None

    return calendar.day_name[day]


if __name__ == '__main__':
    week_day = weekday()
    if week_day is None:
        speak('Unknown date.')
    else:
        speak(f"You were born on {week_day}")
