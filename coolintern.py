import requests
import json
import sqlite3 
import pandas as pd

# This Class gets settings
class settings:
    auth_key =''
    fridge_headers = {'accept': 'application/vnd.bsh.sdk.v1+json','Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}
    freezer_headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}

    # This Function gets all settings of an appliance
    def get_settings(self):
        HAID = input("What is your home appliance ID? ")
        url_setting = 'https://simulator.home-connect.com/api/homeappliances/%s/settings' % (HAID)
        resp_setting =  requests.get(url_setting,headers=self.setting_headers)
        settings = json.loads(resp_setting.content)
        print(settings['data']['settings'])

    # This Function gets all settings of the freezer
    def get_freezer_settings(self):
        HAID = input("What is your home appliance ID? ")
        url_freezer_setting = 'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer' % (HAID)
        resp_freezer_setting = requests.get(url_freezer_setting, headers = self.setting_headers)
        freezer = json.loads(resp_freezer_setting.content)

        # this makes the dictionary data more readable
        raw_data = freezer['data']
        setting = raw_data['key']
        temp = raw_data['value']
        unit = raw_data['unit']
        constraints = raw_data['constraints']

        print("The current settings available are ({}) ".format(setting))
        print("The current temperature is {} {} ".format(temp, unit))
        print("The constraints are {} ".format(constraints))

    # This Function gets all settings of a fridge
    def get_fridge_settings(self):
        HAID = input("What is your home appliance ID? ")
        url_fridge_setting=  'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator' % (HAID)
        resp_fridge_setting = requests.get(url_fridge_setting, headers = self.setting_headers)
        fridge = json.loads(resp_fridge_setting.content)

        # This makes the dictionary data more readable
        raw_data = fridge['data']
        setting = raw_data['key']
        temp = raw_data['value']
        unit = raw_data['unit']
        constraints = raw_data['constraints']

        print("The current settings available are ({}) ".format(setting))
        print("The current temperature is {} {} ".format(temp, unit))
        print("The constraints are {} ".format(constraints))




# This class changes settings
class change_settings:
    auth_key ='Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6MTksIngtcmVnIjoiRVUiLCJ4LWVudiI6IlNJTSJ9.eyJzdWIiOjEyMzkwLCJleHAiOjE2MDgxMjM3MzUsInNjb3BlIjpbIklkZW50aWZ5QXBwbGlhbmNlIiwiRnJpZGdlRnJlZXplci1TZXR0aW5ncyIsIkZyaWRnZUZyZWV6ZXItQ29udHJvbCJdLCJhenAiOiI0NTIwOTE0QUY0Q0E4MjAxREU2NDZGRjRFRkU4OEQwRDkwODk1NzdBMDYwRjE3RjNCMzJBODIzNEJENEQzRDQzIiwiYXVkIjoiNDUyMDkxNEFGNENBODIwMURFNjQ2RkY0RUZFODhEMEQ5MDg5NTc3QTA2MEYxN0YzQjMyQTgyMzRCRDREM0Q0MyIsInBybSI6W10sImlzcyI6ImV1OnNpbTpvYXV0aDoxIiwianRpIjoiOWEyMGM4ZjAtOTc3MC00NzkyLTkyNWItYzc2ZTk0NTRkN2QxIiwiaWF0IjoxNjA4MDM3MzM1fQ.VefqOqYu_uihASVlzQNKgUb-j2JJDWO0xDf_w8pPTxJaXoQ75oHrFG3MeAhKRVfk7cXVRHFtAkfstGdawdA9Ow'
    freezer_headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}
    fridge_headers = {'accept': 'application/vnd.bsh.sdk.v1+json','Accept-Language': 'en-US','authorization': auth_key,'Content-Type': 'application/vnd.bsh.sdk.v1+json',}
    freezer_min = -24 # bounds for changing freezer temp
    freezer_max = -16
    fridge_min = 2 # bounds for changing fridge temp
    fridge_max = 8

    def change_freezer_temp(self):
        HAID = input("What is your home appliance ID? ")
        freezer_url = 'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer' % (HAID)

        # This section gets the current temperature
        resp_freezer_setting = requests.get(freezer_url, headers = self.freezer_headers)
        freezer = json.loads(resp_freezer_setting.content)
        current_freezer_temp = freezer['data']['value']
        print("The current temperature is {} °C".format(current_freezer_temp))

        # This Clarifies that you want to change temperature
        ans1 = input('Would you like to change the temperature? ')

        if ans1.lower() == 'yes':
            # set bounds of min and max
            value = int(input('What would you like to set the temperature to? '))
            while value < -24 or value > -16:
                print('The bounds are {} and {} try again'.format(self.freezer_min, self.freezer_max))
                value = int(input('What would you like to set the temperature to? '))
            data = data = '{ "data": { "key": "Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer", "value": %d, "type": "Double", "unit": "\xB0C", "constraints": { "min": -24, "max": -16 } }}' % (value)
            done = requests.put(freezer_url, headers = self.freezer_headers, data = data)
            print('Changing temperature to {} °C '.format(value))
        else:
            print("Error")

    ### function that changes fridge temp
    def change_fridge_temp(self):
        HAID = input("What is your home appliance ID? ")
        fridge_url = 'https://simulator.home-connect.com/api/homeappliances/%s/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator' % (HAID)

         # This section gets the current temperature
        resp_fridge_setting = requests.get(fridge_url, headers = self.fridge_headers)
        fridge = json.loads(resp_fridge_setting.content)
        current_fridge_temp = fridge['data']['value']
        print("The current temperature is {} °C".format(current_fridge_temp))

        # This Clarifies that you want to change temperature
        ans1 = input('Would you like to change the temperature? ')

        if ans1.lower() == 'yes':
            # set bounds of min and max
            value = int(input('What would you like to set the temperature to? '))
            while value < 2 or value > 8:
                print('The bounds are {} and {} try again'.format(self.fridge_min, self.fridge_max))
                value = int(input('What would you like to set the temperature to? '))
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
        date = input("Enter today's date: ")
        name = input("Enter your name: ")
        HAID = input("Enter the HAID #: ")
        command = input("Enter the command used: ")
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

answer = "yes"
command_list = ["Exit", "Get SQL Data", "Change Freezer Temperature", "Change Fridge Temperature", "Get Settings", "Get Fridge Settings", "Get Freezer Settings"]

settings = settings()
settings_change = change_settings()
SQL = SQL()
while answer.lower() == "yes":


  print("The current commands are {} ".format(command_list))
  command = input("What would you like to do? ")

  # make temperature class
  if command.lower() == "change freezer temperature":
    settings_change.change_freezer_temp()
    
    # ask for name, maybe say name = input()
    # make time stamp timestamp = currenttime()
    # get what they did  action = change freezer temp
    # Enter into SQL data base, Enter(name, action, timestamp)

  if command.lower() == "change fridge temperature":
    settings_change.change_fridge_temp()
    SQL.Create()
    SQL.Data()
    # SQL Function
  if command.lower() == "get settings":
    settings.get_settings()
    SQL.Create()
    SQL.Data()
    # SQL Function
  if command.lower() == "get fridge settings":
    settings.get_fridge_settings()
    SQL.Create()
    SQL.Data()
    # SQL Function
  if command.lower() == "get freezer settings":
    settings.get_freezer_settings()
    SQL.Create()
    SQL.Data()
  if command.lower() == "get sql data":
    SQL.Print()
    # SQL Function
  if command.lower() == "exit":
    break

  else:
    answer = input("Would you like to continue? " )
