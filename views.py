from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from .models import menu_snk
from .models import menu_frst
from .models import menu_scnd
from .models import menu_dsrt
from django.http import HttpResponseBadRequest 
from django.contrib.auth.models import User
from .forms import BookTableForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from .models import Post, Comment
from .forms import VoucherForm
from .forms import CommentForm
# Create your views here.
@login_required(login_url='login')
def HomePage(request):    
    return render(request, 'main/home.html')

def SignupPage(request):    
    if request.method == 'POST':
        uname = request.POST.get('username')        
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')        
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")        
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()            
            return redirect('login')

    return render(request, 'main/signup.html')

def LoginPage(request):
    if request.method == 'POST':        
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')        
        user = authenticate(request, username=username, password=pass1)
        if user is not None:            
            login(request, user)
            return redirect('home')        
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'main/login.html')


def menu (request):
    menu_snks = menu_snk.objects.all()
    menu_frsts = menu_frst.objects.all()
    menu_scnds = menu_scnd.objects.all()
    menu_dsrts = menu_dsrt.objects.all()
    context = {'menu_snks': menu_snks,'menu_frsts': menu_frsts,'menu_scnds': menu_scnds,'menu_dsrts': menu_dsrts}
    return render(request, 'main/menu.html',context=context)


 
def voucher_form(request): 
    form = VoucherForm() 
    if request.method == 'POST': 
        form = VoucherForm(request.POST) 
        if form.is_valid(): 
            form.save() 
    context = {'form': form} 
    return render(request, 'main/voucher.html', context)





def book_table(request): 
    if request.method == 'POST': 
        form = BookTableForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('home') 
    else: 
        form = BookTableForm() 
    return render(request, 'main/book_table.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'main/logout.html')


class PostListView(ListView):    
    model = Post
    template_name = 'main/home2.html'    
    context_object_name = 'posts'
class PostDisplay(DetailView):
    model = Post    
    template_name = 'main/post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()        
        return context
class PostComment(SingleObjectMixin, FormView):
    model = Post    
    form_class = CommentForm
    template_name = 'main/post_detail.html'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()        
        return super().post(request, *args, **kwargs)
    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()        
        kwargs['request'] = self.request
        return kwargs
    def form_valid(self, form):        
        comment = form.save(commit=False)
        comment.post = self.object        
        comment.save()
        return super().form_valid(form)    
    def get_success_url(self):        
        post = self.get_object()
        return reverse('post_detail',kwargs={'pk': post.pk}) + '#comments'
class PostDetailView(View):
    def get(self, request, *args, **kwargs):        
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)    
    def post(self, request, *args, **kwargs):        
        view = PostComment.as_view()
        return view(request, *args, **kwargs)

