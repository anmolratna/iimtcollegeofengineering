from tkinter import messagebox
title='feedback system'
text='HAVE YOU TROUBLE ANY KIND OF ISSUES'
reply=messagebox.askyesno(title,text)
if reply=='yes':
    print('thank you very much..')
else:
    print('we regert the inconvenience.please give me another chance.')
text='every thing is ok'
reply=messagebox.askyesno(title,text)
if reply=='yes':
    print("we have sole this issue as soon as")
else:
    print("thank you gave you precious with us")
