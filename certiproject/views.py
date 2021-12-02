from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.core.paginator import Paginator
from django.views import View
from django.views import generic
import openpyxl
import pymysql
import pandas as pd
from sqlalchemy import create_engine


#def bbs_list(request):
#    return render(request,'./bbs_list.html')

def signin(request):
    # return render(request, '/bbs_list.html')
    if request.method =='POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username = username, password = password)
        if user is not None:
            return render(request, 'bbs_list.html')
            #return render(request, './bbs_list.html')

        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, './login.html')


def bbs_register(request):


# int s_group = 0
    if request.method == 'GET':
        return render(request, './bbs_register.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["1반"]
        print(worksheet)

        table = pd.read_excel(excel_file, sheet_name='1반', header=0)
        engine = create_engine("mysql+pymysql://root:eunju2885!@localhost:3306/StudentIDCard", encoding='utf-8-sig')
        table.to_sql(name='student', con=engine, if_exists='append', index=False)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        return render(request, './bbs_register.html', {"excel_data": excel_data})


def preview(request):

    return render(request, './preview.html')

def register_ondirect(request):

    return render(request, './register_ondirect.html')

