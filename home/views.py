# Import necessary libraries
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Expense, Un_Expense


@login_required(login_url='/login/')
def un_expenses(request):
    salary = 0
    if request.method == 'POST':
        data = request.POST
        salary = int(data.get('salary', 0))
        name = data.get('name')
        price = int(data.get('price', 0))

        Un_Expense.objects.create(
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('/un_expenses')

    queryset = Un_Expense.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))

    total_sum = sum(un_expenses.price for un_expenses in queryset)

    context = {'un_expenses': queryset, 'total_sum': total_sum}
    return render(request, 'un_expenses.html', context)
@login_required(login_url='/login/')
def expenses(request):
    salary = 0
    if request.method == 'POST':
        data = request.POST
        salary = int(data.get('salary', 0))
        name = data.get('name')
        price = int(data.get('price', 0))

        Expense.objects.create(
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('/')

    queryset = Expense.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))

    # Calculate the total sum
    total_sum = sum(expense.price for expense in queryset)

    context = {'expenses': queryset, 'total_sum': total_sum}
    return render(request, 'expenses.html', context)



@login_required(login_url='/login/')
def update_un_expense(request, id):
    queryset = Un_Expense.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = int(data.get('price', 0))

        queryset.name = name
        queryset.price = price
        queryset.save()
        return redirect('/un_expenses')

    context = {'un_expense': queryset}
    return render(request, 'update_un_expense.html', context)


@login_required(login_url='/login/')
def update_expense(request, id):
    queryset = Expense.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = int(data.get('price', 0))

        queryset.name = name
        queryset.price = price
        queryset.save()
        return redirect('/')

    context = {'expense': queryset}
    return render(request, 'update_expense.html', context)



@login_required(login_url='/login/')
def delete_un_expense(request, id):
    queryset = Un_Expense.objects.get(id=id)
    queryset.delete()
    return redirect('/un_expenses')

@login_required(login_url='/login/')
def delete_expense(request, id):
    queryset = Expense.objects.get(id=id)
    queryset.delete()
    return redirect('/')



def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if not user_obj:
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('expenses')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "login.html")


# Register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")


# Logout function
def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def un_pdf(request):
    if request.method == 'POST':
        data = request.POST
        salary = int(data.get('salary'))
        name = data.get('name')
        price = int(data.get('price', 0))

        Un_Expense.objects.create(
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('pdf')

    queryset = Un_Expense.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))

    total_sum = sum(un_expenses.price for un_expenses in queryset)
    username = request.user.username

    context = {'un_expenses': queryset, 'total_sum': total_sum, 'username': username}
    return render(request, 'un_pdf.html', context)

@login_required(login_url='/login/')
def pdf(request):
    if request.method == 'POST':
        data = request.POST
        salary = int(data.get('salary'))
        name = data.get('name')
        price = int(data.get('price', 0))

        Expense.objects.create(
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('pdf')

    queryset = Expense.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))

    # Calculate the total sum
    total_sum = sum(expense.price for expense in queryset)
    # Get the username
    username = request.user.username

    context = {'expenses': queryset, 'total_sum': total_sum, 'username': username}
    return render(request, 'pdf.html', context)
