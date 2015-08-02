# implementation of card game - Memory

import simplegui
import random

char_width=50

# helper function to initialize globals
def init():
    global numbers, exposed, move, state, card1, card2
    numbers = [i%8 for i in range(16)]
    random.shuffle(numbers)
    exposed = [False for i in range(len(numbers))]
    move=0
    state=0
    card1=""
    card2=""
    l.set_text("Moves = " + str(move))

def isPaired():
    return numbers[card1]==numbers[card2]
     
# define event handlers
def mouseclick(pos):
    global state, card1, card2, move
    # state 0 is unopened cards
    idx=pos[0]//char_width
    if state==0:
        exposed[idx]=True
        card1=idx
        state=1
    # state 1 is 1 opened card   
    elif state==1:
        if exposed[idx]==False:
            exposed[idx]=True
            card2=idx
            state=2
            move+=1
            l.set_text("Moves = " + str(move))
    # state 2 is 2 opened cards        
    elif state==2: 
        if exposed[idx]==False:
            if isPaired()==False:
                exposed[card1]=False
                exposed[card2]=False
            exposed[idx]=True
            card1=idx
            card2=""
            state=1  
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    first_width=0
    canvas.draw_line((first_width,0) , (first_width, 100), 1, "Red")
    for i in range(len(numbers)):
        if exposed[i]==True:
            canvas.draw_text(str(numbers[i]), (first_width+5, 80), 60, "White")
        else:
            canvas.draw_line((first_width + char_width//2, 0),(first_width+char_width//2, 100), 48, "Green")
       
        canvas.draw_line((first_width + char_width,0) , (first_width + char_width, 100), 1, "Red")
        first_width+=char_width
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
