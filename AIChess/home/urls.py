from django.urls import path

from home.views import(
	home,
	base,
)

urlpatterns = [
	path('', home, name='home'),
	path('base/', base, name= 'base'),
]