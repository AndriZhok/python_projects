from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Додати уставні URL для автентифікації
    path('', include('django.contrib.auth.urls')),
]