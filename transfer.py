#!C:\Users\nares\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\pythonw.exe
print("Content-Type:text/html")
print()
import cgi
import mysql.connector
print("""<html>
<head>
    <link rel='icon' href='icon1.png' type='image/icon type'>
    <title>Transfer Money</title>
    <link rel="stylesheet" href="table.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="table1.css">
</head>
<body class="black">
    <h1 class="table_name">Transfer Money</h1>
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
con=mysql.connector.connect(host='localhost',port='3306',database='banking_system',user='root',password='')
cus=con.cursor()
try:
    cus.execute("select name,Account_No,email,balance from customers;")
    c=cus.fetchall()
except:
    con.rollback()

print("""<div class="table1div">
<table class="table1">
<tr><th>S.No</th><th>Name</th><th>Account_NO</th><th>Email_ID</th><th>Balance</th><th>$</tr>""")
n=1
for i in c:
    print("""<form action='transaction.py' method='post'>
                 <input type='hidden' value={} name='account_no'>
                 <tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td><input type='submit' class='transfer_button' value='Transfer'></tr></form>""".format(i[1],n,i[0],i[1],i[2],i[3]))
    n=n+1
print("</table></div>")
print("""</body>
<footer>&#169;Copyright 2021 Mabe by Naresh<br>
	for the Project of The Sparks Foundation</footer>
<html>""")
