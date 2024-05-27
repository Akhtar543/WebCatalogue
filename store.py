from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

cartproduct=[]
cartimg=[]
cartprice=[]
cartamount=[]
headings=['Items','Product','Quantity','Price']
hiddenamount=[]
count=0
conf=''
@app.route('/',methods=['GET','POST'])
def main():
    global productimg,productname,price
    if request.method=='GET':
        total=0
        return render_template('/store/shopping.html',conf=conf)
    else:
        productimg=request.form.get('pick')
        match productimg:
            case 'a':
                productname='prod1' #all soon to change(match product name, price, and add more ofc)
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
                    return redirect(url_for('main')) 
                else:
                    error='Please enter a valid amount.'
                    return render_template('aaaa.html',productimg=productimg,error=error)
            else:
                error='Please enter a valid amount.'
                return render_template('aaaa.html',productimg=productimg,error=error)
        else:
            conf=''
            return redirect(url_for('main'))

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
    if request.method=='GET':
        print('a')
        data2=[]
        for i in range(0,cartimglen):
            data2.append(
                (cartproduct[i],
                 f'QTY:{cartamount[i]}',
                 f'${cartprice[i]}0')
            )
        filename=...+'.txt'
        ifexists=bool(path.exists(filename))
        if ifexists==False:
            pythfile=open(filename,'w')
            print(...'s file created successfully!')
            for i in range(0,cartimglen):
                pythfile.write(cartproduct[i],cartamount[i],cartprice[i])
            pythfile.close()
        else:
            pythfile=open(filename,"a")
            for i in range(0,cartimglen):
                pythfile.write(cartproduct[i],cartamount[i],cartprice[i])
            pythfile.close()
        pythfile=open(filename,'r')
        print(pythfile.readline())
        pythfile.close()
        return render_template('/store/storereceipt.html',data=data,headings=headings,total=total)

if __name__=='__main__':
    app.run()
