from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os

from .services import make_qr


def index(request):
    qr_url = None
    qr_filename = None

    if request.method == 'POST':
        url = request.POST.get("url")
        qr_url = make_qr(url)  
        qr_filename = os.path.basename(qr_url)

    return render(request, "qr_code/index.html", {
        "qr_url": qr_url,
        "qr_filename": qr_filename,
    })


def download_qr(request, filename):
    file_path = os.path.join(
        settings.BASE_DIR,
        'qr_code',
        'static',
        'qr_code',
        'qr_code_img',
        filename
    )

    if not os.path.exists(file_path):
        raise Http404("File not found")

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename=filename
    )
