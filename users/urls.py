from django.urls import path

from users.views import signupview, login_view, logout_view,addtocart,view_cart

# from .views import SignUpView, UserVerificationAPIView, UserCodeAgainGenerate, \
#     LoginAPIView,BlacklistRefreshView

urlpatterns=[

    path("signup/",signupview,name="register"),
    path("login/",login_view,name="login"),
    path('logout/',logout_view, name='logout'),
    path('add-to-cart/<int:product_id>/', addtocart, name='add_cart'),
    path('view-cart/', view_cart, name='view_cart'),

]

