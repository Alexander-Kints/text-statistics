from django.db import models


class TextFile(models.Model):
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def create_statistics(self, tf_dict, idf_dict, tfidf_dict):
        for word, tf in tf_dict.items():
            TfIdfStatistics.objects.create(
                text_file=self,
                word=word,
                tf=tf,
                idf=idf_dict.get(word),
                tf_idf=tfidf_dict.get(word)
            )

    def __str__(self):
        return self.file.name

    class Meta:
        db_table = 'text_file'


class TfIdfStatistics(models.Model):
    word = models.CharField(max_length=64)
    tf = models.FloatField()
    idf = models.FloatField()
    tf_idf = models.FloatField()
    text_file = models.ForeignKey(
        TextFile, on_delete=models.CASCADE, related_name='statistics'
    )

    def __str__(self):
        return self.word

    class Meta:
        db_table = 'tf_idf_statistics'
