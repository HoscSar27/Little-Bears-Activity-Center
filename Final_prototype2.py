from tkinter import *

#create window
my_window = Tk()

#attributes of main window
my_window.geometry("800x650")
my_window.title("Little Bears Activity Center")
my_window['background']='#6b339c' #make it purple!!!!!!!

#create page tittle and logo
page_title = Label(my_window, text = "Little Bears Activity Center", font = ("Papyrus", 25), bg = '#6b339c', fg = '#ffffff')
page_title.grid(row= 0, column = 1, columnspan = 2)

global logo_image
logo_image = PhotoImage(file = "panda_logo.png")
logo_label = Label(my_window, image=logo_image, text = "cartoon panda") # image and alternate text
logo_label.grid(row=0, column=3, columnspan = 2)


#define age Groups
group1_label = Label( text= "Ages 3-6", font = ("Copperplate", 15), bg = '#6b339c', fg = '#ffffff')
group2_label = Label( text= "Ages 7-13", font = ("Copperplate", 15), bg = '#6b339c', fg = '#ffffff')
group3_label = Label( text= "Teens", font = ("Copperplate", 15), bg = '#6b339c', fg = '#ffffff')

group1_label.grid(row= 3, column= 0, sticky = W)
group2_label.grid(row= 8, column= 0, sticky = W)
group3_label.grid(row= 14, column= 0, sticky = W)

#descriptions of classes for ages 3-6 pops up when classes are clicked, sign up button appears next to each description
def danceDesc1():
    description1= Label(my_window, text= "A place for little movers to come learn simple dance routines to some of our favorite songs! Price per class: $20", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description1.grid(row= 4, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=4, column= 3)

def karateDesc1():
    description2= Label(my_window, text= "Make friends and begin learning karate. Sign up fee includes uniform: $35 Price per class: $20", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description2.grid(row= 5, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=5, column= 3)

def artDesc1():
    description3= Label(my_window, text= "Different crafts planned everyday! Supplies are provided and children get to take home what they make! Price per class: $20", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description3.grid(row= 6, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=6, column= 3)

#descriptions for classes ages 7-13 and sign up buttons
def danceDesc2():
    description4= Label(my_window, text= "We offer classes in choreographed dance or ballet. Price per group lesson: $20, one time sign up fee: $45(includes shirt)", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description4.grid(row= 10, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=10, column= 3)

def karateDesc2():
    description5= Label(my_window, text= "Make friends and sharpen your skills in karate and lifelong leadership skills. Sign up fee includes uniform: $35, Price per class: $20", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description5.grid(row= 11, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=11, column= 3)

def artDesc2():
    description6= Label(my_window, text= "Take a class in acrylic watercolor or oil painting, or take a class in potery/clay making. Suplies are provided and take home what you make. Price per class: $30", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description6.grid(row= 12, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=12, column= 3)

#description for teen classes and sign up buttons 
def danceDesc3():
    description7= Label(my_window, text= "We offer classes in choreographed dance or ballet. Price per group lesson: $20, one time sign up fee: $45(includes shirt)", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description7.grid(row= 16, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=16, column= 3)

def karateDesc3():
    description5= Label(my_window, text= "Make friends and sharpen your skills in karate and lifelong leadership skills. Sign up fee includes uniform: $35, Price per class: $20", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description5.grid(row= 17, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=17, column= 3)

def artDesc3():
    description6= Label(my_window, text= "Take a class in acrylic watercolor or oil painting, or take a class in potery/clay making. Suplies are provided and take home what you make. Price per class: $30", wraplength = 350, bg = '#6b339c', fg = '#ffffff')
    description6.grid(row= 18, column= 2)

    signup_button= Button(my_window, text= "Sign Up!", command = signUp, bg = '#ffffff')
    signup_button.grid(row=18, column= 3)


#Sign up window for sign up button command 
def signUp():
    signUp_window = Toplevel()
    signUp_window.title("Little Bears Activity Center/Sign up")
    signUp_window.geometry("300x300")
    signUp_window['background']= "#16a836" #make it green!!!!

    #create labels for entry boxes
    name_label = Label(signUp_window,
                       text = "Name: ",
                       justify = "left",
                       font = ("Copperplate", 12),
                       bg = "#16a836"
    )
    phone_label = Label(signUp_window,
                       text = "Phone Number: ",
                         justify = "left",
                       font = ("Copperplate", 12),
                        bg = "#16a836"
    )
    adress_label = Label(signUp_window,
                       text = "Adress: ",
                       justify = "left",
                       font = ("Copperplate", 12),
                        bg = "#16a836"
    )
    email_label = Label(signUp_window,
                       text = "Email: ",
                       justify = "left",
                       font = ("Copperplate", 12),
                        bg = "#16a836"
    )

    #entry boxes
    name_entry = Entry(signUp_window)
    phone_entry = Entry(signUp_window)
    adress_entry = Entry(signUp_window)
    email_entry = Entry(signUp_window)

    #drop down box
    clicked = StringVar()
    clicked.set("Choose Class")
    classChoice = OptionMenu(signUp_window, clicked, "Choose Class", "Little Dancers(3-6)", "TinyTigers Karate(3-6)", "Arts and Crafts(3-6)", "Dance(7-13),", "Ballet(7-13)", "Karate(7-13)", "Acrylic Painting(7-13)",
                             "Watercolor Painting(7-13)", "Oil Painting(7-13)", "Pottery/Claymaking(7-13)", "Dance(Teens),", "Ballet(Teens)", "Karate(Teens)", "Acrylic Painting(Teens)", "Watercolor Painting(Teens)",
                             "Oil Painting(Teens)", "Pottery/Claymaking(Teens)")
    
    #submit button/ entry validation, ensures each entry box has an entry
    def submitButt():
        if name_entry.get() == "":
            errorMess_label=Label(signUp_window, text = "Please enter a Name")
            errorMess_label.grid(row = 11, column = 1, columnspan = 2)
        elif phone_entry.get() == "":
            errorMess_label=Label(signUp_window, text = "Please enter a valid Phone Number")
            errorMess_label.grid(row = 11, column = 1, columnspan = 2)
        elif adress_entry.get == "":
            errorMess_label=Label(signUp_window, text = "Please enter an Address")
            errorMess_label.grid(row = 11, column = 1, columnspan = 2)
        elif email_entry.get() == "":
            errorMess_label=Label(signUp_window, text = "Please enter a valid email")
            errorMess_label.grid(row = 11, column = 1, columnspan = 2)
        else:
            submitMess_label= Label(signUp_window, text = "Thank you for signing up, an email has been sent to the address provided with further information and class times.", wraplength = 250, bg = "#16a836")
            submitMess_label.grid(row = 11, column = 1, columnspan = 2)
            global signup_image
            signup_image = PhotoImage(file = "thumbsup.png")
            signup_label = Label(signUp_window, image=signup_image, text = "thumbs up") #image and alternate text
            signup_label.grid(row=12, column=2,)

    #cancel button and submit button creation
    cancel_button = Button(signUp_window, text = "Cancel", command= signUp_window.destroy, bg = "black", fg = "white")
    submit_button = Button(signUp_window, text = "Submit", command = submitButt, bg = "black", fg = "white")  
    
    #throw everything in there, nicely 
    name_label.grid(row = 1, column = 1)
    phone_label.grid(row = 2, column = 1)
    adress_label.grid(row = 3, column = 1)
    email_label.grid(row = 4, column = 1)
    name_entry.grid(row = 1, column = 2, columnspan = 2)
    phone_entry.grid(row = 2, column = 2, columnspan = 2)
    adress_entry.grid(row = 3, column = 2, columnspan = 2)
    email_entry.grid(row = 4, column = 2, columnspan = 2)
    classChoice.grid(row = 6, column = 2)
    cancel_button.grid(row = 10, column = 1)
    submit_button.grid(row = 10, column = 2)
    

#Age Group Class Options - create, configure, and place
    
#ages 3-6
options1_a_button= Button(my_window, #dance class goes with danceDesc1
                          text= "- Little Dancers",
                          command = danceDesc1,
                          bd = 0,
                          justify = "left",
                          padx = 0,
                          pady= 10,
                          font = ("Copperplate", 12),
                          bg = '#8e339c', #light purple!!!!!!! (different to give a hint to the user that it clicks)
                          fg = '#ffffff'
)
options1_b_button = Button(my_window,
                           text= "- Tiny Tigers Karate", #karate goes with karateDisc1
                           command = karateDesc1,
                           bd = 0,
                           justify = "left",
                           padx = 0,
                           pady = 10,
                           font = ("Copperplate", 12),
                           bg = '#8e339c',
                          fg = '#ffffff'
)
options1_c_button = Button(my_window,
                           text= "- Arts and Crafts", #artDesc1
                           command= artDesc1,
                           bd = 0,
                           justify = "left",
                           padx = 0,
                           pady = 10,
                           font = ("Copperplate", 12),
                           bg = '#8e339c',
                          fg = '#ffffff'
)

options1_a_button.grid(row= 4, column= 1, sticky = W)
options1_b_button.grid(row= 5, column= 1, sticky = W)
options1_c_button.grid(row= 6, column= 1, sticky = W)

#ages 7-13
options2_a_button= Button(my_window,
                          text= "- Dance or Ballet", #danceDesc2
                          command = danceDesc2,
                          bd = 0,
                          justify = "left",
                          padx = 0,
                          pady = 10,
                          font = ("Copperplate", 12),
                          bg = '#8e339c',
                          fg = '#ffffff'
)
options2_b_button = Button(my_window,
                           text= "- Karate and Leadership", #karateDesc2
                           command = karateDesc2,
                           bd = 0,
                           justify = "left",
                           padx = 0,
                           pady = 10,
                           font = ("Copperplate", 12),
                           bg = '#8e339c',
                          fg = '#ffffff'
)
options2_c_button = Button(my_window,
                           text= "- Painting/Clay works", #artDesc2
                           command = artDesc2,
                           bd = 0,
                           justify = "left",
                           padx = 0,
                           pady = 10,
                           font = ("Copperplate", 12),
                           bg = '#8e339c',
                          fg = '#ffffff'
)

options2_a_button.grid(row= 10, column= 1, sticky = W)
options2_b_button.grid(row= 11, column= 1, sticky = W)
options2_c_button.grid(row= 12, column= 1, sticky = W)

#teens
options3_a_button= Button(my_window,
                          text= "- Dance or Ballet", #danceDesc3
                          command = danceDesc3,
                          bd = 0, justify = "left",
                          padx = 0,
                          pady = 10,
                          font = ("Copperplate", 12),
                          bg = '#8e339c',
                          fg = '#ffffff'
)
options3_b_button = Button(my_window,
                           text= "- Karate Warriors", #karateDesc3
                           command = karateDesc3, 
                           bd = 0,
                           justify = "left",
                           padx = 0,
                           pady = 10,
                           font = ("Copperplate", 12),
                           bg = '#8e339c',
                          fg = '#ffffff'
)
options3_c_button = Button(my_window,
                           text= "- Drawing/Painting/Pottery", #artDesc3
                           command = artDesc3,
                           bd = 0,
                           justify = "left",
                           padx = 0,
                           pady = 10,
                           font = ("Copperplate", 12),
                           bg = '#8e339c',
                          fg = '#ffffff'
)

options3_a_button.grid(row= 16, column= 1, sticky = W) 
options3_b_button.grid(row= 17, column= 1, sticky = W)
options3_c_button.grid(row= 18, column= 1, sticky = W)

#close page button
close_button = Button(my_window, text = "Close", command= my_window.destroy, bg = "black", fg = "white", width = 15) #made it black to stand out and blend better with the page 
close_button.grid(row= 20, column = 3, sticky = E)

#initiate main loop
my_window.mainloop()
