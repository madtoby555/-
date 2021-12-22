import dianzisai
import conncet 
import time
import serial
import sqlite3
"""
这个将会是运行的主程序，需要完成更新html,与树莓派socket通讯并存数据到数据库，运行后还需运行flaskweb 以及ngrok
"""
ser = serial.Serial(port='COM4', baudrate=9600, bytesize=8, stopbits=1, timeout=2) #/dev/ttyUSB0
if ser.isOpen() :
        print("open success")
else :
        print("open failed") 
i = 1;
while True:
    datalist =[]
    datadivdedlist = [] #/dev/ttyUSB0
    while True:
        time.sleep(2)
        data =conncet.recv(ser)
        if data != b'' and data !=b'\x00':
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
        datadivdedlist.append(i)
        i = i +1
        cursor.execute('insert into USER VALUES(?,?,?,?,?)',datadivdedlist)
        conn.commit() 
        time.sleep(1)
        print('done')
        conn.close()
    except Exception as e:
        print(e)
    alldata = dianzisai.retrieve_database('all')
    print('get alldata')
    tempdata = dianzisai.retrieve_database('temp')
    print('get tempdata')
    healthdata = dianzisai.retrieve_database('health')
    print('get healthdata')
    (alldata_table , tempdata_table,healthdata_table) = dianzisai.generate_table(alldata,tempdata,healthdata)
    html = dianzisai.generate_html(alldata_table , tempdata_table,healthdata_table)
    print('writing html')
    r = open('./templates/test.html','w',encoding=('utf-8'))
    r.write(html)
    r.flush()
    r.close()
    print('done')
    time.sleep(5)

