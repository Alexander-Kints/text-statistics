from django.db import models

class TextFile(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'text_file'


class TfIdfStatistics(models.Model):
    word = models.CharField(max_length=64)
    tf = models.FloatField()
    idf = models.FloatField()
    tf_idf = models.FloatField()
    text_file = models.ForeignKey(TextFile, on_delete=models.CASCADE, related_name='statistics')

    def __str__(self):
        return self.word

    class Meta:
        db_table = 'tf_idf_statistics'
