from django.shortcuts import render
from .models import CV


def english_cv_view(request):
    cv = CV.objects.get(language="English")
    return render(request, "mycv/cv.html", {"cv": cv})

def german_cv_view(request):
    cv = CV.objects.get(language="German")
    return render(request, 'mycv/cv_german.html', {"cv":cv})
