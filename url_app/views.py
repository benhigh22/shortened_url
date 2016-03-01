from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from url_app.forms import BookmarkForm
from hashids import Hashids


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
            return render(request, 'index.html', {'new_url':new_url})
        return HttpResponseRedirect(reverse("first_view"))

    