import pyautogui as au
import keyboard as kb
import time
#queue for the answer order
queue = []
counter = 1

def click_buttons_in_order(button_set):
    while not len(button_set)==0:
        temp_button = button_set.pop(0)
        print(f"Dequeued button {temp_button.name}")
        temp_button.click()
        #then move the cursor away from the button
        au.move(-500,0)
        time.sleep(0.5)
        
def scan_buttons(button_set):
    while True:
        #scan each button one by one
        for button in button_set:
            #if the color changed, add it to the queue
            if not button.same_color():
                queue.append(button)
                print(f"Added {button.name}")
                #wait till the color doesn't go dark again
                while not button.same_color():
                    #print("Waiting for the color to go dark")
                    continue
                #exit the loop once the color change was detected
                return
            
#button class
class Button:
    def __init__(self,name="None",x=0,y=0) -> None:
        self.name = name
        self.color = None
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Color: {self.name} | X,Y: ({self.x},{self.y} | Value: {self.color})"

    #set coordinates for given button 
    def set_coordinates(self) -> None:
        x,y = au.position()
        self.x = x
        self.y = y
        self.color = au.pixel(x,y)

    def click(self) -> None:
        au.click(self.x,self.y)
        
    #listen for the z key to be pressed, then set coordinates for the button to the location of the mouse 
    def lock_coordinates(self) -> None:
        print(f"Listening for {self.name} coordinates. Press z to lock in.")
        while True:
            if kb.is_pressed('z'):
                self.set_coordinates()
                print(f"Coordinates of {self.name}: X:{self.x} Y:{self.y}\n")
                time.sleep(0.2)
                break

    def same_color(self) -> bool:
        return self.color == au.pixel(self.x, self.y)
    
if __name__=="__main__":
    print("Main")
    #button instances
    red = Button("Red")
    blue = Button("Blue")
    yellow = Button("Yellow")
    green = Button("Green")
    buttons = [green, red, blue, yellow]
    
    #set the coordinates for each button
    for button in buttons:
        button.lock_coordinates()
    print("Now start the game!")
    #start the game
    while True:
        #after starting the game, scan each color change
        for turn in range(counter):
            scan_buttons(buttons)   
        #print the current state of the button queue
        print(f"Current button queue: "+", ".join([button.name for button in queue]))
        #click the buttons in order
        time.sleep(0.5)
        click_buttons_in_order(queue)
        counter+=1
        queue.clear()
        a=0