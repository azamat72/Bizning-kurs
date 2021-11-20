from django.urls.conf import path
from . views import *
app_name = "leads"

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('leads/<int:pk>/', leads_detail),
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete),
    path('create/', create, name="create"),
 
]