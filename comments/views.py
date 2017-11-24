from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from blog.models import Post
from comments import forms

# Create your views here.


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comments_set.all()
            context = {'post': post,
                       'comment_list': comment_list,
                       'form': form
                       }
            return render(request, 'blog/detail.html', context=context)
    else:
        redirect(post)