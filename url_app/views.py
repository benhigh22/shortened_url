from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from hashids import Hashids
from url_app.models import Bookmark, Click


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ('original_url', 'title', 'description')

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        hashids = Hashids(min_length=5)
        object.shortened_url = hashids.encode(object.id)
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("bookmark_list_view")


class BookmarkListView(ListView):
    model = Bookmark


def redirect(request, url):
    redirect_url_object = Bookmark.objects.get(shortened_url=url)
    return HttpResponseRedirect(redirect_url_object.original_url)


class BookmarkDetailView(DetailView):
    model = Bookmark

    def get_object(self):
        url_object = super().get_object()
        Click.objects.create(url=url_object)
        return url_object

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ('original_url', 'title', 'description')

    def get_success_url(self):
        return reverse("first_view")
