from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def data_index_view(request):
    '''This function render index page of Data_sci views'''
    return HttpResponse('Welcome to Leftover Group views!')

def data_sci_item_list_all(request):
    dataset_objs = Product_id.objects.all()
    context_data = {
        "filter_type":"All" ,
        "datasets":dataset_objs
    }
    return render(request, 'data_sci/list_view.html', context= context_data)

def data_sci_item_list_by_id (request, id):
    dataset_objs = Product_id.objects.filter(id = id)
    if len(dataset_objs) <= 0:
        return HttpResponse("ID Not found" )
    context_data = {
        "filter_type":str(id),
        "datasets":dataset_objs
    }
    return render(request, 'data_sci/list_view.html' , context= context_data)

def data_sci_item_add (request):
    if request.method == "POST":
        form_data = request.POST
        new_item = Product_id(
            Product_id_value = form_data[ 'Product_id_value' ],
            Product_type_name = form_data[ 'Product_type_name' ],
            Fat_content_value = form_data[ 'Fat_content_value' ],
            Product_visibility_value = 0,
            Weight_product_value = 0,

        )
        try:
            new_item. save()
        except:
            return HttpResponse ("ERROR!" )
        return redirect ('/data_sci/list_item/all' )
    context_data = {
        'item_id' : "New",
        'form_data' :{
            'Product_id_value' :"",
            'Product_type_name' :"",
            'Fat_content_value' :"",
            'Product_visibility_value' :0,
            'Weight_product_value' :0,
            }
    }
    return render(request, 'data_sci/form.html' , context= context_data)

def data_sci_item_edit(request, id):
    try:
        item = Product_id.objects.get(id = id)
    except:
        return HttpResponse("ID Not found")
    if request.method == "POST":
        form_data = request.POST
        item.Product_type_name = form_data['Product_type_name']
        item.Fat_content_value = form_data['Fat_content_value']
        item.Product_id_value = form_data['Product_id_value']
        item.Product_visibility_value = form_data['Product_visibility_value']
        item.Weight_product_value = form_data['Weight_product_value']
        try:
            item.save()
        except:
            return HttpResponse("ERROR!")
        return redirect('/data_sci/list_item/all')
    context_data = {
        'item_id': id,
        'form_data':{
            'Product_type_name':item.Product_type_name,
            'Fat_content_value':item.Fat_content_value,
            'Product_id_value':item.Product_id_value,
            'Product_visibility_value':item.Product_visibility_value,
            'Weight_product_value':item.Weight_product_value,
}
    }
    return render(request, 'data_sci/form.html', context= context_data)

def data_sci_item_delete(request, id):
    dataset_objs = Product_id.objects.filter(id = id)
    if len(dataset_objs) <= 0:
        return HttpResponse("ID Not found")
    dataset_objs.delete()
    return redirect('/data_sci/list_item/all')

from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd
from data_sci.models import Product_id

def import_data_csv(request):
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR6BatXNFAsz8DzPXdf8cEMr9E55c7P40I3wPOaUDFE1BCDv5dvjEF4arc2ql6LKGG3bLYjZu-7FRmP/pub?output=csv"
    df = pd.read_csv(csv_url)
    data_sets = df[["ProductID", "Weight", "FatContent","ProductVisibility", "ProductType" ]]
    success = []
    errors = []
    for index, row in data_sets.iterrows():
        instance = Product_id(
            Product_id_value = row['ProductID'],
            Weight_product_value = float(row['Weight']),
            Fat_content_value = row['FatContent'],
            Product_visibility_value = float(row['ProductVisibility']),
            Product_type_name = row['ProductType']
        )
        try: 
            instance.save()
            success.append(index)
        except:
            errors.append(index)
    return JsonResponse({"success_index":success, "error_indexs":errors})

import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def example_linear_regression(request):
    total_Weight_product_value = list(Product_id.objects.all().order_by('id').values_list('Weight_product_value', flat=True))
    total_Product_visibility_value = list(Product_id.objects.all().order_by('id').values_list('Product_visibility_value', flat=True))
    x = np.array(total_Weight_product_value).reshape(-1, 1)
    y = np.array(total_Product_visibility_value).reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    
    regr = LinearRegression()
    regr.fit(x_train, y_train)
    
    y_pred = regr.predict(x)
    json_output = {
        'total_Weight_product_value': total_Weight_product_value,
        'total_Product_visibility_value': total_Product_visibility_value,
        'predict_applicants': list(y_pred.flat)
    }
    return JsonResponse(json_output)

def d3_visualization(request):
    context = {}
    return render(request, "data_sci/D3.html", context = context)



