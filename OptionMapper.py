from tkinter import *
import mibian

class OptionSimulation:

    def __init__(self,master):
        master.title('Option Mapper')
        master.iconbitmap('abc.ico')
        master.minsize(width=1000, height=500)
        master.maxsize(width=1000, height=500)
        self.topframe = Frame(master,width=500, height=500)
        self.topframe.pack()
        self.bottomframe = Frame(master, width=500, height=500)
        self.bottomframe.pack()
        self.middleframe = Frame(master, width=500, height=500)
        self.middleframe.pack()
        self.label1 = Label(self.topframe, text='Underlying Price', fg='black')
        self.label2 = Label(self.topframe, text='Strike', fg='black')
        self.label3 = Label(self.topframe, text='Days to Expiry', fg='black')
        self.label4 = Label(self.topframe, text='Volatility', fg='black')
        self.label5 = Label(self.topframe,text='Simulation Difference',fg='black')
        self.label6 = Label(self.topframe,text='Buy/Sell Price',fg='black')
        self.label1.grid(row=2, column=4)
        self.label2.grid(row=2, column=8)
        self.label3.grid(row=2, column=12)
        self.label4.grid(row=2, column=16)
        self.label5.grid(row =2,column =20)
        self.label6.grid(row=2,column =22)
        self.underlying = Entry(self.topframe)
        self.strike = Entry(self.topframe)
        self.days = Entry(self.topframe)
        self.vol = Entry(self.topframe)
        self.diff = Entry(self.topframe)
        self.price =Entry(self.topframe)

        self.underlying.grid(row=4, column=4)
        self.strike.grid(row=4, column=8)
        self.days.grid(row=4, column=12)
        self.vol.grid(row=4, column=16)
        self.diff.grid(row =4,column=20)
        self.price.grid(row=4,column=22)
        self.button1 = Button(self.topframe,text ='Simulate',command=self.pricesimulation)
        self.button1.grid(row=6,column=22)


    def delete_entries(self):
        pass
    def createrange(self,undprice, vol, udif):
        uprice_list = []
        vol_list = []
        vol_list.append(vol)
        uprice_list.append(undprice)
        uvol = vol
        dvol = vol
        uprice = undprice
        dprice = undprice
        for val in range(3):
            u = uvol + 1
            n = dvol - 1
            m = uprice + udif
            v = dprice - udif
            uprice_list.append(m)
            uprice_list.append(v)
            vol_list.append(u)
            vol_list.append(n)
            uvol = u
            dvol = n
            uprice = m
            dprice = v
        return sorted(uprice_list), sorted(vol_list)

    def pricesimulation(self):

        undprice =self.underlying.get()
        vol      =self.vol.get()
        udif     =self.diff.get()
        strike   =self.strike.get()
        days     =self.days.get()
        price    =float(self.price.get())
        data = self.createrange(int(undprice), float(vol), float(udif))
        i = 0.06
        row = 4
        for und in data[0]:
            col =4
            for v in data[1]:
                undlabel1 = Label(self.middleframe,text =und)
                undlabel1.grid(row=2,column=row)
                vlabel = Label(self.middleframe, text=v)
                vlabel.grid(row=col, column=2)

                Oprice = mibian.BS([und, strike, i, days], volatility=v)
                labe2 = Label(self.middleframe, text='CALL', bg='green',fg='white')
                labe2.grid(row=2, column=2)
                call =round(Oprice.callPrice,2)
                if round(price, 0) == round(call, 0):
                    csa = Entry(self.middleframe,bg='green',fg='white' )
                    csa.insert(END,call)
                else:
                    csa = Entry(self.middleframe)
                    csa.insert(END,call)
                csa.grid(row=row,column=col)
                #############################
                undlabel2 = Label(self.bottomframe, text=und)
                undlabel2.grid(row=2, column=row)
                vlabe2 = Label(self.bottomframe, text=v)
                vlabe2.grid(row=col, column=2)

                labe1 = Label(self.bottomframe, text='PUT', bg='red',fg='white')
                labe1.grid(row=2,column=2)
                put =round(Oprice.putPrice, 2)

                if round(price,0) ==round(put,0):
                    psa = Entry(self.bottomframe,bg='red',fg='white')
                    psa.insert(END,put)
                else:
                    psa = Entry(self.bottomframe)
                    psa.insert(END,put)
                psa.grid(row=row, column=col)

                col = col+2

            row =row+2



root = Tk()
b=OptionSimulation(root)
root.mainloop()















