import os,random,sys,time
os.system("pkg install espeak")
from os import system as _ABDULLAH_
def lo(word):
    ABDULLAH = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(ABDULLAH)):
            sys.stdout.write(('\r{}{}').format(str(word), ABDULLAH[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def logo():
	color_logo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\x1b[38;5;208m'])
	print(f"""\n\033[1;90m██   ██ ███████ ██████   ██████ {color_logo} ███    ██ \n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ████   ██ \n\033[1;90m███████ █████   ██████  ██    ██{color_logo} ██ ██  ██    \033[1;97m┏━┓\n\033[1;90m██   ██ ██      ██   ██ ██    ██{color_logo} ██  ██ ██  \033[1;92m ┫\033[1;90m│\033[1;91m\033[47m𝘽\033[00m\033[1;90m│\033[1;92m┣\n\033[1;90m██   ██ ███████ ██   ██  ██████  {color_logo}██   ████   \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙍\033[00m\033[1;90m│\033[1;92m┣\n\t\t\t\t\t      \033[1;90m│\033[1;91m\033[47m𝘼\033[00m\033[1;90m│\n\033[1;97m┌━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┐  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝙉\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘈𝘜𝘛𝘏𝘖𝘙        \033[1;35m:  \033[1;37m𝗠𝗢𝗛𝗔𝗠𝗠𝗘𝗗 𝗔𝗕𝗗𝗨𝗟𝗟𝗔𝗛      \x1b[38;5;208m│  \033[1;92m┫\033[1;90m│\033[1;91m\033[47m𝘿\033[00m\033[1;90m│\033[1;92m┣\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘎𝘐𝘛𝘏𝘜𝘉        \033[1;35m:  \033[1;37mAbdullahX4      \x1b[38;5;208m│   \033[1;97m┗━┛\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \033[1;35m:  \033[1;37m01840888505       \x1b[38;5;208m│\n\033[1;97m│ \033[37;1m[\033[1;31m>_\033[1;37m] \033[1;30m𝘗𝘖𝘞𝘌𝘙         \033[1;35m:  \033[1;31m𝗠𝗢𝗛𝗔𝗠𝗠𝗘𝗗 𝗔𝗕𝗗𝗨𝗟𝗟𝗔𝗛      \x1b[38;5;208m│\n\033[1;97m└━━━━━━━━━━━━━━━━━━\x1b[38;5;208m⊱\033[34;1m   \033[37;1m⊰\x1b[38;5;208m━━━━━━━━━━━━━━━━━━┘\n\t\t \033[1;30m [\033[1;31m\033[1;47m𝙈𝘼𝙍𝙎𝙃𝘼𝙇\033[00m\033[1;30m] """)
try:
    import marshal
    os.system('clear')
    lo("     𝙋𝙇𝙀𝘼𝙎𝙀 𝙒𝘼𝙄𝙏...")
    _ABDULLAH_("clear")
    logo()
    _ABDULLAH_("espeak \"import your script\"")
    __F = input('\n \033[1;92m╔══[🐼] \033[1;90mInput script path\033[1;91m:\033[1;97m ')
    _ABDULLAH_(f"espeak \"you choose input {__F}\"")
    O__ = input(' \033[1;92m╚══[🐼] \033[1;90mOut put path\033[1;91m:\033[1;97m ')
    _ABDULLAH_(f"espeak \"you choose out put {O__}\"")
    try:
        __R = open(__F,'r').read()
    except:
        exit('\n script not found ')
        
    os.system(f'cp {__F} {O__}')
    for _ in range(20):
        cc = open(O__,'r').read()
        data = marshal.dumps(cc)
        _nop_ = open(O__,'w')
        _nop_.write('#_____________________________________\n#|>| THIS TOOL IS ENC BY MAX-ABDULLAH TOOLS☠️🔥\n#|>|FB_LINK:-https://www.facebook.com/Mohammed.Abdullah.04\n#|>|WHATS_APP:-+8801840888505\n#_____________________________________\n')
        _nop_.write('import marshal\n')
        _nop_.write(f'exec(marshal.loads({repr(data)}))')
        _nop_.close()
    print(f'\n [•] file saved in: {O__}')
    exit()
except Exception as e:
    exit(e)