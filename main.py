from VoiceBotConstructor import Bot
from VoiceBotConstructor.Plugins import get_datetime_now, get_day_of_week


vb = Bot(name="Маришка")

@vb.check_command(["привет"],
                name_cmd="hello")
def hello():
    vb.say("Привет мой господин, как я могу быть полезна!")


@vb.check_command(["выключить"], name_cmd="power_off")
def power_off():
    vb.say("Кто это сказал? Я не выключусь!")


vb.start()