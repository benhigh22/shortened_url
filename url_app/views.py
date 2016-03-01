from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, ListView
from url_app.forms import BookmarkForm
from hashids import Hashids
from url_app.models import Bookmark, Click


class FirstView(View):


    def get(self, request):
        bookmark_form = BookmarkForm()
        return render(request, 'index.html', {'form': bookmark_form})


    def post(self, request):
        form_instance = BookmarkForm(request.POST)
        hashids = Hashids()
        if form_instance.is_valid():
            new_url = form_instance.save()
            new_url.shortened_url = hashids.encode(new_url.id)
            new_url.save()
            return render(request, "new_url.html", {'new_url': new_url})
        return HttpResponseRedirect(reverse("first_view"))


class BookmarkListView(ListView):
    model = Bookmark


def redirect(request, url):
    redirect_url_object = Bookmark.objects.get(shortened_url=url)
    return HttpResponseRedirect(redirect_url_object.original_url)



