import random
import subprocess
import ctypes



alphabet = "abcdefghijklmnopqrstuvwxyz"
upperalphabet = alphabet.upper()
pw_len = 14
pwlist = []

for i in range(pw_len//3):
    pwlist.append(alphabet[random.randrange(len(alphabet))])
    pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
    pwlist.append(str(random.randrange(10)))
for i in range(pw_len-len(pwlist)):
    pwlist.append(alphabet[random.randrange(len(alphabet))])

random.shuffle(pwlist)
pwstring = "".join(pwlist)

print(pwstring)

txt = pwstring
subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True)


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('Your password is listed below and has been copied to your clipboard.', pwstring, 1)
