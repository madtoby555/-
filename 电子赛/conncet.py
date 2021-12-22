import serial
from time import sleep
import sqlite3
import time 
def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data

def datasrefresh():
    datalist =[]
    datadivdedlist = [] #/dev/ttyUSB0
    while True:
        time.sleep(5)
        data =recv(ser)
        if data != b'' :
            print("receive : ",data)
            datalist.append(data.decode())
            break;
    for data in datalist[0].split():
        datadivdedlist.append(data)
    print(datadivdedlist)
# then we insert the data into database
    print('here we insert the data',datalist)
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        print(datalist)
        datadivdedlist.append(2)
        cursor.execute('insert into USER VALUES(?,?,?,?,?)',datadivdedlist)
        conn.commit() 
        time.sleep(1)
        print('done')
        conn.close()
    except Exception as e:
        print(e)