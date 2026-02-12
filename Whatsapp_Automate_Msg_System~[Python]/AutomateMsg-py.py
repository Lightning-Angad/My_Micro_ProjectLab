import pywhatkit as kit
import pyautogui
import time

contacts = ["+91xxxxxxxxxx", "+91xxxxxxxxxx", "+91xxxxxxxxxx", "+91xxxxxxxxxx", "+91xxxxxxxxxx"]

message = "Hello, This is a automate message send via Python 😊!"

for number in contacts:
    try:
        kit.sendwhatmsg_instantly(number, message, wait_time=20, tab_close=False)
        time.sleep(5)
        pyautogui.press("enter")
        print(f"Message scheduled successfully for {number}")
    except Exception as e:
        print(f"Failed to send message to {number}: {e}")