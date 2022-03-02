from tkinter import*

my_window = Tk()

page_tittle = Label(my_window, text = "Little Bears Activity Center")
page_tittle.grid(row= 0, column= 1)
#Age Groups
group1_label = Label( text= "Ages 3-6")
group2_label = Label( text= "Ages 7-13")
group3_label = Label( text= "Teens")

group1_label.grid(row= 3, column= 0)
group2_label.grid(row= 8, column= 0)
group3_label.grid(row= 14, column= 0)

#descriptions for ages 3-6
def danceDesc1():
    description1= Label(my_window, text= "A place for little movers to come learn simple dance routines to some of our favorite songs! Price per class: $20")
    description1.grid(row= 4, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=4, column= 3)

def karateDesc1():
    description2= Label(my_window, text= "Make friends and begin learning karate. Sign up fee includes uniform: $35 Price per class: $20")
    description2.grid(row= 5, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=5, column= 3)

def artDesc1():
    description3= Label(my_window, text= "Different crafts planned everyday! Supplies are provided and children get to take home what they make! Price per class: $20")
    description3.grid(row= 6, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=6, column= 3)

#descriptions for ages 7-13
def danceDesc2():
    description4= Label(my_window, text= "We offer classes in choreographed dance or ballet. Price per group lesson: $20, one time sign up fee: $45(includes shirt)")
    description4.grid(row= 10, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=10, column= 3)

def karateDesc2():
    description5= Label(my_window, text= "Make friends and sharpen your skills in karate and lifelong leadership skills. Sign up fee includes uniform: $35, Price per class: $20")
    description5.grid(row= 11, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=11, column= 3)

def artDesc2():
    description6= Label(my_window, text= "Take a class in acrylic watercolor or oil painting, or take a class in potery/clay making. Suplies are provided and take home what you make. Price per class: $30")
    description6.grid(row= 12, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=12, column= 3)

#description for teen classes

def danceDesc3():
    description7= Label(my_window, text= "We offer classes in choreographed dance or ballet. Price per group lesson: $20, one time sign up fee: $45(includes shirt)")
    description7.grid(row= 16, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=16, column= 3)

def karateDesc3():
    description5= Label(my_window, text= "Make friends and sharpen your skills in karate and lifelong leadership skills. Sign up fee includes uniform: $35, Price per class: $20")
    description5.grid(row= 17, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=17, column= 3)

def artDesc3():
    description6= Label(my_window, text= "Take a class in acrylic watercolor or oil painting, or take a class in potery/clay making. Suplies are provided and take home what you make. Price per class: $30")
    description6.grid(row= 18, column= 2)

    signup_button= Button(my_window, text= "Sign Up!")
    signup_button.grid(row=18, column= 3)

#create info in age categories
#ages 3-6
options1_a_button= Button(my_window, text= "- Little Dancers", command = danceDesc1)
options1_b_button = Button(my_window, text= "- Tiny Tigers Karate", command = karateDesc1)
options1_c_button = Button(my_window, text= "- Arts and Crafts", command= artDesc1 )

options1_a_button.grid(row= 4, column= 1)
options1_b_button.grid(row= 5, column= 1)
options1_c_button.grid(row= 6, column= 1)

#ages 7-13
options2_a_button= Button(my_window, text= "- Dance or Ballet", command = danceDesc2)
options2_b_button = Button(my_window, text= "- Karate and Leadership", command = karateDesc2)
options2_c_button = Button(my_window, text= "- Painting/Clay works", command = artDesc2)

options2_a_button.grid(row= 10, column= 1)
options2_b_button.grid(row= 11, column= 1)
options2_c_button.grid(row= 12, column= 1)

#teens
options3_a_button= Button(my_window, text= "- Dance or Ballet", command = danceDesc3)
options3_b_button = Button(my_window, text= "- Karate Worriors", command = karateDesc3)
options3_c_button = Button(my_window, text= "- Drawing/Painting/Pottery", command = artDesc3)

options3_a_button.grid(row= 16, column= 1)
options3_b_button.grid(row= 17, column= 1)
options3_c_button.grid(row= 18, column= 1)

my_window.mainloop()
