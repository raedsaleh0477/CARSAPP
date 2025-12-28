from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Project Apps
    path('', include('core.urls')),               # الصفحة الرئيسية / المستخدمين
    path('products/', include('catalog.urls')),  # المنتجات والتصنيفات
    path('orders/', include('orders.urls')),     # السلة والطلبات
]
