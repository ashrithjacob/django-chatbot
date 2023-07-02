from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from .forms import UploadFileForm
from .models import Document
# Imaginary function to handle an uploaded file.
from .processing import get_summary, get_pdf


def test_single_pg(request):
    l = ['Ashrith', '24', '174']
    if request.method == "POST" and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(document=request.FILES['file'], pub_date=timezone.now())
            newdoc.save()
        pdf_file = get_pdf(request.FILES['file'].read())
        #return HttpResponse(f'{pdf_file.pages[0].extract_text()}')
        return render(request, 'test.html', {'rows':l})
    else:
        form = UploadFileForm()
    # Load documents for the list page
    documents = Document.objects.all()
    return render(request, "index.html", {"form": form})


def upload_file(request):
    total_summary=[]
    if request.method == "POST" and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        pdf_file = get_pdf(request.FILES['file'].read())
        num_page = len(pdf_file.pages)
        if form.is_valid():
            newdoc = Document(document=request.FILES['file'], num_page=num_page, pub_date=timezone.now())
            newdoc.document_url = newdoc.document.name
            newdoc.save()
        page_number = 0
        while page_number < num_page:
            page_summary = get_summary(pdf_file, page_number)
            total_summary.append(page_summary)
            page_number += 1
        return render(request, 'index.html', {"total_summary":total_summary})
    else:
        form = UploadFileForm()
    # Load documents for the list page
    documents = Document.objects.all()
    return render(request, "index.html", {"form": form})


def index(request, val):
    return HttpResponse(f"Hello, world. You're at the chatbot index.,{val}")
    #return render(request, 'home.html', {'records':records})

#TODO
#- make summaries async
#- add path of file uploaded in s3 (aws)
#- add css/ bootstrap for styling