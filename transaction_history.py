#!C:\Users\nares\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\pythonw.exe
print("Content-Type:text/html")
print()
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost',port='3306',database='banking_system',user='root',password='')
cus=con.cursor()
f1=cgi.FieldStorage()

print("""<html>
<head>
    <link rel='icon' href='icon1.png' type='image/icon type'>
    <title>Transaction Histroy</title>
    <link rel="stylesheet" href="table1.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="table1.css">
</head><body class="black">""")
if((f1.getvalue('flag')=='t')):
    amount=int(f1.getvalue('amount'))
    a_no=[int(f1.getvalue('sender')),int(f1.getvalue('receiver'))]
    name=[]
    balance=0
    try:
        cus.execute("select balance from customers where Account_No={}".format(a_no[0]))
        c=cus.fetchall()
        for i in c:
            balance=i[0]  
    except:
        con.rollback()
    for i in a_no:
        try:
            cus.execute("select name from customers where Account_No={};".format(i))
            a=cus.fetchall()
            for j in a:
                name.append(j[0])
        except:
            con.rollbak() 
    try:
        cus.execute("insert into history (Sender_Name,Sender_NO,Receiver_Name,Receiver_no,Amount) values(%s,%s,%s,%s,%s);",(name[0],a_no[0],name[1],a_no[1],amount))
        con.commit()
        cus.execute("update customers set Balance=(select Balance from customers where Account_No={})-{} where Account_No={};".format(a_no[0],amount,a_no[0]))
        con.commit()
        cus.execute("update customers set Balance=(select Balance from customers where Account_No={})+{} where Account_No={};".format(a_no[1],amount,a_no[1]))
        con.commit()
        print("""<script>
    alert("Transaction Completed Successfully!!!");
    </script>""")
    except:
        print("""<script>
    alert("Transaction Failed!!!");
    </script>""")
    
        con.rollback()
print("""<h1 class="table_name">Transaction Histroy</h1>
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
     </script>""")

try:
    cus.execute("select * from History;")
    c=cus.fetchall()
except:
    con.rollback()

print("""<div class="table1div">
    <table class="table1">
    <tr><th>From</th><th>Account_NO</th><th>To</th><th>Account_NO</th><th>Date</th><th>Amount</th></tr>""")
c.reverse()
for i in c:
    print("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(i[0],i[1],i[2],i[3],i[4],i[5]))
print("</table></div>")
print("""</body>
<footer>&#169;Copyright 2021 Mabe by Naresh<br>
	for the Project of The Sparks Foundation</footer>
    <html>""")
