from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from app.models import Mehmonxona


# READ
def mehmonxonalar(request):
    mehmonxonalar = Mehmonxona.objects.all()
    return render(request, "mehmonxonalar.html", {
        "mehmonxonalar": mehmonxonalar
    })


# CREATE
def mehmonxona_create(request):
    if request.method == "POST":
        nomi = request.POST.get("nomi")
        manzil = request.POST.get("manzil")
        malumot = request.POST.get("malumot")
        yulduz_soni = request.POST.get("yulduz_soni")
        xona_soni = request.POST.get("xona_soni")
        bir_kunlik_narx = request.POST.get("bir_kunlik_narx")
        wifi_bormi = request.POST.get("wifi_bormi") == "on"
        emaili = request.POST.get("emaili")
        ochilgan_sana = request.POST.get("ochilgan_sana")

        Mehmonxona.objects.create(
            nomi=nomi,
            manzil=manzil,
            malumot=malumot,
            yulduz_soni=yulduz_soni,
            xona_soni=xona_soni,
            bir_kunlik_narx=bir_kunlik_narx,
            wifi_bormi=wifi_bormi,
            emaili=emaili,
            ochilgan_sana=ochilgan_sana,
        )

        return redirect("mehmonxonalar")

    return render(request, "mehmonxona_create.html")


# DETAIL
def mehmonxona_detail(request, id):
    hotel = get_object_or_404(Mehmonxona, id=id)

    return render(request, "mehmonxona_detail.html", {
        "mehmonxona": hotel
    })


# UPDATE
def mehmonxona_update(request, pk):
    hotel = get_object_or_404(Mehmonxona, id=pk)

    if request.method == "POST":
        hotel.nomi = request.POST.get("nomi")
        hotel.manzil = request.POST.get("manzil")
        hotel.malumot = request.POST.get("malumot")
        hotel.yulduz_soni = request.POST.get("yulduz_soni")
        hotel.xona_soni = request.POST.get("xona_soni")
        hotel.bir_kunlik_narx = request.POST.get("bir_kunlik_narx")
        hotel.wifi_bormi = request.POST.get("wifi_bormi") == "on"
        hotel.emaili = request.POST.get("emaili")
        hotel.ochilgan_sana = request.POST.get("ochilgan_sana")

        hotel.save()

        return redirect("mehmonxona_detail", id=hotel.pk)

    return render(request, "mehmonxona_update.html", {
        "mehmonxona": hotel
    })


# DELETE
def mehmonxona_delete(request, id):
    hotel = get_object_or_404(Mehmonxona, id=id)

    hotel.delete()
    return redirect("mehmonxonalar")
