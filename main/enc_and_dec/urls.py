from .  import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.static import static
# from django.conf import settings
# print(settings)
urlpatterns = [
    
    path("", views.main,name="main"),
    path("encryption/",views.encryption,name="encryption"),
    path("decryption/",views.decryption,name="decryption"),
    # path('encryption/files/',views.download_encryption,name="download_encryption"),
    path('playground/',views.playground,name="playground"),
    path('callme/',views.callme,name="callme"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)