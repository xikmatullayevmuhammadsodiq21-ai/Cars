# from django.shortcuts import render

# # Create your views here.
# def add(request):
#     return render(request, 'add.html')

# def car_detail(request):
#     return render(request, 'car_detail.html')


# def car_list(request):
#     return render(request, 'car_list.html')


# def delete(request):
#     return render(request, 'delete.html')

# def edit(request):
#     return render(request, 'edit.html')


# def home_page(request):
#     return render(request, 'home.html')



from django.shortcuts import render, redirect, get_object_or_404
# Assuming you have a Car model and a CarForm in forms.py
from .models import Car 
from .forms import CarForm 

def home_page(request):
    return render(request, 'home.html')

def car_list(request):
    cars = Car.objects.all() # Get all cars from the database
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, pk):
   
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES) # request.FILES in case you upload images
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'add.html', {'form': form})

def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        # Pass the existing car instance to the form so it knows what to update
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'edit.html', {'form': form, 'car': car})

def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST': # Require a POST request to actually delete
        car.delete()
        return redirect('car_list')
    return render(request, 'delete.html', {'car': car})