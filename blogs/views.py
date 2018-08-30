from django.views import generic
from .models import Articles

class IndexView(generic.ListView):
    template_name = 'blogs/index.html' #模板可以直接放到blogs/templates/下面,不用多一层放到blogs/templates/blogs/下
    context_object_name = 'article_list'
    paginate_by = 2
    def get_queryset(self):
        return Articles.objects.all().order_by('-pub_date')
class DetailView(generic.DetailView):
    model = Articles
    template_name = 'blogs/detail.html'