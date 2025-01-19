import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import json
from PIL import Image , ImageTk



class BankManagement :

    # region command login button (finish)

    def login(self):

        self.label_mainpage.grid_forget()
        self.button_login.grid_forget()
        self.button_registry.grid_forget()

        self.label_login.grid(row=0, column=0, padx=250)

        self.label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_username_login_page.grid(row=1, padx=100, pady=10)

        self.label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_password_login_page.grid(row=2, padx=100, pady= 10)

        self.button_enter.grid(row=3, column=0, padx=200,pady= 10,)
        self.button_back_page2.grid(row=3, column=0, padx=300, pady=10,)
        self.button_forget.grid(row=5, column=0, padx=300, pady=10,)



    #endregion

    # region command enter button (not finished)

    def checking(self):

        username = self.entry_username_login_page.get()
        password = self.entry_password_login_page.get()
        nationalcode = self.entry_nationalcode.get()

        with open('datafile.txt','r') as file :
            var = file.read()

            if username in var and password in var : 

                self.label_login.grid_forget()
                self.label_username_login_page.grid_forget()
                self.entry_username_login_page.grid_forget()
                self.label_password_login_page.grid_forget()
                self.entry_password_login_page.grid_forget()
                self.button_enter.grid_forget()
                self.button_back_page2.grid_forget()

                # ma baghioe code page dakhjele app

            else:
                messagebox.showerror('Error:', 'Invalid username or password')

                self.label_login.grid(row=0, column=0, padx=250)
                self.label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
                self.entry_username_login_page.grid(row=1,padx=100,pady=10)
                
                self.label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
                self.entry_password_login_page.grid(row=2, padx=100, pady= 10)

                self.button_enter.grid(row=3, column=0, padx=200,pady= 10, sticky='w')
                self.button_back_page2.grid(row=3, column=0, padx=300, pady=10, sticky='w')

    #endregion



    # region command back button login page (finish)

    def back_main_page(self):

        self.label_login.grid_forget()

        self.label_username_login_page.grid_forget()
        self.entry_username_login_page.grid_forget()

        self.label_password_login_page.grid_forget()
        self.entry_password_login_page.grid_forget()

        self.button_enter.grid_forget()
        self.button_back_page2.grid_forget()

        self.label_mainpage.grid(row = 0, column = 0, padx=170, sticky='w')
        self.button_login.grid(row = 1, column = 0, padx=200,pady=10, sticky='w')
        self.button_registry.grid(row = 1, column = 0, padx=300, pady=10, sticky='w')

    def image():
        pass


    #endregion

    # region command registry button (finish)

    def registry(self):

        self.label_mainpage.grid_forget()
        self.button_login.grid_forget()
        self.button_registry.grid_forget()

        self.label_registry_page.grid(row=0, column=0, padx=250, pady=10)

        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_name.grid(row=1, padx=10, pady=10)

        self.label_family.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_family.grid(row=2, padx=10, pady=10)

        self.label_email.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.entry_email.grid(row=3, padx=10, pady=10)

        self.label_nationalcode.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.entry_nationalcode.grid(row=4, padx=10, pady=10)

        self.label_age.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.entry_age.grid(row=5, padx=10, pady=10)

        self.label_password_registry.grid(row=6, column=0, padx=10, pady=10,sticky='w')
        self.entry_password_registry.grid(row=6, padx=10, pady=10)

        self.label_confirm_password.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.entry_confirm_password.grid(row=7, padx=10, pady=10)

        self.button_submit.grid(row = 8, column = 0, padx=200,pady=10, sticky='w')
        self.button_back_registry.grid(row = 8, column = 0, padx=300,pady=10, sticky='w') 

    #endregion

    # region command submit button (finished)

    def submit(self):

        data_list = []


        name = self.entry_name.get()
        family = self.entry_family.get()
        age = self.entry_age.get()
        national_code = self.entry_nationalcode.get()
        email = self.entry_email.get()
        password = self.entry_password_registry.get()
        confirm_password = self.entry_confirm_password.get()

        if password == confirm_password :
            user_info = {
                'Name': name,
                'Family': family,
                'National code': national_code,
                'Age': age,
                'E-mail': email,
                'Password':password
            }
            data_list.append(user_info)

            with open('datafile.txt', 'a') as file :
                json.dump(data_list,file)

                messagebox.showinfo('Result:', 'Registration was successfully.\nYour username is your National code')

            self.label_registry_page.grid_forget()
            self.label_name.grid_forget()
            self.entry_name.grid_forget()
            self.label_family.grid_forget()
            self.entry_family.grid_forget()
            self.label_email.grid_forget()
            self.entry_email.grid_forget()
            self.label_nationalcode.grid_forget()
            self.entry_nationalcode.grid_forget()
            self.label_age.grid_forget()
            self.entry_age.grid_forget()
            self.label_password_registry.grid_forget()
            self.entry_password_registry.grid_forget()
            self.label_confirm_password.grid_forget()
            self.entry_confirm_password.grid_forget()
            self.button_submit.grid_forget()
            self.button_back_registry.grid_forget()

            self.label_login.grid(row=0, column=0, padx=250)

            self.label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
            self.entry_username_login_page.grid(row=1, padx=100, pady=10)

            self.label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
            self.entry_password_login_page.grid(row=2, padx=100, pady= 10)

            self.button_enter.grid(row=3, column=0, padx=200,pady= 10, sticky='w')
            self.button_back_page2.grid(row=3, column=0, padx=300, pady=10, sticky='w')

        else:
            messagebox.showerror('Error!!', 'Please check your information')

    #endregion

    # region command back button registry page (finished)

    def backtomainpage(self):
        
            self.label_registry_page.grid_forget()
            self.label_name.grid_forget()
            self.entry_name.grid_forget()
            self.label_family.grid_forget()
            self.entry_family.grid_forget()
            self.label_email.grid_forget()
            self.entry_email.grid_forget()
            self.label_nationalcode.grid_forget()
            self.entry_nationalcode.grid_forget()
            self.label_age.grid_forget()
            self.entry_age.grid_forget()
            self.label_password_registry.grid_forget()
            self.entry_password_registry.grid_forget()
            self.label_confirm_password.grid_forget()
            self.entry_confirm_password.grid_forget()
            self.button_submit.grid_forget()
            self.button_back_registry.grid_forget()

            self.label_mainpage.grid(row = 0, column = 0, padx=170, sticky='w')
            self.button_login.grid(row = 1, column = 0, padx=200,pady=10, sticky='w')
            self.button_registry.grid(row = 1, column = 0, padx=300, pady=10, sticky='w')




    #endregion





    # region create

    def __init__(self):
        self.main_page()

    #endregion

    # region main page GUI

    def main_page(self):

        self.app = ttk.Window(themename='solar')
        self.app.geometry('600x600+600+100')
        self.app.title('Bank Management')

        self.label_mainpage = ttk.Label(self.app, text='Bank management', font=('arial', 18, 'bold'))
        self.label_mainpage.grid(row = 1, column = 0, padx=170, sticky='w')

        self.button_login = ttk.Button(self.app, text='Login', style=SUNKEN, command=self.login)
        self.button_login.grid(row = 2, column = 0, padx=200,pady=10, sticky='w')

        self.button_registry = ttk.Button(self.app, text = 'Registry', style = SUCCESS, command= self.registry) 
        self.button_registry.grid(row = 2, column = 0, padx=300, pady=10, sticky='w')

        ditrect1 = "Bank_Logo.png"
        Image1 = Image.open(ditrect1)
        Image2 = ImageTk.PhotoImage(Image1)
        l_image = ttk.Label(self.app , image=Image2)
        l_image.grid(row = 0, column = 0, padx=170)
        

    #endregion 

    # region login page GUI

        self.label_login = ttk.Label(self.app, text= 'Login', font=('arial', 18, 'bold'))
        self.label_login.grid(row=0, column=0, padx=250)
        self.label_login.grid_forget()
        
        self.label_username_login_page = ttk.Label(self.app, text= 'Username', font= ('arial', 15, 'bold'))
        self.label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.label_username_login_page.grid_forget()
        
        self.entry_username_login_page = ttk.Entry(self.app, bootstyle="danger")
        self.entry_username_login_page.grid(row=1,padx=100,pady=10)
        self.entry_username_login_page.grid_forget()
        
        self.label_password_login_page = ttk.Label(self.app, text= 'Password', font=('arial', 15, 'bold'))
        self.label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.label_password_login_page.grid_forget()
        
        self.entry_password_login_page = ttk.Entry(self.app, bootstyle="danger")
        self.entry_password_login_page.grid(row=2, padx=100, pady= 10)
        self.entry_password_login_page.grid_forget()
        
        self.button_enter = ttk.Button(self.app, text = 'Enter', style = SUCCESS, command=self.checking) # not finished
        self.button_enter.grid(row=3, column=0, padx=200,pady= 10, sticky='w')
        self.button_enter.grid_forget()

        self.button_back_page2 = ttk.Button(self.app, text = 'Back', style = SUCCESS, command= self.back_main_page) 
        self.button_back_page2.grid(row=3, column=0, padx=300, pady=10, sticky='w')
        self.button_back_page2.grid_forget()

        self.button_forget = ttk.Button(self.app, text='Forget password', style= SUCCESS)
        self.button_forget.grid(row=5, column=0, padx=300, pady=10, sticky='w')
        self.button_forget.grid_forget()


    #endregion 

    # region registry page GUI
        self.label_registry_page = ttk.Label(self.app, text= 'Registry', font= ('arial', 18, 'bold'))
        self.label_registry_page.grid(row=0, column=0, padx=250, pady= 10)
        self.label_registry_page.grid_forget()

        self.label_name = ttk.Label(self.app, text='Name', font= ('arial', 15, 'bold'))
        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.label_name.grid_forget()

        self.entry_name = ttk.Entry(self.app, bootstyle='danger')
        self.entry_name.grid(row=1, padx=10, pady=10)
        self.entry_name.grid_forget()

        self.label_family = ttk.Label(self.app, text= 'Family', font=('arial', 15, 'bold'))
        self.label_family.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.label_family.grid_forget()

        self.entry_family = ttk.Entry(self.app, bootstyle='danger')
        self.entry_family.grid(row=2, padx=10, pady=10)
        self.entry_family.grid_forget()

        self.label_email = ttk.Label(self.app, text='E-mail', font=('arial', 15, 'bold'))
        self.label_email.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.label_email.grid_forget()

        self.entry_email = ttk.Entry(self.app, bootstyle = 'danger')
        self.entry_email.grid(row=3, padx=10, pady=10)
        self.entry_email.grid_forget()

        self.label_nationalcode = ttk.Label(self.app, text='National code', font= ('arial', 15, 'bold'))
        self.label_nationalcode.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.label_nationalcode.grid_forget()

        self.entry_nationalcode = ttk.Entry(self.app, bootstyle = 'danger')
        self.entry_nationalcode.grid(row=4, padx=10, pady=10)
        self.entry_nationalcode.grid_forget()

        self.label_age = ttk.Label(self.app, text='Date of birth', font=('arial', 15, 'bold'))
        self.label_age.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.label_age.grid_forget()

        self.entry_age = ttk.Entry(self.app, bootstyle='danger')
        self.entry_age.grid(row=5, padx=10, pady=10)
        self.entry_age.grid_forget()

        self.label_password_registry = ttk.Label(self.app, text= 'Password', font=('arial', 15, 'bold'))
        self.label_password_registry.grid(row=6, column=0, padx=10, pady=10,sticky='w')
        self.label_password_registry.grid_forget()

        self.entry_password_registry = ttk.Entry(self.app, bootstyle = 'danger')
        self.entry_password_registry.grid(row=6, padx=10, pady=10)
        self.entry_password_registry.grid_forget()

        self.label_confirm_password = ttk.Label(self.app, text= 'Confirm password', font=('arial', 15, 'bold'))
        self.label_confirm_password.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.label_confirm_password.grid_forget()
        
        self.entry_confirm_password = ttk.Entry(self.app, bootstyle= 'danger')
        self.entry_confirm_password.grid(row=7, padx=10, pady=10)
        self.entry_confirm_password.grid_forget()

        self.button_submit = ttk.Button(self.app, text='Submit', style=SUCCESS, command= self.submit) 
        self.button_submit.grid(row = 8, column = 0, padx=200,pady=10, sticky='w')  
        self.button_submit.grid_forget()

        self.button_back_registry = ttk.Button(self.app, text='Back', style=SUCCESS, command= self.backtomainpage) 
        self.button_back_registry.grid(row = 8, column = 0, padx=300,pady=10, sticky='w') 
        self.button_back_registry.grid_forget()

    #endregion

        self.app.mainloop()

objectory = BankManagement()