from django.contrib import admin
# 
from .models import Question,Choice,Category

admin.site.register(Category)
admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
class  QuestionAdmin(admin.ModelAdmin):
	search_fields = ['question_text']
	fieldsets = [
        (None,  			 {'fields': ['question_text'],}),
        (None,               {'fields': ['category'],}),
        ]
	inlines = [ChoiceInline]
admin.site.register(Question,QuestionAdmin)
