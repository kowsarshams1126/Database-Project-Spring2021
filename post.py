import tkinter as tk
from functools import partial
from post_query import *
from create_post import create_post


#################################################################################################

def comment_page(user_id,post_id):
    pass

#################################################################################################

def insert_share_post_page(user_id,post_id):
    pass

#################################################################################################
def my_post(user_id):
    #get data
    posts=get_my_post_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("YOUR POSTS")
    
    for item in posts:
        tk.Label(window, text=get_username(item[1])[0][0]).pack()
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[3]).pack()
        
        tk.Label(window, text="number of like:").pack()
        tk.Label(window, text=get_number_of_like(item[0])).pack()
        tk.Label(window, text="number of comments:").pack()
        tk.Label(window, text=get_number_of_comment(item[0])).pack()
        
        tk.Button(window, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(window, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        tk.Button(window, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()

    tk.Button(window, text="new post",command=partial(create_post,user_id)).pack()

    window.geometry('400x400')
    window.mainloop()


def my_share_post(user_id):
    #get data
    posts=get_my_shared_post_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("YOUR SHARED POSTS")

    for item in posts:
        tk.Label(window, text="post:").pack()
        tk.Label(window, text=get_username(item[1])[0][0]).pack()
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[3]).pack()
        
        tk.Label(window, text="number of like:").pack()
        tk.Label(window, text=get_number_of_like(item[0])).pack()
        tk.Label(window, text="number of comments:").pack()
        tk.Label(window, text=get_number_of_comment(item[0])).pack()
        
        tk.Label(window, text="share post:").pack()
        tk.Label(window, text=get_username(item[4])[0][0]).pack()
        tk.Label(window, text=item[5]).pack()
        tk.Label(window, text=item[6]).pack()
        
        tk.Button(window, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(window, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        tk.Button(window, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()

    window.geometry('400x400')
    window.mainloop()
    
def network_create_post_page(user_id):
    #get data
    posts=network_create_post_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("POST OF PEOPLE IN YOUR NETWORK")
    for item in posts:
        tk.Label(window, text=get_username(item[1])[0][0]).pack()
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[3]).pack()

        tk.Label(window, text="number of like:").pack()
        tk.Label(window, text=get_number_of_like(item[0])).pack()
        tk.Label(window, text="number of comments:").pack()
        tk.Label(window, text=get_number_of_comment(item[0])).pack()
        
        tk.Button(window, text="share",command=partial(insert_share_post_page,user_id,item[0])).pack()
        tk.Button(window, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(window, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        tk.Button(window, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()

    window.geometry('400x400')
    window.mainloop()


def network_shared_post_page(user_id):
    #get data
    posts=network_shared_post_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("YOUR NETWORK SHARED POSTS")

    for item in posts:
        tk.Label(window, text="post:").pack()
        tk.Label(window, text=get_username(item[1])[0][0]).pack()
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[3]).pack()

        tk.Label(window, text="number of like:").pack()
        tk.Label(window, text=get_number_of_like(item[0])).pack()
        tk.Label(window, text="number of comments:").pack()
        tk.Label(window, text=get_number_of_comment(item[0])).pack()
        
        tk.Label(window, text="share post:").pack()
        tk.Label(window, text=get_username(item[4])[0][0]).pack()
        tk.Label(window, text=item[5]).pack()
        tk.Label(window, text=item[6]).pack()
        
        tk.Button(window, text="share",command=partial(insert_share_post_page,user_id,item[0])).pack()
        tk.Button(window, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(window, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        tk.Button(window, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()

    window.geometry('400x400')
    window.mainloop()


def network_like_post_page(user_id):
    #get data
    posts=network_like_post_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("NETWORK LIKE POST")
    
    for item in posts:
        tk.Label(window, text=get_username(item[1])[0][0]).pack()
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[3]).pack()
        
        tk.Label(window, text="number of like:").pack()
        tk.Label(window, text=get_number_of_like(item[0])).pack()
        tk.Label(window, text="number of comments:").pack()
        tk.Label(window, text=get_number_of_comment(item[0])).pack()
        
        tk.Button(window, text="share",command=partial(insert_share_post_page,user_id,item[0])).pack()
        tk.Button(window, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(window, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        tk.Button(window, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()

    window.geometry('400x400')
    window.mainloop()


def network_comment_post_page(user_id):
    #get data
    posts=network_comment_post_data(user_id)
    #tk view
    window = tk.Tk()
    window.title("NETWORK COMMENT POST")
    for item in posts:
        tk.Label(window, text=get_username(item[1])[0][0]).pack()
        tk.Label(window, text=item[2]).pack()
        tk.Label(window, text=item[3]).pack()

        tk.Label(window, text="number of like:").pack()
        tk.Label(window, text=get_number_of_like(item[0])).pack()
        tk.Label(window, text="number of comments:").pack()
        tk.Label(window, text=get_number_of_comment(item[0])).pack()
        
        tk.Button(window, text="share",command=partial(insert_share_post_page,user_id,item[0])).pack()
        tk.Button(window, text="like",command=partial(insert_like_post,user_id,item[0])).pack()
        tk.Button(window, text="comment",command=partial(comment_page,user_id,item[0])).pack()
        tk.Button(window, text="add feature",command=partial(comment_page,user_id,item[0])).pack()
        tk.Label(window, text="--------------------------------------").pack()

    window.geometry('400x400')
    window.mainloop()

#################################################################################################

def post_page(user_id):
    
    window = tk.Tk()
    window.title("POST")
    
    tk.Button(window, text="your post",command=partial(my_post,user_id)).pack()
    tk.Button(window, text="shared post",command=partial(my_share_post,user_id)).pack()
    tk.Button(window, text="network_shared_post",command=partial(network_shared_post_page,user_id)).pack()
    tk.Button(window, text="network_create_post",command=partial(network_create_post_page,user_id)).pack()
    tk.Button(window, text="network_like_post",command=partial(network_like_post_page,user_id)).pack()
    tk.Button(window, text="network_comment_post",command=partial(network_comment_post_page,user_id)).pack()
    
    window.geometry('400x400')
    window.mainloop()
#################################################################################################

# def main():
#     post_page(1)
# main()
