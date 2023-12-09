from django.urls import path
from .views import HomeView, ArticleDetailView

app_name = "core"

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="post-details"),
]	