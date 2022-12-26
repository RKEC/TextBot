import requests
import schedule
import time

def send_message():
    messages = ['Good morning Saidhbh', 'Good morning :)', 'Not awake rn but ']

    res = requests.post('https://textbelt.com/text', {
        'phone': num,
        'message': messages,
        'key': 'textbelt',
    })
    print(res.json())


schedule.every().day.at("07:00").do(send_message)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(60)
   