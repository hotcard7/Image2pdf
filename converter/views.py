from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from PIL import Image
from reportlab.pdfgen import canvas
import io

def image_to_pdf(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            image = Image.open(image_file)

            # Prepare response to return a PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="converted.pdf"'

            # Create a buffer to store PDF data
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)

            # Adjust the page size to the image size and draw the image
            x, y = image.size
            p.setPageSize((x, y))

            # Drawing the image
            image_rgb = image.convert('RGB')  # Convert image to RGB mode
            image_path = '/tmp/image_to_pdf_temp.jpeg'  # Temporary path for saving image
            image_rgb.save(image_path)  # Save the image to a temporary path

            # Draw the image from the temporary path
            p.drawImage(image_path, 0, 0, width=x, height=y)
            p.showPage()
            p.save()

            # Move back to the start of the buffer and send as a response
            buffer.seek(0)
            response.write(buffer.getvalue())

            # Optionally remove the temporary file if needed
            import os
            os.remove(image_path)

            return response
        else:
            print("Form is not valid")  # Debugging: print form errors
            print(form.errors)
    else:
        form = ImageUploadForm()

    return render(request, 'converter/upload.html', {'form': form})

def home(request):
    return render(request,'home.html')