from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, SignUpForm


def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Welcome to Echovision Media!")
			return redirect("services")
	else:
		form = SignUpForm()

	return render(request, "accounts/signup.html", {"form": form})


@login_required
def profile_view(request):
	return render(request, "accounts/profile.html", {"profile": request.user.profile})


@login_required
def profile_edit(request):
	profile = request.user.profile
	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			messages.success(request, "Profile updated.")
			return redirect("profile")
	else:
		form = ProfileForm(instance=profile)

	return render(request, "accounts/profile_edit.html", {"form": form})
