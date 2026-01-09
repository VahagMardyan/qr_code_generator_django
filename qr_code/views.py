from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from django.shortcuts import redirect
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

def delete_all_qrs(request):
    if request.method == "POST":
        folder_path = os.path.join(settings.BASE_DIR, 'qr_code', 'static', 'qr_code', 'qr_code_img')
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    return redirect('home')