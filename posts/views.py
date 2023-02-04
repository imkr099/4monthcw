from django.shortcuts import render, redirect
from posts.models import Post, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from django.views.generic import ListView

# Create your views here.

PAGINATION_LIMIT = 3


def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


class MainView(ListView):
    model = Post
    template_name = 'layouts/index.html'


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            posts = Post.objects.filter(
                title__icontains=search,
                description__icontains=search
            )

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'posts': posts,
            'user': request.user,
            'max_page': range(1, max_page+1),
            'prev_page': page - 1,
            'next-page': page + 1 if max_page > page else max_page
        }

        return render(request, 'posts/posts.html', context=context)


class PostsView(ListView):
    model = Post
    template_name = 'posts/posts.html'

    def get(self, request, **kwargs):
        posts = self.get_queryset()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            posts = Post.objects.filter(
                title__icontains=search,
                description__icontains=search
            )

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'posts': posts,
            'user': request.user,
            'max_page': range(1, max_page+1),
            'prev_page': page - 1,
            'next_page': page + 1 if max_page > page else max_page
        }

        return render(request, self.template_name, context=context)


def post_detail_view(request, id):
    if request.method == 'GET':
        post_obj = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post_obj)

        context = {
            'post': post_obj,
            'comments': comments,
            'form': CommentCreateForm
        }

        return render(request, 'posts/detail.html', context=context)

    if request.method == 'POST':
        post_obj = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post_obj)
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                post=post_obj,
                text=form.cleaned_data.get('text')
            )
            return redirect(f'/posts/{post_obj.id}/')

        return render(request, 'posts/detail.html', context={
            'post': post_obj,
            'comments': comments,
            'form': form
        })


def create_post_view(request):
    if request.method == 'GET':
        context = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/posts')
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5
            )
            return redirect('/posts/')
        return render(request, 'posts/create.html', context={
            'form': form
        })