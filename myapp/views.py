from django.shortcuts import render , redirect
from .models import Consume, food
# Create your views here.
def index(request):
    # Add function
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        # Querying database for food which has the name equal to the food which we got from Add.
        consume = food.objects.get(name=food_consumed)
        #Add the food item to consumption list of current user.
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = food.objects.all()

    else:  
        # Get all objects in food model
        foods = food.objects.all()
    # Querying database for food items consumed by the current user(filtered by current user).
    consumed_food = Consume.objects.filter(user=request.user) 
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')