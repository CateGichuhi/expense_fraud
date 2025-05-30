from django.shortcuts import render
from .forms import ReceiptForm
from .models import Receipt
from PIL import Image
import pytesseract

# Optional: set tesseract path if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check_font_mismatch(text):
    # Very naive placeholder logic
    suspicious_fonts = ['𝓯', '𝔬', '𝖓', '𝒕']  # example: fake fancy letters
    for char in text:
        if char in suspicious_fonts:
            return True
    return False

def upload_receipt(request):
    context = {}
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save()

            # OCR processing
            image = Image.open(receipt.image.path)
            text = pytesseract.image_to_string(image)

            # Check for fraud (font mismatch example)
            is_fraud = check_font_mismatch(text)

            # Save results
            receipt.extracted_text = text
            receipt.font_mismatch_flag = is_fraud
            receipt.save()

            context['receipt'] = receipt
    else:
        form = ReceiptForm()

    context['form'] = form
    return render(request, 'fraudcheck/upload.html', context)
