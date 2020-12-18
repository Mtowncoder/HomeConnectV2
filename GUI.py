from tkinter import *
import tkinter as tk

import requests
import json
import sqlite3
import pandas as pd


##### have get settings make a pop up window with the settings
##### For changing temperature have Current Temperature, Entry Box with number, Have "Change Whatever as the Enter button"
#######
#######
####### Make SQL function at the end of every action ############
####### Find way to refresh 






# class pop_up:
    # make error pop up
    
    
    # have one for information

window = Tk()
    
def settings_pop_up(setting1, setting2, setting3):
    win= tk.Tk()

    label= tk.Label(win, text=setting1)
    label.pack()
    label= tk.Label(win, text=setting2)
    label.pack()
    label= tk.Label(win, text=setting3)
    label.pack()
    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()
    win.destroy()
    
def Would_input():
    
    win= tk.Tk()
    prompt = "Would you like to change the temperature? "

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput
    
def Name_input():
    win= tk.Tk()
    prompt = "Enter Name: "

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput

def Date_input():
    win= tk.Tk()
    prompt = "Enter HAID: "

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput

def Action_input():
    win= tk.Tk()
    prompt = "Enter what you did: "

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput
    
def HAID_input():
    win= tk.Tk()
    prompt = "Enter HAID: "

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput

def temp_input():
    win= tk.Tk()
    prompt = "What would you like to change the temperature too? "

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput



class settings:
    auth_key =''
    setting_headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'Accept-Language' : 'en-US', 'authorization': auth_key }
    fridge_headers = {'accept': 'application/vnd.bsh.sdk.v1+json','Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}
    freezer_headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}

    # This Function gets all settings of an appliance
    def get_settings(self):
        HAID = HAID_input()
        url_setting = 'https://simulator.home-connect.com/api/homeappliances/%s/settings' % (HAID)
        resp_setting =  requests.get(url_setting,headers=self.setting_headers)
        settings = json.loads(resp_setting.content)
        print(settings['data']['settings'])

    # This Function gets all settings of the freezer
    def get_freezer_settings(self):
        HAID = HAID_input()
        url_freezer_setting = 'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer' % (HAID)
        resp_freezer_setting = requests.get(url_freezer_setting, headers = self.setting_headers)
        freezer = json.loads(resp_freezer_setting.content)

        # this makes the dictionary data more readable
        raw_data = freezer['data']
        setting = raw_data['key']
        temp = raw_data['value']
        unit = raw_data['unit']
        constraints = raw_data['constraints']
        setting1 = "The current settings available are ({}) ".format(setting)
        setting2 = "The current temperature is {} {} ".format(temp, unit)
        setting3 = "The constraints are {} ".format(constraints)
        settings_pop_up(setting1, setting2, setting3)

        print("The current settings available are ({}) ".format(setting))
        print("The current temperature is {} {} ".format(temp, unit))
        print("The constraints are {} ".format(constraints))

    # This Function gets all settings of a fridge
    def get_fridge_settings(self):
        HAID = HAID_input()
        url_fridge_setting=  'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator' % (HAID)
        resp_fridge_setting = requests.get(url_fridge_setting, headers = self.setting_headers)
        fridge = json.loads(resp_fridge_setting.content)

        # This makes the dictionary data more readable
        raw_data = fridge['data']
        setting = raw_data['key']
        temp = raw_data['value']
        unit = raw_data['unit']
        constraints = raw_data['constraints']
        setting1 = "The current settings available are ({}) ".format(setting)
        setting2 = "The current temperature is {} {} ".format(temp, unit)
        setting3 = "The constraints are {} ".format(constraints)
        
        settings_pop_up(setting1, setting2, setting3)

        print("The current settings available are ({}) ".format(setting))
        print("The current temperature is {} {} ".format(temp, unit))
        print("The constraints are {} ".format(constraints))

class change_settings:
    auth_key =''
    freezer_headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}
    fridge_headers = {'accept': 'application/vnd.bsh.sdk.v1+json','Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}
    freezer_min = -24 # bounds for changing freezer temp
    freezer_max = -16
    fridge_min = 2 # bounds for changing fridge temp
    fridge_max = 8

    def change_freezer_temp(self):
        HAID = HAID_input()
        freezer_url = 'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer' % (HAID)

        # This section gets the current temperature
        resp_freezer_setting = requests.get(freezer_url, headers = self.freezer_headers)
        freezer = json.loads(resp_freezer_setting.content)
        current_freezer_temp = freezer['data']['value']
        print("The current temperature is {} °C".format(current_freezer_temp))

        # This Clarifies that you want to change temperature
        ans1 = Would_input()

        if ans1.lower() == 'yes':
            # set bounds of min and max
            value = int(temp_input())
            while value < -24 or value > -16:
                print('The bounds are {} and {} try again'.format(self.freezer_min, self.freezer_max))
                value = int(temp_input())
            data = data = '{ "data": { "key": "Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer", "value": %d, "type": "Double", "unit": "\xB0C", "constraints": { "min": -24, "max": -16 } }}' % (value)
            done = requests.put(freezer_url, headers = self.freezer_headers, data = data)
            print('Changing temperature to {} °C '.format(value))
        else:
            print("Error")

    ### function that changes fridge temp
    def change_fridge_temp(self):
        HAID = HAID_input()
        fridge_url = 'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator' % (HAID)

         # This section gets the current temperature
        resp_fridge_setting = requests.get(fridge_url, headers = self.fridge_headers)
        fridge = json.loads(resp_fridge_setting.content)
        current_fridge_temp = fridge['data']['value']
        print("The current temperature is {} °C".format(current_fridge_temp))

        # This Clarifies that you want to change temperature
        ans1 = Would_input()

        if ans1.lower() == 'yes':
            # set bounds of min and max
            value = int(temp_input())
            while value < 2 or value > 8:
                print('The bounds are {} and {} try again'.format(self.fridge_min, self.fridge_max))
                value = int(temp_input())
            data = '{ "data": { "key": "Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator", "value": %d, "type": "Double", "unit": "\xB0C", "constraints": { "min": 2, "max": 8 } }}' % (value)
            done = requests.put(fridge_url, headers = self.fridge_headers, data = data)
            print('Changing temperature to {} °C '.format(value))
        else:
            print("Error")
class SQL:

    def Create(self):
        conn = sqlite3.connect('BSHtwo.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Date TEXT, Name TEXT, HAID TEXT, Command TEXT)')

    def Data(self):
        conn = sqlite3.connect('BSHtwo.db')
        c = conn.cursor()
        date = Date_input()
        name = Name_input()
        HAID = HAID_input()
        command = Action_input()
        c.execute("INSERT INTO RecordONE (Date, Name, HAID, Command) VALUES(?, ?, ?, ?)", (date, name, HAID, command))
        conn.commit()
        c.close()
        conn.close()

    def Print(self):
        db = sqlite3.connect('BSHtwo.db')
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table_name in tables:
            table_name = table_name[0]
            table = pd.read_sql_query("SELECT * from %s" % table_name, db)
            print(table)











btn=Button(window, text="Change Freezer Temperature", fg='blue', width = 25, height = 25, command = change_settings().change_freezer_temp)
btn.grid(column=0, row=0)

btn2 = Button(window, text="Change Fridge Temperature", fg='blue', width = 25, height = 25, command = change_settings().change_fridge_temp)
btn2.grid(column=1, row=0)

btn3=Button(window, text="Get Settings", fg='blue',width = 25, height = 25)
btn3.grid(column=2, row=0)

btn4 = Button(window, text="Get Fridge Settings", fg='blue',width = 25, height = 25, command = settings().get_fridge_settings)
btn4.grid(column=3, row=0)

btn5=Button(window, text="Get Freezer Settings", fg='blue',width = 25, height = 25, command = settings().get_freezer_settings)
btn5.grid(column=0, row=1)

btn6 = Button(window, text="Get SQL data", fg='blue',width = 25, height = 25)
btn6.grid(column=1, row=1)

btn7=Button(window, text="This is Button widget", fg='blue',width = 25, height = 25)
btn7.grid(column=2, row=1)

btn8 = Button(window, text="Exit", fg='blue',width = 25, height = 25)
btn8.grid(column=3, row=1)

window.title('Hello Python')
window.geometry("1000x810")
window.mainloop()
