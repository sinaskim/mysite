from django.shortcuts import render ,redirect, get_object_or_404 #django.shortcuts에서 기능들을 이용할 수 있도록 render,redirect,get_object_or_404를 불러온다. 
from .models import Blog,Hashtag #.models에서 Blog를 불러온다.
from .forms import PostForm,CommentForm,HashtagForm #.forms에서 PostForm을 불러온다.
from django.utils import timezone #시간을 이용하기 위해 django.utils에서 timezone을 불러온다.

# Create your views here.
def base(request): #함수 base를 선언
    return render(request, 'blog/base.html') #render을 이용하여 blog/base.html을 띄운다.

#메인페이지
def main(request): #메인함수 선언
    posts = Blog.objects #posts에 Blog의 모든 객체를 저장
    hashtags = Hashtag.objects
    return render(request, 'blog/main.html', {'posts':posts, 'hashtags':hashtags}) #요청되었을때 posts를 모두 띄운다.

#글쓰기 페이지
def write(request): #함수 write선언
    return render(request, 'blog/write.html') #요청되었을 때, write.html을 띄운다.

#글쓰기 함수
        
#편집페이지
def edit(request,id): #edit함수 선언
    post = get_object_or_404(Blog, id=id) #post에 id를받고 
    if request.method == 'POST': # 만약 request.method가 POST면
        form = PostForm(request.POST, instance=post) #form은 PostForm에 request.POST와 INSTANCE=POST를 받은 값이다.
        if form.is_valid(): #만약 form.is_valid가 true이면
            form.save(commit=False) #Fform을 저장한다.
            form.save() #변경된 내용들을 모두 저장한다.
            return redirect('main') #그리고 메인페이지로 돌아간다.
    else:
        form = PostForm(instance=post) #form은 PostForm에 instance이 post와 같은 값이다.
        return render(request, 'blog/edit.html',{'form':form}) #form과 edit.html을 반환한다.

def detail(request,id): #함수 detail을 선언하고 요청되었을때 id를 받는다.
    post = get_object_or_404(Blog, id=id) #post에 get_object_or_404에 BLOG와 ID를 받은 값을 저장한다.
    hashtags = Hashtag.objects
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail',id)
    else:
        form = CommentForm()
        return render(request, 'blog/detail.html',{'post':post, 'form':form}) #post를 띄운다

def delete(request,id): #delete함수 선언
    post = get_object_or_404(Blog, id=id) #post에 get_object_or_404에 BLOG와 ID를 받은 값을 저장한다.
    post.delete() #post를 지운다.
    return redirect('main') #그리고 메인페이지로 돌아간다.

def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'blog/hashtag.html', {'form':form, "error_message":error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'blog/hashtag.html', {'form':form})

def create(request, blog=None):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.datetime.now()
            post.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = PostForm(instance=blog)
        return render(request, 'blog/write.html', {'form':form})


def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'blog/search.html', {'hashtag':hashtag})