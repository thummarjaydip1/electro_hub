from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer, FeedbackSerializer


# CONTACT ADD
@login_required(login_url="auth_login")
def contact_add_data(request):
    try:
        if request.method == "POST":

            Contact.objects.create(
                name=request.POST.get("name"),
                age=request.POST.get("age"),
                email=request.POST.get("email"),
                mobile=request.POST.get("mobile"),
                address=request.POST.get("address"),
            )

            messages.success(request, "Contact Send Successfully")
            return redirect("display_data")

        return render(request, "api/contact.html")

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")


# CONTACT UPDATE
@login_required(login_url="auth_login")
def contact_update_data(request, id):
    try:
        data = get_object_or_404(Contact, id=id)

        if request.user.username == data.name:

            if request.method == "POST":

                data.name = request.POST.get("name")
                data.age = request.POST.get("age")
                data.email = request.POST.get("email")
                data.mobile = request.POST.get("mobile")
                data.address = request.POST.get("address")

                data.save()

                messages.success(request, "Contact Update Successfully")
                return redirect("display_data")

        else:
            messages.warning(request, "You cant update only your contact")
            return redirect("error_page")

        return render(request, "api/contact_update.html", {"data": data})

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")


# CONTACT DELETE
@login_required(login_url="auth_login")
def contact_delete_data(request, id):
    try:
        data = get_object_or_404(Contact, id=id)

        if request.user.username == data.name:

            data.delete()

            messages.warning(request, "Contact Delete Successfully")
            return redirect("display_data")

        else:
            messages.warning(request, "You cant delete only your contact")
            return redirect("error_page")

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")


# DISPLAY DATA
@login_required(login_url="auth_login")
def display_data(request):
    try:

        data = Contact.objects.all()
        dataa = Feedback.objects.all()

        return render(
            request,
            "api/con_fed_disp.html",
            {
                "data": data,
                "dataa": dataa,
            },
        )

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")


# FEEDBACK ADD
@login_required(login_url="auth_login")
def feedback_add_data(request):
    try:

        if request.method == "POST":

            Feedback.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                rating=request.POST.get("rating"),
                message=request.POST.get("message"),
            )

            messages.success(request, "Feedback Send Successfully")
            return redirect("display_data")

        return render(request, "api/feedback.html")

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")


# FEEDBACK UPDATE
@login_required(login_url="auth_login")
def feedback_update_data(request, id):
    try:

        data = get_object_or_404(Feedback, id=id)

        if request.user.username == data.name:

            if request.method == "POST":

                data.name = request.POST.get("name")
                data.email = request.POST.get("email")
                data.rating = request.POST.get("rating")
                data.message = request.POST.get("message")

                data.save()

                messages.success(request, "Feedbcak Update Successfully")
                return redirect("display_data")

        else:
            messages.warning(request, "You cant update only your feedback")
            return redirect("error_page")

        return render(request, "api/feedback_update.html", {"data": data})

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")


# FEEDBACK DELETE
@login_required(login_url="auth_login")
def feedback_delete_data(request, id):
    try:

        data = get_object_or_404(Feedback, id=id)

        if request.user.username == data.name:

            data.delete()

            messages.warning(request, "Record Deleted Successfully")
            return redirect("display_data")

        else:
            messages.warning(request, "You cant delete only your feedback")
            return redirect("error_page")

    except Exception as e:
        print(e)
        messages.warning(request, "Somthing wrong")
        return redirect("error_page")