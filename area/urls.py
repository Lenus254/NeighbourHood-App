
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('new-hood/', views.new_area, name='new-hood'),
    path('view-hood/<hood_id>', views.view_area, name='view-area'),
    path('view-hood/<hood_id>/new-business', views.add_business, name='new-business'),
    path('join_hood/<id>', views.join_area, name='join-area'),
    path('leave_hood/<id>', views.exit_area, name='exit-area'),
    path('search/', views.search_business, name='search'),
    path('<hood_id>/members', views.hood_members, name= 'hood_members'),
    path('<hood_id>/add-post', views.new_post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)