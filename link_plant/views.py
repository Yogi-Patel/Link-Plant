from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link
from django.urls import reverse_lazy

# Create your views here.
class LinkListView(ListView):
    model = Link


class LinkCreateView(CreateView):

    model = Link
    fields = "__all__"

    success_url = reverse_lazy('link-list')

class LinkUpdateView(UpdateView):
    model = Link
    fields = ['Text', 'url']

    success_url = reverse_lazy('link-list')


class LinkDeleteView(DeleteView):

    model = Link
    success_url = reverse_lazy('link-list')


def profile_view(request, profile_slug):

    profile = get_object_or_404(Profile, slug = profile_slug)

    links = profile.links.all()

    context = {
        'profile': profile,
        'links': links,
    }

    return render(request, 'link_plant/profile.html', context)


