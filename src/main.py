import pyautogui as au
import keyboard
#queue for the answer order
queue = []

buttons = set()

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
        buttons.add(self)

    def click(self) -> None:
        au.click(self.x,self.y)


if __name__=="__main__":
    print("Main")
    red = Button("Red")
    red.set_coordinates()
    print(red)
    hold = au.screenshot()
    a=0