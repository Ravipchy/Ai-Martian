from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
# from .models import Certificate
# from .forms import CertificateForm

# Home Page
def home(request):
    return render(request, 'index.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Dashboard Page
def dashboard(request):
    return render(request, 'dashboard.html')  # Corrected spelling

# Services Page
def services(request):
    return render(request, 'services.html')

# # Thanks Page
# def thanks(request):
#     return render(request, 'thanks.html')

# # Verify Page
# def verify(request):
#     return render(request, 'verify.html')

# # Web Developer Intern Page
# def web_intern(request):
#     return render(request, 'web-developer-intern.html')

# def form(request):
#     return render(request,'form.html')