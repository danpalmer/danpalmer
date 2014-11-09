from django.views.generic import TemplateView

from .charts import StepsChart


class Index(TemplateView):
    template_name = 'projects/charts/index.html'

    def get_context_data(self):
        return {
            'chart': StepsChart()
        }
