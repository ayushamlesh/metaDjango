from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# in the app we will first create a function with home name.


def home(request):
    return(HttpResponse("Hello welcome to the chef's table")
           )


# def methods(request):
#     path = request.path
#     method = request.method
#     content = '''
# <center><h2>Testing Django Request Response Objects</h2>
# <p>Request path : " {}</p>
# <p>Request Method :{}</p></center>
# '''.format(path, method)
#     return HttpResponse(content)
# then create url.py file in the chefsApp

def showform(request):
    return render(request, "form.html")


def getform(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name:{} UserID:{}".format(name, id))
