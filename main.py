from VoiceBotConstructor.bot import Bot
from VoiceBotConstructor.filters import crop_phrase, search_city


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
    
    vb.say("Сегодня {} {}".format(time_data.day, month_lst[time_data]))


@vb.check_command(["анекдот"], name_cmd="anecdotes")
def get_today():
    vb.say(get_anecdote())


@vb.check_command(["список дел"], name_cmd="todo list")
def show_todo():
    todo = vb.config["todo_list"]
    if todo:
        vb.say("У вас есть {} записи. ".format(len(todo)) + \
               "\n".join(todo))
    else:
        vb.say("Список дел пуст")


@vb.check_command(["добавить задачу"], name_cmd="add todo list")
def show_todo():
    vb.say("Какую задачу вы хотите добавить?")
    
    text = ""
    while not text:
        text = vb.recognize_speech()
        if text == "отмена":
            vb.say("Добавление задачи отменено")
            break
        
    else:
        vb.config["todo_list"].append(text)
        vb.update_config()
        vb.say("Ваша задача успешно добавленна")


@vb.check_command(["удалить задачу"], name_cmd="delete todo list")
def delete_todo():
    vb.say("Какую задачу вы хотите удалить?")
    
    text = ""
    while not text:
        text = vb.recognize_speech()
        if text == "отмена":
            vb.say("Удаление задачи отменено")
            break
    else:
        if text == "один":
            text = "1"
        vb.config["todo_list"].pop(int(text)-1)
        vb.update_config()
        vb.say("Ваша задача успешно удалена")


vb.start()