from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name':'Joy','age':13},
        {'name':'Dip','age':25}
    ]
    
    text="""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus eligendi dolorum error temporibus consequuntur ipsam deleniti repellat assumenda eaque magni amet, quos reprehenderit. Eum accusamus aliquam distinctio nesciunt inventore quam debitis sint fugit nobis officiis pariatur, odit commodi quaerat minus nam eligendi! Labore nesciunt illo doloribus, soluta sapiente quo quod eaque est nemo similique deserunt nihil assumenda. Quas nulla quos atque obcaecati corporis libero maxime eaque repellendus modi iusto voluptates velit, ipsa incidunt a sed error similique quidem ut necessitatibus iste natus fugit odit qui? Eos sed numquam aut molestiae. Itaque nisi sint optio tenetur quo fugiat quasi facere quos!

    """
    
    return render(request,"index.html",context={"page":"homepage","peoples":peoples,"text":text})

def contact(request):
    return render(request,"contact.html",context={"page":"contact"})

def about(request):
    return render(request,"about.html",context={"page":"about"})

def room(request):
    return HttpResponse("Room page")