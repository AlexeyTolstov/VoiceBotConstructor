from VoiceBotConstructor import Bot


vb = Bot(name="Маришка")

@vb.check_command(["привет"], name_cmd="hello")
def hello():
    vb.say("Привет!")

vb.start()