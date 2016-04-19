import random
import string

def randomstring(prefix="", size=30, chars=string.ascii_letters):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def getsession(request=None, sessions=None):
    sessid = request.get_cookie('sessionid', None)

    if not sessid: return None

    if sessid in sessions:
        return sessions[sessid]

    return None

if __name__ == "__main__":
    for _ in range(10):
        print (randomstring())
