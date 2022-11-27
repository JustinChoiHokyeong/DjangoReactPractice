from django.contrib import admin
from .models import Post

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)
# 특정 모델에 대해서 어드민 등록은 한번만 가능하다

@admin.register(Post) #파이썬 장식자 문법으로 사용, Wrapping, 감싼 대상의 기능을 변경하는 것이다.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length','is_public' , 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        # return len(post.message)
        # return f"{len(post.message)} 글자"
        return "{} 글자".format(len(post.message))
