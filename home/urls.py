from django.urls import path, re_path
from home import views


urlpatterns = [
    # The home page
    path('', views.index.as_view(), name='welcome'),
    path('survey/create/', views.add_surveys, name='add-survey'),
    path('complete', views.Complete.as_view(), name='complete'),
    path('survey', views.SurveyWizardView.as_view(), name='survey')
    # re_path(r'^.+\.+', views.pages, name='pages'),
]
