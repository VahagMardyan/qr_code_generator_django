import qrcode as qr
import os
import hashlib

def make_qr(text:str) -> str:
    img = qr.make(text)
    
    text_hash = hashlib.md5(text.encode()).hexdigest()

    folder_path = "qr_code/static/qr_code/qr_code_img"
    os.makedirs(folder_path, exist_ok=True)
    file_name = f"{text_hash}.png"
    img_path = os.path.join(folder_path, file_name)
    img.save(img_path)
    return f"qr_code/qr_code_img/{file_name}"
