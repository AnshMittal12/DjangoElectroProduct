from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from . import pool
import os


def ProductForm(request):
    return render(request, "ProductInterface.html")


def FetchAllProductType(request):
    DB, SMT = pool.OpenConnection()
    SMT.execute("Select * from productname")
    records = SMT.fetchall()
    print(records)
    return JsonResponse(records, safe=False)


def FetchAllCompanyType(request):
    print(request.GET['productid'])
    DB, SMT = pool.OpenConnection()
    SMT.execute(
        "select * from company where productid={0}".format(request.GET['productid']))
    records = SMT.fetchall()
    print(records)
    return JsonResponse(records, safe=False)


def FetchAllModelType(request):
    print(request.GET['companyid'])
    DB, SMT = pool.OpenConnection()
    SMT.execute("Select * from model where companyid={0}".format(request.GET['companyid']))
    records = SMT.fetchall()
    print(records)
    return JsonResponse(records,safe=False)
def ProductSubmit(request):
    try:
        if request.method == 'POST':
            DB, SMT = pool.OpenConnection()
            productid=request.POST['productid']
            companyid=request.POST['companyid']
            productname=request.POST['modelid']
            date=request.POST['mfg']
            price=request.POST['price']
            offer=request.POST['offer']
            pic=request.FILES['pic']
            q='insert into list(productid,companyid,modelid,mfg,price,offer,picture) values({0},{1},{2},"{3}",{4},{5},"{6}")'.format(productid,companyid,productname,date,price,offer,pic)
            print("query----------------",q)
            SMT.execute(q)
            D=open("d:/DJANGO Practice/Product/assets/"+pic.name,"wb")
            for chunk in pic.chunks():
                D.write(chunk)
            D.close()
            DB.commit()
            return render(request,'ProductInterface.html',{'status':True, "message":"Record Submitted"})
    except Exception as e:
        print(e)
        return render (request,"ProductInterface.html",{'status':False,"message":"Server Error"})
       
def DisplayAllProduct(request):
    try:
        DB,SMT = pool.OpenConnection()
        q="select L.*,(select PN.producttype from productname PN where PN.productid=L.productid) as ProductType ,(select C.companyname from company C where C.companyid=L.companyid) as CompanyName ,(select M.modelname from model M where M.modelid=L.modelid) as ProductName from list L"
        SMT.execute(q)
        records=SMT.fetchall()
        return render(request,"DisplayAllProduct.html",{'data':records})
    except Exception as e:
        print(e)
        return render(request,"DisplayAllProduct.html",{'data':[]})
    
def DisplayById(request):
    try:
        listid=request.GET['listid']
        DB,SMT = pool.OpenConnection()
        q="select L.*,(select PN.producttype from productname PN where PN.productid=L.productid) as ProductType ,(select C.companyname from company C where C.companyid=L.companyid) as CompanyName ,(select M.modelname from model M where M.modelid=L.modelid) as ProductName from list L where listid={0}".format(listid)
        SMT.execute(q)
        records=SMT.fetchone()
        print(q,records)
        if(records):
            print("xxxxxxxxxxxxxxxxx",records)
            return render(request,"DisplayById.html",{'data':records})
        else:
         return render(request,"DisplayById.html",{'data':[]})
    except Exception as e:
        print(e)
        return render(request,"DisplayById.html",{'data':[]})
    
def Edit_Product_Data(request):
    try:
        if request.method == 'POST':
            DB,SMT = pool.OpenConnection()
            if(request.POST['btn']=='Edit'):
                listid=request.POST['listid']
                productid=request.POST['productid']
                companyid=request.POST['companyid']
                productname=request.POST['modelid']
                date=request.POST['mfg']
                price=request.POST['price']
                offer=request.POST['offer']
                q='update list set productid={0},companyid={1},modelid={2},mfg={3},price={4},offer={5} where listid={6}'.format(productid,companyid,productname,date,price,offer,listid)
                print("query----------------",q)
                SMT.execute(q)
                DB.commit()
            else:
                listid=request.POST['listid']
                q="delete from list where listid={0}".format(listid)
                SMT.execute(q)
                DB.commit()
            return redirect('/fetchallrecord')
    except Exception as e:
        print(e)
        return redirect('/fetchallrecord')

def DisplayPicture(request):
    print("REQ" ,dict(request.GET))
    return render(request,"DisplayPicture.html",{'data':dict(request.GET)})

def Edit_Picture(request):
    try:
        if request.method == 'POST':
            DB,SMT = pool.OpenConnection()
            listid=request.POST['listid']
            pic=request.FILES['picture']
            oldfile=request.POST['oldfile']
            q="update list set picture='{0}' where listid={1}".format(pic.name,listid)
            print("query----------------",q)
            SMT.execute(q)
            D=open("d:/DJANGO Practice/Product/assets/"+pic.name,"wb")
            for chunk in pic.chunks():
                D.write(chunk)
            D.close()
            try:
                os.remove('d:/DJANGO Practice/Product/assets/{0}'.format(oldfile))
            except Exception as e:
                print(e)
            DB.commit()
        return redirect('/fetchallrecord')
    except Exception as e:
        print(e)
        return redirect('/fetchallrecord')