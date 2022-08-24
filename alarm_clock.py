class AlarmClock:
    def __init__(self, time): #constructor; instance variables below; what is has.
        self.time= time # current time = ""
        self.alarm_status= ["on", "off"] # whether the alarm is on or off =['on','off']
        self.alarm_time= "" # time the alarm is set to
        
# inquiry_one = AlarmClock("12:00")
# inquiry_one.time()  # display time
    def current_time(self):  # methods; what it can do.
        print(f'The current time is ', self.time)
        
        
# inquiry_two = AlarmClock()
# inquiry_two.time  # change time
    def set_or_change_current_time(self):
        want_change= input('Would you like to change the time? y/n ')
        if want_change=='y':
            time= '12:00'
            change_time = input('What time would you like to set? ')
            print(f'Your time is now ', change_time)
            # return time
        else:
            print(f'Your time remains ', time)

# inquiry_three = AlarmClock()
# inquiry_three.alarm_status  # display alarm status
    def turn_alarm_on_off(self, alarm_status):
        # alarm_status= 'Off'
# inquiry_four = AlarmClock()
# inquiry_four.alarm_time  # change alarm status
        want_change = input('Would you like to turn on alarm? y/n')
        if want_change == 'y':
            change_alarm_status = 'On'
            Print ('Your alarm is now ',change_alarm_status)
            # return change_alarm_status
        else:
            print(f'Your alarm remains ', change_alarm_status)
        
# inquiry_five = AlarmClock()
# inquiry_five.alarm_time  # display alarm time
    def time_of_alarm(self, alarm_time):
        # alarm_time= '15:00'
        print("Your alarm is set to ", alarm_time)
        # return alarm_time

# inquiry_six = AlarmClock()
# inquiry_six.alarm_time  # change alarm
    def set_or_change_alarm_time(self, alarm_time):
        want_change = input('Would you like to change your alarm? y/n')
        if want_change == 'y':
            change_alarm = input('What time would you like to be your alarm? ')
            Print('Your alarm is now ', change_alarm)
            # return change_alarm
    

# # class variables to keep track of the AlarmClock’s 
# # current time, 
# # whether the alarm is on or off,  
# # time the alarm is set to.
# # NOTE: You can use arbitrary strings to represent the time, it does not need to be accurate or change over time

# # method to set (or change) the current time and 
# # print to the console the current time. return ___

# # toggle the alarm on or off. 

# a method to set the current alarm time  input?
# and print to the console the current alarm time.  print or return ()

# import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# Print the clock’s time to the terminal print(___)

# Call the alarm clock’s change time method to change the time

