import socket
from tkinter import *
import time
import threading
import PIL.Image 
import PIL.ImageTk


root=Tk()
root.title("Chat-Bot")
root.geometry("300x500")
root.config(bg="white")

def fun():
    t=threading.Thread(target=recv)
    t.start()

def recv():
    listensocket=socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostname()
    print(ip)

    listensocket.bind(('',port))    
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()

    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"client : "+sendermessage)

xr=0

def sendmsg():
    global xr
    if xr==0:
        s=socket.socket()
        hostname='103.47.34.132'
        port=4050
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbox.insert(0,"You : "+msg)
        s.send(msg.encode())
        xr=xr+1

    else:
        msg=messagebox.get()    
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())

def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()


im = PIL.Image.open("chat.jpg")
startchatimage = PIL.ImageTk.PhotoImage(im)

# startchatimage=PhotoImage(file='send.png')

button=Button(root,image=startchatimage,command=fun,borderwidth=0)
# button=Button(root,text="Start Chat",command=fun,borderwidth=0)
button.place(x=90,y=10)

message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)


im = PIL.Image.open("send.png")
sendmessageimg = PIL.ImageTk.PhotoImage(im)
# sendmessageimg=PhotoImage(file='chat.jpg')

sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=260,y=440)

lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=10,y=80)

root.mainloop()