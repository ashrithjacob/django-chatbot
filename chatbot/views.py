from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from .forms import UploadFileForm
from .models import Document
# Imaginary function to handle an uploaded file.
from .processing import summary, get_pdf


def test_single_pg(request):
    dict = {'name':'Ashrith',
            'age': 26,
            'height': 174
            }
    if request.method == "POST" and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(document=request.FILES['file'], pub_date=timezone.now())
            newdoc.save()
        pdf_file = get_pdf(request.FILES['file'].read())
        return HttpResponse(f'{pdf_file.pages[0].extract_text()}')
    else:
        form = UploadFileForm()
    # Load documents for the list page
    documents = Document.objects.all()
    return render(request, "index.html", {"form": form})


def upload_file(request):
    total_summary={}
    if request.method == "POST" and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(document=request.FILES['file'], pub_date=timezone.now())
            newdoc.save()
        pdf_file = get_pdf(request.FILES['file'].read())
        page_number = 0
        while page_number < len(pdf_file.pages):
            total_summary['page_number'] = summary(pdf_file, page_number)
            page_number += 1
        return render(request, 'index.html', total_summary)
    else:
        form = UploadFileForm()
    # Load documents for the list page
    documents = Document.objects.all()
    return render(request, "index.html", {"form": form})


def index(request, val):
    return HttpResponse(f"Hello, world. You're at the chatbot index.,{val}")
    #return render(request, 'home.html', {'records':records})

