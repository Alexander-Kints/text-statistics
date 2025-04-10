from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from text_statistics.tf_idf.forms import UploadFileForm
from text_statistics.tf_idf.tf_idf_impl import get_tf_idf
from text_statistics.tf_idf.models import TfIdfStatistics

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
            text_file = form.save()
            # return HttpResponseRedirect('/success/')
            context['success'] = True
            tf_dict, idf_dict, tfidf_dict = get_tf_idf(text_file.file.path)

            for word, tf in tf_dict.items():
                stat = TfIdfStatistics.objects.create(
                    text_file=text_file,
                    word=word,
                    tf=tf,
                    idf=idf_dict.get(word),
                    tf_idf=tfidf_dict.get(word)
                )

        return render(request, 'index.html', context=context)
