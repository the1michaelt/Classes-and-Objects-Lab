from time import time


class AlarmClock:
    # constructor; instance variables below; what is has.
    def __init__(self, time, time_change_YN, alarm_time, alarm_status_off, alarm_change_YN):
        self.time = time  # default time # one_display_time = AlarmClock
        self.time_change_YN = time_change_YN  # two_change_time = AlarmClock
        # alarm on off         # three_alarm_status = AlarmClock # whether the alarm is on or off =['on','off']
        self.alarm_time = alarm_time  # four_alarm_time set  #
        self.alarm_status_off = alarm_status_off
        self.alarm_change_YN = alarm_change_YN  # five_change_alarm.set_or_change_alarm_time()  #
        
# inquiry_one = AlarmClock("12:00") # inquiry_one.time()  # display time
    def current_time(self):  # methods; what it can do.
        print('The default time is ', self.time)
       
    
# inquiry_two = AlarmClock() # inquiry_two.time  # change time
    def set_or_change_current_time(self):  
        want_change= input('Would you like to change the default time? y/n ')
        if want_change == 'y':
            change_time = input('What time would you like to set? Enter one between 0:00-23:59.')
            print('Your time is now ',change_time)
        else:
            print('Your time remains ', self.time)

# inquiry_three = AlarmClock() # inquiry_five.alarm_time  # change alarm
    def set_or_change_alarm_time(self):
        want_change = input('Would you like to change your alarm? y/n ')
        if want_change == 'y':
            change_alarm = input('What time would you like to be your alarm? Enter time 0:00-23:59 ')
            print('Your alarm is now ', change_alarm)
      
# inquiry_four = AlarmClock() # inquiry_four.alarm_time  # display alarm time
    def time_of_alarm(self):
        print("Your default alarm is set to ", alarm_time)
        alarm_status = input('Would you like to change the default time? y/n ')
        if alarm_status == 'y':
            change_time = input('What time would you like to set? Enter one between 0:00-23:59.')
            print('Your alarm is now ', change_time)
        else:
            print('Your alarm remains at ', alarm_time )

# inquiry_five = AlarmClock() # inquiry_three.alarm_status  # display alarm status
    def turn_alarm_on_off(self):
        want_change = input('Would you like to turn on an alarm? y/n ')
        if want_change != 'y':
            print('Your alarm remains Off.')
        else:
            print('Your alarm is now On.')
            
# one_display_time = AlarmClock("12:00", "", "", "", "")
# one_display_time.current_time()  # function to_display_time

# two_change_time = AlarmClock("", "Y", "", "", "")
# two_change_time.set_or_change_current_time()  # change_time

# three_alarm_status = AlarmClock("", "", "off", "", "")
# three_alarm_status.turn_alarm_on_off()  # display_alarm_status

# four_alarm_time = AlarmClock("", "", "", "15:00", "")
# four_alarm_time.time_of_alarm()  # display_alarm_time

# five_change_alarm = AlarmClock("", "", "", "", "Y")
# five_change_alarm.set_or_change_alarm_time()  # change_alarm



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

# ("12:00") == time
# one_display_time== object  
# # .current_time() # function to display time

# ("Y") == change_time
# two_change_time.set_or_change_current_time()  # 

# ("off") == display_alarm_status
# three_alarm_status.turn_alarm_on_off()  # 

# ("15:00")== display_alarm_time
# four_alarm_time.time_of_alarm()  # 

# ("Y") ==  new_alarm_time
# five_change_alarm.set_or_change_alarm_time()  # 


