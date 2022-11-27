from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    #verbose_name : 읽기쉬운 모델 객체의 이름 표시, 옵션을 지정하지 않으면 클래스 이름이 소문자로 변경된 것으로 표시된다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Java의 toString
    def __str__(self):
        # return "Custom Post object ({})".format(self.id)
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메시지 글자수"

    