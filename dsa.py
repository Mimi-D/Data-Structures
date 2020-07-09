def letterToIndex(ch):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    num=ord(ch.lower())
    if num<97 or num>122:
        print("INVALID INPUT")
    else:
        value=chr(num)
        find=alphabet.find(value)
        return find