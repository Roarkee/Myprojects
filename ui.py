import tkinter as tk
from datetime import timezone, datetime
import requests
from dotenv import load_dotenv
import os
from tkinter import ttk,messagebox,PhotoImage
# from timezonefinder import TimezoneFinder
# from geopy.geocoders import Nominatim
# import pytz
load_dotenv()
API_KEY=os.getenv("API_KEY")
BASE_URL="https://api.openweathermap.org/data/2.5/weather?"



class Weather:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather App") #title of my gui interface
        self.root.geometry("900x500")  #dimensions of the window
        # self.root.configure(bg="#57adff")
        self.root.resizable(False, False)
        image_icon=PhotoImage(file="assets\\mylogo.png")
        self.root.iconphoto(False, image_icon)

        self.searchbar=PhotoImage(file="assets\\searchbar.png")  #dark image on which the textbox is placed
        self.myimage=tk.Label(self.root,image=self.searchbar)        
        self.myimage.place(x=20, y=20)

        self.textfield=tk.Entry(self.root,justify="center",width=20,border=0,font=("Roboto",20, "bold"), bg="#404040" , fg="white")
        self.textfield.place(x=50,y=40)
        self.textfield.focus()

        self.search_icon=PhotoImage(file="assets\\search_icon.png")        
        self.searchbtn=tk.Button(image=self.search_icon, borderwidth=0,cursor="hand2", bg="#404040")
        self.searchbtn.place(x=375, y=24)
        
        self.mylogo=PhotoImage(file="assets\\logo12.png")
        self.mylogo_label=tk.Label(self.root,image=self.mylogo)
        self.mylogo_label.place(x=150,y=100)

        self.frame_image=PhotoImage(file="assets\\bottom_bar.png")
        self.bottom_bar=tk.Label(self.root,image=self.frame_image)
        self.bottom_bar.pack(padx=5, pady=5, side="bottom")

        label1=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="WIND")
        label1.place(x=100, y=400)
        label2=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="DESCRIPTON")
        label2.place(x=200, y=400)
        label3=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="TEMPERATURE")
        label3.place(x=400, y=400)
        label4=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="PRESSURE")
        label4.place(x=630, y=400)

        wind=tk.Label(text="...", font=("Arial", 20),bg="#1ab5ef")
        wind.place(x=100,y=435)
        win=tk.Label(text="...", font=("Arial", 20),bg="#1ab5ef")
        win.place(x=280,y=435)
        wnd=tk.Label(text="...", font=("Arial", 20),bg="#1ab5ef")
        wnd.place(x=450,y=435)
        ind=tk.Label(text="...", font=("Arial", 20),bg="#1ab5ef")
        ind.place(x=670,y=435)




        '''self.my_frame=tk.Frame(self.root, bg="#57adff",height=30)
        self.my_frame.columnconfigure(0, weight=1)
        self.my_frame.columnconfigure(1, weight=1)
        self.my_frame.columnconfigure(2, weight=1)
        self.my_frame.columnconfigure(3, weight=1)

        self.label1=tk.Label(self.my_frame, text="Wind", font=("Arial", 19),bg="#1b433e",height=3)
        self.label1.grid(row=0, column=0, sticky="we")
        self.label2=tk.Label(self.my_frame,text="Temperature", font=("Arial", 19),bg="#1b433e",height=3)
        self.label2.grid(row=0, column=1, sticky="we")
        self.label3=tk.Label(self.my_frame,text="Pressure", font=("Arial", 19),bg="#1b433e",height=3)
        self.label3.grid(row=0, column=2, sticky="we")
        self.label4=tk.Label(self.my_frame,text="Description", font=("Arial", 19),bg="#1b433e",height=3)
        self.label4.grid(row=0, column=3, sticky="we")
        self.my_frame.pack(padx=5, pady=15 ,side="bottom")
        I was trying ot use grid view but i'm having difficulty. will come back to it again and see if it's possible
        '''
       

    def run(self):
        self.root.mainloop()

    def search(self):
        self.city=self.textfield.get()
        BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
        url=BASE_URL+"appid="+API_KEY+"&q="+{self.city}+"&units=metric"
        response=requests.get(url).json()
        
        


