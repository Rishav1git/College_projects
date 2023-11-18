################################################################
#Modules(start)

from tkinter import *
from tkinter import messagebox as mb
import datetime
import time
import winsound
from threading import *
from tkinter.ttk import *
from time import strftime
import speech_recognition  as sr
import random
import pyttsx3 

#Modules import(end)




#################################################################
global s_off
s_off=True
#################################################################

















#################################################################
#function(start)
def off():
    global s_off
    s_off=False    
###################################
def roll_the_dice():
        roll=Toplevel(root)
        roll.geometry("100x100")
        def dice():
            r=random.randint(1,6)
            mb.showinfo("Yay!",r,parent=roll)
            ps.say(r)
            ps.runAndWait()
            if r=='6'or r=='1':
                off()
        def run():
            global ps
            ps=pyttsx3.init()
            l=sr.Recognizer()
            with sr.Microphone() as source:
                mb.showinfo("Yay!","listening...",parent=roll)
                v=l.listen(source)
                c=l.recognize_google(v)
                print(c)
                c=c.lower()
                if 'roll' in c:
                    dice()
        Button(roll,text="speak",command=run).pack(pady=10)
###################################
def no_game():
    pass
###################################
def choose_num():
    global choosenum
    global root
    choosenum=Toplevel(root)
    choosenum.geometry("300x300")
    import random
    a = random.randint(0,100)
    def run():
        b = ev.get()
        if b == a:
            mb.showinfo("yay","correctly",parent=choosenum)
            off()
        elif b > a and (b-a)>10:
            mb.showinfo("Aww","high",parent=choosenum)
        elif b > a and (b-a) <= 10:
            mb.showinfo("Aww","little high",parent=choosenum)
        elif b < a and (a-b)>10:
            mb.showinfo("Aww"," low",parent=choosenum)
        elif b < a and (a-b)<= 10:
            mb.showinfo("Aww","little low",parent=choosenum)       
    ev=IntVar()
    Label(choosenum,text="Choose any number between'1-100'").pack(padx=50,pady=10)
    Entry(choosenum,textvariable=ev).pack(padx=50,pady=20)
    Button(choosenum,text="run",command=run).pack(padx=50,pady=50)
#####################################
#####################################
def rock_paper_scissor():
    global rps
    global root
    rps=Toplevel(root)
    rps.geometry("300x300")
    def run():
        import random
        a = ["rock","paper","scissor"]
        b = select.get()
        print(b)
        c = random.choice(a)
        if (b == "scissor" and  c == a[0]) or (b == "rock" and c == a[1]) or (b == "paper" and c == a[2]):
            mb.showinfo("Aww","The computer wins",parent=rps)
                                    
        if (b == "scissor" and  c == a[1]) or (b == "rock" and c == a[2]) or (b == "paper" and c == a[0]):
            mb.showinfo("Hurrah!","You win",parent=rps)
            off()                    
        if (b == "scissor" and  c == a[2]) or (b == "rock" and c == a[0]) or (b == "paper" and c == a[1]):
            mb.showinfo("Oh no","Its tie ",parent=rps)                         
    select=StringVar()
    drop=OptionMenu(rps,select,"rock","paper","scissor","rock").pack(padx=50,pady=20)
    Button(rps,text='Play',command=run).pack(padx=50,pady=50)
##########################################
##########################################
def sereis():
        global seris
        global root
        seris=Toplevel(root)
        seris.geometry("300x300")
        import random
        a = random.randint(1,100)
        d = random.randint(1,10)
        s = []
        for i in range(8):
            s.append(a+d*i)
        c = random.randint(0,7)
        r = s[c]
        s[c] = "__"
        #print("In the series:")
        for i in s:
           print(i,end =",")
        def run():
            z =ev.get()
            if z == r:
                mb.showinfo("Hurrah!","You are correct",parent=seris)
                off()
            else:
                mb.showinfo("Oh! no","Try again",parent=seris)
        ev=IntVar()
        Label(seris,text=s).pack(padx=50,pady=20)
        Entry(seris,textvariable=ev).pack(padx=50,pady=20)
        Button(seris,text="run",command=run).pack(padx=50,pady=10)
#####################################
#####################################
def mindbreaker():
        mindbreaker=Toplevel(root)
        mindbreaker.geometry("250x250")
        import random
        str1=StringVar()
        r = random.randint(1,7)
        f = open("words.txt","r")
        rd = f.read().split()
        f.close()
        x = random.choice(rd)
        y = random.choice(rd)
        x = list(x)
        y = list(y)
        def mind(a,b):
            u = []
            v = []
            for i in range(len(a)):
                if ord(a[i])+r <= 91:                  
                    u.append(str(chr(ord(a[i])+r)))
                else:                    
                    u.append(str(chr(ord(a[i])+r-26)))
            for i in range(len(b)):
                if ord(b[i])+r <= 91:                    
                    v.append(str(chr(ord(b[i])+r)))
                else:
                    v.append(str(chr(ord(b[i])+r-26)))
            return u,v
        p,q = mind(x,y)
        def string(a):
            b = ''
            for i in a:
                    b = b + str(i)
            return b
        x = string(x)
        y = string(y)
        p = string(p)
        q = string(q)
        res1="If  "+x+"  is equal to:  "+p
        res2="Then  "+y+"  is equal to: "
        Label(mindbreaker,text=res1).pack(side = TOP)
        Label(mindbreaker,text=res2).pack(side = TOP)
        Entry(mindbreaker,textvariable=str1).pack(pady=10)
        def run():        
            z=str1.get()
            z=z.upper()
            if z == q:
                mb.showinfo("Yay!","You are corect",parent=mindbreaker)
                off()
            elif z == '':
                mb.showinfo("Oops!","Invalid",parent=mindbreaker)
            else:
                mb.showinfo("Oh! No","Wrong Try again!",parent=mindbreaker)
                
        Button(mindbreaker,text="run",command=run).pack(pady=5)
################################

#function(end)
#################################################################
















#################################################################
#GAME(start)

def game():
    global game
    global mains
    game=Toplevel(mains)
    game.geometry("350x350")
    game.iconbitmap('SAC.ico')
###################################
    def choose_num():
        global choosenum
        global game
        choosenum=Toplevel(game)
        choosenum.geometry("300x300")
        import random
        a = random.randint(0,100)
        def run():
            b = ev.get()
            if b == a:
                mb.showinfo("yay","correctly",parent=choosenum)
            elif b > a and (b-a)>10:
                mb.showinfo("Aww","high",parent=choosenum)
            elif b > a and (b-a) <= 10:
                mb.showinfo("Aww","little high",parent=choosenum)
            elif b < a and (a-b)>10:
                mb.showinfo("Aww"," low",parent=choosenum)
            elif b < a and (a-b)<= 10:
                mb.showinfo("Aww","little low",parent=choosenum)       
        ev=IntVar()
        def speak():
            ps1=pyttsx3.init()
            l=sr.Recognizer()
            with sr.Microphone() as source:
                    mb.showinfo("Yay!","listening...",parent=choosenum)
                    v=l.listen(source)
                    c=l.recognize_google(v)
                    print(c)
                    c=int(c)
                    if c == a:
                        mb.showinfo("yay","correctly",parent=choosenum)
                    elif c > a and (c-a)>10:
                        mb.showinfo("Aww","high",parent=choosenum)
                    elif c > a and (c-a) <= 10:
                        mb.showinfo("Aww","little high",parent=choosenum)
                    elif c < a and (a-c)>10:
                        mb.showinfo("Aww"," low",parent=choosenum)
                    elif c < a and (a-c)<= 10:
                        mb.showinfo("Aww","little low",parent=choosenum)
        Label(choosenum,text="Choose any number between'1-100'").pack(padx=50,pady=10)
        Entry(choosenum,textvariable=ev).pack(padx=50,pady=20)
        Button(choosenum,text="run",command=run).pack(padx=50,pady=30)
        Button(choosenum,text="speak",command=speak).pack(padx=50,pady=20)
    #####################################
    #####################################
    def rps():
        global rps
        global game
        rps=Toplevel(game)
        rps.geometry("300x300")
        def run():
            import random
            a = ["rock","paper","scissor"]
            b = select.get()
            print(b)
            c = random.choice(a)
            if (b == "scissor" and  c == a[0]) or (b == "rock" and c == a[1]) or (b == "paper" and c == a[2]):
                mb.showinfo("Aww","The computer wins",parent=rps)
                                        
            if (b == "scissor" and  c == a[1]) or (b == "rock" and c == a[2]) or (b == "paper" and c == a[0]):
                mb.showinfo("Hurrah!","You win",parent=rps)
                                    
            if (b == "scissor" and  c == a[2]) or (b == "rock" and c == a[0]) or (b == "paper" and c == a[1]):
                mb.showinfo("Oh no","Its tie ",parent=rps)
        def speak():
            ps1=pyttsx3.init()
            l=sr.Recognizer()
            with sr.Microphone() as source:
                    mb.showinfo("Yay!","listening...",parent=rps)
                    v=l.listen(source)
                    d=l.recognize_google(v)
                    print(d)
                    d=d.lower()
                    a = ["rock","paper","scissor"]
                    c = random.choice(a)
                    if (d == "scissor" and  c == a[0]) or (d == "rock" and c == a[1]) or (d == "paper" and c == a[2]):
                        mb.showinfo("Aww","The computer wins",parent=rps)
                                                
                    if (d== "scissor" and  c == a[1]) or (d == "rock" and c == a[2]) or (d == "paper" and c == a[0]):
                        mb.showinfo("Hurrah!","You win",parent=rps)
                                            
                    if (d == "scissor" and  c == a[2]) or (d == "rock" and c == a[0]) or (d == "paper" and c == a[1]):
                        mb.showinfo("Oh no","Its tie ",parent=rps)                        
        select=StringVar()
        drop=OptionMenu(rps,select,"rock","paper","scissor","rock").pack(padx=50,pady=20)
        Button(rps,text='Play',command=run).pack(padx=50,pady=50)
        Button(rps,text='speak',command=speak).pack(padx=50,pady=20)
    ##########################################
    ##########################################
    def sereis():
        global seris
        global game
        seris=Toplevel(game)
        seris.geometry("300x300")
        import random
        a = random.randint(1,100)
        d = random.randint(1,10)
        s = []
        for i in range(8):
            s.append(a+d*i)
        c = random.randint(0,7)
        r = s[c]
        s[c] = "__"
        #print("In the series:")
        for i in s:
           print(i,end =",")
        def run():
            z =ev.get()
            if z == r:
                mb.showinfo("Hurrah!","You are correct",parent=seris)
            else:
                mb.showinfo("Oh! no","Try again",parent=seris)
        ev=IntVar()
        def speak():
            ps1=pyttsx3.init()
            l=sr.Recognizer()
            with sr.Microphone() as source:
                    mb.showinfo("Yay!","listening...",parent=seris)
                    v=l.listen(source)
                    c=l.recognize_google(v)
                    print(c)
                    c=int(c)
                    if c == r:
                        mb.showinfo("Hurrah!","You are correct",parent=seris)
                        ps1.say("You are correct")
                    else:
                        mb.showinfo("Oh! no","Try again",parent=seris)
                        ps1.say("Try again")

        Label(seris,text=s).pack(padx=50,pady=20)
        Entry(seris,textvariable=ev).pack(padx=50,pady=20)
        Button(seris,text="run",command=run).pack(padx=50,pady=10)
        Button(seris,text="speak",command=speak).pack(padx=50,pady=10)
    #####################################
    #####################################
    def mindbreaker():
            mindbreaker=Toplevel(game)
            mindbreaker.geometry("250x250")
            import random
            str1=StringVar()
            r = random.randint(1,7)
            f = open("words.txt","r")
            rd = f.read().split()
            f.close()
            x = random.choice(rd)
            y = random.choice(rd)
            x = list(x)
            y = list(y)
            def mind(a,b):
                u = []
                v = []
                for i in range(len(a)):
                    if ord(a[i])+r <= 91:
                        # print("below a",r,a[i],str(chr(ord(a[i])+r)))
                        u.append(str(chr(ord(a[i])+r)))
                    else:
                        # print("above a",r,a[i],str(chr(ord(a[i])+r-26)))
                        u.append(str(chr(ord(a[i])+r-26)))
                for i in range(len(b)):
                    if ord(b[i])+r <= 91:
                        # print("below b",r,b[i],str(chr(ord(b[i])+r)))
                        v.append(str(chr(ord(b[i])+r)))
                    else:
                        # print("above b",r,b[i],str(chr(ord(b[i])+r-26)))
                        v.append(str(chr(ord(b[i])+r-26)))
                return u,v
            p,q = mind(x,y)
            def string(a):
                b = ''
                for i in a:
                        b = b + str(i)
                return b
            x = string(x)
            y = string(y)
            p = string(p)
            q = string(q)
            res1="If  "+x+"  is equal to:  "+p
            res2="Then  "+y+"  is equal to: "            
            Label(mindbreaker,text=res1).pack(side = TOP,pady=10)
            Label(mindbreaker,text=res2).pack(side = TOP,pady=5)
            Entry(mindbreaker,textvariable=str1).pack(pady=10)
            
            def run():        
                z=str1.get()
                z=z.upper()
                if z == q:
                    mb.showinfo("Yay!","You are corect",parent=mindbreaker)
                elif z == '':
                    mb.showinfo("Oops!","Invalid",parent=mindbreaker)
                else:
                    mb.showinfo("Oh! No","Wrong Try again!",parent=mindbreaker)
                        
            Button(mindbreaker,text="run",command=run).pack(pady=10)
            mindbreaker.mainloop()
    ################################
    ################################
    
    def roll_the_dice():
        roll=Toplevel(game)
        roll.geometry("100x100")
        def dice():
            r=random.randint(1,6)
            mb.showinfo("Yay!",r,parent=roll)
            #print(r)
            ps.say(r)
            ps.runAndWait()
        def run():
            global ps
            ps=pyttsx3.init()
            l=sr.Recognizer()
            with sr.Microphone() as source:
                mb.showinfo("Yay!","listening...",parent=roll)
                #print("listening..")
                v=l.listen(source)
                c=l.recognize_google(v)
                print(c)
                c=c.lower()
                if 'roll' in c:
                    dice()
        Button(roll,text="speak for rolling",command=run).pack(pady=10)
    ##################################
    ##################################
    Label(game,text="Games").pack(padx=50,pady=15)
    b1=Button(game,text="choose_num",command=choose_num).pack(padx=50,pady=20)
    b2=Button(game,text="rps",command=rps).pack(padx=50,pady=15)
    b3=Button(game,text="sereis",command=sereis).pack(padx=50,pady=15)
    b4=Button(game,text="mindbreaker",command=mindbreaker).pack(padx=50,pady=15)
    b5=Button(game,text="roll_the_dice",command=roll_the_dice).pack(padx=50,pady=15)
    game.mainloop()
  
#GAME(end)
#################################################################












#################################################################
#ALARM(start)
def alarm():
    
    global root
    global s_off
    root=Toplevel(mains)
    root.geometry("350x350")
    root.iconbitmap('SAC.ico')

#########################
    # Use Threading
    def Threading():
        t1=Thread(target=alarm1)
        t1.start()
#########################

#########################
    def alarm1():
        global s_off
        mb.showinfo("ok","Alarm setted",parent=root)
        a=puzzle.get()
        b=eval(a)
        while True:
            if s_off!=False:
                set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time == set_alarm_time:
                    b()
                    print("on")
                    mb.showinfo("ok","Time to Wake up",parent=root)
                    while s_off!=False:                       
                        print("on")
                        winsound.Beep(500,2000)
            else:
                mb.showinfo("ok","Alarm off",parent=root)
                break
        print("off")
#########################
#############################
    # Add Labels, Frame, Button, Optionmenus
    Label(root,text="Alarm Clock",font=('calibri', 20, 'bold')).pack(padx=50,pady=15)
    Label(root,text="Set Time").pack(padx=50,pady=15)
    frame = Frame(root)
    frame.pack()
    ########
    hour = StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23', '24'
            )
    hour.set(hours[0])
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)
    minute = StringVar(root)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
    minute.set(minutes[0])
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)
    second = StringVar(root)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')   
    second.set(seconds[0])
    ######
    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)
    Button(root,text="Set Alarm",command=Threading).pack(padx=50,pady=15)
    puzzle = StringVar(root)
    puzzles = ('no_game','no_game','choose_number','sereis','rock_paper_scissor','mindbreaker',"roll_the_dice")
    puzzle.set(puzzles[0])
    puz = OptionMenu(frame, puzzle, *puzzles)
    puz.pack()
    s_off=Button(root,text='OFF',command=off).pack(padx=50,pady=15)
    root.mainloop()
    ###########################
#ALRM(end)
##################################################################################################













##################################################################################################

global mains
mains=Tk()
mains.geometry("360x360")




##################################################################
#Clock
def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)
lbl = Label(mains, font=('calibri', 40, 'bold'),background='skyblue',foreground='black')
lbl.pack(padx=1,pady=10)
time()
#Clock
##################################################################



mains.title("Clock")
mains.iconbitmap('SAC.ico')
Label(mains,text="Option Menu").pack(padx=50,pady=15)
br=Button(mains,text='Game',command=game).pack(padx=50,pady=20)
br1=Button(mains,text='Alarm',command=alarm).pack(padx=50,pady=15)

mains.mainloop()

#################################################################
