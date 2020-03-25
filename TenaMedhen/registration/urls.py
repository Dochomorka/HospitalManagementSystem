from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.index,name='index'),
]

# admin.site.site_header = "ጤና መድህን"
# #admin.site.site_title = "ሞጣ ሆስፒታል Admin Portal"
# admin.site.index_title = "ሞጣ የመጀመሪያ ደረጃ ሆስፒታል"