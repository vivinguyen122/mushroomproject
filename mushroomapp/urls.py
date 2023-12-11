from django.conf.urls.static import static
from django.urls import path, include
from mushroomapp import views
from mushroomproject import settings

urlpatterns = [

    # my po2 test
    path('api/forums/', views.ForumApiView.as_view(), name='forum-api-view'),  # show api page w all forums
    path('api/posts/', views.PostApiView.as_view(), name='posts-api-view'),  # show api page w all posts

    path('api/posts/<int:post_id>/', views.PostDetailView.as_view(), name='posts-detail-api-view'),  # show api page w post details
    path('api/forums/<int:forum_id>/', views.ForumDetailView.as_view(), name='posts-detail-api-view'),  # show api page w forum details

    path('api/search/', views.SearchView.as_view(), name='search-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)