from django.urls import path
from .views import contact,about,signup_cust,signup_vendor,login,login_vendor,logout,productview,proall,proall_vendor,search,productadd,productdel,productupdate,profilemanager_vendor,profilemanager,abc


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('index/',hello)
    path('',login, name="login"), #go to this page without writing /app1/index in url
    path('contact/',contact, name="contact"),
    path('about/',about, name="about"),
    path('signup/',signup_cust, name="signup"),
    path('signup_vendor/',signup_vendor, name="signup_vendor"),
    path('login/',login, name="login"),
    path('login_vendor/',login_vendor, name="login_vendor"),
    path('logout/',logout, name="logout"),
    path('view/<int:pid>/',productview, name="productview"), #allow any int in url and store it in pid
    path('del/<int:pid>/',productdel, name="productdel"), #allow any int in url and store it in pid
    path('update/<int:pid>/',productupdate, name="productupdate"), #allow any int in url and store it in pid
    path('allproducts/',proall, name="proall"),
    path('allproductsvendor/',proall_vendor, name="proall_vendor"),
    path('search/',search, name="search"),
    path('productadd/',productadd, name="productadd"),
    path('profilemanager_vendor/',profilemanager_vendor, name="profilemanager_vendor"),
    path('profilemanager/',profilemanager, name="profilemanager"),
    path('abc/',abc, name="abc"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
