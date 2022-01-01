import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def sendSineEmail(email):
    usr = 'funcgensignalsproject@gmail.com'
    psw = 'funcgensignalsproject@696969'
    fromaddr = usr
    toaddr = email
    with open('sine_wave.png', 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Sine Wave Generated'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("Please find the generated Waveform attached.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('sine_wave.png'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(usr, psw)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    print("Email sent successfully!")
    s.quit()

def sendSqaureEmail(email):
    usr = 'funcgensignalsproject@gmail.com'
    psw = 'funcgensignalsproject@696969'
    fromaddr = usr
    toaddr = email
    with open('square_wave.png', 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Square Wave Generated'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("Please find the generated Waveform attached.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('square_wave.png'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(usr, psw)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    print("Email sent successfully!")
    s.quit()

def sendSawtoothEmail(email):
    usr = 'funcgensignalsproject@gmail.com'
    psw = 'funcgensignalsproject@696969'
    fromaddr = usr
    toaddr = email
    with open('sawtooth_wave.png', 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Sawtooth Wave Generated'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("Please find the generated Waveform attached.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('sawtooth_wave.png'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(usr, psw)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    print("Email sent successfully!")
    s.quit()

def sendTriangleEmail(email):
    usr = 'funcgensignalsproject@gmail.com'
    psw = 'funcgensignalsproject@696969'
    fromaddr = usr
    toaddr = email
    with open('triangle_wave.png', 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Triangle Wave Generated'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("Please find the generated Waveform attached.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('triangle_wave.png'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(usr, psw)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    print("Email sent successfully!")
    s.quit()

def sendFourierEmail(email):
    usr = 'funcgensignalsproject@gmail.com'
    psw = 'funcgensignalsproject@696969'
    fromaddr = usr
    toaddr = email
    with open('fourier_series.png', 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Fourier Series Generated'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("Please find the generated Waveform attached.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename('fourier_series.png'))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(usr, psw)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    print("Email sent successfully!")
    s.quit()
