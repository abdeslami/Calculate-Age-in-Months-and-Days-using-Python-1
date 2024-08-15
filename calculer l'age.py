from tkinter import *
from tkinter import messagebox
#create the main app window

age_app= Tk()

#change app Text 
age_app.title('Calculatrise')#titre od app
#set Dimensions"width=400 and height=200"
age_app.geometry("400x200")
#Write Age Label
the_input=Label(age_app,text="Write Your Age",height=2,font=("Arial",20),fg="red")#label fg=text color
the_input.pack()#append label
#create the Input For Age
age=StringVar()
#set default values
age.set("00")
age_input =Entry(age_app,width=77,font=('Arial',30),textvariable=age)#create input
age_input.pack()#append input
def cal():
    #Get Age In Years 
    the_age_value=age.get()
    #Get time 
    months=int(the_age_value)*12
    weeks=months*4
    days=int(the_age_value)*365

    line_one=f"Your age In Month Is :{months}"
    line_two=f"Your age In Month Is :{weeks}"
    line_thee=f"Your age In Month Is :{days}"
    all_lines=[line_one,line_two,line_thee]
    messagebox.showinfo('title your age Unitid',"\n".join(all_lines))


#create button the Calculate
btn=Button(age_app,text="Calculate Age" ,width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,command=cal)#command apple function when click button
btn.pack()
age_app.mainloop()#ykhalih khdam malanihay