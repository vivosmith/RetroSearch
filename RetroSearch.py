from tkinter import *
import webbrowser

def callback(event):
    global enter
    enter=entr.get()
    webbrowser.open_new(r"https://www.google.com/search?biw=911&bih=409&noj=1&site=webhp&tbs=cdr%3A1%2Ccd_min%3A1940%2Ccd_max%3A2008&source=hp&q="+enter+"&oq="+enter+"&gs_l=hp")
root = Tk()
root.wm_title("RetroSearch")
link = Button(root, text="RetroSearch", cursor="hand2",fg="grey")
entr=Entry(root,bd=10,width=40)
entr.pack()
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()