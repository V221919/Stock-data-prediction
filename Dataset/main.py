from tkinter import * 
from tkinter import ttk 
from PIL import Image,ImageTk
import pandas as pd
# from accessdata import Employee


class FetchData:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x700+0+0")
        self.root.title("Data Reterived System")
        self.title=Label(self.root,text="Data Reterived System",bd=12,font=('arial 15 bold'), width=12,bg='gray')
        self.title.pack(fill=X)
        #background Image
        self.bgImage=ImageTk.PhotoImage(file='images/bgimage.jpg')
        self.bgImageLabel=Label(self.root,image=self.bgImage)
        self.bgImageLabel.place(x=0,y=35)

        #Employee Data 
        self.userImage=ImageTk.PhotoImage(file='images/user.png')
        self.userImageLabel=Label(self.root,image=self.userImage)
        self.userImageLabel.place(x=200,y=150)  

        #Comp Button 
        companyButton=Button(self.root,text="PREDICTION",command=self.accessData,font=('arial 15 bold'),bg='gray',fg='white',cursor="hand2",width=10)
        companyButton.place(x=200,y=285)

        #ExitImage
        self.exitImage=ImageTk.PhotoImage(file='images/exit.png')
        self.exitLabel=Label(self.root,image=self.exitImage)
        self.exitLabel.place(x=540,y=150)

        # Exit Button
        exitButton=Button(self.root,text="Exit",font=('arial 16 bold'),command=self.exitWindows,bg='gray',fg='white',cursor="hand2",width=9)
        exitButton.place(x=540,y=286)

    def exitWindows(self):
        self.root.destroy()

    def accessData(self):    
        import data1
        # data=pd.read_csv("tesla.csv",usecols=[0,3])
        # CountComp=data.loc[(data.Country == 'India')]
        # data20=CountComp.iloc[0:20,0:2]
        # print(data20)
if(__name__=="__main__"):
    root=Tk()
    app=FetchData(root)
    root.mainloop()
