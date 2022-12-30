import requests
import schedule
import time
import random
import env

def send_message():
    
    messages = env.MESSAGES

    message = messages[random.randint(0, len(messages)-1)] + " - Richard"
    print("Message: {}".format(message))

    res = requests.post('https://textbelt.com/text', {
        'phone': env.PHONE,
        'message': message,
        'key': 'textbelt',
    })
    print(res.json())
    next_time()
    return schedule.CancelJob

def next_time():
    schedule.clear()
    schedule.every().day.at("7:00").do(send_message)

next_time()

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(60)
   