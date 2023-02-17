from django.shortcuts import render
import os
import yolov5
import os
import cv2
import io
import os
import glob
from PIL import Image
import torch




def landing(request):
    return render(request, 'dashboard/landing.html')

def result_images(request):
    if request.method == "POST":
        model = torch.hub.load(
            'ultralytics/yolov5', 'custom', path='C:/Users/admin/school_study/django-object-detection/apps/dashboard/semi_best_0206_0911.pt', autoshape=True
        )  # force_reload = recache latest code
        model.eval()

        file = request.FILES.getlist('file')
        pf = []
        context = {}
        for file in file:
            filename = file.name.rsplit("/")[0]
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes))
            img.save(f"media/detectimage/{filename}",format="JPEG")

            results = model(img,size=640)
            results.render()
            data = results.pandas().xyxy[0][['name']].values.tolist()

            for img in results.ims:
                img_base64 = Image.fromarray(img)
                img_base64.save(f"media/finddetectimage/{filename}", format="JPEG")
            
            if len(data) == 0:
                pf.append("PASS")
            if len(data) != 0:
                pf.append("FAIL")
            root = "media/finddetectimage"
            files = []
            for file in glob.glob("{}/*.*".format(root)):
                fname = file.split(os.sep)[-1]
                files.append(fname)
            firstimage = "media/finddetectimage"+files[0]
        
            context["files"] = files
            context["pf"] = pf
            context["firstimage"] = firstimage
            context["enumerate"] = enumerate
            context["len"] = len
        print(pf)
        return render(request, 'dashboard/result.html',context)
    
def delete_files(request):
    
    directory = ['media/detectimage','media/finddetectimage']
    for direc in directory:
        for filename in os.listdir(direc):
            file_path = os.path.join(direc, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    return render(request, 'dashboard/delete.html')


            
        


    



