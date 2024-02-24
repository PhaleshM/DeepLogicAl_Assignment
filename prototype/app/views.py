from django.shortcuts import render
from .models import UploadedFile
from .utils import response 
import markdown2
import json

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        toggle = request.POST.get('toggle')
        if toggle=="True":
            toggle=True
        else:
            toggle=False
        upload = UploadedFile(file=file, doc_type=toggle)
        upload.save()
        if toggle:
            res = response(upload.file.path, "t")
            if res!=None:
                res=json.dumps(res,indent=6)
        else:
            res = response(upload.file.path, "T")
            if res!= None:
                res=markdown2.markdown(res)
        
        if res==None:
            res="File does not support. Filetype can be a PDF or an image [jpeg, jpg, png]."
            
        return render(request, 'app/response.html', {'response': res,'toggle':toggle})
    return render(request, 'app/upload_form.html')
