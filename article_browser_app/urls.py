from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, \
    DeletePostView, AddCategoryView, category_view, category_list_view, \
    AddCommentView, logout_user

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>',
         ArticleDetailView.as_view(),
         name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(),
         name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(),
         name='delete_post'),
    path('category/<str:cats>/', category_view, name='category'),
    path('category-list/', category_list_view, name='category-list'),
    path('logout/', logout_user, name='category-list'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(),
         name='add_comment'),

]
