"""SecurityPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import SectionListView, SectionDetailView
from .admin import securitypolicy_admin_site

urlpatterns = [
    path('', SectionListView.as_view(), name='policy-home'),
    path('section/', SectionDetailView.as_view(), name='section-detail'),
    path('section/<int:pk>', SectionDetailView.as_view(), name='section-detail'),
    path('admin/', securitypolicy_admin_site.urls),
]

