# Конструктор голосовых помощников на Python 

Этот проект разработан на языке Python с целью облегчить создание голосовых помощников и ускорить их интеграцию в различные проекты.


### Установка:

``` bash
git clone https://github.com/AlexeyTolstov/VoiceBotConstructor
cd VoiceBotConstructor
pip install -r requirements.txt
```

### Примеры использования:

``` python
from voice_bot import Bot

vb = Bot(name="Маришка")

@vb.check_command(["привет"], name_cmd="hello")
def hello():
    vb.say("Привет!")

vb.start()
```