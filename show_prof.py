import sqlite3
import datetime
from functools import partial
from tkinter import *
import tkinter.font
import tkinter as tk


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


def insert_like_post(args):
    pass
def comment_page(args):
    pass


def profile_mainPage(caller_user_id, username):
    global numOfNotifs

    data_from_user_table = cur.execute(f'select * from user where username="{username}" ').fetchall()[0]
    user_id = data_from_user_table[0]
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
    featuredDs = cur.execute(f'select * from post where post_id in (select post_id from feature where (user_id= "{user_id}" ))').fetchall()
    print(featuredDs)
    featureTXT = ""
    lf1=LabelFrame(mainPage)
    for item in featuredDs:

        tk.Label(lf1, text=item[1]).pack()
        tk.Label(lf1, text=item[2]).pack()
        tk.Label(lf1, text=item[3]).pack()
        tk.Button(lf1, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(lf1, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        # tk.Button(lf1, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(lf1, text="--------------------------------------").pack()
    lf1.grid(row=6, column=2)
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
    locationL = Label(mainPage, text="Location: ")
    location = cur.execute(f'select location from user where username="{username}"').fetchall()[0][0]
    locationD = Label(mainPage, text=location)
    locationL.grid(row=11, column=1)
    locationD.grid(row=11, column=2)
    ccL = Label(mainPage, text="Current Company: ")
    cc = cur.execute(f'select company from user where username="{username}"').fetchall()[0][0]
    ccD = Label(mainPage, text=cc)
    ccL.grid(row=12, column=1)
    ccD.grid(row=12, column=2)
    invite = Button(mainPage, text="Invite", command=lambda: do_invitation(caller_user_id, user_id))
    invite.grid(row=13, column=1)


    mainPage.geometry('400x400')
    mainPage.mainloop()
