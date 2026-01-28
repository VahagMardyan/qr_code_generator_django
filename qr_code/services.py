import qrcode as qr
import base64
from io import BytesIO

def make_qr(text:str) -> str:
    img = qr.make(text)
    
    buffer = BytesIO()
    img.save(buffer, format="PNG")

    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return qr_base64
