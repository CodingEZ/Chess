from tkinter import *
import dataStorage as DS

def run(width=800, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill='white', width=0)
        x.redrawAll(canvas)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        x.mousePressed(event)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        x.keyPressed(event)
        redrawAllWrapper(canvas, data)
    
    # Initialize data
    class Struct(object):
        pass

    data = Struct()
    data.width = width
    data.height = height
    x = DS.dataStorage(data)
    # create the root and the canvas
    root = Tk()
    frame = Frame(root)
    canvas = Canvas(root, width=x.data.width, height=x.data.height)
    canvas.pack()
    # set up events
    redrawAllWrapper(canvas, x.data)    # this is to show the interface
    root.bind("<Button-1>", lambda event: mousePressedWrapper(event, canvas, x.data))
    root.bind("<Key>", lambda event: keyPressedWrapper(event, canvas, x.data))
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


# run the program here
run(900, 600)
