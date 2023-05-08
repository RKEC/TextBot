import requests
import schedule
import time
import random
import env
import smtplib
import ssl

count=0
email = env.EMAIL
password = env.PASSWORD

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
    send_email(message, count)
    next_time()
    return schedule.CancelJob

def send_email(message, count):
    context = ssl.create_default_context()
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls(context=context)
    conn.ehlo()
    conn.login(email, password)
    conn.sendmail(email, email, f'Subject: Text {count} sent! \n\n Text message: {message}')

def next_time():
    global count
    schedule.clear()
    schedule.every().day.at("07:00").do(send_message)
    count+=1

next_time()

if __name__ == '__main__':
    print("Program has started")
    while True:
        schedule.run_pending()
        time.sleep(60)
   
