from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('export/csv/', export_students_csv, name='export_students_csv'),
    path('', export_success, name='export_success'),
    path("export/pdf/",construct_pdf_from_model,name="export_pdf")
]
