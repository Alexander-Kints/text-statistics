from django.urls import path

import text_statistics.tf_idf.views as views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path(
        'statistics/<int:file_id>/',
        views.StatisticsView.as_view(),
        name='statistics'
    ),
]
