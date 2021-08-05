from wall_profiles.models import Profile
from wall_profiles.forms import WallProfileForm
from django.shortcuts import redirect, render
from wall_blogs.models import Post

def user_home_page(request, pk):
    profile = Profile.objects.get(pk=pk)
    posts = Post.objects.all().filter(user_owned=profile)
    context = {
        "profile": profile,
        "posts": posts,
    }
    return render(request, 'profile/user_home_page.html', context)

def profile_completed(user):
    if not user.is_complete:
        for k, v in user.__dict__.items():
            if v == None:
                return False
            user.is_complete = True
    return True


def complete_profile(request):
    profile = Profile.objects.get(pk=request.user.pk)
    if not profile_completed(profile):        
        if request.method == "POST":
            form = WallProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('user home page', pk=request.user.pk)
            else:
                form = WallProfileForm(instance=profile)
                context = {
                    "form": form,
                }
                return redirect('user home page', pk=request.user.pk)
           
        form = WallProfileForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'profile/complete_profile.html', context)
    return redirect('user home page', pk=request.user.pk)


def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = WallProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user home page', pk=pk)
        else:
            return redirect('edit profile', pk=pk)
    form = WallProfileForm(instance=profile)
    context ={
        "form":form,
    }
    return render(request, 'profile/edit-profile.html', context)
