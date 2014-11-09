from weasyprint import HTML

from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, View
from django.template.loader import render_to_string

from danpalmer.blog.models import Post


class Home(ListView):
    template_name = 'home/view.html'
    context_object_name = 'posts'

    queryset = Post.objects.order_by(
        '-published',
    ).filter(
        published__isnull=False,
    )[:3]


class CV(TemplateView):
    template_name = 'home/cv.html'


class CVPDF(View):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = \
            'attachment; filename="dan-palmer-cv.pdf"'

        html = render_to_string('home/cv.html')

        HTML(
            string=html,
            base_url='http://%s/' % request.get_host(),
        ).write_pdf(response)

        return response
