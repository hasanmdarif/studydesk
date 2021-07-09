# from django.contrib.messages import constants as messages
from django.shortcuts import render
from django.views import generic
from .models import ContactUs, Post

# Create your views here.
def contactUs(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        subject = request.POST["subject"]
        content = request.POST["content"]

        # if len(name)<3 or len(email)<5 or len(phone)<10 or len(subject)<8 or len(content)<15:
        #     messages.error(request, "Please fill the form correctly")

        # else:
        contact = ContactUs(name=name, email=email, phone=phone,subject=subject,content=content)
        contact.save()
        # messages.success(request, "We got your message")

    return render(request, "contact.html")


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def search(request):
    # post_list = Post.objects.all()
    query = request.GET.get('query')
    post_list = Post.objects.filter(title__icontains=query)
    params ={'post_list': post_list,'query':query}
    return render (request,'search.html',params)
    # return HttpResponse('this is search')

class AboutUs(generic.ListView):
    model = Post
    template_name = 'about.html'
