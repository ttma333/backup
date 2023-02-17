from django.urls import path
from . import views

app_name = "detectobj"

urlpatterns = [
    path("<int:pk>/selected_image/",
         views.InferencedImageDetectionView.as_view(),
         name="detection_image_detail_url"
         ),
    path("<int:pk>/selected_image2/",
         views.InferencedImageDetectionView2.as_view(),
         name="detection_image_detail_url2"
         ),
]
