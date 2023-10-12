from tkinter import filedialog

def knoka():

    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )


    tf = open(tf)
    f = tf.readlines()

    return f




