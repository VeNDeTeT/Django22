from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        #return Post.objects.filter(is_published=True) # только статьи показывает
        return Post.objects.all().order_by('-created_at') # показывает все и статьи и черновики



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


# CRUD
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:list')
