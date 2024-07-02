from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.models import *
import csv
from reportlab.pdfgen import canvas

def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['name','usn','sem'])

    students = Students.objects.all().values_list('name','usn','sem')
    for student in students:
        writer.writerow(student)
    return response

def construct_pdf_from_model(request):
    students=Students.objects.all()
    response=HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment;filename="student_data.pdf"'
    c=canvas.Canvas(response)
    c.drawString(70,720,"name")
    c.drawString(170,720,"usn")
    c.drawString(270,720,"sem")
    y=660
    for student in students:
        c.drawString(70,y,student.name)
        c.drawString(170,y,student.usn)
        c.drawString(270,y,str(student.sem))
        y=y-60
    c.showPage()
    c.save()
    return response

def export_success(request):
    return render(request, 'index.html')