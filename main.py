from wmi import WMI
from pywinauto import Application
from pydirectinput import press ,write,keyDown,keyUp
from colorama import Fore
from time import sleep
from os import system

system("color")
f = WMI()
pids = []






def get_pids():

    global pids

    for process in f.Win32_Process():

        if process.Name == "RobloxPlayerBeta.exe":
            pids.append(process.ProcessId)
            print(Fore.YELLOW,f"Checking {process.ProcessId}",Fore.WHITE)

            try:
                app = Application().connect(process=process.ProcessId)
                app.top_window().set_focus()
                print(Fore.GREEN,f"{process.ProcessId} OK",Fore.WHITE)
            except:
                pids.remove(process.ProcessId)
                print(Fore.RED,"Fake pid detect , Remove "+str(process.ProcessId),Fore.WHITE)







print(Fore.GREEN,"Checking pids",Fore.WHITE)



get_pids()



print(Fore.GREEN,f"Finishs pids = {pids}",Fore.WHITE)
print("""
[1] press key
[2] write text & write command""")


choose = int(input("[>]"))



if choose == 1:

    key = input("Key : ")

    delay = float(input("Delay : "))

    while True:

        for pid in pids:

            print(Fore.GREEN,str(pid)+" Sending",Fore.WHITE)

            try:

                app = Application().connect(process=pid)
                app.top_window().set_focus()
            except:

                pids.remove(pid)
                print(Fore.GREEN,"Remove "+str(pid),Fore.WHITE)
                
            press(key)
            print(Fore.GREEN,str(pid)+" Sent",Fore.WHITE)

            sleep(delay)







elif choose == 2:

    text = input("text : ")
    delay = float(input("Delay : "))

    while True:

        for pid in pids:

            print(Fore.GREEN,str(pid)+" Sending",Fore.WHITE)

            try:

                app = Application().connect(process=pid)
                app.top_window().set_focus()

            except:

                pids.remove(pid)
                print(Fore.GREEN,"Remove "+str(pid),Fore.WHITE)


            press('/')

            keyDown("ctrl")
            keyDown("a")

            keyUp("ctrl")
            keyUp("a")

            press("backspace")

            write(text)

            press("enter")

            print(Fore.GREEN,str(pid)+" Sent",Fore.WHITE)
    
            sleep(5)
    