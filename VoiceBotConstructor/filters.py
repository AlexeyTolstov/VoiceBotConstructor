def crop_phrase(msg: str, cmd_phrases: list, voice_bot: list):
    msg = msg.lower()
    for name in voice_bot:
        if name in msg:
            msg = msg[msg.index(name) + len(name):]
            break
    
    for cmd_phrase in set(cmd_phrases):
        if cmd_phrase in msg:
            msg = msg[msg.index(cmd_phrase) + len(cmd_phrase):]
            break
    
    return msg.lstrip()

def search_city(msg: str):
    l = msg.lstrip()
    if l[0] == "в":
        l = l[2:]

    if l[-1] == "е":
        l = l[:-1]
    
    return l

if __name__ == "__main__":
    print(search_city("Бийске"))