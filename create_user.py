#!C:\Users\nares\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\pythonw.exe
print("Content-Type:text/html")
print()
print("""<html>
<head>
	<link rel='icon' href='icon1.png' type='image/icon type'>
	<link rel="stylesheet" href="table.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="table1.css">
    <style>
        input,select{
		margin-left:10%;
		width:80%;
		display:block;
		}
		td,th{
		width:50%;
		}
		a{
	text-decoration:none;
}
</style>
""")
import cgi
import mysql.connector
con=mysql.connector.connect(host='localhost',port='3306',database='banking_system',user='root',password='')
cus=con.cursor()
f1=cgi.FieldStorage()
if(f1.getvalue('account_no')):
    print("""<title>Details</title></head>
    <body class="black"><h1>Details</h1>
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
    a_no=f1.getvalue('account_no')
    cus.execute("select * from customers where Account_No={};".format(a_no))
    d=cus.fetchall()
    print("<table class='table1'>")
    for i in d:
        print("""<tr><th>Content</th><th>Data</th></tr>
        <tr><td>Name</td><td>{}</td></tr>
        <tr><td>Account No</td><td>{}</td></tr>
        <tr><td>Gender</td><td>{}</td></tr>
        <tr><td>Age</td><td>{}</td></tr>
        <tr><td>Phone NO</td><td>{}</td></tr>
        <tr><td>Email Id</td><td>{}</td></tr>
        <tr><td>Balance</td><td>{}</td></tr>""".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print("""</table><br>
    <table style="width:95%;margin-left:2.5%;margin-right:2.5%;">
    <tr rowspan="1">
   <form action='transaction.py' method='post'>
        <input type="hidden" name="account_no" value="{}"><td>
        <input type="submit" name="transfer_button" value="Transfer" class="transfer_button btn1"></form></td>
        <td><a href="customer.py"><input style="width:80%;height=40%;" type="button" value="Back" class="transfer_button btn1"></a></td></tr></table></body>""".format(a_no))
    
        
else:
    print("""<title>Create User</title>
    </head><h1 style="margin-left:20%;margin-right:20%;">Enter Your Details to Create Account</h1>
<body class="black">
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
     </script>
    <form action="customer.py" method="post"><table class="table1">
        <input type="hidden" name="flag" value="c">
        <tr><td>Name:</td><td><input type="text" name="name" parrern="[A-Za-z. ]" required></td></tr>
        <tr><td>Gender:</td><td><select name="gender"><option value="Male">Male</option><option value="Female">Female</option></select></td></tr>
        <tr><td>Age:</td><td><input type="number" name="age" min="18" max="100" required></td></tr>
        <tr><td>Phone NO:</td><td><input type="number" name="phone_no" pattern="[0-9]{10}" required></td></tr>
        <tr><td>Email Id:</td><td><input type="text" name="email" pattern="[a-z][0-9][@][a-z]{3-5}.com" required></td></tr>
	    <tr><td>Deposit Amount:</td><td><input type="number" min="100" pattern="[0-9]" required name="depositamount"></tr><tr><br></tr></table>
	    <table style="width:97.5%;margin-right:2.5%;">
        <tr><td style="text-align:center;" colspan="2"><input style="margin-right:10%;" type="submit" name="submit" class="transfer_button btn1" value="Proceed"></td></tr></table>
    </form>
</body>""")
print("""<footer class='footer'>&#169;Copyright 2021 Mabe by Naresh<br>
	for the Project of The Sparks Foundation</footer>
</html>""")