from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Photo

@login_required
def photo_list(request):
    # 보여줄 사진 데이터

    photos=Photo.objects.all()
    # 포토 오브젝트에서 orm 매니저한테 전부 다줘

    return render(request,'photo/list.html',{'photos':photos})#context-value  #photos=object_list
    # render는 화면에표시 하는것
    # template폴더에서부터 photo 밑에 list라는 것임
    # 템플릿안에서는 photos라는 이름으로 쓰겠다. but object_list가 기본임 !


from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.shortcuts import redirect #uploadview에 필요함

#먼저 넣어준다 createview보다
class PhotoUploadView(LoginRequiredMixin,CreateView):
    model=Photo
    fields = ['photo','text']#뭐입력받을꺼야?  작성자(author ) ,작성시간(created)
    template_name = 'photo/upload.html'

    #저장 방법 3가지 save method 거기안에서, 여기서 처리 , front-end javascript지

    def form_valid(self,form):
        form.instance.author_id = self.request.user.id #foreign key 언더바 id 넣어줘야한다.

        #데이터가 올바른것인가
        if form.is_valid():
            # 데이터가 올바르다면 저장하겠다.
            form.instance.save()
            return redirect('/')#success url 하는방법
        else:
            return self.render_to_response({'form':form})#회원가입 잘못 했을때 비밀번호 일치하지않습니다 내용이 채워져있는거 유지

class PhotoDeleteView(DeleteView):
    model=Photo
    success_url = '/'
    template_name = 'photo/delete.html'
    #단일 객체라  내부적으로 알아서 object로 던져줌

class PhotoUpdateView(UpdateView):
    model=Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'
