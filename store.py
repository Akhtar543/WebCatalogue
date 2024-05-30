from flask import Flask,render_template,request,redirect,url_for
from os import path
import calendar

app=Flask(__name__)

cartproduct=[]
cartimg=[]
cartprice=[]
cartamount=[]
headings=['Items','Product','Quantity','Price']
headings2=['Product','Quantity','Price']
hiddenamount=[]
count=0
total=0
tax=0
productimg=''
conf=''
error=''
regusername=None
regpassword=None

@app.route('/',methods=['GET','POST'])
def signin():
    global regusername,regpassword
    if request.method=="GET":
        return render_template("/store/signIn.html", error="")
    else:
        password=request.form.get("password")
        username=request.form.get("username")
        if regusername==None and regpassword==None:
            if len(password) > 4 and len(username) > 2:
                regusername=username
                regpassword=password
                return redirect(url_for("info"))
            else:
                if len(password) < 5 and len(username) < 3:
                    return render_template("/store/signIn.html", error="Both username and password are too short")
                if len(password) < 5:
                    return render_template("/store/signIn.html", error="Your password is too short(5 or more)")
                if len(username) < 3:
                    return render_template("/store/signIn.html", error="Your username is too short (3 or more)")
        else:
            if password==regpassword and username==regusername:
                return redirect(url_for("info"))
            else:
                return render_template("/store/signIn.html", error="Incorrect Username or Password")

@app.route('/Personal Information',methods=['GET','POST'])
def info():
    global fname,lname,dob,pnum,address,email,dccn,expd,cvv,count
    if request.method=='GET':
        if count==0:
            return render_template('/store/info.html',regusername=regusername)
        else:
            return render_template('/store/info.html',regusername=regusername,firstn=fname,
                                   lastn=lname,dob=dob,pnum=pnum,address=address,
                                   email=email,dccn=dccn,expd=expd,cvv=cvv)
    else:
        count=1
        calmcheck=0
        fname=request.form.get('txtfirst')
        lname=request.form.get('txtlast')
        dob=request.form.get('txtdob')
        pnum=request.form.get('txtphone')
        address=request.form.get('txtaddress')
        email=request.form.get('txtemail')
        dccn=request.form.get('txtd/ccn')
        expd=request.form.get('txtexpd')
        cvv=request.form.get('txtcvv')
        if len(fname)>0 and len(lname)>0:
            calmcheck+=1
        if ..dob..:#datepart
            calmcheck+=1
        if pnum==10:
            calmcheck+=1
        if len(address)>0:
            calmcheck+=1
        if len(email)>0:
            calmcheck+=1
        match len(dccn):
            case 15:
                calmcheck+=1
            case 16:
                calmcheck+=1
        if ..expd..: #datepart
            calmcheck+=1
        match len(cvv):
            case 3:
                calmcheck+=1
            case 4:
                calmcheck+=1
        if calmcheck==8:
            return redirect(url_for('shopping'))
        else:
            error='An error in one the information you have entered.'
            return render_template('/store/info.html',regusername=regusername,error=error)

@app.route('/ChromeHearts',methods=['GET','POST'])
def shopping():
    global productimg,productname,price
    if request.method=='GET':
        total=0
        return render_template('/store/shopping.html',conf=conf)
    else:
        productimg=request.form.get('pick')
        match productimg:
            case 'a':
                productname='prod1' #all soon to change(product name, price, and add more ofc)
                price=10.00
                return redirect(url_for('shop',productname=productname))
            case 'b':
                productname='prod2'
                price=20.00
                return redirect(url_for('shop',productname=productname))
            case 'c':
                productname='prod3'
                price=30.00
                return redirect(url_for('shop',productname=productname))
            case 'd':
                productname='prod4'
                price=40.00
                return redirect(url_for('shop',productname=productname))
            case 'e':
                productname='prod5'
                price=50.00
                return redirect(url_for('shop',productname=productname))
            case 'f':
                productname='prod6'
                price=60.00
                return redirect(url_for('shop',productname=productname))
            case 'g':
                productname='prod7'
                price=70.00
                return redirect(url_for('shop',productname=productname))
            case 'h':
                productname='prod8'
                price=80.00
                return redirect(url_for('shop',productname=productname))
            case 'i':
                productname='prod9'
                price=90.00
                return redirect(url_for('shop',productname=productname))
            case 'cart':
                return redirect(url_for('cart'))

@app.route('/<productname>',methods=['GET','POST'])
def shop(productname):
    global conf,count
    if request.method=='GET':
        return render_template('/store/option.html',productimg=productimg,conf=conf)
    else:
        mystery=request.form.get('clicked')
        amount=request.form.get('amount')
        check=amount.isdigit()
        if mystery=='a':
            if check==True:
                amount=int(amount)
                if amount>=1:
                    cartproduct.append(productname)
                    cartimg.append(productimg)
                    cartprice.append(price)
                    cartamount.append(amount)
                    if count==0:
                        hiddenamount.append(count)
                        count=count+1
                    else:
                        hiddenamount.append(count)
                        count=count+1
                    conf='Added to cart.'
                    return redirect(url_for('shopping')) 
                else:
                    error='Please enter a valid amount.'
                    return render_template('/store/option.html',productimg=productimg,error=error)
            else:
                error='Please enter a valid amount.'
                return render_template('/store/option.html',productimg=productimg,error=error)
        else:
            conf=''
            return redirect(url_for('shopping'))

@app.route('/cart',methods=['GET','POST'])
def cart():
    if request.method=='GET':
        global data,total,cartimglen
        data=[]
        total=0
        cartimglen=len(cartimg)
        for i in range(0,cartimglen):
            total=total+(cartprice[i]*cartamount[i])
            data.append(
                (f'<img src="/static/store/{cartimg[i]}.jpg">',
                 cartproduct[i],
                 f'QTY: {cartamount[i]}',
                 f'${cartprice[i]}0')
            )
        return render_template('/store/cart.html',data=data,headings=headings,total=total,hiddenamount=hiddenamount,cartimglen=cartimglen)
    else:
        zanumber=request.form.get('remove')
        check=zanumber.isdigit()
        print(check)
        if check==True:
            zanumber=int(zanumber)
            cartimg.pop(zanumber)
            cartproduct.pop(zanumber)
            cartamount.pop(zanumber)
            cartprice.pop(zanumber)
            return redirect(url_for('cart'))
        else:
            return redirect(url_for('receipt'))

@app.route('/receipt',methods=['GET','POST'])
def receipt():
    global total
    if request.method=='GET':
        print('a')
        data2=[]
        for i in range(0,cartimglen):
            data2.append(
                (cartproduct[i],
                 f'QTY:{cartamount[i]}',
                 f'${cartprice[i]}0')
            )
        filename=regusername+'.txt'
        ifexists=bool(path.exists(filename))
        tax=round(total*.08875,2)
        total = total+tax
        if ifexists==False:
            pythfile=open(filename,'w')
            print(regusername+'s file created successfully!')
            for i in range(0,cartimglen):
                pythfile.write(f'{cartproduct[i]} QTY:{cartamount[i]} ${cartprice[i]}0\n')
            pythfile.write(f'Tax:{tax}\n')
            pythfile.write(f'Total:{total}\n')
            pythfile.close()
        else:
            pythfile=open(filename,"a")
            for i in range(0,cartimglen):
                pythfile.write(f'{cartproduct[i]} QTY:{cartamount[i]} ${cartprice[i]}0\n')
            pythfile.write(f'Tax:{tax}\n')
            pythfile.write(f'Total:{total}\n')
            pythfile.close()
        pythfile=open(filename,'r+')
        print(pythfile.read())
        pythfile.close()
        return render_template('/store/storereceipt.html')

if __name__=='__main__':
    app.run()



