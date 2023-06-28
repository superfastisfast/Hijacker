try:
    def colored(r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    import os
    import time
    import random
    try:
        import psutil
    except:
        os.system('python -m install psutil')
        import psutil
        os.system('cls')

    try:
        import numpy as num
    except:
        os.system('python -m install numpy')
        import numpy
        os.system('cls')

    import sys

    try:
        import pyttsx3
    except:
        os.system("python -m install pyttsx3")
        import pyttsx3
        os.system('cls')

    try:
        import pyautogui
    except:
        os.system("python -m install install pyautogui")
        import pyautogui
        os.system('cls')
    
    import socket

    try:
        from mailtm import Email
    except:
        os.system("python -m install mailtm")
        from mailtm import Email
        os.system('cls')
        
    try:
        from pystyle import Write, Colors
    except:
        os.system("python -m install pystyle")
        from pystyle import Write, Colors
        os.system('cls')

    from urllib.request import urlopen
    import webbrowser

    def SmartPrint(str):
        Write.Print(str + "\n", Colors.cyan_to_green, interval=0.005)

    def SmartInput1(str):
        TMPT = Write.Input(str, Colors.white, interval=0.00123456789)

        return TMPT

    def SmartPrint1(str):
        Write.Print(str + "\n\n", Colors.red_to_purple, interval=0.007)

    def SmartPrint2(str):
        Write.Print(str + "\n\n", Colors.white, interval=0.009)

    def RandomDictPicker(list = [], Letters = 26):
        obj = ""
        for x in range(Letters):
            obj += list[random.randint(0, len(list)) - 1]
        return obj
    
    
    def getIP():
        d = str(urlopen('http://checkip.dyndns.com/')
                .read())
    
        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

    SmartPrint("Loading Binary")
    def BinaryTranslator(str, Binary):
        if Binary == 1:
            return ''.join(format(ord(i), '08b') for i in str)
        if Binary == 0:
            tmp = ""
            for i in str:
                if not i == " ":
                    tmp += i
                    
            return ''.join(chr(int(tmp[i*8:i*8+8],2)) for i in range(len(tmp)//8))
    SmartPrint("Loaded Binary!")

    SmartPrint("Loading Wait Function")
    wait = time.sleep
    SmartPrint("Loaded Wait Function")

    SmartPrint("Loading Morse Code")
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    SmartPrint("Loaded Morse Code")

    SmartPrint("Loading Clear Function")
    def clear():
        os.system("cls")
    SmartPrint("Loaded Clear Function")

    SmartPrint("loading Pytts Engine")
    engine = pyttsx3.init()
    SmartPrint("Loaded Pytts Engine")

    
    voices = engine.getProperty('voices')
    SmartPrint("Get Voice")

    
    SmartPrint("Getting GAG Binary Encryption")
    def gag(str, GOUG):
        string = ""

        for i in str:
            if GOUG == 1:
                if i == "0":
                    string += "a"
                if i == "1":
                    string += "g"
                if i == " ":
                    string += "_"
            if GOUG == 0:
                if i == "a":
                    string += "0"
                if i == "g":
                    string += "1"
                if i == "_":
                    string += " "
        return string
    SmartPrint("Fetched GAG")

    SmartPrint("Getting BABA Binary Encryption")
    def baba(str, Baba):
        string = ""

        for i in str:
            if Baba == 1:
                if i == "0":
                    string += "a"
                if i == "1":
                    string += "b"
                if i == " ":
                    string += "."
            if Baba == 0:
                if i == "a":
                    string += "0"
                if i == "b":
                    string += "1"
                if i == ".":
                    string += " "
        return string
    SmartPrint("Fetched BABA")
    

    PcUsername = os.getenv("USERNAME")
    PcName = os.getenv("COMPUTERNAME")

    ver = "1.0"
    SmartPrint("Loaded Version")


    def encrypt(message):
        cipher = ''
        for letter in message:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                cipher += '/'
        return cipher


    SmartPrint("Load Text-To-Speech")
    def TTS(text):
        engine.say(text)
        engine.runAndWait()
    SmartPrint("Loaded Text-To-Speech")

    os.system('title Hijacker V-' +ver)
    SmartPrint("Title Changed")

    Voice_Is = False
    Debug = False
    
    def no_space(str):
        string = ""
        for i in str:
            if i == " ":
                string += ""
            else:
                string += i
        
        return string

    def Spinner():
        l = ['|', '/', '-', '\\', ' ']
        for i in l+l+l:
            sys.stdout.write(f"""\r {i}""")
            sys.stdout.flush()
            time.sleep(0.1)


    #   _    _          _____ 
    #  | |  | |   /\   / ____|
    #  | |__| |  /  \ | |  __ 
    #  |  __  | / /\ \| | |_ |
    #  | |  | |/ ____ \ |__| |
    #  |_|  |_/_/    \_\_____|

    #Presented by Hack-A-Gone Team, What A Pleasure!

    def _THag():
        print(" _    _          _____ ")
        print("| |  | |   /\   / ____|")
        print("| |__| |  /  \ | |  __ ")
        print("|  __  | / /\ \| | |_ |")
        print("| |  | |/ ____ \ |__| |")
        print("|_|  |_/_/    \_\_____|")

        print("\nPresented by Hack-A-Gone Team\n\n")
        
    with open("DATA/NewUser.txt", "r") as w:
        tmp = w.read()

        if tmp == "False":
            with open("DATA/NewUser.txt", "w") as x:
                x.truncate(0)
                x.write("True")

                wait(0.8)
                SmartPrint1(f'H-Bot >> New User Detected')
                Spinner()
                clear()

                tmp = input("H-Bot >> Name? ")

                SmartPrint(f'H-Bot >> Hi, {tmp}')
                SmartPrint('H-Bot >> I am a bot, as you can see..\n\n')

                wait(0.7)

                with open('DATA/Name.txt', 'a') as i:
                    i.truncate(0)
                    i.write(tmp)
                    i.close()
                
                SmartPrint(f"H-Bot >> Now reloading...")
                wait(0.8)
                clear()
                os.system("RunHijacker.bat")

                x.close()
        w.close()
        

    with open('DATA/Name.txt', 'r') as i:
        raw_name = i.readlines()

        i.close()
    
    if raw_name == []:
        name = "null"
        print(colored(255, 0, 0, "H-Bot >> ERROR LOADING NAME."))
    else:
        name = raw_name[0]

    wait(1)

    clear()
    wait(0.7)
    SmartPrint1(f'H-Bot >> Logged as {name}')
    suffix = "Hijacker"
    SmartPrint1("H-Bot >> Starting...")
    wait(0.7)
    SmartPrint1("H-Bot >> Started!")
    Spinner()
    clear()

    passcode_password = "8921"
    _THag()

    while True:
        #ignore these lines.
        with open('DATA/Name.txt', 'r') as i:
            raw_name = i.readlines()
            if not raw_name[0] == name:
                print(f'H-Bot >> {name} changed name to {raw_name[0]} \n')
            if raw_name == []:
                name = "NULL"
            else:
                name = raw_name[0]

            i.close()
        #################################################################################################################################################################################################################################################################################################
        
        word = SmartInput1(suffix +"-"+ name +": ")
        word = str(word).lower().split()
        argword = word
        word = argword[0]

        if Debug == True:
            print(argword)
            print(word)

        if word == "autoclick":
            while True:
                pyautogui.click()
        
        if word == "write" or word == "spam": # spam write
            if word == "spam":
                what_type = input("H-Bot >> (this will spam write a specified word/sentence) word to spam? ")
            if word == "write":
                what_type = input("H-Bot >> (this will spam write a specified word/sentence) word to write? ")
            wait(3)
            while True:
                pyautogui.write(what_type)
                pyautogui.press('enter')
        
        if word == "clear" or word == "cls":
            clear()
        
        if word == "spiral": # makes a spiral
            print("H-Bot >> activating in 5 seconds")
            wait(5)
            distance = 100
            while distance > 0:
                pyautogui.drag(distance, 0, duration=0.5)   # move right
                distance -= 5
                pyautogui.drag(0, distance, duration=0.5)   # move down
                pyautogui.drag(-distance, 0, duration=0.5)  # move left
                distance -= 5
                pyautogui.drag(0, -distance, duration=0.5)  # move up
        
        if word == "exit":
            os.system('exit')

        if word == "version":
            if Voice_Is == True:
                engine.say("version is " +ver)
                engine.runAndWait()
            print("H-Bot >> " +ver)

        if word == "ping":
            SmartPrint("\nH-Bot >> Running, cant you see?\n")

        if word == "echo":
            what_echo = ""
            for x in range(len(argword)):
                if not argword[x] == "echo":
                    what_echo += argword[x] + " "
            print(what_echo)

        if word == "edit":
            if not argword == [argword[0]]:
                what_edit = argword[1]
            else:
                what_edit = ""
            
            if what_edit == "tts":
                if not Voice_Is:
                    Voice_Is = True
                else:
                    Voice_Is = False

            elif Voice_Is:
                if what_edit == "voice":
                    engine.say("change voice to female or male? please input through terminal")
                    engine.runAndWait()
                    what_voice = input("H-Bot >> change voice to female or male? ")

                    if what_voice == "male":
                        engine.setProperty('voice', voices[0].id)
                        engine.say("This is how i sound now")
                        engine.runAndWait()
                    elif what_voice == "female":
                        engine.setProperty('voice', voices[1].id)
                        engine.say("This is how i sound now")
                        engine.runAndWait()
                else:
                    pass

            else:
                if what_edit == "voice":
                    what_voice = input("H-Bot >> change voice to female or male? ")

                    if what_voice == "male":
                        engine.setProperty('voice', voices[0].id)
                        engine.say("This is how i sound now")
                        engine.runAndWait()
                        print(colored(255, 0, 0,'H-Bot >> Voice is not enabled, this will only work for the text command, "tts"'))

                    elif what_voice == "female":
                        engine.setProperty('voice', voices[1].id)
                        engine.say("This is how i sound now")
                        engine.runAndWait()
                        print(colored(255, 0, 0,'H-Bot >> Voice is not enabled, this will only work for the text command, "tts"'))
                    else:
                        print(colored(255, 0, 0,'H-Bot >> Unknown voice type'))

            if what_edit == "name":
                if len(argword) == 3:
                    what_new_name = argword[3 -1]

                    with open('DATA/Name.txt', 'w') as i:
                        i.write(what_new_name)
                elif len(argword) > 3:
                    SmartPrint1(f'\nSyntax Error [need 1 given {len(argword) - 2}]: edit name [Username]')
                elif len(argword) < 3:
                    SmartPrint1(f'\nSyntax Error [needed 1 given {len(argword) - 2}]: edit name [Username]')
                

        if word == "bash" or word == "batch":
            if Voice_Is == True:
                engine.say("H-Bot >> please input through terminal.")
                engine.runAndWait()

            if word == "bash":
                whatbash = input("H-Bot >> What bash command? ")
            if word == "batch":
                whatbash = input("H-Bot >> What batch command? ")
            
            whatbash = str(whatbash).lower()

            if whatbash == "cmd": #cmd is not allowed!
                print("H-Bot >> Hijacker™️, cannot run cmd.")
            if whatbash == "bash":
                print("H-Bot >> Hijacker™️, will not continue to Linux.")

            else:
                os.system(whatbash)

        if word == "path":
            print(path) 

        if word == "elastic":
            ELasticMoveX = input("H-Bot >> x? ")
            ELasticMoveY = input("H-Bot >> y? ")
            pyautogui.moveTo(ELasticMoveX, ELasticMoveY, 2, pyautogui.easeInElastic) # NO but hackings diff
        
        if word == "credits":
            _THag()

        if word == "tts":
            word_tts = ""
            for x in range(len(argword)):
                if not argword[x] == "tts":
                    word_tts += argword[x] + " "
            TTS(word_tts)
        
        if word == "gag":
            gag_word = input("H-Bot >> Binary to GAG? ")

            print(gag(gag_word, 1))

        if word == "ungag":
            gag_word = input("H-Bot >> GAG to Binary? ")

            print(gag(gag_word, 0))

        if word == "binary" or word == "bin":
            bin_word = input("H-Bot >> Text to binary? ")

            bin_word = BinaryTranslator(bin_word, 1)

            print(bin_word)

        if word == "acsii" or word == "unbin":
            ascii_word = input("H-Bot >> Binary to Text? ")

            ascii_word = BinaryTranslator(no_space(ascii_word), 0)

            print(ascii_word)
        
        if word == "reload":
            clear()
            os.system("RunHijacker.bat")
        
        if word == "browser" or word == "internet" or word == "google":
            webbrowser.open('https://www.google.com/')
        
        if word == "shutdown" or word == "SHUTDOWN" or word == "Shutdown": # this will run a command on a sub-shell that will shutdown the computer
            print("H-Bot >> ok, this pc will shutdown in 5 seconds.")
            wait(0.6)
            os.system("shutdown /s /t 0")
        
        if word == "0110010101110010011100100110111101110010" or word == "0100010101110010011100100110111101110010" or word == "0100010101010010010100100100111101010010":
            clear()
            print(colored(255, 0, 0, f'\n\n\n\n\nH-Bot >> AN ERROR HAS OCOURRED ON {os.getenv("COMPUTERNAME")} ON USER {os.getenv("USERNAME")} DUE TO [UNKNOWN]\n\n\n'))
            wait(3)
            print("H-Bot >> Just kidding.\n\n")
        
        if word == "baba":
            baba_word = input("Text To Baba? ")
            print(baba(baba_word, 1))

        if word == "unbaba":
            baba_word = input("Baba To Text? ")
            print(baba(baba_word, 0))
        
        if word == "nospace":
            word_nospace = input("H-Bot >> What to remove spaces from? ")
            string = ""

            for i in word_nospace:
                if i == " ":
                    string += ""
                else:
                    string += i
            print(string)

        if word == "morseencrypt" or word == "me":
            Morse = input("H-Bot >> Text to Morse? ")
            Morse = encrypt(Morse.upper())
            print(Morse)
        
        if word == "pcn" or word == "pcname" or word == "PCNAME":
            print(PcName)

        if word == "username":
            print(PcUsername)
        
        if word == "email" or word == "te" or word == "tempmail" or word == "tempmail":
            Spinner()

            def listener(message):
                print("\nSubject: " + message['subject'])
                print("Content: " + message['text'] if message['text'] else message['html'])

            # Get Domains
            Mail = Email()
            print("\nDomain: " + Mail.domain)

            # Make new email address
            Mail.register()
            print("\nEmail Adress: " + str(Mail.address))

            # Start listening
            while True:
                word = input("H-Bot >> Press Any key To Check Again. ('exit' to escape): ")
                try:
                    Mail.start(listener)
                    print("Refreshing...")
                    print("")
                    if word == "exit" or word == "Exit":
                        break
                except:
                    SmartPrint1("Hjacker-Bot >> Error: We could not connect to the Internet. Perhaps enable wifi if you have it off.")
        
        
        if word == "restart":
            os.system("shutdown /r /t 1")

            if RobloxAPPFoundDuringInjection == True:
                SmartPrint(f"Inject DLL File To Roblox-Application")
            else:
                SmartPrint1(f"Error Application not found..")
        
        if word == "Multiply-every-two":
            what_byte = ""
            for x in range(len(argword)):
                if not argword[x] == "byte":
                    what_byte += argword[x] + " "
            
            try:
                what_byte = int(what_byte)

                tmp = 1
                tmp2 = [1]

                for x in range(what_byte):
                    tmp = tmp * 2
                    tmp2.append(tmp)
                
                print(tmp2)
            
            except:
                SmartPrint1("H-Bot >> Error: Not a Integer or Provided number too large")

#handle Exceptions
except KeyboardInterrupt:
    clear()
    print(colored(255, 0, 0, f'\n\n\n\n\nH-Bot >> AN ERROR HAS OCOURRED ON {os.getenv("COMPUTERNAME")} ON USER {os.getenv("USERNAME")} DUE TO KeyBoardInterrupt\n\n\n'))

# except:
#     clear()
#     print(colored(255, 0, 0, f'\n\n\n\n\nH-Bot >> AN ERROR HAS OCOURRED ON {os.getenv("COMPUTERNAME")} ON USER {os.getenv("USERNAME")} DUE TO [UNKNOWN]\n\n\n'))
