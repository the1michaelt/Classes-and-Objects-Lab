from alarm_clock import AlarmClock

# inquiry_one= AlarmClock()
one_display_time = AlarmClock("12:00","","","","")
one_display_time.current_time()  # function to display time

two_change_time= AlarmClock("","y","","","")
two_change_time.set_or_change_current_time()  # change time

three_change_alarm = AlarmClock("","","y","","")
three_change_alarm.set_or_change_alarm_time()  # change alarm

four_alarm_time= AlarmClock("","","","15:00","")
four_alarm_time.time_of_alarm() #display alarm time

five_alarm_status= AlarmClock("","","","","off")
five_alarm_status.turn_alarm_on_off()  # display alarm status

# # # Three objects
# #        self.time = "" # current time = ""
# #        # whether the alarm is on or off =['on','off']
# #        self.alarm_status = ["on", "off"]
# #        self.alarm_time =

# # # class variables to keep track of the AlarmClock’s
# # # current time,
# # # whether the alarm is on or off,
# time the alarm is set to.
# NOTE: You can use arbitrary strings to represent the time, it does not need to be accurate or change over time

# # # method to set (or change) the current time and
# # # print to the console the current time. return ___

# # # toggle the alarm on or off. 

# # # a method to set the current alarm time  input?
# # # and print to the console the current alarm time.  print or return ()

# # # import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.

# # # Print the clock’s time to the terminal print(___)

# # # Call the alarm clock’s change time method to change the time
