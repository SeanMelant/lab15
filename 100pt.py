#########################################
#
#    100pt - Putting it together!
#
#########################################

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=480,height=320, background='purple')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="yellow")
oldYeller = drawpad.create_rectangle(240,240,260,260, fill="yellow")
direction = 4
class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "blue")
		self.up.grid(row=0,column=0)											
		self.up.bind("<Button-1>", self.moveUp)
                self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "orange")
		self.down.grid(row=0,column=1)												
		self.down.bind("<Button-1>", self.moveDown)
                self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "blue")
		self.left.grid(row=0,column=2)												
		self.left.bind("<Button-1>", self.moveLeft)
                self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "orange")
		self.right.grid(row=0,column=3)												
		self.right.bind("<Button-1>", self.moveRight)
		drawpad.pack()
		self.animate()
	def moveUp(self, event):   
		global oldYeller
		x1,y1,x2,y2 = drawpad.coords(oldYeller)
	        if y1 >= 0 and y2 <= drawpad.winfo_height():
	           drawpad.move(oldYeller,0,-10)
        def moveDown(self, event):   
		global oldYeller
		x1,y1,x2,y2 = drawpad.coords(oldYeller)
	        if y1 >= 0 and y2 <= drawpad.winfo_height():
	           drawpad.move(oldYeller,0,10)
        def moveLeft(self, event):   
		global oldYeller
		x1,y1,x2,y2 = drawpad.coords(oldYeller)
	        if x1 >= 0 and x2 <= drawpad.winfo_width():
	           drawpad.move(oldYeller,-10,0)
        def moveRight(self, event):   
	    global oldYeller
	    x1,y1,x2,y2 = drawpad.coords(oldYeller)
	    if x1 >= 0 and x2 <= drawpad.winfo_width():
	        drawpad.move(oldYeller,10,0)
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)   
            if tx1 <= 0:
                direction = 10
            elif tx2 >= drawpad.winfo_width():
                direction = -10               
            drawpad.move(target,direction,0)
            didWeHit = self.collisionDetect()
            if didWeHit == False:
                drawpad.after(1,self.animate)
            else:
                pass
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1,y1,x2,y2 = drawpad.coords(oldYeller)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)                
	        if x1 > tx1 and x2 < tx2 and y1 > ty1 and y2 < ty2:
	            return True
	        else:
	            return False
myapp = MyApp(root)
root.mainloop()