import cv2
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from Plant import detect_4
from tkinter.filedialog import askopenfilename

def upload_file():
    
    file = askopenfilename(title = "Select a file", filetypes = (("image files" ,("*.jpg","*.png")),("all files","*.*")))
    
    l1.configure(text = "" + file)

    #print(l1['text']) # image path

def detect(img):
    #read the image using cv2 library and call the function detect_4 which gives tuple
    frame = cv2.imread(img)
    plt.imshow(frame) # for displaying image

    # call function detect_4

    result = detect_4(frame)

    #print(result)

    output_label_1['text'] = "1. Using custom model: " + result[0]

    output_label_2['text'] = "2. Fine tuning the layers in classification part: " + result[1]

    output_label_3['text'] = "3. Fine tuning the whole network: " + result[2]

    output_label_4['text'] = "4. Fine tuning the model from scratch: " + result[3]
    

    '''
    1. custom mode1
    2. Fine tuning the layers in classification part
    3. Fine tuning the whole network
    4. Fine tuning the model from scratch
    '''
    
    

root = Tk()

root.geometry('900x700')

root.title('Plant Disease Detection')

frm = ttk.Frame(root,padding = 10)

frm.pack()

l1 = ttk.Label(frm, text = "Image path")


b1 = ttk.Button(frm, text = "Upload file", width = 15, command = lambda : upload_file())

l1.grid(column = 1, row = 0,padx = 30, pady = 40)

b1.grid(column = 0, row = 0, padx = 30)

output_label_1 = ttk.Label(frm, text = "", font = ('Helvetica Bold', 22), foreground ="red")

output_label_2 = ttk.Label(frm, text = "", font = ('Helvetica Bold', 22), foreground ="blue")

output_label_3 = ttk.Label(frm, text = "", font = ('Helvetica Bold', 22), foreground ="green")

output_label_4 = ttk.Label(frm, text = "", font = ('Helvetica Bold', 22), foreground ="blue")

b2 = ttk.Button(frm, text = "Detect Disease",width = 30, command = lambda : detect(l1['text'])).grid(column = 1, row = 1, padx = 30,pady = 10)

output_label_1.grid(row = 3, column = 1, padx = 30, pady = 15)

output_label_2.grid(row = 4, column = 1, padx = 30, pady = 15)

output_label_3.grid(row = 5, column = 1, padx = 30, pady = 15)

output_label_4.grid(row = 6, column = 1, padx = 30, pady = 15)


b3 = ttk.Button(frm, text = "Quit Session",width = 30, command = root.destroy).grid(column = 1, row = 2, padx = 30,pady = (20,50))

root.mainloop()


