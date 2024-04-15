from datetime import datetime


day_of_week_lst = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
]


month_lst = {
    1: "январь",
    2: "февраль",
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь"
}


def get_datetime_now():
    return datetime.now()


def get_day_of_week(date: datetime):
    return day_of_week_lst[(date.day + date.month + date.year + 1) % 7]


if __name__ == "__main__":
    now = get_datetime_now()
    print(get_day_of_week(now))