from django import forms

from text_statistics.tf_idf.models import TextFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = TextFile
        fields = ('file', )
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'file-input',
                'accept': '.txt'
            })
        }
