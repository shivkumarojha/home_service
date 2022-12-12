from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'services'


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('plans/', views.plans, name='plans'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('send_message/', views.send_message, name='send_message'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)