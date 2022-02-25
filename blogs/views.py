from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

# Create your views here.
@login_required
def index(request):
    """The home page for the Blog."""
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/index.html',context)


#Creating forms
@login_required
def new_blog(request):
    """Adding a new post."""
    if request.method != 'POST':
        #No data submitted, process data.
        form = BlogForm()
    else:
        #POST data submitted, process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect("blogs:index")

    #Display a blank or invald form.
    context = {'form':form}
    return render(request, 'blogs/new_blog.html', context)

#Editing posts
@login_required
def edit_blog(request,blog_id):
    """Edit an existing blog post."""
    blog = BlogPost.objects.get(id=blog_id)
    post = blog.text
    post = get_object_or_404(blog, id=blog_id)
    #Making sure the blog posts belongs to the current user.
    if blog.owner != request.user:
        raise Http404
 
    if request.method != "POST":
        #keep the page with the details of the current page.
        form = BlogForm(instance=blog)
    else:
        #POST data submitted; process data.
        form = BlogForm(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blog':blog,'form':form}
    return render(request,'blogs/edit_blog.html',context)