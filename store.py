from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

cartproduct=[]
cartimg=[]
cartprice=[]
cartamount=[]
hiddenamount=[]
conf=''
@app.route('/',methods=['GET','POST'])
def main():
    global productimg,productname,price
    if request.method=='GET':
        total=0
        return render_template('aaa.html',conf=conf)
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
    global conf
    if request.method=='GET':
        return render_template('aaaa.html',productimg=productimg,conf=conf)
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
                    conf='Added to cart.'
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
        data=[]
        total=0
        headings=['Items','Product','Quantity','Price']
        cartimglen=len(cartimg)
        for i in range(cartimglen):
            total=total+(cartprice[i]*cartamount[i])
            data.append(
                (f'<img src="/static/store/{cartimg[i]}.jpg" style="width:200px;height:200px;">',
                 cartproduct[i],
                 f'QTY: {cartamount[i]}',
                 f'${cartprice[i]}0')
            )
            print(hiddenamount)
        return render_template('cart.html',data=data,headings=headings,total=total,cartproduct=cartproduct,cartimglen=cartimglen)
    '''else:
        zanumber=request.form.get('remove')
        cartimg.remove()
        cartproduct.remove()
        cartamount.remove()
        cartprice.remove()
        '''

if __name__=='__main__':
    app.run()
