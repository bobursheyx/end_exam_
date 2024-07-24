from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
	path('logout/', views.custom_logout, name="logout"),
	path('un_pdf/', views.un_pdf, name='un_pdf'),
	path('pdf/', views.pdf, name='pdf'),
	path('admin/', admin.site.urls),
	path('login/', views.login_page, name='login'),
	path('register/', views.register_page, name='register'),
	path('', views.expenses, name='expenses'),
	path('un_expenses', views.un_expenses, name='un_expenses'),
	path('update_un_expense/<id>',views.update_un_expense, name='update_un_expense'),
	path('update_expense/<id>', views.update_expense, name='update_expense'),
	path('delete_un_expense/<id>', views.delete_un_expense, name='delete_un_expense'),
	path('delete_expense/<id>', views.delete_expense, name='delete_expense'),
]
