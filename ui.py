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
        
        #textbox where the user inputs data
        self.textfield=tk.Entry(self.root,justify="center",width=20,border=0,font=("Roboto",20, "bold"), bg="#404040" , fg="white")
        self.textfield.place(x=50,y=40)
        self.textfield.focus()
        self.textfield.bind("<Return>", self.search)

        #search button
        self.search_icon=PhotoImage(file="assets\\search_icon.png")        
        self.searchbtn=tk.Button(image=self.search_icon, borderwidth=0,cursor="hand2", bg="#404040", command=self.search)
        self.searchbtn.place(x=375, y=24)

        

        self.mylogo=PhotoImage(file="assets\\logo12.png")
        self.mylogo_label=tk.Label(self.root,image=self.mylogo)
        self.mylogo_label.place(x=150,y=100)

        # long blue bar at the bottom
        self.frame_image=PhotoImage(file="assets\\bottom_bar.png")
        self.bottom_bar=tk.Label(self.root,image=self.frame_image)
        self.bottom_bar.pack(padx=5, pady=5, side="bottom")


        #labels in the bottom bar
        self.label1=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="WIND")
        self.label1.place(x=100, y=400)
        self.label2=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="DESCRIPTON")
        self.label2.place(x=200, y=400)
        self.label3=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="HUMIDITY")
        self.label3.place(x=400, y=400)
        self.label4=tk.Label(self.root, font=("Roboto", 20, "bold"), bg="#1ab5ef", fg="white", text="PRESSURE")
        self.label4.place(x=630, y=400)

        self.wind=tk.Label(text="...", font=("Arial", 17),bg="#1ab5ef")
        self.wind.place(x=100,y=435)
        self.desc=tk.Label(text="...", font=("Arial", 17),bg="#1ab5ef")
        self.desc.place(x=230,y=435)
        self.humid=tk.Label(text="...", font=("Arial", 17),bg="#1ab5ef")
        self.humid.place(x=450,y=435)
        self.pres=tk.Label(text="...", font=("Arial", 17),bg="#1ab5ef")
        self.pres.place(x=670,y=435)
        self.temp=tk.Label(text="", font=("Verdana", 40), fg="#2335ab")
        self.temp.place(x=475,y=120)
        self.feel=tk.Label(text="", font=("Verdana",20))
        self.feel.place(x=475, y=230)
      
    
    




    def run(self):
        self.root.mainloop()

    def search(self, event=None):
        self.city=self.textfield.get()
        BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
        url=f"{BASE_URL}appid={API_KEY}&q={self.city}&units=metric"
        response=requests.get(url).json()
        self.wind_speed=response["wind"]["speed"]
        self.pressure=response["main"]["pressure"]
        self.humidity=response["main"]["humidity"]
        self.description=response["weather"][0]["description"]
        self.weather_icon=response["weather"][0]["icon"]
        self.temperature=response["main"]["temp"]
        self.feels_like=response["main"]["feels_like"]
        self.condition=response["weather"][0]["main"]
        # self.weather_image=PhotoImage(file=f"assets\\{self.weather_icon}@2x.png")        
            
        self.wind.config(text=f"{self.wind_speed} m/s")
        self.pres.config(text=f"{self.pressure} hPa")
        self.humid.config(text=f"{self.humidity}%")
        self.desc.config(text=self.description)
        self.temp.config(text=f"{self.temperature}°C")
        self.feel.config(text=f"{self.condition}|Feels like:{self.feels_like}°C")
        
        # self.mylogo_label.config(image=self.weather_image)
        self.textfield.delete(0, tk.END)
        
        
        




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
       

  
        


