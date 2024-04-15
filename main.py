from VoiceBotConstructor import Bot
from VoiceBotConstructor.Plugins import get_datetime_now, get_day_of_week


vb = Bot(name="Маришка")

@vb.check_command(["привет"], name_cmd="hello")
def hello():
    vb.say("Привет мой господин, как я могу быть полезна!")


@vb.check_command(["день недели"], name_cmd="time")
def hello():
    now = get_datetime_now()
    vb.say(get_day_of_week(now))


vb.start()