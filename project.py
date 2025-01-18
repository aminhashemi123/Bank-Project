import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import json

class BankManagement:

    # region Command Login Button (Finished)
    def login(self):
        self.clear_main_page()
        
        self.label_login.grid(row=0, column=0, padx=250)

        self.label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_username_login_page.grid(row=1, padx=100, pady=10)

        self.label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.entry_password_login_page.grid(row=2, padx=100, pady=10)

        self.button_enter.grid(row=3, column=0, padx=200, pady=10, sticky='w')
        self.button_back_page2.grid(row=3, column=0, padx=300, pady=10, sticky='w')

    # endregion

    # region Command Enter Button (Not Finished)
    def checking(self):
        username = self.entry_username_login_page.get()
        password = self.entry_password_login_page.get()

        with open('datafile.txt', 'r') as file:
            data = file.read()

            if username in data and password in data:
                self.clear_login_page()
                # Move to the next page of the app
            else:
                messagebox.showerror('Error:', 'Invalid username or password')

    # endregion

    # region Command Back Button Login Page (Finished)
    def back_main_page(self):
        self.clear_login_page()
        self.display_main_page()

    # endregion

    # region Command Registry Button (Finished)
    def registry(self):
        self.clear_main_page()
        
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

        self.label_password_registry.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.entry_password_registry.grid(row=6, padx=10, pady=10)

        self.label_confirm_password.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.entry_confirm_password.grid(row=7, padx=10, pady=10)

        self.button_submit.grid(row=8, column=0, padx=200, pady=10, sticky='w')
        self.button_back_registry.grid(row=8, column=0, padx=300, pady=10, sticky='w')

        self.label_upload_image.grid(row=9, column=0, padx=10, pady=10, sticky='w')
        self.button_upload_image.grid(row=9, column=0, padx=200, pady=10, sticky='w')

    # endregion

    # region Command Submit Button (Finished)
    def submit(self):
        name = self.entry_name.get()
        family = self.entry_family.get()
        age = self.entry_age.get()
        national_code = self.entry_nationalcode.get()
        email = self.entry_email.get()
        password = self.entry_password_registry.get()
        confirm_password = self.entry_confirm_password.get()

        if password == confirm_password:
            user_info = {
                'Name': name,
                'Family': family,
                'National Code': national_code,
                'Age': age,
                'Email': email,
                'Password': password,
            }

            with open('datafile.txt', 'a') as file:
                json.dump(user_info, file)

            messagebox.showinfo('Result:', 'Registration was successful.\nYour username is your National Code')
            self.back_main_page()
        else:
            messagebox.showerror('Error!!', 'Passwords do not match. Please try again.')

    # endregion

    # region Command Back Button Registry Page (Finished)
    def backtomainpage(self):
        self.clear_registry_page()
        self.display_main_page()

    # endregion

    # region Command Upload Image
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Bank_Logo",
            filetypes=[("Bank_Logo", "*.jpg *.jpeg *.png *.bmp *.gif")],
        )
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((100, 100))  # Resize the image to fit
            self.profile_photo = ImageTk.PhotoImage(image)
            self.label_upload_image_display.configure(image=self.profile_photo)

    # endregion

    # region Clear Pages
    def clear_main_page(self):
        self.label_mainpage.grid_forget()
        self.button_login.grid_forget()
        self.button_registry.grid_forget()

    def clear_login_page(self):
        self.label_login.grid_forget()
        self.label_username_login_page.grid_forget()
        self.entry_username_login_page.grid_forget()
        self.label_password_login_page.grid_forget()
        self.entry_password_login_page.grid_forget()
        self.button_enter.grid_forget()
        self.button_back_page2.grid_forget()

    def clear_registry_page(self):
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
        self.label_upload_image.grid_forget()
        self.button_upload_image.grid_forget()
        self.label_upload_image_display.grid_forget()

    # endregion

    # region Display Main Page
    def display_main_page(self):
        self.label_mainpage.grid(row=0, column=0, padx=170, sticky='w')
        self.button_login.grid(row=1, column=0, padx=200, pady=10, sticky='w')
        self.button_registry.grid(row=1, column=0, padx=300, pady=10, sticky='w')

    # endregion

    # region Create GUI
    def __init__(self):
        self.app = ttk.Window(themename='solar')
        self.app.geometry('600x600')
        self.app.title('Bank Management')

        # Main Page
        self.label_mainpage = ttk.Label(self.app, text='Bank Management', font=('arial', 18, 'bold'))
        self.button_login = ttk.Button(self.app, text='Login', style=SUNKEN, command=self.login)
        self.button_registry = ttk.Button(self.app, text='Registry', style=SUCCESS, command=self.registry)
        self.display_main_page()

        # Login Page
        self.label_login = ttk.Label(self.app, text='Login', font=('arial', 18, 'bold'))
        self.label_username_login_page = ttk.Label(self.app, text='Username', font=('arial', 15, 'bold'))
        self.entry_username_login_page = ttk.Entry(self.app, bootstyle="danger")
        self.label_password_login_page = ttk.Label(self.app, text='Password', font=('arial', 15, 'bold'))
        self.entry_password_login_page = ttk.Entry(self.app, bootstyle="danger", show="*")
        self.button_enter = ttk.Button(self.app, text='Enter', style=SUCCESS, command=self.checking)
        self.button_back_page2 = ttk.Button(self.app, text='Back', style=SUCCESS, command=self.back_main_page)

        # Registry Page
        self.label_registry_page = ttk.Label(self.app, text='Registry', font=('arial', 18, 'bold'))
        self.label_name = ttk.Label(self.app, text='Name', font=('arial', 15, 'bold'))
        self.entry_name = ttk.Entry(self.app, bootstyle='danger')
        self.label_family = ttk.Label(self.app, text='Family', font=('arial', 15, 'bold'))
        self.entry_family = ttk.Entry(self.app, bootstyle='danger')
        self.label_email = ttk.Label(self.app, text='E-mail', font=('arial', 15, 'bold'))
        self.entry_email = ttk.Entry(self.app, bootstyle='danger')
        self.label_nationalcode = ttk.Label(self.app, text='National Code', font=('arial', 15, 'bold'))
        self.entry_nationalcode = ttk.Entry(self.app, bootstyle='danger')
        self.label_age = ttk.Label(self.app, text='Age', font=('arial', 15, 'bold'))
        self.entry_age = ttk.Entry(self.app, bootstyle='danger')
        self.label_password_registry = ttk.Label(self.app, text='Password', font=('arial', 15, 'bold'))
        self.entry_password_registry = ttk.Entry(self.app, bootstyle='danger', show="*")
        self.label_confirm_password = ttk.Label(self.app, text='Confirm Password', font=('arial', 15, 'bold'))
        self.entry_confirm_password = ttk.Entry(self.app, bootstyle='danger', show="*")
        self.button_submit = ttk.Button(self.app, text='Submit', style=SUCCESS, command=self.submit)
        self.button_back_registry = ttk.Button(self.app, text='Back', style=SUCCESS, command=self.backtomainpage)

        # Upload Image
        self.label_upload_image = ttk.Label(self.app, text='Upload Profile Image:', font=('arial', 15, 'bold'))
        self.button_upload_image = ttk.Button(self.app, text='Upload', style=INFO, command=self.upload_image)
        self.label_upload_image_display = ttk.Label(self.app)

        self.app.mainloop()
    # endregion


# Initialize the application
app = BankManagement()
