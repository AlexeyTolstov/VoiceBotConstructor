# Конструктор голосовых помощников на Python 

Этот проект разработан на языке Python с целью облегчить создание голосовых помощников и ускорить их интеграцию в различные проекты.


### Установка:

``` bash
git clone https://github.com/AlexeyTolstov/VoiceBotConstructor
cd VoiceBotConstructor
pip install -r requirements.txt
```

#### ⚠ При установке у вас могут возникнуть некоторые проблемы с программным обеспечением. В тексте ошибки будут сказанны необходимые действия.

### Примеры использования:

``` python
from VoiceBotConstructor import Bot

vb = Bot(name="Маришка")

@vb.check_command(["привет"], name_cmd="hello")
def hello():
    vb.say("Привет!")

vb.start()
```

### Документация находится в директории `Documantation`