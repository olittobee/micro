from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('content/<int:topic_id>',views.content,name='content'),  
    path('edit/',views.edit,name='edit'),
    path('profile/',views.profile,name='profile'),
   # path('log/',views.log,name='log'),
    path('signup/',views.signup,name='signup'),
    path('email/',views.edit,name= 'email') 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)