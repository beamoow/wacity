from django.shortcuts import render, redirect, get_object_or_404
from store.models import Profile, Product, Category , Purchase
from store.forms import ProfileForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

import json 

data =[]



def all_products(request):
    
    category = request.GET.get('category')

    if category == None:
        products = Product.products.all()           
    else:
        products = Product.objects.filter(category__name=category)
       
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'store/home.html', context)


def add_to_cart(request):
    global data
    pk = request.POST.get("pk", "")
    title = request.POST.get("title", "")
    myitem={
        "pk": pk,
        "title": title,
        "quantity": 1
        }
    data += [myitem,]
    dictionary = {"data": data}
    json_object = json.dumps(dictionary, indent = 4)
    print(json_object)
    response = render(request, 'store/products/mycart.html')
    response.set_cookie('mycart', json_object)
    return response



# def add_to_cart(request):
#     global data
#     pk = request.POST.get("pk", "")
#     title = request.POST.get("title", "")
#     quantity = 1
#     myitem={
#         "pk": pk,
#         "title": title,
#         "quantity": quantity
#         }
#     data += [myitem,]
#     dictionary = {"data": data}
#     json_object = json.dumps(dictionary, indent = 4)
#     print(json_object)
#     response = redirect("http://127.0.0.1:8000/")
#     response.set_cookie('mycart', json_object)
#     Purchase(myitem).save()
#     return response


# def add_to_cart(request):
#     user = request.user
#     product_id = request.GET.get('prod_id')
#     product = get_object_or_404(Product, id=product_id)

#     # Check whether the Product is alread in Cart or Not
#     item_already_in_cart = Cart.objects.filter(product=product_id, user=user)
#     if item_already_in_cart:
#         cp = get_object_or_404(Cart, product=product_id, user=user)
#         cp.quantity += 1
#         cp.save()
#     else:
#         Cart(user=user, product=product).save()
    
#     return redirect('store:mycart')




def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/detail.html', {'product': product})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("http://127.0.0.1:8000/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="store/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="store/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("http://127.0.0.1:8000/")


def profile(request): 
    instance = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/')
    else:
        context = {
            'form':form,
            'user':request.user
            }
        return render(request, 'store/profile.html', context) 




