###############################################################################
## Gui interface classes
## Made with reference to http://www.blog.pythonlibrary.org/2012/07/26/
##  tkinter-how-to-show-hide-a-window/
## Currently, only the Path Mode interface has been implemented. It is
##  suggested that class Path be used as a template for implemantation of
##  other GUI class dealies
## Alot of the comments from the previous version are missing cause laziness
##  might put them in later, maybe...
###############################################################################
import tkinter as tk
from functools import partial
########################################################################
class Path(tk.Toplevel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        tk.Toplevel.__init__(self)
        self.title("Path Mode")
        self.pathButtons = []
        self.path = []
        self.orderindex = 0

        # Instantiation of grid and start buttons
        for x in range(self.dimensions()):
            col = []
            for y in range(self.dimensions()):
                butt = tk.Button(self ,text=" ", command=partial(self.clickpath, x, y))
                butt.grid(column=x, row=y)
                col.append(butt)
            self.pathButtons.append(col)

        start = tk.Button(self, text="Start", command=self.clickstart).grid(
            column=(int(self.dimensions() / 2)-1), row=(self.dimensions()+1),
            columnspan=2)

        back = tk.Button(self, text="Back", command=self.onClose).grid(
            column=(int(self.dimensions() / 2)+1), row=(self.dimensions()+1),
            columnspan=2)

    #----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()

    def dimensions(self):
        return 20

    def clickpath(self, x, y):
        #function to do stuff with index of button on grid/list
        global orderindex #needed to access global variable
        but = self.pathButtons[x][y] #acces button from grid buttons
        if(but.cget('text') == self.orderindex): # if button has text tag
            but.configure(text=" ") #set it blank
            self.path.pop() #remove last patth[] element (coordinate)
            self.orderindex -= 1
        elif(but.cget('text') == ' '):
            but.configure(text=self.orderindex+1) #add order index to button text tag
            self.path.append([x, y]) #append
            self.orderindex += 1

    def clickstart(self):
        # executes start button function(s)
        # for debug purposes at this point
        # will eventually send list of coordinates to the 'directions' module
        print(self.path)
        print(self.orderindex)
    # Instantiation of grid and start buttons

########################################################################
class Menu(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Gogo Robo Maaaaaaaaaaaaaaaania~")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        dButt = tk.Button(self.frame, text="Direct Mode", command=self.openDirect)
        pButt = tk.Button(self.frame, text="Path Mode", command=self.openPath)
        mButt = tk.Button(self.frame, text="Map Mode", command=self.openMap)
        dButt.pack()
        pButt.pack() #lol
        mButt.pack()

    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    #----------------------------------------------------------------------
    #Open methods all open path mode till others are implemented
    def openDirect(self):
        """"""
        self.hide()
        subFrame = Path(self)

    #----------------------------------------------------------------------
    def openPath(self):
        """"""
        self.hide()
        subFrame = Path(self)

    #----------------------------------------------------------------------
    def openMap(self):
        """"""
        self.hide()
        subFrame = Path(self)

    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    main = Menu(root)
    root.mainloop()