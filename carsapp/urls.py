from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# =============================
# URL Patterns
# =============================
urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # تطبيقات المشروع
    path('', include('core.urls')),               # الصفحة الرئيسية
    path('products/', include('catalog.urls')),  # المنتجات والتصنيفات
    path('orders/', include('orders.urls')),     # السلة والطلبات
]


# =============================
# Static & Media (Development)
# =============================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
