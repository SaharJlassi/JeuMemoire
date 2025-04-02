from tkinter import *

root=Tk()
cnv=Canvas(root,width=600,height=400,bg="ivory")
cnv.pack()
icon=PhotoImage(file="./image/kiwi.png")
id_im=0

def clic(event):
    global id_im
    cnv.delete(id_im)
    center=(event.x , event.y)
    id_im=cnv.create_image(center,image=icon)
    

cnv.bind("<Button>",clic)
root.mainloop()