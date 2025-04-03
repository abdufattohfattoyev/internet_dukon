from django.urls import path
from .views import home_page,categories_view,categories_add,addproduct_view,update_category,SearchProductView,detail_page,category_products,category_detail_page,update_product


urlpatterns=[
    path("",home_page,name="home"),
    path("categories/",categories_view,name="categories"),
    path("search/",SearchProductView.as_view(),name="search_product"),
    path("categories_add/",categories_add,name="categories_add"),
    path("add_product/",addproduct_view,name="add_product"),
    path('update_category/<int:category_id>/', update_category, name='update_category'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('category_products/<int:category_id>/', category_products, name='category_products'),
    path('detail/<int:id>/', detail_page, name='detail_product'),
    path('category_detail_page/<int:id>/', category_detail_page, name='category_detail_page'),
]