from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .forms import LostItemForm, FoundItemForm
from django.shortcuts import render
from .models import LostItem, FoundItem


def lost_items(request):
    lost_items_list = LostItem.objects.all()
    return render(request, 'admin_module/lost_items.html', {'lost_items_list': lost_items_list})


def found_items(request):
    found_items_list = FoundItem.objects.all()
    return render(request, 'admin_module/found_items.html', {'found_items_list': found_items_list})


def lost_items(request):
    lost_items_list = LostItem.objects.all()
    return render(request, 'admin_module/lost_items.html', {'lost_items_list': lost_items_list})


def found_items(request):
    found_items_list = FoundItem.objects.all()
    return render(request, 'admin_module/found_items.html', {'found_items_list': found_items_list})


def post_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST)
        if form.is_valid():
            new_lost_item = form.save(commit=False)
            new_lost_item.user = request.user
            new_lost_item.save()
            return redirect('lost_items')
    else:
        form = LostItemForm()
    return render(request, 'admin_module/post_lost_item.html', {'form': form})


def edit_lost_item(request, item_id):
    lost_item = get_object_or_404(LostItem, id=item_id, user=request.user)

    if request.method == 'POST':
        form = LostItemForm(request.POST, instance=lost_item)
        if form.is_valid():
            form.save()
            return redirect('lost_items')
    else:
        form = LostItemForm(instance=lost_item)

    return render(request, 'admin_module/edit_lost_item.html', {'form': form})


def delete_lost_item(request, item_id):
    lost_item = get_object_or_404(LostItem, id=item_id, user=request.user)

    if request.method == 'POST':
        lost_item.delete()
        return redirect('lost_items')

    return render(request, 'admin_module/delete_lost_item.html', {'lost_item': lost_item})


def mark_item_found(request, item_id):
    lost_item = get_object_or_404(LostItem, id=item_id, user=request.user)

    if request.method == 'POST':
        found_item_form = FoundItemForm(request.POST)
        if found_item_form.is_valid():
            found_item = found_item_form.save(commit=False)
            found_item.user = request.user
            found_item.save()
            lost_item.delete()
            return redirect('lost_items')
    else:
        found_item_form = FoundItemForm()

    return render(request, 'admin_module/mark_item_found.html', {'found_item_form': found_item_form, 'lost_item': lost_item})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to the home page after registration
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'admin_module/register.html', {'form': form})
