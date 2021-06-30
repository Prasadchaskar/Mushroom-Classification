from tkinter import *
import pickle
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image

root = Tk()
root.geometry('1500x1000')
root.title("Heart Disease Prediction")

# Background Image
bg = ImageTk.PhotoImage(file='heart.jpg')
bg_label = Label(image=bg).place(x=337,y=50,relwidth=1,relheight=1)

def predict_win():
    top = Toplevel()
    top.geometry('1000x1000')
    top.title("Prediction Window")
    f1 = Frame(top, bg='bisque2')
    f1.place(x=70, y=5, height=900, width=800)
    main_labl = Label(f1,text="Heart Disease Prediction",font="comicsansms 18 bold",bg='cyan',fg='red')
    age = Label(f1,text="Age",font="comicsansms 15 bold")
    gen = Label(f1,text="Gender",font="comicsansms 15 bold")
    cp = Label(f1,text="Chest Pain Type",font="comicsansms 15 bold")
    bp = Label(f1,text="Blood Pressure",font="comicsansms 15 bold")
    chol = Label(f1,text="Cholestrol",font="comicsansms 15 bold")
    sugar = Label(f1,text="Blood Sugar(1=yes,0=No)",font="comicsansms 15 bold")
    er = Label(f1,text="Electrocardiographic Result",font="comicsansms 15 bold")
    heart_rate = Label(f1,text="Heart Rate",font="comicsansms 15 bold")
    exchng = Label(f1,text="Exercise induced angina (1 = yes; 0 = no)",font="comicsansms 15 bold")
    oldpeak = Label(f1,text="Oldpeak",font="comicsansms 15 bold")
    slope = Label(f1,text="Slope",font="comicsansms 15 bold")
    vessels = Label(f1,text="Number of major vessels (0-3)",font="comicsansms 15 bold")
    thal = Label(f1,text="Thal",font="comicsansms 15 bold")


    def get_data():
        lables ={
                1:'YES',
                0:'NO'
            }
        with open('E:\DataScienceProjects/heartmodel.sav','rb') as f:
            mp = pickle.load(f) 
            result = lables[mp.predict([[int(age_val.get()),
                                    int(gen_val.get()),
                                    int(cp_val.get()),
                                    int(bp_val.get()),
                                    int(chol_val.get()),
                                    int(sugar_val.get()),
                                    int(er_val.get()),
                                    int(heart_rate_val.get()),
                                    int(exchng_val.get()),
                                    float(oldpeak_val.get()),
                                    int(slope_val.get()),
                                    int(vessels_val.get()),
                                    int(thal_val.get())
                                    ]])[0]]
            tmsg.showinfo(title='Prediction Result',message=f"{result} you have heart desease")


    main_labl.place(x=250,y=20)
    age.place(x=70,y=100)
    gen.place(x=70,y=150)
    cp.place(x=70,y=200)
    bp.place(x=70,y=250)
    chol.place(x=70,y=300)
    sugar.place(x=70,y=350)
    er.place(x=70,y=400)
    heart_rate.place(x=70,y=450)
    exchng.place(x=70,y=500)
    oldpeak.place(x=70,y=550)
    slope.place(x=70,y=600)
    vessels.place(x=70,y=650)
    thal.place(x=70,y=700)

    age_val = StringVar()
    gen_val = StringVar()
    cp_val = StringVar()
    bp_val = StringVar()
    chol_val = StringVar()
    sugar_val = StringVar()
    er_val = StringVar()
    exchng_val = StringVar()
    heart_rate_val = StringVar()
    oldpeak_val = StringVar()
    slope_val = StringVar()
    vessels_val = StringVar()
    thal_val = StringVar()

    age_val_entry = Entry(f1,textvariable=age_val,font = "Helvetica 15 bold",bg="lightskyblue")
    gen_val_entry = Entry(f1,textvariable=gen_val,font = "Helvetica 15 bold",bg="lightskyblue")
    cp_val_entry = Entry(f1,textvariable=cp_val,font = "Helvetica 15 bold",bg="lightskyblue")
    bp_val_entry = Entry(f1,textvariable=bp_val,font = "Helvetica 15 bold",bg="lightskyblue")
    chol_val_entry = Entry(f1,textvariable=chol_val,font = "Helvetica 15 bold",bg="lightskyblue")
    sugar_val_entry = Entry(f1,textvariable=sugar_val,font = "Helvetica 15 bold",bg="lightskyblue")
    er_val_entry = Entry(f1,textvariable=er_val,font = "Helvetica 15 bold",bg="lightskyblue")
    heart_rate_val_entry = Entry(f1,textvariable=heart_rate_val,font = "Helvetica 15 bold",bg="lightskyblue")
    exchng_val_entry = Entry(f1,textvariable=exchng_val,font = "Helvetica 15 bold",bg="lightskyblue")
    oldpeak_val_entry = Entry(f1,textvariable=oldpeak_val,font = "Helvetica 15 bold",bg="lightskyblue")
    slope_val_entry = Entry(f1,textvariable=slope_val,font = "Helvetica 15 bold",bg="lightskyblue")
    vessels_val_entry = Entry(f1,textvariable=vessels_val,font = "Helvetica 15 bold",bg="lightskyblue")
    thal_val_entry = Entry(f1,textvariable=thal_val,font = "Helvetica 15 bold",bg="lightskyblue")

    age_val_entry.place(x=530,y=100)
    gen_val_entry.place(x=530,y=150)
    cp_val_entry.place(x=530,y=200)
    bp_val_entry.place(x=530,y=250)
    chol_val_entry.place(x=530,y=300)
    sugar_val_entry.place(x=530,y=350)
    er_val_entry.place(x=530,y=400)
    heart_rate_val_entry.place(x=530,y=450)
    exchng_val_entry.place(x=530,y=500)
    oldpeak_val_entry.place(x=530,y=550)
    vessels_val_entry.place(x=530,y=600)
    slope_val_entry.place(x=530,y=650)
    thal_val_entry.place(x=530,y=700)

    Button(f1,text="Submit", width=10, height=2,fg='black',command=get_data).place(x=450,y=750)

Label(root,text="Project Information",font = "Helvetica 25 bold",justify=CENTER).place(x=600,y=10)
project_ifo = '''
    First in notebook I have performed Exploratory Data Analysis on the Heart Diseases UCI and tried to 
    identify relationship between heart disease and various other features. 
    After EDA data pre-processing is done I have applied k-NN(k-Nearest Neighbors) method.
    After saving model I used saved model in this GUI and try te predict you have heart disease or not
    by taking various inputs from user.
'''
Label(root,text=project_ifo,font = "Helvetica 20 bold",justify=LEFT).place(x=20,y=50)

features='''
The dataset contains the following features:
    1. age(in years)
    2. sex: (1 = male; 0 = female)
    3. cp: chest pain type
    4. trestbps: resting blood pressure (in mm Hg on admission to the hospital)
    5. chol: serum cholestoral in mg/dl
    6. fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
    7. restecg: resting electrocardiographic results
    8. thalach: maximum heart rate achieved
    9. exang: exercise induced angina (1 = yes; 0 = no)
    10. oldpeak: ST depression induced by exercise relative to rest
    11. slope: the slope of the peak exercise ST segment
    12. ca: number of major vessels (0-3) colored by flourosopy
    13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
    14. target: 1 or 0

'''
Label(root,text=features,justify=LEFT,font = "Helvetica 15 bold").place(x=50,y=250)
Button(root,text="Make Prediction", width=20, height=2,bg='blue2',command=predict_win).place(x=600,y=650)


menu = Menu(root)
menu.add_command(label="Make Prediction",command=predict_win)
menu.add_command(label="Exit",command=quit)
root.configure(menu=menu)

root.mainloop()