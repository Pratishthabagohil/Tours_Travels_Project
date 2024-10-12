# In trvels/urls.py
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact_view, name='contact'),
    path('location/<int:id>/', views.location, name='location'), # New path for the Discover page
    path('inquiry/', views.inquiry_form, name='inquiry_form'),
    path('submit_inquiry/', views.submit_inquiry, name='submit_inquiry'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

