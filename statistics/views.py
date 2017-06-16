from django.views.generic.base import TemplateView
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum

from feed.models import Tweet

class StatisticsView(TemplateView):
    template_name = "statistics.html"

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data(**kwargs)

        count_stats = Tweet.objects \
            .annotate(month=TruncMonth('timestamp')) \
            .values('month') \
            .annotate(count=Count('pk')) \
            .order_by()

        context['count_stats'] = {stat['month'].strftime('%B, %Y'): stat['count'] for stat in count_stats}

        return context
