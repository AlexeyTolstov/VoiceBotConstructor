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


def get_datetime_now():
    return datetime.now()


def get_day_of_week(date: datetime):
    return day_of_week_lst[(date.day + date.month + date.year + 1) % 7]


if __name__ == "__main__":
    now = get_datetime_now()
    print(get_day_of_week(now))