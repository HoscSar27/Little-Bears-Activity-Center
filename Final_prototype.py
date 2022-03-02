import tkinter as tk
window = tk.Tk()
#create
title_frame = tk.Frame()
page_title = tk.Label(master = title_frame,
                      text = "Little Bears Activity Center")
#pack
title_frame.grid(row=0, column=2)
page_title.grid(row=0, column=2)


#creating the lists I want for now, format them later
list_1_frame = tk.Frame()
list_1_frame.grid(row=2, column= 0)

agegroup_1 = tk.Label(master = list_1_frame,
                      text = "Ages 3 to 6",
                      fg = "blue"
)
agegroup_2 = tk.Label(master = list_1_frame,
                      text = "Ages 7 to 13",
                      fg = "blue"
)
agegroup_3 = tk.Label(master = list_1_frame,
                      text = "Teens",
                      fg = "blue"
)

agegroup_1.grid(row=2, column= 0)
agegroup_2.grid(row=3, column= 0)
agegroup_3.grid(row=4, column= 0)


tk.Button(text = "Quit", command = window.destroy)
tk.Button.grid(row=5, column= 3)

window.mainloop()
