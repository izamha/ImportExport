from django.shortcuts import render
from django.views.generic import TemplateView
from .admin import PostResource
from django.http import HttpResponse


class MainView(TemplateView):
    template_name = 'core/home.html'


def export(request, format):
    posts_resource = PostResource()
    dataset = posts_resource.export()
    if format == 'csv':
        dataset_format = dataset.csv
    else:
        dataset_format = dataset.xls
    response = HttpResponse(dataset_format, content_type=f'text/{format}')
    response['Content-Disposition'] = f"attachment; filename=posts.{format}"
    return response
