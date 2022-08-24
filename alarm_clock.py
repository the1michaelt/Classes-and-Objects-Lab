class AlarmClock:
    def __init__(self): #constructor; instance variables below; what is has.
        self.time="" # current time = ""
        self.alarm_status= ["on", "off"] # whether the alarm is on or off =['on','off']
        self.alarm_time= "# time the alarm is set to = ""
        
    def current_time(self): #methods; what it can do.
        time= '12:00'
        print(f'The current time is ', {time})
        return time
        
    def set_or_change_current_time(self, time):
        want_change= input('Would you like to change the time? y/n')
        if want_change=='y':
            change_time = input('What time would you like to set? ')
            time= time.append(change_time)
            return time
        else:
            print(f'Your time remains ', {time})
    
    def turn_alarm_on_off(self, alarm_status):
        alarm_status= 'Off'
        want_change = input('Would you like to turn on alarm? y/n')
        if want_change == 'y':
            alarm_status = 'On'
            Print ('Your alarm is now ',{alarm_status})
            return alarm_status
        else:
            print(f'Your alarm remains ', {alarm_status})
        
            
    def time_of_alarm(self, alarm_time):
        alarm_time= '15:00'
        print("Your alarm is set to ", {alarm_time})
        return alarm_time
    
    def set_or_change_alarm_time(self, alarm_time):
        want_change = input('Would you like to turn on alarm? y/n')
        if want_change == 'y':
            change_alarm = input('What time would you like to be your alarm? ')
            Print('Your alarm is now ', {alarm_time})
            return alarm_time
    

# class variables to keep track of the AlarmClock’s 
# current time, 
# whether the alarm is on or off,  
# time the alarm is set to.
# NOTE: You can use arbitrary strings to represent the time, it does not need to be accurate or change over time

# method to set (or change) the current time and 
# print to the console the current time. return ___

# toggle the alarm on or off. 

# a method to set the current alarm time  input?
# and print to the console the current alarm time.  print or return ()

# import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# Print the clock’s time to the terminal print(___)

# Call the alarm clock’s change time method to change the time

