from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
\
    path("new/", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("view-question/<int:pk>",views.card_question_view,name="card-question"),
    path("box/<int:box_num>",views.BoxView.as_view(),name='box'),
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
    path('delete/<int:pk>', views.CardDeleteView.as_view(), name='card-delete'),
    path("", views.CardListView.as_view()),

]
