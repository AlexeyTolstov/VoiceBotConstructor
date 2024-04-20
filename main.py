from VoiceBotConstructor.bot import Bot

vb = Bot(name="Маришка")


@vb.check_command(["привет"], name_cmd="hello")
def hello():
    vb.say("Привет мой господин, как я могу быть полезна!")

vb.start()