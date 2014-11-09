from django.views.generic import ListView, DetailView

from .models import Post


class Index(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    queryset = Post.objects.order_by(
        '-published',
    ).filter(
        published__isnull=False,
    )


class View(DetailView):
    model = Post
    template_name = 'blog/post.html'
