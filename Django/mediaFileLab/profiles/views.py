from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profiles/profile.html', context)

def home(request):
    user = request.user
    if user.is_authenticated:
        context = {
            'user':user
            }
        print(user.profile.avatar)
        return render(request, 'profiles/main.html', context)
    return render(request, 'profiles/main.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Account created successfully! Great job, {form.cleaned_data.get('username')}!")
    else:
        form = UserRegisterForm()

    return render(request, 'profiles/register.html', {'form':form})

# def user_login(request):
#     if request.method == 'POST':
#         pass
#     pass

def logout(request):
    pass
