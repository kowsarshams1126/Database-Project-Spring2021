import sqlite3
import datetime
from tkinter import *
import tkinter.font
from network_query import find_mutual_connection,connection_data

con = sqlite3.connect('linkedin_db.db')
cur = con.cursor()



def do_invitation(param, user_id):
    res = cur.execute(
        f'select notification_id from notification where type=2 and user_idT="{user_id}" and user_idR="{param}"').fetchall()
    if len(res) == 0:
        cur.execute(
            f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{2}","{user_id}","{param}","{datetime.date.today()}")')
        con.commit()
    else:
        cur.execute(
            f'update notification set read="{0}",date="{datetime.date.today()}" where notification_id="{res[0][0]}"')
        con.commit()


def filter_it(sp,user_id, name, param, param1,viewName,x):
    print(name)
    print(param)
    print(param1)
    sp.destroy()
    search(user_id,name,param,param1,"",0)


def addNotif(user_id, param):
    res=cur.execute(f'select notification_id from notification where type=2 and user_idT="{user_id}" and user_idR="{param}"').fetchall()
    if (len(res)==0):
        cur.execute(f'insert into notification(read,type,user_idT,user_idR,date) values ("{0}","{2}","{user_id}","{param}","{datetime.date.today()}")')
        con.commit()
    else:
        cur.execute(
            f'update notification set read="{0}",date="{datetime.date.today()}" where notification_id="{res[0][0]}"')
        con.commit()





def view_profile(caller_id,user_id, param):
    addNotif(user_id,param)
    print(user_id)
    data_from_user_table = cur.execute(f'select * from user where user_id="{user_id}" ').fetchall()[0]
    user_id = data_from_user_table[0]
    # print(len(data_from_user_table))
    # print(data_from_user_table)
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
    invite = Button(mainPage, text="Invite", command=lambda: do_invitation(caller_id, user_id))
    invite.grid(row=13, column=1)
    in_connection=connection_data(user_id)

    for data in in_connection:
        if data[0]==caller_id:
            invite.grid_forget()



def do_it(caller_id,cont,user,user_id,i):


    userName=Label(cont,text=user[1])
    seeB=Button(cont,text="View Profile.",command=lambda: view_profile(caller_id,user_id,user[0]))
    userName.grid(row=0,column=1)
    seeB.grid(row=0,column=2)
    cont.grid(row=i,column=1)


def search(user_id,name,location,cc,viewName,x):
    if x==0:

        # print(f'user_id:{user_id}')
        # print(f'name={name}')
        # print(f'location={location}')
        # print(f'cc={cc}')
        search_page=Tk()
        if (location=="" or location==None):
            if(cc=="" or cc== None):
                searchRes = cur.execute(
                    f'select * from user where username like "%{name}%" and user_id!="{user_id}" ').fetchall()
                cur.execute(
                    f'create view IF NOT EXISTS v0 as select * from user where username like "%{name}%"  and user_id!="{user_id}"')
            else:
                # print("HI")
                searchRes = cur.execute(
                    f'select * from user where username like "%{name}%"  and company like  "%{cc}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f' create view IF NOT EXISTS v0 as select * from user where username like "%{name}%"  and company like  "%{cc}%"  and user_id!="{user_id}"')
        else:
            if(cc=="" or cc==None):
                searchRes = cur.execute(
                    f'select * from user where username like "%{name}%" and location like "%{location}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f'create view IF NOT EXISTS v0 as select * from user where username like "%{name}%" and location like "%{location}%"  and user_id!="{user_id}"')
            else:
                searchRes = cur.execute(
                    f'select * from user where username like "%{name}%" and location like "%{location}%" and company like  "%{cc}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f'create view IF NOT EXISTS v0 as select * from user where username like "%{name}%" and location like "%{location}%" and company like  "%{cc}%"  and user_id!="{user_id}"')

        print(searchRes)
        x+=1


        cont1=LabelFrame(search_page,text="filter")
        l1=Label(cont1,text="Location: ")
        l2=Label(cont1,text="Current Company: ")
        sv1=StringVar(cont1)
        sv2=StringVar(cont1)
        e1=Entry(cont1,textvariable=sv1)
        e2=Entry(cont1,textvariable=sv2)
        cont1.grid(row=0,column=1)
        l1.grid(row=0,column=1)
        l2.grid(row=1,column=1)
        e1.grid(row=0,column=2)
        e2.grid(row=1,column=2)
        i=0
        listOfUsers=[]
        cur.execute('drop table if exists temp;')
        con.commit()

        cur.execute(f'''create table temp  (user_id integer NOT NULL,
                                            name VARCHAR(100) NOT NULL,
                                            ME_num integer NOT NULL,
                                            PRIMARY KEY (user_id));''')
        con.commit()


        for user in searchRes:
            cur.execute(f'insert into temp(user_id,ME_num,name) values ("{user[0]}","{find_mutual_connection(user_id,user[0])}","{user[1]}")')
        con.commit()
        searchRes=cur.execute(f'select * from temp order by ME_num').fetchall()
        cur.execute('drop table if exists temp;')
        con.commit()


        for user in searchRes:
            print(user)

            i+=1
            cont=LabelFrame(search_page)
            do_it(user_id,cont,user,user_id,i)

        filterB=Button(cont1,text="Filter",command=lambda :filter_it(search_page,user_id,name,sv1.get(),sv2.get(),"v"+str(x-1),x))
        filterB.grid(row=3,column=1)
        search_page.mainloop()
    else:

        print(cur.execute(f'select * from {viewName}').fetchall())

        # print(f'user_id:{user_id}')
        # print(f'name={name}')
        # print(f'location={location}')
        # print(f'cc={cc}')
        # print(f'vn={viewName}')
        # print(f'x={x}')
        search_page=Tk()
        if (location=="" or location==None):
            if(cc=="" or cc== None):
                searchRes = cur.execute(
                    f'select * from {viewName} where username like "%{name}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f'create view IF NOT EXISTS v{x} as select * from {viewName} where username like "%{name}%"  and user_id!="{user_id}"')
            else:
                # print("HI")
                # print(cur.execute(f'select * from {viewName}').fetchall())
                searchRes = cur.execute(
                    f'select * from {viewName} where username like "%{name}%"  and company like  "%{cc}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f' create view IF NOT EXISTS v{x} as select * from {viewName} where username like "%{name}%"  and company like  "%{cc}%"  and user_id!="{user_id}"')
        else:
            if(cc=="" or cc==None):
                searchRes = cur.execute(
                    f'select * from {viewName} where username like "%{name}%" and location like "%{location}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f'create view IF NOT EXISTS v{x} as select * from {viewName} where username like "%{name}%" and location like "%{location}%"  and user_id!="{user_id}"')
                # print(cur.execute(f'select * from {viewName}').fetchall())

            else:
                searchRes = cur.execute(
                    f'select * from {viewName} where username like "%{name}%" and location like "%{location}%" and company like  "%{cc}%"  and user_id!="{user_id}"').fetchall()
                cur.execute(
                    f'create view IF NOT EXISTS v{x} as select * from {viewName} where username like "%{name}%" and location like "%{location}%" and company like  "%{cc}%"  and user_id!="{user_id}"')

        print(searchRes)
        x+=1
        cont1=LabelFrame(search_page,text="filter")
        l1=Label(cont1,text="Location: ")
        l2=Label(cont1,text="Current Company: ")
        sv1=StringVar(cont1)
        sv2=StringVar(cont1)
        e1=Entry(cont1,textvariable=sv1)
        e2=Entry(cont1,textvariable=sv2)
        cont1.grid(row=0,column=1)
        l1.grid(row=0,column=1)
        l2.grid(row=1,column=1)
        e1.grid(row=0,column=2)
        e2.grid(row=1,column=2)
        i=0
        for user in searchRes:
            i+=1
            cont=LabelFrame(search_page)
            do_it(user_id,cont,user,user_id,i)

        filterB=Button(cont1,text="Filter",command=lambda :filter_it(search_page,user_id,name,sv1.get(),sv2.get(),"v"+str(x-1),x))
        filterB.grid(row=3,column=1)
        search_page.mainloop()



    
