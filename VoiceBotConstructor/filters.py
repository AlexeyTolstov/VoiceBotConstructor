def crop_phrase(msg: str, cmd_phrases: list, voice_bot: str):
    msg = msg.replace(voice_bot, "")
    
    for cmd_phrase in cmd_phrases:
        if cmd_phrase in msg:
            msg = msg.replace(cmd_phrase, "")
            break
    
    return msg