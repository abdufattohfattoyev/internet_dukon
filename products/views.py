from django.db.models import Q
from django.shortcuts import render, redirect,redirect, get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product,Category
from .forms import AddCategoryForm, AddProductForm
from django.contrib import messages


def home_page(request):
    products = Product.objects.all()
    context={
        "products":products
    }
    return render(request,"home.html",context)

def categories_view(request):
    categories=Category.objects.filter(status=True)
    context = {
        "categories": categories
    }
    return render(request, "categories.html", context)

def categories_add(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            if Category.objects.filter(title__iexact=title).exists():
                messages.error(request, "Bu Categoriya allaqachon mavjud")

            else:
                form.save()
                messages.error(request, "Categoriya muvaffaqiyatli qo'shildi")
            return redirect('home')
    else:
        form = AddCategoryForm
    context = {
        "form": form
    }
    return render(request, "category_add.html", context)

def addproduct_view(request):
    if request.method=="POST":
        form=AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=AddProductForm()
    context={
        "form":form
    }
    return render(request,"product_add.html",context)


def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        form = AddCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = AddCategoryForm(instance=category)

    context = {
        "form": form,
        "category": category
    }
    return render(request, "category_update.html", context)


class SearchProductView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "search_product.html"

    def get_queryset(self):
        query=self.request.GET.get("q")
        if query:
            return Product.objects.filter(
                Q(title__icontains=query)|Q(description__icontains=query)
            )
        else:
            return Product.objects.none()


def detail_page(request,id):
    product=Product.objects.filter(id=id).first()
    # product=get_object_or_404(Product,id=id)
    context={
        "product":product
    }
    return render(request,"product_detail.html",context)

## Buni sharti Urlga ID o'rniga PK berish kk

# class ProductView(DetailView):
#     model = Product


def category_products(request, category_id):
    category = Category.objects.filter(id=category_id, status=True).first()
    products = Product.objects.filter(category=category)

    context = {
        "category": category,
        "products": products
    }
    return render(request, "category_products.html", context)

def category_detail_page(request, id):
    category = get_object_or_404(Category, id=id)
    context = {
        "category": category
    }
    return render(request, "category_detail.html", context)

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot muvaffaqiyatli yangilandi")
            return redirect('detail_product', id=product.id)
    else:
        form = AddProductForm(instance=product)

    context = {
        "form": form,
        "product": product
    }
    return render(request, "product_update.html", context)
