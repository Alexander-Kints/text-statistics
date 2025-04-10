from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from text_statistics.tf_idf.forms import UploadFileForm

class IndexView(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'index.html', context={
            'form': form,
        })

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        context={'form': form}
        if form.is_valid():
            file = form.save()
            print(file.file.path)
            # return HttpResponseRedirect('/success/')
            context['success'] = True

        return render(request, 'index.html', context=context)
