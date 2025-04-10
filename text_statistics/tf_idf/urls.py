from django.urls import path
import text_statistics.tf_idf.views as views

urlpatterns = [
    path('', views.IndexView.as_view()),
]
