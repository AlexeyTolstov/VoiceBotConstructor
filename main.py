from VoiceBotConstructor.bot import Bot
from VoiceBotConstructor.filters import crop_phrase, search_city
from VoiceBotConstructor.num2word import num2word

from VoiceBotConstructor.Plugins.time_data import get_datetime_now, get_day_of_week, month_lst
from VoiceBotConstructor.Plugins.weather import get_weather_info
from VoiceBotConstructor.Plugins.games.anecdotes import get_anecdote


vb = Bot(name="Маришка")


@vb.check_command(["привет"], name_cmd="hello")
def hello():
    vb.say("Привет мой господин, как я могу быть полезна!")


@vb.check_command(["время"], name_cmd="time")
def time():
    time_data = get_datetime_now()
    vb.say(f"Сейчас {time_data.hour} {time_data.minute}")


@vb.check_command(["погода", "температура"], name_cmd="weather")
def time(text: str):
    city = search_city(crop_phrase(text, ["погода", "температура"], vb.names))
    weather_info = get_weather_info(city, "YOUR_TOKEN")
    
    if weather_info is None:
        vb.say("Город {} не найден".format(city))
    else:
        vb.say("В городе {} сейчас {} градусов. ".format(city.title(), int(weather_info.temp)) +
           "Ощущается как {}.".format(int(weather_info.feel_like)))


@vb.check_command(["день недели"], name_cmd="day of week")
def day_of_week():
    time_data = get_datetime_now()
    vb.say("Сегодня {}".format(get_day_of_week(time_data)))


@vb.check_command(["число", "день"], name_cmd="day now")
def get_today():
    time_data = get_datetime_now()
    
    vb.say("Сегодня {} {}".format(time_data.day, month_lst[time_data.month]))


@vb.check_command(["анекдот"], name_cmd="anecdotes")
def get_today():
    vb.say(get_anecdote())


@vb.check_command(["список дел"], name_cmd="todo list")
def show_todo():
    todo = vb.config["todo_list"]
    if todo:
        vb.say("У вас есть {} записи: \n\t".format(len(todo)) + "\n\t".join(todo))
    else:
        vb.say("Список дел пуст")


@vb.check_command(["добавь задачу", "добавь задачи", "добавь заметку", "добавь заметки", "добавь запись", "добавь записи"], name_cmd="add todo list")
def add_todo():
    vb.say("Какую запись вы хотите добавить?")
    
    text = ""
    while not text:
        text = vb.recognize_speech()

        if not text:
            continue
        
        if any((s in text for s in set(["отмена", "отменить", "стоп"]))):
            vb.say("Добавление задачи отменено")
            break
    else:
        vb.config["todo_list"].append(text)
        vb.update_config()
        vb.say("Ваша запись успешно добавленна")


@vb.check_command(["удали задачу", "удали задачи", "удали заметку", "удали заметки", "удали запись", "удали записи"], name_cmd="delete todo list")
def delete_todo():
    vb.say("Под каким номером вы хотите удалить запись?")
    
    text = ""
    while not text:
        text = vb.recognize_speech()

        if not text:
            continue

        if any((s in text for s in set(["отмена", "отменить", "стоп"]))):
            vb.say("Удаление задачи отменено")
            break
    else:
        for num in range(len(vb.config["todo_list"]), 0, -1):
            if num2word(num) in text:
                vb.config["todo_list"].pop(num-1)
                vb.update_config()
                vb.say("Ваша запись успешно удалена")
                break
        else:
            vb.say("Запись не удалось найти")


vb.start()