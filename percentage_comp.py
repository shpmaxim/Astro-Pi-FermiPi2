"""
version adapted for: north Queensland, Australia
photo: north_queensland.jpg
June 24, 2009
"""

# imports
import cv2
import numpy as np
import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

# creation of the graphical interface 
window = tk.Tk()    
window.title('Graphic analysis')
window.geometry("")
window.resizable(height = False, width = False)
window.configure(bg = 'white')

# filepaths
filepath = os.path.dirname(__file__)
res_folder = os.path.join(filepath, 'res')
img_1 = os.path.join(res_folder, 'black.png')
img_2 = os.path.join(res_folder, 'green_comp.png')
img_3 = os.path.join(res_folder, 'almost_white.png')
img_4 = os.path.join(res_folder, 'white_comp.png')
img_5 = os.path.join(res_folder, 'light_brown.png')
img_6 = os.path.join(res_folder, 'brown_comp.png')  
saving_dir = os.path.join(res_folder, 'analysis_data')
save_file_dir = os.path.join(saving_dir, 'analysis_data.txt')

# opening images
img_1_o = Image.open(img_1)
img_2_o = Image.open(img_2)
img_3_o = Image.open(img_3)
img_4_o = Image.open(img_4)
img_5_o = Image.open(img_5)
img_6_o = Image.open(img_6)

# creating the folder in which the program will save the analysis' results (try-except mechanism to avoid save fail if folder already exists)
try:
    os.mkdir(saving_dir)
except OSError as error:
    print(error)

#  target colors list in RGB + names
color = [[11,17,7], [169,168,93], [216,202,163], [246,241,228], [137,119,83], [85,75,53]]
names = ['black', 'light green', 'beige', 'white', 'light brown', 'brown']

# defining the restart function
def another():
    for widgets in window.winfo_children():
        widgets.destroy()
    main()

def main():
    try:
        # opening the file dialog to choose the photo for analysis
        photopath = filedialog.askopenfilename()
        # reading image
        orig_img = Image.open(photopath)

        # creating lists for image names + percentage
        img_list = [img_1_o, img_2_o, img_3_o, img_4_o, img_5_o, img_6_o]
        percentage_list = []

        # upper part of the graphical interface
        photo_n = tk.Label(window, text = 'photo ' + photopath, bg = 'white', font = ('Arial', 15))
        sep = tk.Label(window, text = '---------------------------------------------', bg = 'white', font = ('Arial', 15))
        photo_n.grid(row = 0, column = 0, columnspan=3)
        sep.grid(row= 1, column = 0, columnspan=3)

        for i in range(6):
            # creating color sapmples widgets
            img_o = img_list[i].resize((50, 50), Image.LANCZOS)
            img_oo = ImageTk.PhotoImage(img_o)
            img_l = tk.Label(window, image=img_oo, borderwidth=0)
            img_l.image = img_oo
            img_l.grid(row = i+2, column = 0, pady = 5)
            # creating color names windgets
            target = tk.Label(window, text = '  ' + names[i], bg = 'white', font = ('Arial', 13))
            target.grid(row = i+2, column = 1, sticky= 'W')

            # range parameter for RGB values
            diff = 20
            # setting the boundaries (cv2 works in BGR format, mind the conversion)
            boundaries = [([color[i][2]-diff, color[i][1]-diff, color[i][0]-diff], [color[i][2]+diff, color[i][1]+diff, color[i][0]+diff])]
            # image resize parameter
            scalePercent = 0.3
            # new sizes
            img = cv2.imread(photopath)
            width = int(img.shape[0] * scalePercent)
            height = int(img.shape[1] * scalePercent)
            newSize = (width, height)
            # image resize
            img = cv2.resize(img, newSize, None, None, None, cv2.INTER_AREA)

            for (lower, upper) in boundaries:
                # analysis and pixel count 
                lower = np.array(lower, dtype=np.uint8)
                upper = np.array(upper, dtype=np.uint8)
                mask = cv2.inRange(img, lower, upper)
                output = cv2.bitwise_and(img, img, mask=mask)
                ratio_color = cv2.countNonZero(mask)/(img.size/3)
                # percentage calculation 
                colorPercent = ratio_color * 100

                # creating result widgets
                percentage = tk.Label(window, text = str(round(colorPercent, 2)) + '%', bg = 'white', font = ('Arial', 13))
                percentage.grid(row = i+2, column = 2, sticky= 'W', padx= 5)
                percentage_list.append(colorPercent)

                # declaring the save finction
                def save():
                    analysis = open(save_file_dir, 'a')
                    analysis.write('\n\n\nAnalysis results for photo \t' + photopath + '\n\n')
                    for i in range(6):
                        analysis.write(names[i] + '\t -- \t' + str(round(percentage_list[i], 2)) + '% \n')

        # creating the save button
        sep_s = tk.Label(window, text = '---------------------------------------------', bg = 'white', font = ('Arial', 15))
        sep_s.grid(row = 9, column = 0, columnspan=3)
        save_btn = tk.Button(window, text = 'Save results', command = save, width = 15)
        save_btn.grid(row = 10, column = 0, columnspan= 3, pady = 5)

        # creating the restart button
        another_btn = tk.Button(window, text = 'Analyze another photo', command = another, width = 15)
        another_btn.grid(row = 11, column = 0, columnspan=3)

        # opening the orignal image for optical (user) comparison and result validation
        orig_img.show()
    except OSError as UnidentifiedImageError:
        print('please choose a different file type')
        err_label = tk.Label(window, text = 'Please choose another file', font = ('Arial', 13), bg = 'white').pack()
        btn_another = tk.Button(window, text = 'Choose another file', command = another).pack()
        photopath = filedialog.askopenfilename()
    except: 
        print('unexpected error')
        btn_another = tk.Button(window, text = 'Choose another file', font = ('Arial', 15), bg = 'white', command = another).pack()

main()
window.mainloop()