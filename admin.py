from django.contrib import admin
from .models import menu_snk
from .models import menu_frst
from .models import menu_scnd
from .models import menu_dsrt
from .models import Voucher
from .models import BookTable  
from .models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment    
    extra = 0
class PostAdmin(admin.ModelAdmin):
    inlines = [        
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(menu_snk) 
admin.site.register(Voucher)
admin.site.register(menu_frst) 
admin.site.register(menu_scnd) 
admin.site.register(menu_dsrt) 
admin.site.register(BookTable)
