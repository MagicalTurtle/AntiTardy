from datetime import date, datetime
import json
import webbrowser
import pyautogui
from secrets import CHROME_PATH
import time
import os 

# get path
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# load classes dataset
with open(dir_path+'/classes.json') as f:
    class_db = json.load(f)


def check_day():
    # get day of the week, monday = 0
    weekday = datetime.today().weekday()
    if weekday == 1 or weekday == 3:
        day = "a"
        print("it's an A day..")
    else:
        if weekday == 2 or weekday == 4:
            day = "b"
            print("it's a B day..")
        else:
            print("it's not an A or B day..")
            day = "null"
    return day

def check_class(day):
    # gets current time
    current_time = datetime.now().strftime("%H:%M")

    # if advisory
    if current_time == "08:58"  or current_time == "08:59"  or current_time == "09:00":
        current_class = 0
    else:
        # if first/fifth block
        if current_time == "09:24" or current_time == "09:25" or current_time == "09:26":
            current_class = 1
        else:
            # if second/sixth block
            if current_time == "10:52" or current_time == "10:53" or current_time == "10:54":
                current_class = 2
            else:
                # if third/seventh block
                if current_time == "13:05" or current_time == "13:06" or current_time == "13:07":
                    current_class = 3
                else:
                    if current_time == "14:33" or current_time == "14:34" or current_time == "14:35":
                        current_class = 4
                    else:
                        # no class right now
                        current_class = -1

    # determines class with day and time
    if current_class > 0:
        course = day + str(current_class)
    elif current_class == 0:
        course = "advisory"
    elif current_class == -1:
        # no class
        course = "null"
        pass

    # if theres a class it gets meet code
    if course != "null":
        meet_link = class_db[course]
    else:
        meet_link = 'null'
    
    return meet_link, current_class

def open_class(url):
    #  webbrowser time
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser(CHROME_PATH))

    # google sign in
    webbrowser.get('chrome').open(url, new=0, autoraise=True)
    time.sleep(1)
    pyautogui.keyDown('crtl')
    pyautogui.press('r')
    pyautogui.keyUp('crtl')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.moveTo(3187, 580)
    pyautogui.click()

if __name__ == "__main__":
    while True:
        day = check_day()
        n=100000000
        while True:
            meet_url, current_class = check_class(day)
            if meet_url != 'null':
                break
            else:
                if n == 100000000:
                    print('no classes right now...')
                    n=0
                else:
                    n+=1
        open_class(meet_url)
        if current_class == 0:
            print('ADVISORY is right now..')
            time.sleep(1200)
        elif current_class == 1:
            print('FIRST class is right now..')
            time.sleep(4800)
        elif current_class == 2:
            print('SECOND class is right now..')
            time.sleep(4800)
        elif current_class == 3:
            print('THIRD class is right now..')
            time.sleep(4800)
        elif current_class == 4:
            print('FOURTH class is right now..')
            time.sleep(4800)
        else:
            print('this shouldnt run')