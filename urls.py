"""tableHubProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tableApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('customerreg', views.custReg),
    path('hotelreg', views.restReg),
    path('login', views.login),

    path('adminhome', views.adminhome),
    path('adminhotel', views.adminhotel),
    path('updateuser', views.updateuser),
    path('admincustomer', views.admincustomer),
    path('adminFeedback', views.adminFeedback),
    path('adminReport', views.adminReport),
    path('adminViewBookingItems', views.adminViewBookingItems),
    path('adminaddcoupons', views.adminaddcoupons),
    path('adminviewcoupons', views.adminviewcoupons),
    path('adminUpdateCoupon', views.adminUpdateCoupon),
    path('adminaddquizz', views.adminaddquizz),
    path('adminviewquizz', views.adminviewquizz),
    path('adminDeleteQuiz', views.adminDeleteQuiz),


    path('resthome', views.resthome),
    path('hotelmenu', views.hotelmenu),
    path('hotelviewmenu', views.hotelviewmenu),
    path('hotelupdatemenu', views.hotelupdatemenu),
    path('hoteldeletemenu', views.hoteldeletemenu),
    path('hotelslot', views.hotelslot),
    path('hotelviewtables', views.hotelviewtables),
    path('hoteldeletetable', views.hoteldeletetable),
    path('hotelorder', views.hotelorder),
    path('hotelorderdetails', views.hotelorderdetails),
    path('hotelprofile', views.hotelprofile),
    path('hotelChats', views.hotelChats),
    path('hotelChat', views.hotelChat),
    path('hotelslotpark', views.hotelslotpark),
    path('hotelviewParking', views.hotelviewParking),
    path('hoteldeleteParking', views.hoteldeleteParking),


    path('custhome', views.custhome),
    path('customersearch', views.customersearch),
    path('customerviewdish', views.customerviewdish),
    path('customer_vw_sugg_dishes', views.customer_vw_sugg_dishes),
    path('customerviewdetails', views.customerviewdetails),
    path('customercart', views.customercart),
    path('customertableslot', views.customertableslot),
    path('payment', views.payment),
    path('payment2', views.payment2),
    path('customerorder', views.customerorder),
    path('customerorderdetails', views.customerorderdetails),
    path('customeraddreview', views.customeraddreview),
    path('customerCancelorder', views.customerCancelorder),
    path('custRemoveFroCart', views.custRemoveFroCart),
    path('custQuiz', views.custQuiz),
    path('customerprofile', views.customerprofile),
    path('custPurPre', views.custPurPre),
    path('custChat', views.custChat),
    path('custChats', views.custChats),
    path('customerviewparking', views.customerviewparking),
]
