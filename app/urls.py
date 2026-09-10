from django.urls import path
from .views import mehmonxonalar, mehmonxona_detail


from django.urls import path

from .views import (
    mehmonxonalar,
    mehmonxona_create,
    mehmonxona_detail,
    mehmonxona_update,
    mehmonxona_delete,
)

urlpatterns = [
    # READ — barcha mehmonxonalar
    path("", mehmonxonalar, name="mehmonxonalar"),

    # CREATE — mehmonxona qo‘shish
    path("create/", mehmonxona_create, name="mehmonxona_create"),

    # READ — bitta mehmonxona
    path(
        "mehmonxona/<int:id>/",
        mehmonxona_detail,
        name="mehmonxona_detail"
    ),

    # UPDATE — tahrirlash
    path(
        "mehmonxona/<int:pk>/update/",
        mehmonxona_update,
        name="mehmonxona_update"
    ),

    # DELETE — o‘chirish
    path(
        "mehmonxona/<int:id>/delete/",
        mehmonxona_delete,
        name="mehmonxona_delete"
    ),
]