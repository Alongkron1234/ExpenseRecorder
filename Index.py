from os import startfile
from tkinter import *
from tkinter import ttk, messagebox
import csv
from tkinter import font
from datetime import datetime
root=Tk()
root.title('โปรแกรมบันทึกค่าใช้จ่าย by Alongkron')
root.geometry('700x750+400+80')

#2.24.55
#################

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')


def About():
    messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจากมั้ย')

helpmenu=Menu(menubar)
menubar.add_cascade(label='help', menu=helpmenu)
helpmenu.add_command(label='About', command=About)

donatemenu=Menu(menubar)
menubar.add_cascade(label='Donate', menu=donatemenu)
#############

#B1=Button(root, text='Hello')
#B1.pack(ipadx=50, ipady=20)


days={'Mon':'จันทร์','Tue':'อังคาร','Wed':'พุธ','Thu':'พฤหัสบดี',
        'Fri':'ศุกร์','Sat':'เสาร์','Sun':'อาทิตย์'}

        
def Save(event=None):
    try:
        expense=V_expense.get()
        price=V_price.get()
        order=V_order.get()

        if expense=='':
            print('NoData')
            messagebox.showwarning('Error', 'กรุณากรอกรายจ่าย')
            return
        elif price=='':
            messagebox.showwarning('Error', 'กรุณากรอกราคา')
            return
        elif order=='':
            order=1

        result=int(price)*int(order)
        print(f'รายการ: {expense} ราคา: {price}')
        print(f'จำนวน {order} ราคารวม {result}')
        text=f'รายการ: {expense} ราคา: {price}\n'
        text=text + f'จำนวน {order} ราคารวม {result} บาท'
        V_show.set(text)
        V_expense.set('')
        V_price.set('')
        V_order.set('')
        E1.focus()
        

        #___บันทึกข้อมูลลงcsv___##
        today=datetime.now().strftime('%a')
        dt=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        dt=days[today] + '-' + dt
        with open('savedata.csv','a', encoding='utf-8', newline='') as f: #withเปิดไฟล์แล้วปิด 'a' บันทึกข้อมูลเรื่อยๆ
            fw=csv.writer(f) #สร้างฟังค์ชั่นสำหรับเขียนข้อมูล
                            
            data=[dt,expense, price, order, result]  #ข้อมูลที่ต้องการใส่
            fw.writerow(data)
        update_table()
    except Exception as e:
        print('ERROR:',e)
        messagebox.showwarning('Error', 'กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        V_expense.set('')
        V_price.set('')
        V_order.set('')
        E1.focus()
        
      
        

FONT1=(None, 17)

###########################################################
Fd=PhotoImage(file='D:\Icon\Foldeicon.png')
lt=PhotoImage(file='D:\Icon\Checklist-icon (1).png')

n=ttk.Notebook(root)
n.pack(fill=BOTH, expand=1)

P1=Frame(n) #สร้างFrame
# P1.pack()  #ไม่ต้องใส่
P2=Frame(n) #สร้างFrame
# P2.pack()  #ไใ่ต้องใส่

n.add(P1, text=f'{"Add Expense": ^{20}}', image=Fd, compound='top',) #เหมือนใช้ตอนนี้แพ็คแทน pack()   P1
n.add(P2, text=f'{"Expense list": ^{21}}', image=lt, compound='top') #เหมือนใช้ตอนนี้แพ็คแทนpack()    P2


Im=PhotoImage(file='D:\Icon\money-wallet-icon.png')

F1=Frame(P1)  #โปรแกรมถูกใส่ใน F1 แล้วเอา F1 ใส่ P1
F1.pack()

L=ttk.Label(F1, image=Im)
L.pack(pady=10)
##text1###
L=ttk.Label(F1, text='รายการค่าใช้จ่าย', font=FONT1).pack(pady=10)

V_expense=StringVar()
E1=ttk.Entry(F1,textvariable=V_expense,font=FONT1)
E1.pack()

###text2###
L=ttk.Label(F1, text='ราคา (บาท)', font=FONT1).pack(pady=10)

V_price=StringVar()
E2=ttk.Entry(F1,textvariable=V_price,font=FONT1)
E2.pack()

####text3###
V_order=StringVar()

L=ttk.Label(F1, text='จำนวน', font=FONT1).pack(pady=10)
E3=ttk.Entry(F1, textvariable=V_order,font=FONT1)
E3.pack()

Bm=PhotoImage(file='D:\Icon\Save-icon.png')

B2=ttk.Button(F1, text='save', command=Save, image=Bm, compound='left')
B2.pack(ipadx=10,ipady=5, pady=15)

V_show=StringVar()
V_show.set('------ผลลัพธ์-------')
show=ttk.Label(F1, textvariable=V_show,font=FONT1, foreground='green')
show.pack(pady=20)

E3.bind('<Return>', Save)

###########Tab2#################

def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:    #เปิดfile csv ชื่อว่า f
        fr=csv.reader(f)  
        data=list(fr)
    return data
        # print(data)
        # print('--------')
        # print(data[0][0])
###############################
# LL=ttk.Label(P2, text='รายการทั้งหมด', font=FONT1, foreground='green')
# LL.pack()
################################## 
# F2=Frame(P2)
# F2.pack()


# def update_record():
#     getdata=read_csv()
#     V_Shows.set('')
#     text=''
#     for d in getdata:
#         txt='{} {} {} {} {}\n'.format(d[0], d[1], d[2], d[3], d[4])
#         text=text+txt
#     V_Shows.set(text)

# V_Shows=StringVar()
# L4=ttk.Label(F2, textvariable=V_Shows, font=(None, 13), foreground='green')
# L4.pack(pady=10)
# update_record()
#################################


#tabel
LL=ttk.Label(P2, text='ตารางรายการทั้งหมด', font=FONT1, foreground='green')
LL.pack(pady=10)
header=['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']    #เหมือนจองที่ heading
resulttable=ttk.Treeview(P2,columns=header,show='headings',height=15)
resulttable.pack()
# for i in range(len(header)):
#     resulttable.heading(header[i],text=header[i])                #ใส่heading

for h in header:
    resulttable.heading(h,text=h)


headerwidth=[170,170,80,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

# resulttable.insert('','end', value=['จันทร์','น้ำดื่ม',30,5,120])

def update_table():
    resulttable.delete(*resulttable.get_children())   #clear
    data=read_csv()
    for d in data:
        resulttable.insert('',0,value=d)

update_table()




root.bind('<Tab>', lambda x: E2.focus())

root.mainloop()