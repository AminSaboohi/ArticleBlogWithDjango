from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages


class HomeView(ListView):
    model = Post
    template_name = 'blog_home.html'
    ordering = ['id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def logout_user(request):
    logout(request)
    messages.success(request, message="You Have Been Logged Out...")
    return redirect('home')


def category_list_view(request):
    cat_menu_list = Post.objects.categories.all()
    return render(request,
                  template_name='category_list.html',
                  context={'cat_menu_list': cat_menu_list})


def category_view(request, cats):
    category_posts = Post.objects.filter(category__title__contains=cats).all()
    first_post = category_posts.first()
    cats = first_post.category.title
    return render(request,
                  template_name='categories.html',
                  context={'cats': cats,
                           'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = self.object
        context = super(ArticleDetailView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
