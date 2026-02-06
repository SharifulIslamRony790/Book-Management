from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('', RedirectView.as_view(url='book/list/', permanent=False)),  # Redirect root to book list
]
