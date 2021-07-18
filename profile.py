import sqlite3
from datetime import datetime
from tkinter import *
import tkinter.font
from network_query import connection_data

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()
hi=0
bi=0
mi=0
pi=0
ji=0


def f1(container1, entries1, et1, addB, removeButtons, txt):
    print(txt)
    tv = StringVar(container1, txt)
    et1.append(tv)
    e1 = (Entry(container1, textvariable=tv))
    entries1.append(e1)
    b1 = Button(container1, text="Remove", command=lambda: f2(b1, e1, tv))
    removeButtons.append(b1)
    entries1[-1].grid(row=len(entries1) - 1, column=1)
    removeButtons[-1].grid(row=len(entries1) - 1, column=2)
    addB.grid_forget()
    addB.grid(row=len(entries1), column=1)


def f2(b1s, e1, tv):
    b1s.destroy()
    print("HI")
    e1.destroy()
    print(e1)
    tv.set("")


def f11(user_id,container, datas, data, button1, output):
    # for da in len(datas):
    if data == "":
        datas.append("")

    print("Hi")
    new_container = LabelFrame(container)
    new_container.grid(row=len(datas), column=1)
    l1 = Label(new_container, text="high school at ")
    l2 = Label(new_container, text=" in field ")
    l3 = Label(new_container, text=" from ")
    l4 = Label(new_container, text=" to ")

    print(":::::::::::::::::::")
    if data == "":
        et1 = StringVar(new_container)
        et2 = StringVar(new_container)
        et3 = StringVar(new_container)
        et4 = StringVar(new_container)
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    else:
        et1 = StringVar(new_container, value=datas[-1][0])
        et2 = StringVar(new_container, value=datas[-1][1])
        et3 = StringVar(new_container, value=datas[-1][2])
        et4 = StringVar(new_container, value=datas[-1][3])
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    l1.grid(row=len(datas), column=1)
    e1.grid(row=len(datas), column=2)
    l2.grid(row=len(datas), column=3)
    e2.grid(row=len(datas), column=4)
    l3.grid(row=len(datas), column=5)
    e3.grid(row=len(datas), column=6)
    l4.grid(row=len(datas), column=7)
    e4.grid(row=len(datas), column=8)
    output.append((new_container,e1,e2,e3,e4,'h'))
    bg_id=1;

    rb = Button(new_container, text="Remove", command=lambda: f21(new_container,user_id,et1,et2,et3,et4))
    rb.grid(row=len(datas), column=9)
    sb = Button(new_container, text="submit", command=lambda: f22(bg_id,user_id,et1,et2,et3,et4))
    sb.grid(row=len(datas), column=10)


    button1.grid_forget()
    button1.grid(row=len(datas) + 1, column=1)

def f22(bg_id,user_id,et1,et2,et3,et4):
    print(et1.get())
    cur.execute(f'delete from background where user_id="{user_id}" and location="{et1.get()}" and field="{et2.get()}" and f="{et3.get()}" and t="{et4.get()}"')
    con.commit()
    cur.execute(f'insert into background(location,field,f,t,user_id,type) values("{et1.get()}","{et2.get()}","{et3.get()}","{et4.get()}","{user_id}", "h")')
    con.commit()
def f21(new_container,user_id,et1,et2,et3,et4):
    print(et1.get())
    cur.execute(f'delete from background where user_id="{user_id}" and location="{et1.get()}" and field="{et2.get()}" and f="{et3.get()}" and t="{et4.get()}"')
    con.commit()
    new_container.destroy()



def f12(container, datas, data, button1, output):
    # for da in len(datas):
    if data == "":
        datas.append("")

    print("Hi")
    new_container = LabelFrame(container)
    new_container.grid(row=len(datas), column=1)
    l1 = Label(new_container, text="bachelor degree from ")
    l2 = Label(new_container, text=" in field ")
    l3 = Label(new_container, text=" from ")
    l4 = Label(new_container, text=" to ")

    print(":::::::::::::::::::")
    if data == "":
        et1 = StringVar(new_container)
        et2 = StringVar(new_container)
        et3 = StringVar(new_container)
        et4 = StringVar(new_container)
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    else:
        et1 = StringVar(new_container, value=datas[-1][0])
        et2 = StringVar(new_container, value=datas[-1][1])
        et3 = StringVar(new_container, value=datas[-1][2])
        et4 = StringVar(new_container, value=datas[-1][3])
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    l1.grid(row=len(datas), column=1)
    e1.grid(row=len(datas), column=2)
    l2.grid(row=len(datas), column=3)
    e2.grid(row=len(datas), column=4)
    l3.grid(row=len(datas), column=5)
    e3.grid(row=len(datas), column=6)
    l4.grid(row=len(datas), column=7)
    e4.grid(row=len(datas), column=8)
    output.append((new_container,e1,e2,e3,e4,'b'))

    rb = Button(new_container, text="Remove", command=lambda: f21(new_container, et1, et2, et3, et4, e1, e2, e3, e4))
    rb.grid(row=len(datas), column=9)
    button1.grid_forget()
    button1.grid(row=len(datas) + 1, column=1)


def f13(container, datas, data, button1, output):
    # for da in len(datas):
    if data == "":
        datas.append("")

    print("Hi")
    new_container = LabelFrame(container)
    new_container.grid(row=len(datas), column=1)
    l1 = Label(new_container, text="master degree from ")
    l2 = Label(new_container, text=" in field ")
    l3 = Label(new_container, text=" from ")
    l4 = Label(new_container, text=" to ")

    print(":::::::::::::::::::")
    if data == "":
        et1 = StringVar(new_container)
        et2 = StringVar(new_container)
        et3 = StringVar(new_container)
        et4 = StringVar(new_container)
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    else:
        et1 = StringVar(new_container, value=datas[-1][0])
        et2 = StringVar(new_container, value=datas[-1][1])
        et3 = StringVar(new_container, value=datas[-1][2])
        et4 = StringVar(new_container, value=datas[-1][3])
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    l1.grid(row=len(datas), column=1)
    e1.grid(row=len(datas), column=2)
    l2.grid(row=len(datas), column=3)
    e2.grid(row=len(datas), column=4)
    l3.grid(row=len(datas), column=5)
    e3.grid(row=len(datas), column=6)
    l4.grid(row=len(datas), column=7)
    e4.grid(row=len(datas), column=8)
    output.append((new_container,e1,e2,e3,e4,'m'))

    rb = Button(new_container, text="Remove", command=lambda: f21(new_container, et1, et2, et3, et4, e1, e2, e3, e4))
    rb.grid(row=len(datas), column=9)
    button1.grid_forget()
    button1.grid(row=len(datas) + 1, column=1)


def f14(container, datas, data, button1, output):
    # for da in len(datas):
    if data == "":
        datas.append("")

    print("Hi")
    new_container = LabelFrame(container)
    new_container.grid(row=len(datas), column=1)
    l1 = Label(new_container, text="PHD degree from ")
    l2 = Label(new_container, text=" in field ")
    l3 = Label(new_container, text=" from ")
    l4 = Label(new_container, text=" to ")

    print(":::::::::::::::::::")
    if data == "":
        et1 = StringVar(new_container)
        et2 = StringVar(new_container)
        et3 = StringVar(new_container)
        et4 = StringVar(new_container)
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    else:
        et1 = StringVar(new_container, value=datas[-1][0])
        et2 = StringVar(new_container, value=datas[-1][1])
        et3 = StringVar(new_container, value=datas[-1][2])
        et4 = StringVar(new_container, value=datas[-1][3])
        e1 = Entry(new_container, textvariable=et1)
        e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    l1.grid(row=len(datas), column=1)
    e1.grid(row=len(datas), column=2)
    l2.grid(row=len(datas), column=3)
    e2.grid(row=len(datas), column=4)
    l3.grid(row=len(datas), column=5)
    e3.grid(row=len(datas), column=6)
    l4.grid(row=len(datas), column=7)
    e4.grid(row=len(datas), column=8)
    output.append((new_container,e1,e2,e3,e4,'p'))

    rb = Button(new_container, text="Remove", command=lambda: f21(new_container, et1, et2, et3, et4, e1, e2, e3, e4))
    rb.grid(row=len(datas), column=9)
    button1.grid_forget()
    button1.grid(row=len(datas) + 1, column=1)


def f15(container, datas, data, button1, output):
    # for da in len(datas):
    if data == "":
        datas.append("")

    print("Hi")
    new_container = LabelFrame(container)
    new_container.grid(row=len(datas), column=1)
    l1 = Label(new_container, text="Working at ")
    # l2=Label(new_container,text=" in field ")
    l3 = Label(new_container, text=" from ")
    l4 = Label(new_container, text=" to ")

    print(":::::::::::::::::::")
    if data == "":
        et1 = StringVar(new_container)
        # et2 = StringVar(new_container)
        et3 = StringVar(new_container)
        et4 = StringVar(new_container)
        e1 = Entry(new_container, textvariable=et1)
        # e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    else:
        et1 = StringVar(new_container, value=datas[-1][0])
        # et2 = StringVar(new_container,value=datas[-1][1])
        et3 = StringVar(new_container, value=datas[-1][2])
        et4 = StringVar(new_container, value=datas[-1][3])
        e1 = Entry(new_container, textvariable=et1)
        # e2 = Entry(new_container, textvariable=et2)
        e3 = Entry(new_container, textvariable=et3)
        e4 = Entry(new_container, textvariable=et4)
    l1.grid(row=len(datas), column=1)
    e1.grid(row=len(datas), column=2)
    # l2.grid(row=len(datas),column=3)
    # e2.grid(row=len(datas),column=4)
    l3.grid(row=len(datas), column=3)
    e3.grid(row=len(datas), column=4)
    l4.grid(row=len(datas), column=5)
    e4.grid(row=len(datas), column=6)

    rb = Button(new_container, text="Remove", command=lambda: f21(new_container, et1, None, et3, et4, e1, None, e3, e4))
    output.append((new_container,e1,None,e3,e4,'j'))
    rb.grid(row=len(datas), column=7)
    button1.grid_forget()
    button1.grid(row=len(datas) + 1, column=1)


# def f21(new_container, e1, e2, e3, e4, et1, et2, et3, et4):
#     print(new_container.winfo_children())
#     new_container.grid_forget()
#     e1.set("")
#     e3.set("")
#     e4.set("")
#     # et1.destroy()
#     # et3.destroy()
#     # et4.destroy()
#
#
#     if e2 != None:
#         e2.set("")
#         # et2.destroy()


def send_edit_to_DB(editPage, username, user_id, v1, v2, v3, v4, v5, v6,v7,v8, v11, entries1, entries2, entries3,
                    entries4, final):
    editPage.destroy()
    cur.execute(f'''UPDATE user SET name="{v1.get()}",
                                    gender="{1 if str(v2.get()).__eq__("Female") else 0 if v2.get() == "Male" else ""}",
                                    introducion="{v4.get()}",
                                    about="{v5.get()}",
                                    email="{v3.get()}",
                                    birthday="{"" if v11.get() == "yyyy-mm-dd" else v11.get()}",
                                    company="{v7.get()}",
                                    location="{v8.get()}"
                        WHERE username="{username}"
                                    ''')
    cur.execute(f'delete from feature where user_id="{user_id}"')
    con.commit()

    cur.execute(f'delete from skill where user_id="{user_id}"')
    con.commit()

    cur.execute(f'delete from language where user_id="{user_id}"')
    con.commit()

    cur.execute(f'delete from accomplishment where user_id="{user_id}"')

    con.commit()
    for entry in entries1:
        if entry.get() != "" and entry.get != None:
            cur.execute(f'insert into feature(content,user_id) values ("{entry.get()}","{user_id}")')
    con.commit()

    for entry in entries2:
        if entry.get() != "" and entry.get != None:
            cur.execute(f'insert into skill(content,user_id) values ("{entry.get()}","{user_id}")')
    con.commit()

    for entry in entries3:
        if entry.get() != "" and entry.get != None:
            cur.execute(f'insert into accomplishment(content,user_id) values ("{entry.get()}","{user_id}")')
    con.commit()

    for entry in entries4:
        if entry.get() != "" and entry.get != None:
            cur.execute(f'insert into language(content,user_id) values ("{entry.get()}","{user_id}")')
    con.commit()

    F = True

    cur.execute(f'delete from background where user_id="{user_id}"')
    con.commit()

    for data in final:
        try:
            print(data[0].get())
        except:
            final.remove(data)
        else:
            if data[1].get()!=None and data[1].get()!="" and data[3].get()!=None and data[3].get()!="":
                print("Error in saving data")
            else:
                cur.execute(
                    f'insert into background(location,field,f,t,type,user_id) values ("{data[1].get()}","{data[2].get()}","{data[3].get()}","{data[4].get()}","{data[5]}","{user_id}") ')
                con.commit()

    # cur.execute(
    #     f'insert into background(location,field,f,t,type,user_id) values ("{data[0].get()}","{data[1].get()}","{data[2].get()}","{data[3].get()}","{data[4]}","{user_id}") ')
    con.commit()

    con.commit()


def delete(cont,user_id, e1, e2, e3, e4,type):
    res = cur.execute(f'''select * from  background where
                                                        user_id="{user_id}" and
                                                        location="{str(e1.get())}" and
                                                        field="{str(e2.get())}" and
                                                        f="{str(e3.get())}" and
                                                        type="{type}" and
                                                        t="{str(e4.get())}"  ''').fetchall()
    if len(res)==0:
        if(e1.get()=="" and e2.get()=="" and e3.get()=="" and e4.get()=="" ):
            cont.destroy()
        else:
            x=Toplevel()
            l = Label(x, text="Unable to delete item with this property; this data wasn't be or saved in our database.\n complete the form or makes all filelds empty.")
            l.grid(row=0,column=0)

    else:
        print("HHHHHHHHHHHHHHH")
        cur.execute(f'''delete  from  background where
                                                                        user_id="{user_id}" and
                                                                        location="{str(e1.get())}" and
                                                                        field="{str(e2.get())}" and
                                                                        f="{str(e3.get())}" and
                                                                        t="{str(e4.get())}" and
                                                                        type="{type}"''')
        con.commit()
        cont.destroy()


def submit(user_id, e1, e2, e3, e4,type):
    if e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="":
        x = Toplevel()
        l = Label(x, text="Please complete all of the fields.")
        l.grid(row=0, column=0)
    else:
        res = cur.execute(f'''select * from  background where
                                                                user_id="{user_id}" and
                                                                location="{str(e1.get())}" and
                                                                field="{str(e2.get())}" and
                                                                f="{str(e3.get())}" and
                                                                t="{str(e4.get())}" and
                                                                type="{type}"''').fetchall()
        if len(res)==0:
            cur.execute(f'insert into background(user_id,location,field,f,t,type) values ("{user_id}","{str(e1.get())}","{str(e2.get())}","{str(e3.get())}","{str(e4.get())}","{type}")')
            con.commit()


def submit_job(user_id, e1, e3, e4, type):
    if e1.get() == "" or e3.get() == "" or e4.get() == "":
        x = Toplevel()
        l = Label(x, text="Please complete all of the fields.")
        l.grid(row=0, column=0)
    else:
        res = cur.execute(f'''select * from  background where
                                                                user_id="{user_id}" and
                                                                location="{str(e1.get())}" and
                                                                f="{str(e3.get())}" and
                                                                t="{str(e4.get())}" and
                                                                type="{type}"''').fetchall()
        if len(res) == 0:
            cur.execute(
                f'insert into background(user_id,location,f,t,type,field) values ("{user_id}","{str(e1.get())}","{str(e3.get())}","{str(e4.get())}","{type}","None")')
            con.commit()


def delete_job(cont, user_id, e1, e3, e4):
    res = cur.execute(f'''select * from  background where
                                                        user_id="{user_id}" and
                                                        location="{str(e1.get())}" and
                                                        f="{str(e3.get())}" and
                                                        t="{str(e4.get())}"  ''').fetchall()
    if len(res) == 0:
        if (e1.get() == ""  and e3.get() == "" and e4.get() == ""):
            cont.destroy()
        else:
            x = Toplevel()
            l = Label(x, text="Unable to delete item with this property; this data wasn't be or saved in our database.\n complete the form or makes all filelds empty.")
            l.grid(row=0, column=0)
    else:
        print("HHHHHHHHHHHHHHH")
        cur.execute(f'''delete  from  background where
                                                                        user_id="{user_id}" and
                                                                        location="{str(e1.get())}" and
                                                                        f="{str(e3.get())}" and
                                                                        t="{str(e4.get())}" and
                                                                        type="{type}"''')
        con.commit()
        cont.destroy()


def add(b,user_id, container,data,i,type,x):
    b.grid_forget()


    global hi,bi,mi,pi,ji
    b.grid(row=len(x)+10,column=0)
    print(len(x))
    x.append(None)

    print(len(x))
    if len(data)!=0:
        hi+=1
        bi+=1
        mi+=1
        pi+=1
        ji+=1
        # if type=='b':
        #     i=bi
        # if type=='h':
        #     i=hi
        # if type=='m':
        #     i=mi
        # if type=='p':
        #     i=pi
        # if type=='j':
        #     i=ji
        if type!='j':
            new_container = LabelFrame(container)
            new_container.grid(row=len(x), column=1)
            l1 = Label(new_container, text="high school at " if type=='h' else "bachlor degree from " if type=='b' else "master degree from " if type=='m' else "PHD degree from " if type=='p' else "")
            l2 = Label(new_container, text=" in field ")
            l3 = Label(new_container, text=" from ")
            l4 = Label(new_container, text=" to ")

            print(":::::::::::::::::::")
            # if data == []:
            #     et1 = StringVar(new_container)
            #     et2 = StringVar(new_container)
            #     et3 = StringVar(new_container)
            #     et4 = StringVar(new_container)
            #     e1 = Entry(new_container, textvariable=et1)
            #     e2 = Entry(new_container, textvariable=et2)
            #     e3 = Entry(new_container, textvariable=et3)
            #     e4 = Entry(new_container, textvariable=et4)
            # else:
            et1 = StringVar(new_container, value=data[0])
            et2 = StringVar(new_container, value=data[1])
            et3 = StringVar(new_container, value=data[2])
            et4 = StringVar(new_container, value=data[3])
            e1 = Entry(new_container, textvariable=et1)
            e2 = Entry(new_container, textvariable=et2)
            e3 = Entry(new_container, textvariable=et3)
            e4 = Entry(new_container, textvariable=et4)
            l1.grid(row=i, column=1)
            e1.grid(row=i, column=2)
            l2.grid(row=i, column=3)
            e2.grid(row=i, column=4)
            l3.grid(row=i ,column=5)
            e3.grid(row=i, column=6)
            l4.grid(row=i, column=7)
            e4.grid(row=i, column=8)

            rb = Button(new_container, text="Remove", command=lambda :delete(new_container,user_id,e1,e2,e3,e4,type))
            rb.grid(row=i, column=9)
            sb = Button(new_container, text="submit", command=lambda : submit(user_id,e1,e2,e3,e4,type))
            sb.grid(row=i, column=10)
            i+=1
        else:
            new_container = LabelFrame(container)
            new_container.grid(row=len(x), column=1)
            l1 = Label(new_container,
                       text="Working at " )
            # l2 = Label(new_container, text=" in field ")
            l3 = Label(new_container, text=" from ")
            l4 = Label(new_container, text=" to ")

            print(":::::::::::::::::::")
            # if data == []:
            #     et1 = StringVar(new_container)
            #     et2 = StringVar(new_container)
            #     et3 = StringVar(new_container)
            #     et4 = StringVar(new_container)
            #     e1 = Entry(new_container, textvariable=et1)
            #     e2 = Entry(new_container, textvariable=et2)
            #     e3 = Entry(new_container, textvariable=et3)
            #     e4 = Entry(new_container, textvariable=et4)
            # else:
            et1 = StringVar(new_container, value=data[0])
            # et2 = StringVar(new_container, value=data[1])
            et3 = StringVar(new_container, value=data[2])
            et4 = StringVar(new_container, value=data[3])
            e1 = Entry(new_container, textvariable=et1)
            # e2 = Entry(new_container, textvariable=et2)
            e3 = Entry(new_container, textvariable=et3)
            e4 = Entry(new_container, textvariable=et4)
            l1.grid(row=i, column=1)
            e1.grid(row=i, column=2)
            # l2.grid(row=i, column=3)
            # e2.grid(row=i, column=4)
            l3.grid(row=i, column=5)
            e3.grid(row=i, column=6)
            l4.grid(row=i, column=7)
            e4.grid(row=i, column=8)

            rb = Button(new_container, text="Remove", command=lambda: delete_job(new_container, user_id, e1, e3, e4))
            rb.grid(row=i, column=9)
            sb = Button(new_container, text="submit", command=lambda: submit_job(user_id, e1, e3, e4, type))
            sb.grid(i, column=10)
            i += 1

    else:
        if type != 'j':
                new_container = LabelFrame(container)
                new_container.grid(row=len(x), column=1)
                l1 = Label(new_container,
                           text="high school at " if type == 'h' else "bachlor degree from " if type == 'b' else "master degree from " if type == 'm' else "PHD degree from " if type == 'p' else "")
                l2 = Label(new_container, text=" in field ")
                l3 = Label(new_container, text=" from ")
                l4 = Label(new_container, text=" to ")

                print(":::::::::::::::::::")
                # if data == []:
                et1 = StringVar(new_container)
                et2 = StringVar(new_container)
                et3 = StringVar(new_container)
                et4 = StringVar(new_container)
                e1 = Entry(new_container, textvariable=et1)
                e2 = Entry(new_container, textvariable=et2)
                e3 = Entry(new_container, textvariable=et3)
                e4 = Entry(new_container, textvariable=et4)
                # else:
                # et1 = StringVar(new_container, value=data[0])
                # et2 = StringVar(new_container, value=data[1])
                # et3 = StringVar(new_container, value=data[2])
                # et4 = StringVar(new_container, value=data[3])
                # e1 = Entry(new_container, textvariable=et1)
                # e2 = Entry(new_container, textvariable=et2)
                # e3 = Entry(new_container, textvariable=et3)
                # e4 = Entry(new_container, textvariable=et4)
                l1.grid(row=i, column=1)
                e1.grid(row=i, column=2)
                l2.grid(row=i, column=3)
                e2.grid(row=i, column=4)
                l3.grid(row=i, column=5)
                e3.grid(row=i, column=6)
                l4.grid(row=i, column=7)
                e4.grid(row=i, column=8)

                rb = Button(new_container, text="Remove",
                            command=lambda: delete(new_container, user_id, e1, e2, e3, e4,type))
                rb.grid(row=i, column=9)
                sb = Button(new_container, text="submit", command=lambda: submit(user_id, e1, e2, e3, e4, type))
                sb.grid(row=i, column=10)
                i += 1
        else:

            new_container = LabelFrame(container)
            new_container.grid(row=len(x), column=1)
            l1 = Label(new_container,text="Working at ")
            l2 = Label(new_container, text=" in field ")
            l3 = Label(new_container, text=" from ")
            l4 = Label(new_container, text=" to ")

            print(":::::::::::::::::::")
            # if data == []:
            et1 = StringVar(new_container)
            # et2 = StringVar(new_container)
            et3 = StringVar(new_container)
            et4 = StringVar(new_container)
            e1 = Entry(new_container, textvariable=et1)
            # e2 = Entry(new_container, textvariable=et2)
            e3 = Entry(new_container, textvariable=et3)
            e4 = Entry(new_container, textvariable=et4)
            # else:
            # et1 = StringVar(new_container, value=data[0])
            # et2 = StringVar(new_container, value=data[1])
            # et3 = StringVar(new_container, value=data[2])
            # et4 = StringVar(new_container, value=data[3])
            # e1 = Entry(new_container, textvariable=et1)
            # e2 = Entry(new_container, textvariable=et2)
            # e3 = Entry(new_container, textvariable=et3)
            # e4 = Entry(new_container, textvariable=et4)
            l1.grid(row=i, column=1)
            e1.grid(row=i, column=2)
            # l2.grid(row=i, column=3)
            # e2.grid(row=i, column=4)
            l3.grid(row=i, column=5)
            e3.grid(row=i, column=6)
            l4.grid(row=i, column=7)
            e4.grid(row=i, column=8)

            rb = Button(new_container, text="Remove", command=lambda: delete_job(new_container, user_id, e1, e3, e4))
            rb.grid(row=i, column=9)
            sb = Button(new_container, text="submit", command=lambda: submit_job(user_id, e1, e3, e4, type))
            sb.grid(row=i, column=10)
            i += 1


def do_it(user_id):
    global hi,bi,mi,pi,ji
    editBG=Tk()
    highschool=LabelFrame(editBG,text="High School")
    bachlor=LabelFrame(editBG,text="Bachlor")
    master=LabelFrame(editBG,text="Master")
    phd=LabelFrame(editBG,text="PHD")
    job=LabelFrame(editBG,text="Jobs")
    highschool.grid(row=1,column=1)
    bachlor.grid(row=2,column=1)
    master.grid(row=3,column=1)
    phd.grid(row=4,column=1)
    job.grid(row=5,column=1)
    list1=[]
    ab1=Button(highschool,text="Add",command=lambda :add(ab1,user_id,highschool,[],hi,'h',list1))
    ab2=Button(bachlor,text="Add",command=lambda :add(ab2,user_id,bachlor,[],bi,'b',list1))
    ab3=Button(master,text="Add",command=lambda :add(ab3,user_id,master,[],mi,'m',list1))
    ab4=Button(phd,text="Add",command=lambda :add(ab4,user_id,phd,[],pi,'p',list1))
    ab5=Button(job,text="Add",command=lambda :add(ab5,user_id,job,[],ji,'j',list1))
    ab1.grid(row=1,column=1)
    ab2.grid(row=1,column=1)
    ab3.grid(row=1,column=1)
    ab4.grid(row=1,column=1)
    ab5.grid(row=1,column=1)
    highSchoolD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="h"  ').fetchall()
    bachlorD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="b"  ').fetchall()
    masterD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="m"  ').fetchall()
    PHDD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="p"  ').fetchall()
    jobsD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="j"  ').fetchall()
    i=0
    for data in highSchoolD:
        add(ab1,user_id, highschool, data,i,'h',list1)
        i+=1
    i=0
    for data in bachlorD:
        add(ab2,user_id,bachlor,data,i,'b',list1)
        i+=1
    i=0
    for data in masterD:
        add(ab3,user_id,master,data,i,'m',list1)
        i += 1
    i = 0

    for data in PHDD:
        add(ab4,user_id,phd,data,i,'p',list1)
        i += 1
    i = 0

    for data in jobsD:
        add(ab5,user_id,job,data,i,'j',list1)
        i += 1



def editInfo(mainPage, username):
    data_from_user_table = cur.execute(f'select * from user where username="{username}" ').fetchall()[0]
    user_id = data_from_user_table[0]
    mainPage.destroy()
    editPage = Tk()
    Edit = Label(editPage, text="EDIT", bd=4)
    Edit.grid(row=0, column=1)
    v1 = StringVar(editPage, value=data_from_user_table[1] if data_from_user_table[1] != None and data_from_user_table[
        1] != "" else "")
    userName = Label(editPage, text="Username:", anchor='w')
    usernameD = Entry(editPage, textvariable=v1)
    userName.grid(row=1, column=1)
    usernameD.grid(row=1, column=2)
    gender = Label(editPage, text='Gender:')
    genderTXT = "" if data_from_user_table[2] == None or data_from_user_table[2] == '' else (
        "Female" if data_from_user_table[2] == 1 else "Male")
    guid2=Label(editPage,text="Format:Female\Male")
    guid2.grid(row=2,column=3)
    v2 = StringVar(editPage, value=genderTXT)
    genderD = Entry(editPage, textvariable=v2)
    gender.grid(row=2, column=1)
    genderD.grid(row=2, column=2)
    birthday = Label(editPage, text='Birthday:')
    birthdayTXT = (
        str(data_from_user_table[6]) if data_from_user_table[6] != None and str(data_from_user_table[6]) != ''
        else "")
    guid=Label(editPage,text="Format:yyyy-mm-dd")
    guid.grid(row=3,column=3)
    v11 = StringVar(editPage, value=birthdayTXT)
    birthdayD = Entry(editPage, textvariable=v11)
    birthday.grid(row=3, column=1)
    birthdayD.grid(row=3, column=2)
    email = Label(editPage, text='Email:')
    v3 = StringVar(editPage, value=data_from_user_table[3])
    emailD = Entry(editPage, textvariable=v3)
    email.grid(row=4, column=1)
    emailD.grid(row=4, column=2)
    intro = Label(editPage, text="Introduction:", anchor='w')
    v4 = StringVar(editPage, value=data_from_user_table[4])
    introD = Entry(editPage, textvariable=v4)
    intro.grid(row=5, column=1)
    introD.grid(row=5, column=2)
    about = Label(editPage, text="About Me:", anchor='w')
    v5 = StringVar(editPage, value=data_from_user_table[5])
    aboutD = Entry(editPage, textvariable=v5)
    about.grid(row=6, column=1)
    aboutD.grid(row=6, column=2)
    featured = Label(editPage, text="Featured:", anchor='w')
    featuredDs = cur.execute(f'select content from feature where (user_id= "{user_id}" )').fetchall()
    featureTXT = ""
    container1 = LabelFrame(editPage)
    container1.grid(row=7, column=2)
    entries1 = []
    removeButtons1 = []
    entries_Text_vars1 = []
    addButton1 = Button(container1, text="add feature",
                        command=lambda: f1(container1, entries1, entries_Text_vars1, addButton1, removeButtons1, ""))
    addButton1.grid(row=len(entries1), column=1)
    for i in range(len(featuredDs)):
        f1(container1, entries1, entries_Text_vars1, addButton1, removeButtons1, featuredDs[i][0])

    v6 = StringVar(editPage, value=featureTXT)
    featured.grid(row=7, column=1)
    highSchool = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="h"  ').fetchall()
    bachlor = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="b"  ').fetchall()
    master = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="m"  ').fetchall()
    PHD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="p"  ').fetchall()
    jobs = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="j"  ').fetchall()

    en5_1_at = []
    ent5_1_at = []
    en5_1_in = []
    ent5_1_in = []
    en5_1_from = []
    ent5_1_from = []
    en5_1_to = []
    ent5_1_to = []
    final=[]


    container5 = LabelFrame(editPage)
    # container5.grid(row=8, column=2)
    container5_1 = LabelFrame(container5, text="High School")
    container5_1.grid(row=1, column=1)
    output1 = []
    hs = []
    editBG=Button(editPage,text="Edit background info.",command=lambda :do_it(user_id))
    editBG.grid(row=8,column=2)

    AddButton5_1 = Button(container5_1, text="Add",
                          command=lambda: (f11(user_id,container5_1, highSchool, "", AddButton5_1, final)))
    for data in highSchool:
        hs.append(data)
        f11(user_id,container5_1, hs, data, AddButton5_1, output1)

    # AddButton5_1.grid(row=2, column=1)
    # container5_2 = LabelFrame(container5, text="Bachelor")
    # container5_2.grid(row=2, column=1)
    # output2 = []
    # b = []
    # AddButton5_2 = Button(container5_2, text="Add",
    #                       command=lambda: (f12(container5_2, bachlor, "", AddButton5_2, final)))
    # for data in bachlor:
    #     b.append(data)
    #     f12(container5_2, b, data, AddButton5_2, output2)
    # AddButton5_2.grid(row=1, column=1)
    # container5_3 = LabelFrame(container5, text="Master")
    # container5_3.grid(row=3, column=1)
    # output3 = []
    # m = []
    # AddButton5_3 = Button(container5_3, text="Add",
    #                       command=lambda: (f13(container5_3, master, "", AddButton5_3, final)))
    # for data in master:
    #     m.append(data)
    #     f13(container5_3, m, data, AddButton5_3, output3)
    # AddButton5_3.grid(row=2, column=1)
    # container5_4 = LabelFrame(container5, text="PHD")
    # container5_4.grid(row=4, column=1)
    # output4 = []
    # p = []
    # AddButton5_4 = Button(container5_4, text="Add",
    #                       command=lambda: (f14(container5_4, PHD, "", AddButton5_4, final)))
    # for data in PHD:
    #     p.append(data)
    #     f14(container5_4, p, data, AddButton5_4, output4)
    # AddButton5_4.grid(row=2, column=1)
    # container5_5 = LabelFrame(container5, text="Jobs")
    # container5_5.grid(row=5, column=1)
    # output5 = []
    # j = []
    # AddButton5_5 = Button(container5_5, text="Add",
    #                       command=lambda: (f15(container5_5, jobs, "", AddButton5_5, final)))
    # for data in jobs:
    #     j.append(data)
    #     f15(container5_5, j, data, AddButton5_5, output5)
    # AddButton5_5.grid(row=2, column=1)
    #
    # background = Label(editPage, text="Background", anchor='w')
    # background.grid(row=8, column=1)
    skillDs = cur.execute(f'select content from skill where (user_id= "{user_id}" )').fetchall()

    container2 = LabelFrame(editPage)
    container2.grid(row=9, column=2)
    entries2 = []
    entries_Text_vars2 = []
    removeButtons2 = []

    addButton2 = Button(container2, text="add skill",
                        command=lambda: f1(container2, entries2, entries_Text_vars2, addButton2, removeButtons2, ""))
    for i in range(len(skillDs)):
        f1(container2, entries2, entries_Text_vars2, addButton2, removeButtons2, skillDs[i][0])
    addButton2.grid(row=len(entries2), column=1)
    skills = Label(editPage, text="Skills:")
    skills.grid(row=9, column=1)

    accomplishmentD = cur.execute(f'select content from accomplishment where user_id= "{user_id}"').fetchall()
    accomplishments = Label(editPage, text="Accomplishments:", anchor='w')
    accomplishments.grid(row=10, column=1)

    container3 = LabelFrame(editPage)
    container3.grid(row=10, column=2)
    entries3 = []
    entries_Text_vars3 = []
    removeButtons3 = []

    addButton3 = Button(container3, text="add accomplishment",
                        command=lambda: f1(container3, entries3, entries_Text_vars3, addButton3, removeButtons3, ""))
    for i in range(len(accomplishmentD)):
        f1(container3, entries3, entries_Text_vars3, addButton3, removeButtons3, accomplishmentD[i][0])
    addButton3.grid(row=len(entries3), column=1)

    supportedLanguages = Label(editPage, text="Supported Languages:", anchor='w')
    supportedLanguages.grid(row=11, column=1)
    supportedLanguagesD = cur.execute(f'select content from language where user_id= "{user_id}" ').fetchall()

    container4 = LabelFrame(editPage)
    container4.grid(row=11, column=2)
    entries4 = []
    removeButtons4 = []
    entries_Text_vars4 = []

    addButton4 = Button(container4, text="add language",
                        command=lambda: f1(container4, entries4, entries_Text_vars4, addButton4, removeButtons4, ""))
    for i in range(len(supportedLanguagesD)):
        f1(container4, entries4, entries_Text_vars4, addButton4, removeButtons4, supportedLanguagesD[i][0])
    addButton4.grid(row=len(entries4), column=1)
    locationL = Label(editPage, text="Location: ")
    location = cur.execute(f'select location from user where username="{username}"').fetchall()[0][0]
    v7=StringVar(editPage, value=data_from_user_table[-3] if data_from_user_table[-3] != None and data_from_user_table[
        -3] != "" else "")
    locationD = Entry(editPage, textvariable=v7)
    locationL.grid(row=12, column=1)
    locationD.grid(row=12, column=2)
    ccL = Label(editPage, text="Current Company: ")
    v8=StringVar(editPage, value=data_from_user_table[-4] if data_from_user_table[-4] != None and data_from_user_table[
        -4] != "" else "")
    ccD = Entry(editPage, textvariable=v8)
    ccL.grid(row=13, column=1)
    ccD.grid(row=13, column=2)

    submit = Button(editPage, text="Submit",
                    command=lambda: send_edit_to_DB(editPage, username, user_id, v1, v2, v3, v4, v5, v6,v7,v8, v11,
                                                    entries_Text_vars1, entries_Text_vars2, entries_Text_vars3,
                                                    entries_Text_vars4,final))
    submit.grid(row=14, column=1)


def makeNew(i, param, notif_page):
    userName=cur.execute(f'select name from user where user_id="{param[-2]}"').fetchall()[0]
    if param[3]==1:
        Label1 = Label(notif_page, text=f'It\'s {userName}\'s birthday!')
    if param[3]==2:
        Label1 = Label(notif_page, text=f'{userName} saw your profile!')

    Label1.grid(row=i,column=0)





def show_notifs(user_id):
    notif_page=Tk()
    notifs=cur.execute(f'select * from notification where user_idR="{user_id}" and read="{0}"').fetchall()
    labels=[Label(notif_page,text="")]*len(notifs)
    svs=[StringVar(notif_page)]*len(notifs)
    for i in range(len(notifs)):
        makeNew(i,notifs[i],notif_page)
    cur.execute(f'update notification set read="{1}" where user_idR="{user_id}"')
    con.commit()


def addNotif(user_id, param):
    res=cur.execute(f'select notification_id from notification where type=1 and user_idT="{user_id}" and user_idR="{param}"').fetchall()
    if (len(res)==0):
        cur.execute(f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{2}","{user_id}","{param}","{datetime.date.today()}")')
        con.commit()
    else:
        cur.execute(
            f'update notification set read="{0}",date="{datetime.date.today()}" where notification_id="{res[0][0]}"')
        con.commit()



def profile_mainPage(username):
    global numOfNotifs


    data_from_user_table = cur.execute(f'select * from user where username="{username}" ').fetchall()[0]
    user_id = data_from_user_table[0]
    # ui,un
    for user in connection_data(user_id):
        birth_date = cur.execute(f'select * from user where user_id="{user[0]}" ').fetchall()[0]
        if birth_date==datetime.date.today():
            addNotif(user[0],user_id)

    print(len(data_from_user_table))
    print(data_from_user_table)
    mainPage = Tk()
    font = tkinter.font.Font(mainPage, size=40)
    profile = Label(mainPage, text="PROFILE", font=font, bd=4)
    profile.grid(row=0, column=1)
    userName = Label(mainPage, text="Username:", anchor='w')
    usernameD = Label(mainPage, text=data_from_user_table[1])
    userName.grid(row=1, column=1)
    usernameD.grid(row=1, column=2)
    gender = Label(mainPage, text='Gender:\n Birthday:')
    genderTXT = "" if data_from_user_table[2] == None or data_from_user_table[2] == '' else (
        "Female" if data_from_user_table[2] == 1 else "Male")
    genderD = Label(mainPage, text=genderTXT + '\n' + (
        str(data_from_user_table[6]) if data_from_user_table[6] != None and str(data_from_user_table[6]) != ''
        else ""))
    gender.grid(row=2, column=1)
    genderD.grid(row=2, column=2)
    email = Label(mainPage, text='Email:')
    emailD = Label(mainPage, text=data_from_user_table[3])
    email.grid(row=3, column=1)
    emailD.grid(row=3, column=2)
    # pic=Label(mainPage)
    intro = Label(mainPage, text="Introduction:", anchor='w')
    introD = Label(mainPage, text=data_from_user_table[4])
    intro.grid(row=4, column=1)
    introD.grid(row=4, column=2)
    about = Label(mainPage, text="About Me:", anchor='w')
    aboutD = Label(mainPage, text=data_from_user_table[5], anchor='w')
    about.grid(row=5, column=1)
    aboutD.grid(row=5, column=2)
    featured = Label(mainPage, text="Featured:", anchor='w')
    featuredDs = cur.execute(f'select content from feature where (user_id= "{user_id}" )').fetchall()
    featureTXT = ""
    for i in range(len(featuredDs)):
        featureTXT += featuredDs[i][0] + (', ' if i != len(featuredDs) - 1 else '.')
    featuredD = Label(mainPage, text=featureTXT)
    featuredD.grid(row=6, column=2)
    featured.grid(row=6, column=1)
    highSchool = cur.execute(
        f'select location,field from background where user_id= "{user_id}" and type="h"  ').fetchall()
    bgTXT_highschool = ("High school at: " + highSchool[0][0] + " in " + highSchool[0][1] + "\n") if len(
        highSchool) > 0 else ""
    bachlor = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="b"  ').fetchall()
    bgTXT_bachlors = "Bachlor degrees:\n" if len(bachlor) > 0 else ""
    for degree in bachlor:
        bgTXT_bachlors += "\t from " + degree[0] + " in " + degree[1] + " from " + str(degree[2]) + " to " + (
            str(degree[3]) if degree[3] != None else 'now') + "\n"
    print(bgTXT_bachlors)
    master = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="m"  ').fetchall()
    bgTXT_master = "Master degrees:\n" if len(master) > 0 else ""
    for degree in master:
        print(degree)
        bgTXT_master += "\t from " + degree[0] + " in " + degree[1] + " from " + str(degree[2]) + " to " + (
            str(degree[3]) if degree[3] != None else 'now') + "\n"
    PHD = cur.execute(
        f'select location,field,f,t from background where user_id= "{user_id}" and type="p"  ').fetchall()
    bgTXT_PHD = "PHD degrees:\n" if len(PHD) > 0 else ""
    for degree in PHD:
        bgTXT_PHD += "\t from " + degree[0] + " in " + degree[1] + " from " + str(degree[2]) + " to " + (
            str(degree[3]) if degree[3] != None else 'now') + "\n"
    jobs = cur.execute(f'select location,f,t from background where user_id= "{user_id}" and type="j"  ').fetchall()
    bgTXT_jobs = "Working in:\n" if len(PHD) > 0 else ""
    for job in jobs:
        bgTXT_jobs += job[0] + " from " + str(job[1]) + " to " + (str(job[2]) if job[2] != None else 'now')
    background = Label(mainPage, text="Background", anchor='w')
    backgroundD = Label(mainPage,
                        text=bgTXT_highschool + bgTXT_bachlors + bgTXT_master + bgTXT_PHD + bgTXT_jobs,
                        anchor='w')
    background.grid(row=5, column=1)
    backgroundD.grid(row=5, column=2)
    skillDs = cur.execute(f'select content from skill where (user_id= "{user_id}" )').fetchall()
    skillTXT = ""
    for i in range(len(skillDs)):
        skillTXT += skillDs[i][0] + (', ' if i != len(skillDs) - 1 else '.')
    skills = Label(mainPage, text="Skills:")
    skills.grid(row=7, column=1)
    skillD = Label(mainPage, text=skillTXT)
    skillD.grid(row=7, column=2)
    accomplishmentD = cur.execute(f'select content from accomplishment where user_id= "{user_id}"').fetchall()
    accomplishmentTXT = ""
    for i in range(len(accomplishmentD)):
        accomplishmentTXT += accomplishmentD[i][0] + (', ' if i != len(accomplishmentD) - 1 else '.')
    accomplishments = Label(mainPage, text="Accomplishments:", anchor='w')
    accomplishments.grid(row=8, column=1)
    accomplishmentDs = Label(mainPage, text=accomplishmentTXT)
    accomplishmentDs.grid(row=8, column=2)
    # additionalInfo=Label(mainPage,text="Additional Information:", anchor='w')
    # additionalInfo.grid(row=9,column=1)
    # additionalInfoTXT=str(cur.execute(f'select additionalInfo from user where user_id="{username}"').fetchall()[0][0])
    # print(additionalInfoTXT)
    # print(str(additionalInfoTXT))
    # additionalInfoD=Label(mainPage,text="" if str(additionalInfoTXT)=='None' else additionalInfoTXT)
    # additionalInfoD.grid(row=9,column=2)
    supportedLanguages = Label(mainPage, text="Supported Languages:", anchor='w')
    supportedLanguages.grid(row=10, column=1)
    supportedLanguagesD = cur.execute(f'select content from language where user_id= "{user_id}"').fetchall()
    supportedLanguagesTXT = ""
    for i in range(len(supportedLanguagesD)):
        supportedLanguagesTXT += supportedLanguagesD[i][0] + (', ' if i != len(supportedLanguagesD) else '.')
    supportedLanguagesDs = Label(mainPage, text=supportedLanguagesTXT)
    supportedLanguagesDs.grid(row=10, column=2)
    locationL=Label(mainPage,text="Location: ")
    location=cur.execute(f'select location from user where username="{username}"').fetchall()[0][0]
    locationD=Label(mainPage,text=location)
    locationL.grid(row=11,column=1)
    locationD.grid(row=11,column=2)
    ccL=Label(mainPage,text="Current Company: ")
    cc=cur.execute(f'select company from user where username="{username}"').fetchall()[0][0]
    ccD=Label(mainPage,text=cc)
    ccL.grid(row=12,column=1)
    ccD.grid(row=12,column=2)

    refresh = Button(mainPage, text="Refresh")
    edit = Button(mainPage, text="Edit Info", command=lambda: editInfo(mainPage, username))
    numOfNotifs = len(cur.execute(f'select * from notification where user_idR="{user_id}" and read="{0}"').fetchall())
    notifs = Button(mainPage, text=("There isn't any new notif." if numOfNotifs == 0 else f'{numOfNotifs} new notif{"s" if numOfNotifs>1 else""}!'),command=lambda :show_notifs(user_id))
    refresh.grid(row=13, column=1)
    edit.grid(row=13, column=2)
    notifs.grid(row=13, column=3)

    mainPage.mainloop()
