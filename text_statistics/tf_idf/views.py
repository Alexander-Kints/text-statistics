from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from text_statistics.tf_idf.forms import UploadFileForm
from text_statistics.tf_idf.models import TextFile, TfIdfStatistics
from text_statistics.tf_idf.tf_idf_impl import get_tf_idf


class IndexView(View):
    def get(self, request):
        form = UploadFileForm()
        files = TextFile.objects.all().order_by('-created_at')[:20]
        return render(request, 'index.html', context={
            'form': form,
            'files': files
        })

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            text_file = form.save()
            tf_dict, idf_dict, tfidf_dict = get_tf_idf(text_file.file.path)
            text_file.create_statistics(tf_dict, idf_dict, tfidf_dict)
            return HttpResponseRedirect(f'/statistics/{text_file.id}/')

        return render(request, 'index.html', context={'form': form})


class StatisticsView(ListView):
    model = TfIdfStatistics
    template_name = 'statistics.html'
    context_object_name = 'stats'
    paginate_by = 50

    def get_queryset(self):
        text_file = get_object_or_404(TextFile, id=self.kwargs.get('file_id'))
        return TfIdfStatistics.objects.filter(
            text_file=text_file
        ).order_by('-idf')
