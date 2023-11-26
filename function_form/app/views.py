from django.shortcuts import render
from app.forms import NameForm, BirthForm, BurgerForm,FontForm,TeenForm,xyzForm,averageForm
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.

#OPENING PAGE
def Open_Page(request:HttpRequest) -> render:
    return render(request, "index.html")




#CODINGBAT OVER FORMS
def Codingbat_Hub(request: HttpRequest) -> render:
    return render(request, "CodingbatHub.html")

def font_times(request:HttpRequest) -> render:
    form = FontForm(request.GET)
    if form.is_valid():
        str_1 = form.cleaned_data["str_1"]
        num_1 = form.cleaned_data["num_1"]
        front_len = 3
        if front_len > len(str_1):
            front_len = len(str_1)
        front = str_1[:front_len]
        
        result = ""
        for i in range(num_1):
            result = result + front
        return render(request, "font-times.html",{"form":form, "result":result})
    else:
        return render(request, "font-times.html")
    
def teen(request:HttpRequest) -> render:
    form = TeenForm(request.GET)
    if form.is_valid():
        int_value1 = form.cleaned_data["int_value1"]
        int_value2 = form.cleaned_data["int_value2"]
        int_value3 = form.cleaned_data["int_value3"]

        def not_teen(n):
            return n if n not in [13,14,17,18,19] else 0

        total = not_teen(int_value1)+not_teen(int_value2)+not_teen(int_value3)
        return render(request, "no-teen-sum.html", {"form":form, "total":total})
    else:
        return render(request, "no-teen-sum.html")
    


def xyz(request:HttpRequest) -> render:
    form = xyzForm(request.GET)
    if form.is_valid():
        xyz_string = form.cleaned_data["xyz_string"]
        if "xyz" in xyz_string and ".xyz" not in xyz_string:
            answer = True
        else:
            answer = False
        return render(request, "xyz.html", {"form":form, "answer":answer})
    else:
        return render(request, "xyz.html")

def centered_average(request:HttpRequest) -> render:
    form = averageForm(request.GET)
    if form.is_valid():
        val_1 = form.cleaned_data["val_1"]
        val_2 = form.cleaned_data["val_2"]
        val_3 = form.cleaned_data["val_3"]
        val_4 = form.cleaned_data["val_4"]
        val_5 = form.cleaned_data["val_5"]
        val_6 = form.cleaned_data["val_6"]
        val_7 = form.cleaned_data["val_7"]
        val_8 = form.cleaned_data["val_8"]
        val_9 = form.cleaned_data["val_9"]
        val_10 = form.cleaned_data["val_10"]

        nums = [val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,val_9,val_10]

        nums.sort()
        count = 0
        total = 0
        for i in range(1, len(nums) - 1):
            count += 1
            total += nums[i]
        average= total / count

        return render(request, "centered-average.html", {"average":average,"form":form})
    else:
        return render(request, "centered-average.html")



#FUNCTIONS OVER FORMS
def hub_page(request: HttpRequest) -> render:
    print(request.GET)
    return render(request, "FunctionHub.html")

def Hey_You(request: HttpRequest):
    form = NameForm(request.GET)
    if form.is_valid():
        input_name = form.cleaned_data["input_name"]
        return render(request, "Hey.html", {"form":form, "input_name": input_name})
    else:
        return render(request, "Hey.html", {"form":form})


def Age_in_2050(request: HttpRequest):
    form = BirthForm(request.GET)
    if form.is_valid():
        birthyear = form.cleaned_data["birthyear"]
        ageyear = form.cleaned_data["ageyear"]
        answer = ageyear - birthyear
        return render(
            request,
            "Age.html",
            {"birthyear": birthyear, "ageyear": ageyear, "answer": answer},
        )
    else:
        return render(request, "Age.html")


def Order(request: HttpRequest):
    form = BurgerForm(request.GET)
    if form.is_valid():
        Burger = form.cleaned_data["Burger"]
        Fries = form.cleaned_data["Fries"]
        Drink = form.cleaned_data["Drink"]
        BurgerT = Burger * 4.5
        FriesT = Fries * 1.5
        DrinkT = Drink * 1
        total = BurgerT + FriesT + DrinkT
        return render(
            request,
            "Order.html",
            {"Burger": Burger, "Fries": Fries, "Drink": Drink, "total": total},
        )
    else:
        return render(request, "Order.html")
