from tkinter import*

import pyautogui
import time

#Window Details.
window= Tk()
window.geometry('420x250')
window.title('Create New Files')
#icon= PhotoImage(file='folder.png')
window.iconbitmap(r'E:\00_Programming Practice\02.Python\03. Creating New Project Files\icon.ico')
#window.iconphoto(True,icon)
window.config(background='#373a42')


#inside

#inside title text
label = Label(window,
              text='Enter the file name',
              font=('montserrat ','27','bold'),
              bg='#373a42',
              fg='#ffffff')
#label.pack()
label.place(relx = 0.5, rely = 0.25, anchor = CENTER)



#EntryBox
entry=Entry(window,
            font=('montserrat ','18','bold'),bg='#ffffff', fg='#373a42')
#entry.pack()
entry.place(relx = 0.5, rely = 0.5, anchor = CENTER, height = '50', width = '250')

#Button

def create():
    filename= entry.get()
    # Create Main File
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'n')
    pyautogui.typewrite(filename)
    pyautogui.press('enter')

    # Sub Files

    time.sleep(.5)

    # Assets
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'ctrl', 'n')
    pyautogui.typewrite('Assets')
    pyautogui.press('enter')

    # Reference
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'ctrl', 'n')
    pyautogui.typewrite('Reference')
    pyautogui.press('enter')
    pyautogui.press('backspace')

    # Project Files
    pyautogui.hotkey('shift', 'ctrl', 'n')
    pyautogui.typewrite('Project Files')
    pyautogui.press('enter')

    # Renders
    time.sleep(.5)
    pyautogui.hotkey('shift', 'ctrl', 'n')
    pyautogui.typewrite('Renders')
    pyautogui.press('enter')

    # Wips
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'ctrl', 'n')
    pyautogui.typewrite('Wips')
    pyautogui.press('enter')

    # Finals
    time.sleep(1)
    pyautogui.hotkey('shift', 'ctrl', 'n')
    pyautogui.typewrite('Finals')
    pyautogui.press('enter')
    pyautogui.press('backspace')


button= Button(window,text='Create File',command=create, font=('montserrat ','14','italic'),
               fg='#ffffff',bg='#373a42',height = '1', width = '10' )
#button.pack(side='bottom')
button.place(relx = 0.5, rely = 0.8, anchor = CENTER)




window.mainloop()