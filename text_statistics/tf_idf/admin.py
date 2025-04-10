from django.contrib import admin

from text_statistics.tf_idf.models import TextFile, TfIdfStatistics


@admin.register(TextFile)
class TextFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'created_at']


@admin.register(TfIdfStatistics)
class TfIdfStatisticsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_file__file', 'word', 'tf', 'idf', 'tf_idf']
