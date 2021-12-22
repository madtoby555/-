# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:12:32 2021

@author: Mad_ToBy
this python srcipt was designed for retrieve data from database
and genereate html we need for website 
"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import sqlite3

def create_table():
    conn = sqlite3.connect('data.db')
    cursor  = conn.cursor()
    cursor.execute("CREATE TABLE"+'USER'+
                 '''(ID INT PRIMARY KEY NOT NULL,
                    NAME             TEXT  NOT NULL ,
                    TEMP             REAL NOT NULL , 
                    HEALTH           INT  NOT NULL ,
                    ENTER            INT  NOT NULL ,
                    TIME            text  NOT NUll 
                    );''')
    conn.commit()
    conn.close()

def retrieve_database(string):
    conn = sqlite3.connect('data.db')
    cursor  = conn.cursor()
    if string == 'all':
        cursor.execute("select * from USER")
        data = pd.DataFrame(cursor.fetchall())
    if string == 'temp':
       cursor.execute('select * from USER  where temp >= 38.0 ')
       data = pd.DataFrame(cursor.fetchall())
    if string =='health':
       cursor.execute('select * from USER  where health = 0', )
       data = pd.DataFrame(cursor.fetchall())
    conn.close()
    return data 

def generate_table(alldata,tempdata,healthdata):
    ''' this function is for generate the apporatie html file for showing
    every 1 mins will refresh the html

    input 
    ----------------------------------------------------------------------
    alldata    ------ all the records in the database table 
    tempdata   ------ the records whose tempture is over 38.6
    healthdata ------ the records whose health cloumns is 1
    
    output
    --------------------------------------------------------
    html file to replace the originl file 
    '''
    alldata_table = ''
    for (index,record) in alldata.iterrows():
        alldata_table += '<tr>  \n'
        for i in range(0,5):
            alldata_table += '<td>' + str(record[i])+'</td>\n'
        alldata_table += '</tr> \n'
    tempdata_table = ''
    for (index,record) in tempdata.iterrows():
        tempdata_table += '<tr>  \n'
        for i in range(0,5):
            if i == 4:
                tempdata_table += "<td class = 'unhealth'>"+ str(record[i])+"</td>\n"
            else:
                tempdata_table += '<td>' + str(record[i])+'</td>\n'
        tempdata_table += '</tr> \n'
    healthdata_table = ''
    for (index,record) in healthdata.iterrows():
        healthdata_table += '<tr>  \n'
        for i in range(0,5):
            if i == 1:
                healthdata_table += "<td class = 'unhealth'>" + str(record[i])+'</td>\n'
            else:
                healthdata_table += '<td>' + str(record[i])+'</td>\n'
        healthdata_table += '</tr> \n'
    return alldata_table , tempdata_table,healthdata_table

def generate_html(alldata_table,tempdata_table,healthdata_table):
    html = '''
    <!DOCTYPE html>
    <html lang="zh">
    <head>
    <meta charset="UTF-8">
    <title>汕头大学防疫检测控制台</title>
    <link rel="stylesheet" type="text/css" href="../static/style.css">
    <!--[if lt IE 9]>
    <script>
      document.createElement("article");
      document.createElement("aside");
      document.createElement("footer");
      document.createElement("header");
      document.createElement("main");
      document.createElement("nav");
      document.createElement("section");
    </script>
    <![endif]-->
  </head>
  <body>
    <header class="banner">
      <h1>汕头大学防疫检测控制台</h1>
      <p>I am for everyone, everyone is for me</p>
    </header>

    <nav>
      <ul>
        <li><a href="dianzisai.html">首页</a></li>
        <li><a href="archive.html">实时数据</a></li>
        <li><a href="about.html">关于</a></li>
      </ul>
    </nav>

    <main>
      <section>
        <h2>全部数据</h2>
        <article>
          <header>
            <h3>下列数据包含所有用户</h3>
            <strong id = 'small'>系统时间:2021年3月2日</strong>
          </header>
            <table id  = 'alldata' class = 'table'>
                <tr>
                   <th>姓名</th>
                    <th>健康码情况</th>
                    <th>时间 </th>
                    <th>体温</th>
                     <th>编号</th>
                </tr>
                ''' + alldata_table +'''
            </table>
        </article>
      </section>

      <section>
        <h2>异常情况</h2>
        <article>
          <header>
            <h3>温度不达标</h3>
            <p>有3位未处理</p>
          </header>
        <table>
            <tr>
                    <th>姓名</th>
                    <th>健康码情况</th>
                    <th>时间 </th>
                    <th>体温</th>
                     <th>编号</th>
            </tr>
            '''+ tempdata_table+'''
        </table>
        </article>

        <article>
          <header>
            <h3>健康码不达标</h3>
            <p>目前仍有3位未处理</p>
          </header>
          <table>
            <tr>
                    <th>姓名</th>
                    <th>健康码情况</th>
                    <th>时间 </th>
                    <th>体温</th>
                     <th>编号</th>
        </tr>'''+healthdata_table+'''
            
        </table>
        </article>
      </section>
      <section float = right>
         <h2 >日流量预览 </h2> 
          <article>
            <header>
            </header>
            <img src="../static/aa.png" >
          </article>
      </section>
    </main>

    <aside>
      <h2><a href="report.html">报告故障</a></h2>
      <p>为了自身安全，请佩戴口罩</p>
    </aside>

    <footer>
      <p>Footer Information</p>
    </footer>
  <script type="text/javascript">
        function del(rowid){
            var del=window.confirm("您确定删除吗？");
            if(del){
                location.href="delete.php?id="+rowid;
            }else{

            }
        }
    </script>
  </body>
</html>
    '''
    return str(html)
