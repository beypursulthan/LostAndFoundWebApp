from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .forms import UserLostItemForm, UserFoundItemForm
from django.shortcuts import render
from .models import UserLostItem, UserFoundItem


def user_lost_items(request):
    if request.user.is_authenticated:
        user_lost_items_list = UserLostItem.objects.filter(user=request.user)
        return render(request, 'user_module/user_lost_items.html', {'user_lost_items_list': user_lost_items_list})
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'user_module/user_not_authenticated.html')


def user_found_items(request):
    if request.user.is_authenticated:
        user_found_items_list = UserFoundItem.objects.filter(user=request.user)
        return render(request, 'user_module/user_found_items.html', {'user_found_items_list': user_found_items_list})
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'user_module/user_not_authenticated.html')


def user_lost_items(request):
    user_lost_items_list = UserLostItem.objects.filter(user=request.user)
    return render(request, 'user_module/user_lost_items.html', {'user_lost_items_list': user_lost_items_list})


def user_found_items(request):
    user_found_items_list = UserFoundItem.objects.filter(user=request.user)
    return render(request, 'user_module/user_found_items.html', {'user_found_items_list': user_found_items_list})


def post_user_lost_item(request):
    if request.method == 'POST':
        form = UserLostItemForm(request.POST)
        if form.is_valid():
            new_user_lost_item = form.save(commit=False)
            new_user_lost_item.user = request.user
            new_user_lost_item.save()
            return redirect('user_lost_items')
    else:
        form = UserLostItemForm()
    return render(request, 'user_module/post_user_lost_item.html', {'form': form})


def edit_user_lost_item(request, item_id):
    user_lost_item = get_object_or_404(
        UserLostItem, id=item_id, user=request.user)

    if request.method == 'POST':
        form = UserLostItemForm(request.POST, instance=user_lost_item)
        if form.is_valid():
            form.save()
            return redirect('user_lost_items')
    else:
        form = UserLostItemForm(instance=user_lost_item)

    return render(request, 'user_module/edit_user_lost_item.html', {'form': form})


def delete_user_lost_item(request, item_id):
    user_lost_item = get_object_or_404(
        UserLostItem, id=item_id, user=request.user)

    if request.method == 'POST':
        user_lost_item.delete()
        return redirect('user_lost_items')

    return render(request, 'user_module/delete_user_lost_item.html', {'user_lost_item': user_lost_item})


def mark_user_item_found(request, item_id):
    user_lost_item = get_object_or_404(
        UserLostItem, id=item_id, user=request.user)

    if request.method == 'POST':
        user_found_item_form = UserFoundItemForm(request.POST)
        if user_found_item_form.is_valid():
            user_found_item = user_found_item_form.save(commit=False)
            user_found_item.user = request.user
            user_found_item.save()
            user_lost_item.delete()
            return redirect('user_lost_items')
    else:
        user_found_item_form = UserFoundItemForm()

    return render(request, 'user_module/mark_user_item_found.html', {'user_found_item_form': user_found_item_form, 'user_lost_item': user_lost_item})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Replace 'home' with the name of your home view
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# views.py


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Replace 'home' with the name of your home view
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
