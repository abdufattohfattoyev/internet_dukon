from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Cart
from .forms import UserRegisterForm, LoginForm,CartForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages



#Mahsulotni savatga qo'shish

def addtocart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["product_qty"]
            if qty > 0 and qty <= product.quantity:
                try:
                    cart_item, created = Cart.objects.get_or_create(
                        user=request.user,
                        product=product,
                        defaults={'quantity': qty}
                    )
                    if not created:
                        cart_item.quantity += qty
                        cart_item.save()
                    else:
                        product.quantity -= qty
                        product.save()
                    messages.success(request, f"{qty} dona {product.title} savatga qo‘shildi")
                    return redirect("view_cart")
                except Exception as e:
                    messages.error(request, "Savatga qo‘shishda xatolik yuz berdi")
                    return redirect("view_cart")
            else:
                messages.warning(request, "Noto‘g‘ri miqdor yoki omborda yetarli mahsulot yo‘q")
                return redirect("view_cart")
    else:
        form = CartForm()
    context = {
        "form": form,
        "product": product
    }
    return render(request, "addtocart.html", context)


def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    total_cart_price = sum(item.total_price or 0 for item in cart_items)
    for item in cart_items:
        item.total_price = item.quantity * item.product.selling_price
    context = {
        "cart_items": cart_items,
        "total_cart_price": total_cart_price,
    }
    return render(request, "viewcart.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, "Siz tizimdan chiqdingiz")
        return render(request, "registration/logout.html")
    else:
        # Agar foydalanuvchi autentifikatsiya qilinmagan bo'lsa
        messages.info(request, "Siz tizimga kirmagansiz!")
        return redirect('login')


def signupview(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(form.cleaned_data["password1"])
            user.save()
            messages.success(request,"Muvaffaqiyatli ro'yxatdan o'tdingiz")
            return redirect("login")
    else:
        form=UserRegisterForm()

    context={
        "form":form
    }
    return render(request,"registration/signup.html",context)


# def login_view(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, "Muvaffaqiyatli tizimga kirdingiz")
#             return redirect("home")
#     else:
#         form = UserLoginForm()
#
#     context = {"form": form}
#     return render(request, "registration/login.html", context)



def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,"Siz Login Qilgansiz")
        return redirect("home")

    else:
        if request.method=="POST":
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(request,username=username,password=password)

                if user is not None:
                    login(request,user)
                    messages.success(request,"Siz saytga muvaffaqiyatli kirdizngiz")
                    return redirect("home")
                else:
                    form.add_error(None,"Username yoki parol xato")

        else:
            form=LoginForm()

    context={
        "form":form
    }

    return render(request, "registration/login.html", context)
