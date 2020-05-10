from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import NewRider, myForm
from django.urls import reverse

# Import my models
from .models import Rider

# Create your views here.
def myView(request):
    userName = 'Miguel Ángel Simon Martínez'
    userNameShort = 'M A Simón'
    roleAsMember = '(i)responsable de web local y coordinador de bar'
    description = 'Soy investigador predoctoral en el grupo QUINST de la UPV, donde investigamos como domar el mundo cuántico para nuestro beneficio.'
    img = 'myApp/images/miguel.jpg'
    context = {
        'title': 'User: '+userNameShort,
        'description': description,
        'roleAsMember' : roleAsMember,
        'userName' : userName,
        'img' : img
    }
    return render(
        request,
        'myApp/mytemplate.html',
        context=context
    )

# View for a home page
def myHomeView(request,riderName=''):
    return render(
        request,
        'myApp/home.html',
        {
            'viewName':'riderRegistration',
            'riderName':riderName
        }
    )

# Create a view for registering riders
def riderSignIn(request):
    if request.method == 'POST':
        form = NewRider(request.POST)
        if form.is_valid():
            form.save()
            return myHomeView(request,riderName=request.POST['riderName'])
            # return HttpResponseRedirect(reverse(myHomeView,args = [request.POST['riderName']]))
    else:
        form = NewRider()
    return render(
        request,
        'myApp/registration.html',
        dict(
            form = form,
        )
    )

# Create a view for the riders_list page
def ridersView(request):
    # get the list of riders
    riders_list = Rider.objects.order_by('riderName')
    context = {
        'page_title':'Riders',
        'riders_list':riders_list
    }
    return render(
        request,
        'myApp/ridersViewTemplate.html',
        context = context
    )

# API view
def riderAPI(request):
    names = request.GET.getlist('names');
    # return_str = """
    # <head>
    #     <style>
    #         body {text-align:center}
    #     </style>
    # </head>
    # """.lstrip()
    # return_str += '<body>'
    # return_str += ''.join(
    #     ['<p>{}</p>'.format(name) for name in names]
    # )
    # return_str += '</body>'
    # return HttpResponse(
    #     return_str
    # )

    return JsonResponse(names,safe=False)
