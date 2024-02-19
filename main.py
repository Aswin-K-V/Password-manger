from tkinter import *
from tkinter import messagebox
import random 
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_list=password_letters+password_numbers+password_symbols


    random.shuffle(password_list)

    pass_gen = "".join(password_list)
    password_entry.insert(0,pass_gen)
    pyperclip.copy(pass_gen)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
     website=website_name.get()
     try:
          
        with open("data.json","r") as data_file:
            data=json.load(data_file)
     except FileNotFoundError:
            print("file not found")
     else:                   
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email} Password{password}")
        else:
            messagebox.showinfo(title="Error",message="password not found")     
          
              




def save():
    website=website_name.get()
    email=Email.get()
    password=password_entry.get()

    new_data={website:{"email":email,"password":password}}
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="0",message="Fields empty")
    else:
        try:    
            with open("data.json","r") as data_file:
                 data=json.load(data_file)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
             with open("data.json","w") as data_file:
                  json.dump(new_data,data_file,indent=4)
                
        else:        
                data.update(new_data)
                with open("data.json","w") as data_file:    
                    json.dump(data,data_file,indent=4)
        finally:
              website_name.delete(0,END)
              password_entry.delete(0,END)
 
# ---------------------------- UI SETUP ------------------------------- #

#window
window=Tk()
window.config(padx=20,pady=20,bg="#F2EFE5")
window.title("Password manager")


#canvas
canvas=Canvas(width=200,height=200,bg="#F2EFE5",highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_name=Entry(text="Website",width=35)
website_name.grid(row=1,column=1,columnspan=2)
website_name.focus()# curser pointer

website_Label=Label(text="Website:",bg="#F2EFE5")
website_Label.grid(row=1,column=0)

search=Button(text="Search",bg="#CCD3CA",command=search)
search.grid(row=1,column=3)

Email_Label=Label(text="Email/Username:",padx=10,pady=10,bg="#F2EFE5")
Email_Label.grid(row=2,column=0)


Email=Entry(width=35)
Email.insert(0,"example@gmail.com")
Email.grid(row=2,column=1,columnspan=2)

password_Label=Label(text="Password:",padx=10,pady=10,bg="#F2EFE5")
password_Label.grid(row=3,column=0)
password_entry=Entry(width=34)
password_entry.grid(row=3,column=1)


Gen_password=Button(text="Generate Password",padx=5,pady=5,bg="#CCD3CA",command=generate_password)
Gen_password.grid(row=3,column=3)

Add=Button(text="Add",bg="#CCD3CA",command=save)
Add.grid(row=4,column=1,columnspan=2)













window.mainloop()