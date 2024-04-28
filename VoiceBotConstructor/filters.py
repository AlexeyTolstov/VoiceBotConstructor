def crop_phrase(msg: str, cmd_phrases: list, voice_bot: list):
    for name in voice_bot:
        msg = msg.lower().replace(name.lower(), "")
    
    for cmd_phrase in cmd_phrases:
        if cmd_phrase in msg:
            msg = msg.replace(cmd_phrase.lower(), "")
            break
    
    return msg

def search_city(msg: str):
    msg = msg.lstrip()[2:] # в `городе`
    if "-" in msg: l = msg.split("-")
    else: l = msg.split(" ")

    l[0] = l[0][:-1]

    return " ".join(l)