from tkinter import *
from tkinter import ttk
import customtkinter
import time
from PIL import Image, ImageOps, ImageDraw, ImageTk

root = Tk()

class Globals():
    username = None
    password = None
    SignedIn = False 
    photo_added = False
    photo = None
    system_language = None

time_var = time.asctime()
answer = None

####################################################################################################################################

def settings():
    system_languages = ["English", "Русский"]

    Settings = Toplevel(root)
    Settings.title("Settings")
    Settings.geometry("900x500")
    Settings.resizable(width=False, height=False)
    SettingsFrame = Frame(Settings, bg="white")

    LanguageLabel =Label(SettingsFrame, bg="white", fg="black", text="Language(Beta): ")
    LanguageCombobox = ttk.Combobox(Settings, values=system_languages, state="readonly")
    LanguageLabel.configure(font=('Arial', 15))
    LanguageCombobox.configure(font=('Arial', 15))
    LanguageCombobox.current(0)

    SettingsFrame.place(relheight=1, relwidth=1)
    LanguageLabel.place(x=10, y=10)
    LanguageCombobox.place(x=170, y=10)

    def LanguageFunc(event):
        Globals.system_language = LanguageCombobox.get()

    LanguageCombobox.bind("<<ComboboxSelected>>", LanguageFunc)

def login():
    Login = Toplevel(root)
    Login.title("Login")
    Login.geometry("300x300")
    Login.resizable(False, False)
    LoginFrame = Frame(Login, bg="white")
    LoginFrame.place(relheight=1, relwidth=1)

    def show_photo_and_name():
        LoginFrame.destroy()
        new_frame = Frame(Login, bg="white")
        new_frame.place(relheight=1, relwidth=1)

        NameLabel = Label(new_frame, text=Globals.username, bg="white", fg="#333333", font=('Helvetica', 17, 'bold'), bd=2, relief="groove",padx=10, pady=5)
        PhotoLabel = Label(new_frame, image=Globals.photo, bg="white")
        PhotoLabel.image = Globals.photo

        PhotoLabel.place(x=100, y=20)
        NameLabel.pack(expand=True, fill='both')

    def data_handler():
        Globals.username = UsernameEntry.get()
        Globals.password = PasswordEntry.get()
        Globals.SignedIn = True

        for widget in LoginFrame.winfo_children():
            widget.destroy()

        PathLabel = Label(LoginFrame, text="ENTER PHOTO PATH:", bg="white", font=('Arial', 15))
        PhotoPathEntry = Entry(LoginFrame, bg="grey", fg="white", font=('Courier New', 15))
        

        def create_photo(event):
            path = PhotoPathEntry.get()
            try:
                im = Image.open(path)
                size = (100, 100)
                mask = Image.new('L', size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + size, fill=255)

                im = im.resize(size)
                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                output.thumbnail(size, Image.Resampling.LANCZOS)
                output.save("Images/account_photo.png")

                Globals.photo = PhotoImage(file="Images/account_photo.png")
                Globals.photo_added = True
                show_photo_and_name()

            except FileNotFoundError:
                print("Файл не найден")

        PathLabel.place(x=50, y=30)
        PhotoPathEntry.place(x=30, y=100)

        PhotoPathEntry.bind("<Return>", create_photo)

    if not Globals.SignedIn:
        UsernameLabel = Label(LoginFrame, text="ENTER USERNAME:", bg="white", font=('Arial', 15))
        PasswordLabel = Label(LoginFrame, text="ENTER PASSWORD:", bg="white", font=('Arial', 15))
        UsernameEntry = Entry(LoginFrame, bg="grey", fg="white", font=('Courier New', 15))
        PasswordEntry = Entry(LoginFrame, bg="grey", fg="white", show="*", font=('Courier New', 15))
        SignUpButton = Button(LoginFrame, text="SIGN UP", command=data_handler, bg="grey", relief=FLAT)

        UsernameLabel.place(x=50, y=20)
        UsernameEntry.place(x=30, y=60)
        PasswordLabel.place(x=50, y=100)
        PasswordEntry.place(x=30, y=140)
        SignUpButton.place(x=120, y=220)
    
def open_terminal():
    Terminal = Toplevel(root)
    Terminal.title("Terminal")
    Terminal.geometry("900x500")
    Terminal.resizable(width=False, height=False)

    def command_handler(event):
        terminal_command = command_entry.get()
        if not Globals.SignedIn:
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = "Sign up first!"
            answer_label = Label(main_frame_terminal, text=">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
        elif terminal_command == "/time":
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = time.asctime()
            answer_label = Label(main_frame_terminal, text="C:/system52/EnterOS/" + Globals.username+ ">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
            command_entry.delete(0, len(terminal_command))
        elif terminal_command == "/commands":
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = "/username - Get your username\n/time - Get time\n/system_language - View your system language\n/exit - Close terminal\n/echo ... - Terminal will repeat phrase you write"
            answer_label = Label(main_frame_terminal, text="C:/system52/EnterOS/" + Globals.username+ ">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
            command_entry.delete(0, len(terminal_command))
        elif terminal_command == "/username":
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = Globals.username
            answer_label = Label(main_frame_terminal, text="C:/system52/EnterOS/" + Globals.username+ ">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
            command_entry.delete(0, len(terminal_command))
        elif terminal_command == "/system_language":
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = Globals.system_language
            answer_label = Label(main_frame_terminal, text="C:/system52/EnterOS/" + Globals.username+ ">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
            command_entry.delete(0, len(terminal_command))
        elif terminal_command == "/exit":
            Terminal.destroy()
        elif terminal_command.startswith("/echo ") :
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = terminal_command[5:]
            answer_label = Label(main_frame_terminal, text="C:/system52/EnterOS/" + Globals.username+ ">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
            command_entry.delete(0, len(terminal_command))
        else:
            for widget in main_frame_terminal.winfo_children():
                if isinstance(widget, Label) and widget not in (InfoLable, arrow_label):
                    widget.destroy()
            answer = "Wrong command!"
            answer_label = Label(main_frame_terminal, text="C:/system52/EnterOS/" + Globals.username+ ">>> " + answer, fg="white", bg="black")
            answer_label.config(font=('Courier New', 18))
            answer_label.place(x=0, y=100)
            command_entry.delete(0, len(terminal_command))
    
    def terminal_top():
        if Terminal.state() == 'normal':
            Terminal.iconify()
        else:
            Terminal.deiconify()
    
    main_frame_terminal = Frame(Terminal, bg="black")
    InfoLable = Label(main_frame_terminal, text="©Enter Games Corporation 2025.\nTo get list of command use /commands", bg="black", fg="white")
    command_entry = Entry(main_frame_terminal, bg="black", fg="white")
    arrow_label = Label(main_frame_terminal, text=">", fg="white", bg="black")
    bottom_terminal_panel = Button(bottom_frame, image=SmallTerminalImg, bg="grey", relief=FLAT, command=terminal_top)
    InfoLable.config(font=('Courier New', 18))
    command_entry.config(font=('Courier New', 15))
    arrow_label.config(font=('Courier New', 20))

    main_frame_terminal.place(relheight=1, relwidth=1)
    InfoLable.place(x=0, y=0)
    command_entry.place(x=30, y=70)
    arrow_label.place(x=0, y=65)
    bottom_terminal_panel.place(x=200, y=5)

    command_entry.bind("<Return>", command_handler)

def file_manager():
    Manager = Toplevel(root)
    Manager.title("File Manager")
    Manager.geometry('900x500')
    Manager.resizable(width=False, height=False)

    def Manager_Top():
        if Manager.state() == 'normal':
            Manager.iconify()
        else:
            Manager.deiconify()
    def AddFile():
        pass

    AddImgIcon = PhotoImage(file="Images/Add.png")

    MainManagerFrame = Frame(Manager, bg="white")
    TopManagerFrame = Frame(Manager, bg="grey")
    Manager_bottom_panel = Button(bottom_frame, image=SmallManagerIcon, bg="grey", relief=FLAT, command=Manager_Top)
    AddButton = Button(TopManagerFrame, image=AddImgIcon, bg="grey", relief=FLAT, width=25, height=25, command=AddFile)
    AddButton.image = AddImgIcon

    MainManagerFrame.place(relheight=1, relwidth=1)
    TopManagerFrame.place(relheight=0.1, relwidth=1, y=0)
    Manager_bottom_panel.place(x=250, y=5)
    AddButton.place(x=10, y=10)
    
####################################################################################################################################

def close_system():
    root.destroy()

root.title('EnterOS') 
root.geometry('1900x1000')
root.resizable(width=False, height=False)
root.attributes('-fullscreen', True)

Terminal_open = False
main_frame = Frame(root, bg="white")
bottom_frame = Frame(root, bg="grey")

main_frame.place(relheight=1, relwidth=1)
bottom_frame.place(relheight=0.2, relwidth=1, y=810)

Background_image = Image.open("Images/Background.png")
Bg = ImageTk.PhotoImage(Background_image)
AccountImg = PhotoImage(file="Images/Account.png")
QuitImg = PhotoImage(file="Images/Logout.png")
SettingsImg = PhotoImage(file="Images/Settings.png")
SmallTerminalImg = PhotoImage(file="Images/SmallTerminal.png")
# TerminalImg = PhotoImage(file="Images/Terminal.png")
TerminalImg = Image.open("Images/Terminal.png")
terminal_icon = customtkinter.CTkImage(light_image=TerminalImg, size=(100, 100))
ManagerImg = Image.open("Images/FileManager.png")
Manager_icon = customtkinter.CTkImage(light_image=ManagerImg, size=(100, 100))
SmallManagerIcon = PhotoImage(file="Images/SmallManager.png")

Background = Label(main_frame, image=Bg)
account_btn = Button(bottom_frame, image=AccountImg, height=50, width=50, command=login, relief=FLAT, bg="grey")
close_btn = Button(bottom_frame, image=QuitImg, height=50, width=50, command=close_system, relief=FLAT, bg="grey")
time_label = Label(bottom_frame, text=time_var, bg="gray", width=0, height=0, font=24)
settings_button = Button(bottom_frame, image=SettingsImg, height=50, width=50, command=settings, relief=FLAT, bg="grey")
# terminal_btn = Button(main_frame, image=TerminalImg, height=100, width=100, relief=FLAT, bg="white", command=open_terminal, fg="black")
terminal_btn = customtkinter.CTkButton(
    master=main_frame,
    image=terminal_icon,
    text="",
    command=open_terminal,
    fg_color="transparent",
    bg_color="transparent",
    width=100,
    height=100,
    corner_radius=0
)
explorer_button = customtkinter.CTkButton(
    master=main_frame,
    image=Manager_icon,
    text="",
    command=file_manager,
    fg_color="transparent",
    bg_color="transparent",
    width=100,
    height=100,
    corner_radius=0
)

Background.place(x=0, y=0, relheight=1, relwidth=1)
Background.lower()
terminal_btn.place(x=40, y=50)
explorer_button.place(x=200, y=50)
time_label.place(x=1295, y=15)
close_btn.place(x=100, y=0)
settings_button.place(x=50, y=0)
account_btn.place(x=0, y=0)

def update_time():
    time_label.config(text=time.asctime())
    root.after(1000, update_time) 
update_time()

root.mainloop()