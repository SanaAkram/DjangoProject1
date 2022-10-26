from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
<<<<<<< HEAD
    path('users/', include('users.urls')),
=======
>>>>>>> 525424ab5fce6ff436d8d7092917833e4f22a6ef
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
