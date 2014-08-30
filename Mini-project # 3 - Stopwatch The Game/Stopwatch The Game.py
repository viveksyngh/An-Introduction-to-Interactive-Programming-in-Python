# template for "Stopwatch: The Game"

# define global variables
import simplegui
counter = 0
total = 0
hit = 0
status = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t = int(t)
    second = t/10
    fraction_of_sec = t%10
    minute = second/60
    second = second%60
    string = str(minute) + ":"
    if second == 0 :
        string = string + "00"
    elif  0 < second < 10 :
        string = string + "0" + str(second)
    else :
        string = string + str(second)
        
    string = string + "." + str(fraction_of_sec)
    return string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start() :
    global status
    timer.start()
    status = timer.is_running()
    
    
def Stop() :
    global total,hit,status
    if status == True :
        total = total + 1
        if counter%10 == 0 :
            hit = hit + 1
    timer.stop()
    status = timer.is_running()
       

def Reset() :
    global total,hit
    total = 0
    hit = 0
    timer.stop()
    global counter 
    counter = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler() :
    global counter 
    counter = counter + 1
    
    
# define draw handler
def draw_handler(canvas) :
    global counter
    canvas.draw_text(format(str(counter)),[100,100],32,"Red")
    canvas.draw_text(str(hit) + "/" + str(total),[220,25],32,"Red")
# create frame

frame = simplegui.create_frame("Home",300,200)

# register event handlers

timer = simplegui.create_timer(100,timer_handler)
frame.add_button("Start",Start,100)
frame.add_button("Stop",Stop,100)
frame.add_button("Reset",Reset,100)
frame.set_draw_handler(draw_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
