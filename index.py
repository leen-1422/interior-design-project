from tkinter import *
from tkinter import messagebox

window=Tk() #instantiate an instance of a window
window.title("interior design app")#change the title name from tk to something else
window.geometry("1390x784")#change the size of the window
bg=PhotoImage(file="idk.png")
label=Label(window,image=bg)
label.place(x=0,y=0,relwidth=1,relheight=1)

def LoginPage():
    global bg1
    pro=Toplevel()
    pro.title("Login")
    pro.geometry("1390x784")
    bg1=PhotoImage(file="shop-bg.png")
    label1=Label(pro,image=bg1)
    label1.place(x=0,y=0,relwidth=1,relheight=1)

    def loginfun():
        messagebox.showinfo(message="login is successful")
    #title
    logintopFrame=Frame(pro,bd=10,relief=RIDGE,bg='#6f5e5e')
    logintopFrame.pack(side=TOP)
    loginLabel= Label(logintopFrame,text="LOGIN ",font=('Arial',30,'bold'),fg='white',bg='#6f5e5e',width=20,bd=9)
    loginLabel.grid(row=0,column=0)
    fr1=Frame(pro, width='500', height='600', bg='gray',bd=10)
    fr1.place(x=440,y=100)
    #label
    lb1= Label(pro,text='USERNAME :',font=('Couriere',14),fg='white', bg='#6f5e5e')
    lb1.place(x=450,y=250)
    lb2= Label(pro,text='PASSWORD :' ,font=('Couriere',14),fg='white', bg='#6f5e5e')
    lb2.place(x=450,y=350)

    #entry
    en1 = Entry(pro, width=30,bd=3)
    en1.place(x= 600 ,y=250)
    en2 = Entry(pro, width=30,bd=3)
    en2.place(x=600 ,y=350)

    bt1=Button(pro,text='Login',font=('courier',15),bg='#6f5e5e',width=20,bd=5,command=loginfun)
    bt1.place(x=520,y=550)
def ShopPage():
    global bg2
    top2=Toplevel()
    top2.title("Shop")
    top2.geometry("1390x784")
    bg2=PhotoImage(file="shop-bg.png")
    label2=Label(top2,image=bg2)
    label2.place(x=0,y=0,relwidth=1,relheight=1)
    topFrame=Frame(top2,bd=10,relief=RIDGE,bg='#6f5e5e')
    topFrame.pack(side=TOP)
    titleLabel= Label(topFrame,text="Our Furniture Store ",font=('Arial',30,'bold'),fg='white',bg='#6f5e5e',width=51,bd=9)
    titleLabel.grid(row=0,column=0)

    def submitfun():
       if messagebox.askyesnocancel(title='attention',message='are you sure you want to submit your order?'):
           messagebox.showinfo(message="Thank you for your order.")

    def totalcostfun():
        total1=int(e_chair.get())
        total2=int(e_bed.get())
        total3=int(e_couch.get())
        total4=int(e_desk.get())
        total5=int(e_table.get())
        total6=int(e_nightStand.get())
        total7=int(e_bookShelf.get())
        total8=int(e_dinningTable.get())
        total9=int(e_tv.get())
        total10=int(e_red.get())
        total11=int(e_pink.get())
        total12=int(e_blue.get())
        total13=int(e_black.get())
        total14=int(e_white.get())
        total15=int(e_yellow.get())
        total16=int(e_gray.get())
        total17=int(e_orange.get())
        total18=int(e_brown.get())
        total19=int(e_tile.get())
        total20=int(e_carpet.get())
        total21=int(e_hardwood.get())
        total22=int(e_marble.get())
        total23=int(e_granit.get())
        total24=int(e_stone.get())
        total25=int(e_cork.get())
        total26=int(e_laminate.get())
        total27=int(e_concrete.get())

        furniturePrice=(total1*500)+(total2*1600)+(total3*4200)+(total4*700)+(total5*1800)+(total6*600)+(total7*600)\
                       +(total8*900)+(total9*2600)
        cost1.set(str(furniturePrice)+'SAR')

        paintPrice=(total10*150)+(total11*150)+(total12*150)+(total13*150)+(total14*150)+(total15*150)+(total16*150)\
                       +(total17*150)+(total18*150)
        cost2.set(str(paintPrice)+'SAR')

        floorPrice=(total19*500)+(total20*1600)+(total21*4200)+(total22*700)+(total23*1800)+(total24*600)+(total25*600)\
                       +(total26*900)+(total27*2600)
        cost3.set(str(floorPrice)+'SAR')

        subtotalResult= floorPrice+paintPrice+floorPrice
        cost4.set(str(subtotalResult)+'SAR')
        taxResult=subtotalResult*0.15
        cost5.set(str(taxResult)+'SAR')
        taxtotalResult=subtotalResult+taxResult
        cost6.set(str(taxtotalResult)+'SAR')
    def chairfun():
        if var1.get()==1:
            chairText.config(state=NORMAL)
            chairText.delete(0,END)
            chairText.focus()
        else:
            chairText.config(state=DISABLED)
            e_chair.set('0')
    def bedfun():
        if var2.get()==1:
            bedText.config(state=NORMAL)
            bedText.delete(0,END)
            bedText.focus()
        else:
            bedText.config(state=DISABLED)
            e_bed.set('0')
    def couchfun():
        if var3.get()==1:
            couchText.config(state=NORMAL)
            couchText.delete(0,END)
            couchText.focus()
        else:
            couchText.config(state=DISABLED)
            e_couch.set('0')
    def deskfun():
        if var4.get()==1:
            deskText.config(state=NORMAL)
            deskText.delete(0,END)
            deskText.focus()
        else:
            deskText.config(state=DISABLED)
            e_desk.set('0')
    def tablefun():
        if var5.get()==1:
            tableText.config(state=NORMAL)
            tableText.delete(0,END)
            tableText.focus()
        else:
            tableText.config(state=DISABLED)
            e_table.set('0')
    def nightstandfun():
        if var6.get()==1:
            NightStandText.config(state=NORMAL)
            NightStandText.delete(0,END)
            NightStandText.focus()
        else:
            NightStandText.config(state=DISABLED)
            e_nightStand.set('0')
    def bookshelffun():
        if var7.get()==1:
            bookShelfText.config(state=NORMAL)
            bookShelfText.delete(0,END)
            bookShelfText.focus()
        else:
            bookShelfText.config(state=DISABLED)
            e_bookShelf.set('0')
    def dinningtablefun():
        if var8.get()==1:
            dinningTableText.config(state=NORMAL)
            dinningTableText.delete(0,END)
            dinningTableText.focus()
        else:
            dinningTableText.config(state=DISABLED)
            e_dinningTable.set('0')
    def tvfun():
        if var9.get()==1:
            tvText.config(state=NORMAL)
            tvText.delete(0,END)
            tvText.focus()
        else:
            tvText.config(state=DISABLED)
            e_tv.set('0')
    def redfun():
        if var10.get()==1:
            redText.config(state=NORMAL)
            redText.delete(0,END)
            redText.focus()
        else:
            redText.config(state=DISABLED)
            e_red.set('0')
    def pinkfun():
        if var11.get()==1:
            pinkText.config(state=NORMAL)
            pinkText.delete(0,END)
            pinkText.focus()
        else:
            pinkText.config(state=DISABLED)
            e_pink.set('0')
    def bluefun():
        if var12.get()==1:
            blueText.config(state=NORMAL)
            blueText.delete(0,END)
            blueText.focus()
        else:
            blueText.config(state=DISABLED)
            e_blue.set('0')
    def blackfun():
        if var13.get()==1:
            blackText.config(state=NORMAL)
            blackText.delete(0,END)
            blackText.focus()
        else:
            blackText.config(state=DISABLED)
            e_black.set('0')
    def whitefun():
        if var14.get()==1:
            whiteText.config(state=NORMAL)
            whiteText.delete(0,END)
            whiteText.focus()
        else:
            whiteText.config(state=DISABLED)
            e_white.set('0')
    def yellowfun():
        if var15.get()==1:
            yellowText.config(state=NORMAL)
            yellowText.delete(0,END)
            yellowText.focus()
        else:
            yellowText.config(state=DISABLED)
            e_yellow.set('0')
    def grayfun():
        if var16.get()==1:
            grayText.config(state=NORMAL)
            grayText.delete(0,END)
            grayText.focus()
        else:
            grayText.config(state=DISABLED)
            e_gray.set('0')
    def orangefun():
        if var17.get()==1:
            orangeText.config(state=NORMAL)
            orangeText.delete(0,END)
            orangeText.focus()
        else:
            orangeText.config(state=DISABLED)
            e_orange.set('0')
    def brownfun():
        if var18.get()==1:
            brownText.config(state=NORMAL)
            brownText.delete(0,END)
            brownText.focus()
        else:
            brownText.config(state=DISABLED)
            e_brown.set('0')
    def tilefun():
        if var19.get()==1:
            tileText.config(state=NORMAL)
            tileText.delete(0,END)
            tileText.focus()
        else:
            tileText.config(state=DISABLED)
            e_tile.set('0')
    def carpetfun():
        if var20.get()==1:
            carpetText.config(state=NORMAL)
            carpetText.delete(0,END)
            carpetText.focus()
        else:
            carpetText.config(state=DISABLED)
            e_carpet.set('0')
    def hardwoodfun():
        if var21.get()==1:
            hardwoodText.config(state=NORMAL)
            hardwoodText.delete(0,END)
            hardwoodText.focus()
        else:
            hardwoodText.config(state=DISABLED)
            e_hardwood.set('0')
    def marblefun():
        if var22.get()==1:
            marbleText.config(state=NORMAL)
            marbleText.delete(0,END)
            marbleText.focus()
        else:
            marbleText.config(state=DISABLED)
            e_marble.set('0')
    def granitfun():
        if var23.get()==1:
            granitText.config(state=NORMAL)
            granitText.delete(0,END)
            granitText.focus()
        else:
            granitText.config(state=DISABLED)
            e_granit.set('0')
    def stonefun():
        if var24.get()==1:
            stoneText.config(state=NORMAL)
            stoneText.delete(0,END)
            stoneText.focus()
        else:
            stoneText.config(state=DISABLED)
            e_stone.set('0')
    def corkfun():
        if var25.get()==1:
            corkText.config(state=NORMAL)
            corkText.delete(0,END)
            corkText.focus()
        else:
            corkText.config(state=DISABLED)
            e_cork.set('0')
    def laminatefun():
        if var26.get()==1:
            laminateText.config(state=NORMAL)
            laminateText.delete(0,END)
            laminateText.focus()
        else:
            laminateText.config(state=DISABLED)
            e_laminate.set('0')
    def concretefun():
        if var27.get()==1:
            concreteText.config(state=NORMAL)
            concreteText.delete(0,END)
            concreteText.focus()
        else:
            concreteText.config(state=DISABLED)
            e_concrete.set('0')

    menuFrame=Frame(top2,bd=10,relief=RIDGE,bg='#6f5e5e')
    menuFrame.pack(side=LEFT)
    costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='#6f5e5e',pady=10)
    costFrame.pack(side=BOTTOM)
    furnitureFrame=LabelFrame(menuFrame,text="Furniture",font=('Arial',19,'bold'),bd=10,relief=RIDGE,fg='white',bg='#6f5e5e')
    furnitureFrame.pack(side=LEFT)
    paintFrame=LabelFrame(menuFrame,text="Paint",font=('Arial',19,'bold'),bd=10,relief=RIDGE,fg='white',bg='#6f5e5e')
    paintFrame.pack(side=LEFT)
    floorFrame=LabelFrame(menuFrame,text="Floor",font=('Arial',19,'bold'),bd=10,relief=RIDGE,fg='white',bg='#6f5e5e')
    floorFrame.pack(side=LEFT)
    rightFrame=Frame(top2,bd=15,relief=RIDGE,bg='#6f5e5e')
    rightFrame.pack(side=RIGHT)
    calFrame=Frame(rightFrame,bd=1,relief=RIDGE)
    calFrame.pack()
    reciptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#6f5e5e')
    reciptFrame.pack()
    btnFrame=Frame(rightFrame)
    btnFrame.pack()

    #variables
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()
    var16=IntVar()
    var17=IntVar()
    var18=IntVar()
    var19=IntVar()
    var20=IntVar()
    var21=IntVar()
    var22=IntVar()
    var23=IntVar()
    var24=IntVar()
    var25=IntVar()
    var26=IntVar()
    var27=IntVar()
    e_chair=StringVar()
    e_bed=StringVar()
    e_couch=StringVar()
    e_desk=StringVar()
    e_table=StringVar()
    e_nightStand=StringVar()
    e_bookShelf=StringVar()
    e_dinningTable=StringVar()
    e_tv=StringVar()
    e_red=StringVar()
    e_pink=StringVar()
    e_blue=StringVar()
    e_black=StringVar()
    e_white=StringVar()
    e_yellow=StringVar()
    e_gray=StringVar()
    e_orange=StringVar()
    e_brown=StringVar()
    e_tile=StringVar()
    e_carpet=StringVar()
    e_hardwood=StringVar()
    e_marble=StringVar()
    e_granit=StringVar()
    e_stone=StringVar()
    e_cork=StringVar()
    e_laminate=StringVar()
    e_concrete=StringVar()
    cost1=StringVar()
    cost2=StringVar()
    cost3=StringVar()
    cost4=StringVar()
    cost5=StringVar()
    cost6=StringVar()
    e_chair.set('0')
    e_bed.set('0')
    e_couch.set('0')
    e_desk.set('0')
    e_table.set('0')
    e_nightStand.set('0')
    e_bookShelf.set('0')
    e_dinningTable.set('0')
    e_tv.set('0')
    e_red.set('0')
    e_pink.set('0')
    e_blue.set('0')
    e_black.set('0')
    e_white.set('0')
    e_yellow.set('0')
    e_gray.set('0')
    e_orange.set('0')
    e_brown.set('0')
    e_tile.set('0')
    e_carpet.set('0')
    e_hardwood.set('0')
    e_marble.set('0')
    e_granit.set('0')
    e_stone.set('0')
    e_cork.set('0')
    e_laminate.set('0')
    e_concrete.set('0')

    #furniture
    chair=Checkbutton(furnitureFrame,text="Chair",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var1,command=chairfun,fg='white')
    chair.grid(row=0,column=0,sticky=W)
    bed=Checkbutton(furnitureFrame,text="Bed",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                    variable=var2,command=bedfun,fg='white')
    bed.grid(row=1,column=0,sticky=W)
    couch=Checkbutton(furnitureFrame,text="Couch",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var3,command=couchfun,fg='white')
    couch.grid(row=2,column=0,sticky=W)
    desk=Checkbutton(furnitureFrame,text="Desk",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                     variable=var4,command=deskfun,fg='white')
    desk.grid(row=3,column=0,sticky=W)
    table=Checkbutton(furnitureFrame,text="Table",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var5,command=tablefun,fg='white')
    table.grid(row=4,column=0,sticky=W)
    NightStand=Checkbutton(furnitureFrame,text="NightStand",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                           variable=var6,command=nightstandfun,fg='white')
    NightStand.grid(row=5,column=0,sticky=W)
    bookShelf=Checkbutton(furnitureFrame,text="BookShelf",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                          variable=var7,command=bookshelffun,fg='white')
    bookShelf.grid(row=6,column=0,sticky=W)
    dinningTable=Checkbutton(furnitureFrame,text="DinningTable    ",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                             variable=var8,command=dinningtablefun,fg='white')
    dinningTable.grid(row=7,column=0,sticky=W)
    tv=Checkbutton(furnitureFrame,text="Tv",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                   variable=var9,command=tvfun,fg='white')
    tv.grid(row=8,column=0,sticky=W)

    #entry for furniture
    chairText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_chair)
    chairText.grid(row=0,column=1)
    bedText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_bed)
    bedText.grid(row=1,column=1)
    couchText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_couch)
    couchText.grid(row=2,column=1)
    deskText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_desk)
    deskText.grid(row=3,column=1)
    tableText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_table)
    tableText.grid(row=4,column=1)
    NightStandText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_nightStand)
    NightStandText.grid(row=5,column=1)
    bookShelfText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_bookShelf)
    bookShelfText.grid(row=6,column=1)
    dinningTableText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_dinningTable)
    dinningTableText.grid(row=7,column=1)
    tvText=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_tv)
    tvText.grid(row=8,column=1)

    #paint
    red=Checkbutton(paintFrame,text="Regular paint",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                    variable=var10,command=redfun,fg='white')
    red.grid(row=0,column=0,sticky=W)
    pink=Checkbutton(paintFrame,text="Wood",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                     variable=var11,command=pinkfun,fg='white')
    pink.grid(row=1,column=0,sticky=W)
    blue=Checkbutton(paintFrame,text="Glass",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                     variable=var12,command=bluefun,fg='white')
    blue.grid(row=2,column=0,sticky=W)
    black=Checkbutton(paintFrame,text="Masonry",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var13,command=blackfun,fg='white')
    black.grid(row=3,column=0,sticky=W)
    white=Checkbutton(paintFrame,text="Wall panel",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var14,command=whitefun,fg='white')
    white.grid(row=4,column=0,sticky=W)
    yellow=Checkbutton(paintFrame,text="Stone wall",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                       variable=var15,command=yellowfun,fg='white')
    yellow.grid(row=5,column=0,sticky=W)
    gray=Checkbutton(paintFrame,text="Wall Paper",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                     variable=var16,command=grayfun,fg='white')
    gray.grid(row=6,column=0,sticky=W)
    orange=Checkbutton(paintFrame,text="3D wall texture design",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                       variable=var17,command=orangefun,fg='white')
    orange.grid(row=7,column=0,sticky=W)
    brown=Checkbutton(paintFrame,text="Stucco",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var18,command=brownfun,fg='white')
    brown.grid(row=8,column=0,sticky=W)
    #entry for paint
    redText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_red)
    redText.grid(row=0,column=1)
    pinkText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_pink)
    pinkText.grid(row=1,column=1)
    blueText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_blue)
    blueText.grid(row=2,column=1)
    blackText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_black)
    blackText.grid(row=3,column=1)
    whiteText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_white)
    whiteText.grid(row=4,column=1)
    yellowText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_yellow)
    yellowText.grid(row=5,column=1)
    grayText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_gray)
    grayText.grid(row=6,column=1)
    orangeText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_orange)
    orangeText.grid(row=7,column=1)
    brownText=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_brown)
    brownText.grid(row=8,column=1)

    #floor
    tile=Checkbutton(floorFrame,text="Tile ",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                     variable=var19,command=tilefun,fg='white')
    tile.grid(row=0,column=0,sticky=W)
    carpet=Checkbutton(floorFrame,text="Carpet",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                       variable=var20,command=carpetfun,fg='white')
    carpet.grid(row=1,column=0,sticky=W)
    hardwood=Checkbutton(floorFrame,text="Hardwood        ",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                         variable=var21,command=hardwoodfun,fg='white')
    hardwood.grid(row=2,column=0,sticky=W)
    marble=Checkbutton(floorFrame,text="Marble",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                       variable=var22,command=marblefun,fg='white')
    marble.grid(row=3,column=0,sticky=W)
    granit=Checkbutton(floorFrame,text="Granit",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                       variable=var23,command=granitfun,fg='white')
    granit.grid(row=4,column=0,sticky=W)
    stone=Checkbutton(floorFrame,text="Stone",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                      variable=var24,command=stonefun,fg='white')
    stone.grid(row=5,column=0,sticky=W)
    cork=Checkbutton(floorFrame,text="Cork",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                     variable=var25,command=corkfun,fg='white')
    cork.grid(row=6,column=0,sticky=W)
    laminate=Checkbutton(floorFrame,text="Laminate",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                         variable=var26,command=laminatefun,fg='white')
    laminate.grid(row=7,column=0,sticky=W)
    concrete=Checkbutton(floorFrame,text="Concrete",font=('arial',18,'bold'),bg='#6f5e5e',onvalue=1,offvalue=0,
                         variable=var27,command=concretefun,fg='white')
    concrete.grid(row=8,column=0,sticky=W)
    #entry for floor
    tileText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_tile)
    tileText.grid(row=0,column=1)
    carpetText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_carpet)
    carpetText.grid(row=1,column=1)
    hardwoodText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_hardwood)
    hardwoodText.grid(row=2,column=1)
    marbleText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_marble)
    marbleText.grid(row=3,column=1)
    granitText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_granit)
    granitText.grid(row=4,column=1)
    stoneText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_stone)
    stoneText.grid(row=5,column=1)
    corkText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_cork)
    corkText.grid(row=6,column=1)
    laminateText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_laminate)
    laminateText.grid(row=7,column=1)
    concreteText=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=6,state=DISABLED,textvariable=e_concrete)
    concreteText.grid(row=8,column=1)

    #actions done to the entry
    CostFurnitureFrame=Label(costFrame,text="cost of furniture",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    CostFurnitureFrame.grid(row=0,column=0,padx=41)
    textCostFurniture=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=cost1)
    textCostFurniture.grid(row=0,column=1,padx=41)

    CostPaintFrame=Label(costFrame,text="cost of Paint",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    CostPaintFrame.grid(row=1,column=0,padx=41)
    textCostPaint=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=cost2)
    textCostPaint.grid(row=1,column=1,padx=41)

    CostPaintFloor=Label(costFrame,text="cost of Floor",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    CostPaintFloor.grid(row=2,column=0,padx=41)
    textCostFloor=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=cost3)
    textCostFloor.grid(row=2,column=1,padx=41)

    subTotalFrame=Label(costFrame,text="total before tax",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    subTotalFrame.grid(row=0,column=2,padx=41)
    textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=cost4)
    textSubTotal.grid(row=0,column=3,padx=41)

    TaxFrame=Label(costFrame,text="tax",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    TaxFrame.grid(row=1,column=2,padx=41)
    textTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=cost5)
    textTax.grid(row=1,column=3,padx=41)

    totalFrame=Label(costFrame,text="total after tax",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    totalFrame.grid(row=2,column=2,padx=41)
    texttotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=cost6)
    texttotal.grid(row=2,column=3,padx=41)

    #right buttons
    totalbtn=Button(btnFrame,text='total',font=('arial',14,'bold'),fg='white',bg='#6f5e5e',bd=3,padx=5,command=totalcostfun)
    totalbtn.grid(row=0,column=0)
    submitbtn=Button(btnFrame,text='Submit',font=('arial',14,'bold'),fg='white',bg='#6f5e5e',bd=3,padx=5,command=submitfun)
    submitbtn.grid(row=0,column=1)

    #text  area
    txtlabel=Label(reciptFrame,text='Enter any extra details:         ',font=('arial',14,'bold'),fg='white',bg='#6f5e5e')
    txtlabel.grid(row=0,column=0)


    txtrec=Text(reciptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
    txtrec.grid(row=1,column=0)


def ServicesPage():
    global bg3
    top3=Toplevel()
    top3.title("Services")
    top3.geometry("1390x784")
    bg3=PhotoImage(file="shop-bg.png")
    label3=Label(top3,image=bg3)
    label3.place(x=0,y=0,relwidth=1,relheight=1)
    topFrame=Frame(top3,bd=10,relief=RIDGE,bg='#6f5e5e')
    topFrame.pack(side=TOP)
    titleLabel= Label(topFrame,text="Our Services ",font=('Arial',30,'bold'),fg='white',bg='#6f5e5e',width=51,bd=9)
    titleLabel.grid(row=0,column=0)

    def cal1fun():
        cal1=int(e_e1.get())
        cal2=int(e_e2.get())
        totalcal=(cal1)*(cal2)
        c1.set(str(totalcal)+' m2')

    def cal2fun():
        cal3=int(e_e3.get())
        cal4=int(e_e4.get())
        totalcal2=(cal3)*(cal4)
        c2.set(str(totalcal2)+' m2')
    def cal3fun():
        cal5=int(e_e5.get())
        cal6=int(e_e6.get())
        totalcal3=(cal5)*(cal6)*1.5
        c3.set(str(totalcal3)+' watt')


    #variables
    e_e1=StringVar()
    e_e2=StringVar()
    e_e3=StringVar()
    e_e4=StringVar()
    e_e5=StringVar()
    e_e6=StringVar()
    c1=StringVar()
    c2=StringVar()
    c3=StringVar()

    menuFrame=Frame(top3,bd=10,relief=RIDGE,bg='#6f5e5e')
    menuFrame.pack(side=TOP)
    furnitureFrame=LabelFrame(menuFrame,text="Floor Area",font=('Arial',19,'bold'),bd=10,relief=RIDGE,fg='white',bg='#6f5e5e')
    furnitureFrame.pack(side=LEFT)
    paintFrame=LabelFrame(menuFrame,text="Room Area",font=('Arial',19,'bold'),bd=10,relief=RIDGE,fg='white',bg='#6f5e5e')
    paintFrame.pack(side=LEFT)
    floorFrame=LabelFrame(menuFrame,text="Light Intensity",font=('Arial',19,'bold'),bd=10,relief=RIDGE,fg='white',bg='#6f5e5e')
    floorFrame.pack(side=LEFT)
    costFrame1=Frame(furnitureFrame,bd=4,relief=RIDGE,bg='#6f5e5e',pady=10)
    costFrame1.pack(side=BOTTOM)
    costFrame2=Frame(paintFrame,bd=4,relief=RIDGE,bg='#6f5e5e',pady=10)
    costFrame2.pack(side=BOTTOM)
    costFrame3=Frame(floorFrame,bd=4,relief=RIDGE,bg='#6f5e5e',pady=10)
    costFrame3.pack(side=BOTTOM)

    l1=Label(furnitureFrame,text='Width',pady=30,bg='#6f5e5e',fg='white',font=('Arial',15,'bold'))
    l1.pack()
    e1=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=10,textvariable=e_e1)
    e1.pack()
    l2=Label(furnitureFrame,text='Height',pady=30,bg='#6f5e5e',fg='white',font=('Arial',15,'bold'))
    l2.pack()
    e2=Entry(furnitureFrame,font=('arial',18,'bold'),bd=2,width=10,textvariable=e_e2)
    e2.pack()
    fl1=Label(furnitureFrame,text='  ',pady=30,bg='#6f5e5e')
    fl1.pack()

    l3=Label(paintFrame,text='Width',pady=30,bg='#6f5e5e',fg='white',font=('Arial',15,'bold'))
    l3.pack()
    e3=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=10,textvariable=e_e3)
    e3.pack()
    l4=Label(paintFrame,text='Height',pady=30,bg='#6f5e5e',fg='white',font=('Arial',15,'bold'))
    l4.pack()
    e4=Entry(paintFrame,font=('arial',18,'bold'),bd=2,width=10,textvariable=e_e4)
    e4.pack()
    fl1=Label(paintFrame,text='  ',pady=30,bg='#6f5e5e')
    fl1.pack()

    l5=Label(floorFrame,text='Width',pady=30,bg='#6f5e5e',fg='white',font=('Arial',15,'bold'))
    l5.pack()
    e5=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=10,textvariable=e_e5)
    e5.pack()
    l6=Label(floorFrame,text='Height',pady=30,bg='#6f5e5e',fg='white',font=('Arial',15,'bold'))
    l6.pack()
    e6=Entry(floorFrame,font=('arial',18,'bold'),bd=2,width=10,textvariable=e_e6)
    e6.pack()
    fl1=Label(floorFrame,text='  ',pady=30,bg='#6f5e5e')
    fl1.pack()


    #actions done to the entry
    CostFurnitureFrame=Label(costFrame1,text="Floor Arae:",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    CostFurnitureFrame.grid(row=0,column=0,padx=11)
    textCostFurniture=Entry(costFrame1,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=c1)
    textCostFurniture.grid(row=0,column=1,padx=11)

    CostPaintFrame=Label(costFrame2,text="Room Area",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    CostPaintFrame.grid(row=1,column=0,padx=30)
    textCostPaint=Entry(costFrame2,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=c2)
    textCostPaint.grid(row=1,column=1,padx=11)

    CostPaintFloor=Label(costFrame3,text="Light Intensity",font=('arial',16,'bold'),bg='#6f5e5e',fg='white')
    CostPaintFloor.grid(row=2,column=0,padx=30)
    textCostFloor=Entry(costFrame3,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=c3)
    textCostFloor.grid(row=2,column=1,padx=11)


    calbtn1=Button(furnitureFrame,text='Calculate',font=('arial',14,'bold'),fg='white',bg='#6f5e5e',bd=3,padx=5,
                   command=cal1fun)
    calbtn1.pack()
    calbtn2=Button(paintFrame,text='Calculate',font=('arial',14,'bold'),fg='white',bg='#6f5e5e',bd=3,padx=5,
                   command=cal2fun)
    calbtn2.pack()
    calbtn3=Button(floorFrame,text='Calculate',font=('arial',14,'bold'),fg='white',bg='#6f5e5e',bd=3,padx=5,
                   command=cal3fun)
    calbtn3.pack()


s=Label(window,text=" ",bg="white").grid(row=0,column=0,padx=250)
btn1=Button(window,text="About us",
            font=("Comic Sans",15),
            bg="#6f5e5e",
            fg="white",
            cursor="hand2",
            activeforeground="white",
            activebackground="#6f5e5e",
            borderwidth=0)
btn1.grid(row=1,column=1,padx=20,pady=50)
btn2=Button(window,text="Services",
            font=("Comic Sans",15),
            bg="#6f5e5e",
            fg="white",
            cursor="hand2",
            activeforeground="white",
            activebackground="#6f5e5e",
            borderwidth=0,
            command=ServicesPage)


btn2.grid(row=1,column=2,padx=20,pady=50)
btn3=Button(window,text="Shop",
            font=("Comic Sans",15),
            bg="#6f5e5e",
            fg="white",
            cursor="hand2",
            activeforeground="white",
            activebackground="#6f5e5e",
            borderwidth=0,
            command=ShopPage)
btn3.grid(row=1,column=3,padx=20,pady=50)
btn4=Button(window,text="Login",
            font=("Comic Sans",15),
            bg="#6f5e5e",
            fg="white",
            cursor="hand2",
            activeforeground="white",
            activebackground="#6f5e5e",
            borderwidth=0,
            command=LoginPage)
btn4.grid(row=1,column=4,padx=20,pady=50)

window.mainloop()#display window