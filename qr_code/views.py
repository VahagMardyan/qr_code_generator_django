from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from django.shortcuts import redirect
import os

from .services import make_qr


def index(request):
    qr_code_data = None
    text = ""

    if request.method == 'POST':
        text = request.POST.get("url")
        # Այստեղ ստանում ենք Base64 տողը
        qr_code_data = make_qr(text)

    return render(request, "qr_code/index.html", {
        "qr_code_data": qr_code_data,
        "input_value": text,
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