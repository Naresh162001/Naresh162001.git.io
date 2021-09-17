#!C:\Users\nares\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\pythonw.exe
print("Content-Type:text/html")
print()
import cgi
f=cgi.FieldStorage()
import mysql.connector
con=mysql.connector.connect(host='localhost',port='3306',database='banking_system',user='root',password='')
cus=con.cursor()
print("""<html>
<head>
    <link rel='icon' href='icon1.png' type='image/icon type'>
    <br>
    <title>Transaction</title>
    <link rel="stylesheet" href="table.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="table1.css">
    <!--<style>
        @media screen and (min-width:920px){
	        h1{font-size:350%;}
	        th{font-size:150%;}
	        tr{font-size:175%;}
	        li{font-size:150%;}
	        input{font-size:90%}
	        select{font-size:90%}
	        #menuBtn{width: 70px;right: 65px;}
        }
        @media screen and (min-width:560px) and (max-width:920px){
	        h1{font-size:245%;}
	        th{font-size:105%;}
	        tr{font-size:122.5%;}
	        li{font-size:105%;}
	        input{font-size:70%}
	        select{font-size:70%}
	        #menuBtn{width: 49px;right: 45.5px;}
        }
        @media screen and (min-width:230px) and (max-width:560px){
	        #menuBtn{width: 35px;right: 32.5px;}
        }
        @media screen and (max-width:230px){
	        h1{font-size:105%;}
	        th{font-size:45%;}
	        tr{font-size:52.5%;}
	        li{font-size:45%;}
	        input{font-size:30%}
	        select{font-size:30%}
	        #menuBtn{width: 21px;right: 19.5px;}
        }
        
              
              </style>-->
 </head>
 <body class="black">
     <h1>Make Transaction</h1>
     <h3 id="bankname">Spark<div Style="color:#0000ff;"> Bank</div></h3>
     <nav id="sideBox">
        <ul>
            <li><a href="index.html">HOME</a></li>
            <li><a href="customer.py">OUR CUSTOMERS</a></li>
            <li><a href="transaction_history.py">TRANSACTION HISTORY</a></li>
            <li><a href="transfer.py">TRANSFER MONEY</a></li>
            <li><a href="create_user.py">New User</a></li>
        </ul>
    </nav>
    <img src="menuicon.png" id="menuBtn">
    <script>
        var menuBtn = document.getElementById("menuBtn");
        var sideBox = document.getElementById("sideBox");
        sideBox.style.right = "-250px"
        menuBtn.onclick = function () {
            if (sideBox.style.right == "-250px") {
                sideBox.style.right = "0px";
            }
            else {
                sideBox.style.right = "-250px";
            }
        }
     </script><table class="table1" id="transaction_table">""")
try:
     cus.execute("Select Name,Account_No from customers;")
     c=cus.fetchall()
except:
     con.rollback()
b=f.getvalue('account_no')
na,a_n=[i[0] for i in c],[i[1] for i in c]
index_a_n=a_n.index(int(b))
del a_n[index_a_n]
del na[index_a_n]
try:
     cus.execute("Select name,Account_No,email,balance from customers where Account_NO={};".format(b))
     s=cus.fetchall()
except:
     con.rollback()
print("""<form action='transaction_history.py' method='post'><input type='hidden' value='t' name='flag'><input type='hidden' value="{}" name='sender' required><tr><td>Receiver</td><td>
 <select name='receiver' id='select_box'>""".format(b)) 
for i,j in zip(na,a_n):
     print("<option value='{}'>{}</option>".format(j,i))
for i in s:    
    print("</select></td><tr><td>Amount</td><td><input type='number' name='amount' min='100' max='{}' required></td></tr>".format(i[3]))
    print("<tr style='background-color:black;'><td colspan='2'><input type='submit' class='transfer_button  btn1' name='Transfer' value='Transfer'></td></tr></form></table>")
    print("""
     <h1>Your Details<h1>
     <table class="table1">
<tr><th>Name</th><th>Account_NO</th><th>Email_ID</th><th>Balance</th></tr>""")

    print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(i[0],i[1],i[2],i[3]))
print("""</table></body>
<footer style="font-size:20%;" class="footer">&#169;Copyright 2021 Mabe by Naresh<br>
	for the Project of The Sparks Foundation</footer>""")
print("</html>")
