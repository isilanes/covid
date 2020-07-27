from django.shortcuts import render, redirect


def user(request):
    return render(request, "user.html", {})


def main_index(request):
    if request.user.is_authenticated:
        return redirect('plots:show')
    else:
        return redirect('login:login')
