from django.db import models

class Receipt(models.Model):
    image = models.ImageField(upload_to='receipts/')
    extracted_text = models.TextField(blank=True, null=True)
    font_mismatch_flag = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt {self.id} - Uploaded at {self.uploaded_at}"
