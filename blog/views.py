from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'new_site/index.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def about(request):
    return render(request, 'old_site/about.html')

def old_index(request):
    return render(request, 'old_site/old_index.html')

def portfolio(request):
    return render(request, 'old_site/portfolio.html')

def contact(request):
    return render(request, 'old_site/contact.html')

def story(request):
    return render(request, 'a_walk_without_someone/story.html')

def story_intro(request):
    if request.method == "POST":
        print (request.POST["youName"])
        print (request.POST["loverName"])
        print (request.POST["youActivity"])
        print (request.POST["youCity"])
        print (request.POST["favDrink"])
        print (request.POST["favTouch"])
        print (request.POST["loverGender"])


        if (request.POST["loverGender"]) == "He":
            he_her_they = "he"
            him_her_them = "him"
            his_her_their = "his"
            he_she_they = "he"
            He_She_They = "He"
        elif (request.POST["loverGender"]) == "She":
            he_her_they = "she"
            him_her_them = "her"
            his_her_their = "her"
            he_she_they = "she"
            He_She_They = "She"
        elif (request.POST["loverGender"]) == "They":
            he_her_they = "they"
            him_her_them = "them"
            his_her_their = "their"
            he_she_they = "they"
            He_She_They = "They"
        else:
            return render(request, 'a_walk_without_someone/story_intro.html')


        if (request.POST["favTouch"]) == "Someone rubbing your feet":
            passFavTouch = "rub my feet"
        elif (request.POST["favTouch"]) == "Someone rubbing your back":
            passFavTouch = "rub my back"
        elif (request.POST["favTouch"]) == "Someone rubbing your head":
            passFavTouch = "rub my head"
        elif (request.POST["favTouch"]) == "Someone rubbing your belly":
            passFavTouch = "rub my belly"
        else:
            return render(request, 'a_walk_without_someone/story_intro.html')

        


        #build context dictionary with values user entered
        data = {"youName": request.POST["youName"],
                "loverName": request.POST["loverName"],
                "youActivity": request.POST["youActivity"],
                "youCity": request.POST["youCity"],
                "favDrink": request.POST["favDrink"],
                "passFavTouch": passFavTouch,
                "he_her_they": he_her_they,
                "him_her_them": him_her_them,
                "his_her_their": his_her_their,
                "he_she_they": he_she_they,
                "He_She_They": He_She_They,
                }

        return render(request, 'a_walk_without_someone/story.html', data)
      
    else:
        return render(request, 'a_walk_without_someone/story_intro.html')


        
# This is the above view simplified.  Use this to make a button if you don't find anything better
# def story_intro(request):
#     if request.method == "POST":
#         return render(request, 'a_walk_without_someone/story.html', data)
      
#     else:
#         return render(request, 'a_walk_without_someone/story_intro.html')












