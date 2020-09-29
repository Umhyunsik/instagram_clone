from django.contrib.auth.models import User
from django import forms

#폼 : 폼태그 -> HTML의 태그 -> 프론트단에서 사용자의 입력을 받는 인터페이스
# 장고의 폼 : HTML의 폼역할 ,데이터베이스에 저장할 내용을 형식,제약조건
class RegisterForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput)
    #widget 비밀번호  * 표시
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        #총 6개를 입력받는거임 위에 password,password2 포함
    def clean_password2(self):
        cd =self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError("Passwords not matched")
        return cd['password2']