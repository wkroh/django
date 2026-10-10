from django.shortcuts import render

def index(request):
    return render(
request,
'pages/index.html',
{
"name" : "ali ahmed aliii",
"age": 2**240,


}

)
def  about(request):
    pass

# Create your views here.
