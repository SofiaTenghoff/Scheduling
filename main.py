# import the Tkinter package as tk
import tkinter as tk

# import the date class and the datetime class from the datetime module
from datetime import date, datetime

# establish morning primetime as its own variable
one_prime_time = "morning prime time"

#establish unity as its own variable
unity = "unity meeting/assembly"

# establish period one as its own variable
period_one = "period one"

# establish period 2 as its own variable
period_two = "period two"

# establish period 3 as its own variable
period_three = "period three"

#establish period 4 as its own variable
period_four = "period four"

#establish homeroom as its own variable
homeroom = "home room"

#establish lunch as its own variable
lunch = "lunch"

# establish period 5 as its own variable
period_five = "period five"

#establish period 6 as its own variable
period_six = "period six"

#establish afternoon primetime as a variable
two_prime_time = "afternoon prime time"


# make current_time equal time without the date

current_datetime = datetime.now()

current_time = current_datetime.replace(year=2024, month=1, day=1)

def stringToDatetime(str_time):
   return datetime.strptime(str_time, "%H:%M")


# make timedifference equal class start time(blocksched value) minus current time
def timedifference(blocksched):

    class_time = stringToDatetime(blocksched).replace(year=2024, month=1, day=1)
    difference = class_time - current_time
    return difference.total_seconds() / 60

    if (stringToDatetime(blocksched[0]) or stringToDatetime(blocksched[1]) or stringToDatetime(blocksched[2]) or stringToDatetime(blocksched[3]) or stringToDatetime(blocksched[4]) or stringToDatetime(blocksched[5]) or stringToDatetime(blocksched[6])) - current_time <= 10:
        return blocksched - current_time


# ensure that the buttons actually update labels
def update_label(label, message):
    label.config(text=message)

# establish Asched as a function that tells you how long it is until each class of the A schedule starts
def Asched():
    messages = []
    if timedifference("07:45") <= 10:
        messages.append("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("7:45")))
        if timedifference("08:30") <= 10:
            messages.append("Hey queen, %s starts in %d minutes!" 
                  % (period_one, timedifference("8:30")))
            if timedifference("09:50") <= 10:
                messages.append("Hey queen, %s starts in %d minutes!" 
                      % (unity, timedifference("9:50")))
                if timedifference("11:10") <= 10:
                    messages.append("Hey queen, %s starts in %d minutes!" 
                          % (period_four, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        messages.append("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            messages.append("Hey queen, %s starts in %d minutes!" 
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                messages.append("Hey queen, %s starts in %d minutes!" 
                                      % (period_five, timedifference("1:35")))
                                if timedifference("02:45") <= 10:
                                    messages.append("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("2:45")))
                                    return "/n".join(messages)

# establish Bsched as a function that tells you how long it is until each class of the B schedule starts
def Bsched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!"
              % (one_prime_time, timedifference("7:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_one, timedifference("8:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_three, timedifference("9:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_two, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (period_six, timedifference("1:35")))
                                if timedifference("02:45") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("02:45")))

# establish Csched as a function that tells you how long it is until each class of the C schedule starts 
def Csched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_two, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_three, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_four, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (period_five, timedifference("01:35")))
                                if timedifference("02:45") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("02:45")))

# establish Dsched as a function that tells you how long it is until each class of the D schedule starts
def Dsched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_one, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_five, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_four, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (period_six, timedifference("01:35")))
                                if timedifference("02:45") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("02:45")))

# establish Esched as a function that tells you how long it is until each class of the E schedule starts
def Esched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_two, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_three, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (unity, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Hey queen, %s starts in %d minutes!" 
                              % (lunch, timedifference("12:30")))
                        if timedifference("01:35") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                  % (period_six, timedifference("01:35")))
                            if timedifference("02:45") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (two_prime_time, timedifference("02:45")))

# establish Esched_early_dismissal as the early dismissal Friday schedule:
def Esched_early_dismissal():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_two, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_three, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_six, timedifference("11:10"))) 

# establish Fsched as a function that tells you how long it is until each class of the F schedule starts(remember F, D,then G)
def Fsched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_one, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!"
                      % (period_three, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_two, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            print("Hey queen, %s starts in %d minutes!"
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (period_four, timedifference("01:35")))
                                if timedifference("02:45") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("02:45")))

# establish Dsched as a function
def Dsched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_one, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_five, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_four, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (period_six, timedifference("01:35")))
                                if timedifference("02:45") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("02:45")))

# establish Gsched as a function
def Gsched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
              % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                  % (period_two, timedifference("08:30")))
            if timedifference("09:50") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                      % (period_three, timedifference("09:50")))
                if timedifference("11:10") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                          % (period_five, timedifference("11:10")))
                    if timedifference("12:30") <= 10:
                        print("Sorry...you have %s in %d minutes" 
                              % (homeroom, timedifference("12:30")))
                        if timedifference("12:45") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                  % (lunch, timedifference("12:45")))
                            if timedifference("01:35") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                      % (period_six, timedifference("01:35")))
                                if timedifference("02:45") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                          % (two_prime_time, timedifference("02:45")))




# establish Hsched as a function
def Hsched():

    if timedifference("07:45") <= 10:
        print("Hey queen, %s starts in %d minutes!" 
            % (one_prime_time, timedifference("07:45")))
        if timedifference("08:30") <= 10:
            print("Hey queen, %s starts in %d minutes!" 
                % (period_one, timedifference("08:30")))
            if timedifference("09:25") <= 10:
                print("Hey queen, %s starts in %d minutes!" 
                    % (period_four, timedifference("09:25")))
                if timedifference("10:20") <= 10:
                    print("Hey queen, %s starts in %d minutes!" 
                        % (period_three, timedifference("10:20")))
                    if timedifference("11:15") <= 10:
                        print("Hey queen, %s starts in %d minutes!" 
                            % (period_two, timedifference("11:15")))
                        if timedifference("12:10") <= 10:
                            print("Hey queen, %s starts in %d minutes!" 
                                % (period_five, timedifference("12:10")))
                            if timedifference("12:55") <= 10:
                                print("Hey queen, %s starts in %d minutes!" 
                                    % (lunch, timedifference("12:55")))
                                if timedifference("02:00") <= 10:
                                    print("Hey queen, %s starts in %d minutes!" 
                                        % (period_six, timedifference("02:00")))
                                    if timedifference("02:45") <= 10:
                                        print("Hey queen, %s starts in %d minutes!" 
                                            % (two_prime_time, timedifference("02:45")))


'''
# import the Tkinter package as tk
import tkinter as tk

# import the date class from the datetime module
from datetime import date
'''

# define Monday as day 0 of the week
Monday = date(2024, 6, 3).weekday()

# define Tuesday as day 1 of the week
Tuesday = date(2024, 6, 4).weekday()

# define Wednesday as day 2 of the week
Wednesday = date(2024, 6, 5).weekday()

# define Thursday as day 3 of the week
Thursday = date(2024, 6, 6).weekday()

# define Friday as day 4 of the week
Friday = date(2024, 6, 7).weekday()

# create a graphic user interface window
window = tk.Tk()

# define a function that displays what will be printed when the button is clicked
def norm_button_clicked():

    messages = []
    if date.today().weekday() == Monday:
        messages = Asched()
    if date.today().weekday() == Tuesday:
        messages = Bsched()
    if date.today().weekday() == Wednesday:
        messages = Csched()
    if date.today().weekday() == Thursday:
        messages = Dsched()
    if date.today().weekday() == Friday:
        messages = Esched
    update_label(output_label, messages)
    
# create the normal button
norm_button = tk.Button(window, text="Normal Five Day Week", 
    command=norm_button_clicked)

norm_button.grid(column = 1, row =1)

# output label
output_label = tk.Label(window, text = "")
output_label.grid(column=1, row=3, columnspan=3)

def four_day_H_Monday():
    messages = []
    if date.today().weekday() == Monday:
       messages = Hsched()
    if date.today().weekday() == Tuesday:
       messages = Fsched()
    if date.today().weekday() == Wednesday:
        messages = Dsched()
    if date.today().weekday() == Thursday:
        messages = Gsched()
    update_label(output_label, messages)

# define a function that explains what will happen when the four day week with H Monday is clicked
H_Monday_button = tk.Button(window, text="Four-day Week with H schedule on Monday", 
    command=four_day_H_Monday)

def four_day_H_Tuesday():
    messages = []
    if date.today().weekday() == Tuesday:
        messages = Hsched()
    if date.today().weekday() == Wednesday:
        messages = Fsched()
    if date.today().weekday() == Thursday:
        messages = Dsched()
    if date.today().weekday() == Friday:
        messages = Gsched()
    update_label(output_label, messages)
# define a function that explains what will happen when the four day week with H Tuesday is clicked
# define the message that the H Tuesday button displays
H_Tuesday_button = tk.Button(window, text="Four-day Week with H schedule on Tuesday", 
                             command=four_day_H_Tuesday)


# define a function that explains what will happen when the four day week with H Thursday is clicked
def four_day_H_Thursday():
    messages = []
    if date.today().weekday() == Monday:
        messages = Fsched()
    if date.today().weekday() == Tuesday:
        messages = Dsched()
    if date.today().weekday() == Wednesday:
        messages = Gsched()
    if date.today().weekday() == Thursday:
        messages = Hsched()
    update_label(output_label, messages)
# define the message that the H Thursday button displays
H_Thursday_button = tk.Button(window, text="Four-day Week with H schedule on Thursday", 
                              command=four_day_H_Thursday)


# define a function that explains what will happen when the four day week with H Friday is clicked
def four_day_H_Friday():
    messages = []
    if date.today().weekday() == Tuesday:
        messages = Fsched()
    if date.today().weekday() == Wednesday:
        messages = Dsched()
    if date.today().weekday() == Thursday:
        messages = Gsched()
    if date.today().weekday() == Friday:
        messages = Hsched()
    update_label(output_label, messages)
# define the message that the H Friday button displays
H_Friday_button = tk.Button(window, text="Four-day Week with H schedule on Friday", 
                            command=four_day_H_Friday)


# define a function that explains what will happen when five day week with early dismissal Friday is clicked
def early_dismissal_Fri():
    messages = []
    if date.today().weekday() == Monday:
        messages = Asched()
    if date.today().weekday() == Tuesday:
        messages = Bsched()
    if date.today().weekday() == Wednesday:
        messages = Csched()
    if date.today().weekday() == Thursday:
        messages = Dsched()
    if date.today().weekday() == Friday:
        messages = Esched_early_dismissal()
    update_label(output_label, messages)
# define the message that the early dismissal button displays
Early_dismissal_button = tk.Button(window, text="Five-day Week with Early Dismissal on Friday", 
                                   command=early_dismissal_Fri)



    
# create a variable for the frame from my window
frame = tk.Frame(window, width=10, height=10)
#frame.pack()
# create a grid for your buttons with 10 units of space in between each button
frame.grid(row=3, column=3, padx=10, pady=10)

# specify the placement and dimensions of the normal week button
norm_button = tk.Button(window, text="Normal Five Day Week", 
    command=norm_button_clicked)
norm_button.grid(column=1, row=1)

# specify the placement and dimensions of the H Monday button
H_Monday_button = tk.Button(window, text="Four-day Week with H schedule on Monday", 
    command=four_day_H_Monday)
H_Monday_button.grid(column=2, row=1)

# specify the placement and dimensions of the H Tuesday button
H_Tuesday_button = tk.Button(window, text="Four-day Week with H schedule on Tuesday", 
     command=four_day_H_Tuesday)
H_Tuesday_button.grid(column=3, row=1)

# specify the placement and dimensions of the H Thursday button
H_Thursday_button.grid(column=1, row=2)

# specify the placement and dimensions of the H Friday button
H_Friday_button.grid(column=2, row=2)

# specify the placement and dimensions of the early dismissal button
Early_dismissal_button.grid(column=3, row=2)

window.mainloop()


print("test")