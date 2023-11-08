from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def d3_visualization(request):
    context = {}
    return render(request, "data_sci/D3.html", context = context)
