num_word = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать"
}

def num2word(n: int) -> str:
    if n < 0: 
       return "минус {}".format(num2word(abs(n))) 

    if 0 <= n <= 10:
        return num_word[n]
    
    elif 11 <= n <= 19:
        if n == 11: return "одиннадцать"
        if n == 12: return "двенадцать"
        if n == 13: return "тринадцать"
        if 14 <= n <= 19: return num2word(n % 10)[:-1] + "надцать"
        
    elif 20 <= n < 40:
        if n % 10:
            return num2word(n // 10) + "дцать " + num2word(n % 10)
        return num2word(n // 10) + "дцать"
    
    elif 40 <= n < 50:
        if n % 10 == 0:
            return "сорок"
        return "сорок " + num2word(n % 10)
    
    elif 50 <= n < 90:
        if n % 10:
            return num2word(n // 10) + "десят " + num2word(n % 10)
        return num2word(n // 10) + "десят "
    
    elif 90 <= n < 100:
        return "девяносто " + num2word(n % 10)
    
    elif 100 <= n < 200:
        return "сто " + num2word(n % 100)
    
    elif 200 <= n < 300:
        return "двести " + num2word(n % 100)
    
    elif 300 <= n < 500:
        return num2word(n // 100) + "тристо " + num2word(n % 100)
    
    elif 500 <= n < 1000:
        return num2word(n // 100) + "сот " + num2word(n % 100)


if __name__ == "__main__":
    for i in range(100):
        print(num2word(i))