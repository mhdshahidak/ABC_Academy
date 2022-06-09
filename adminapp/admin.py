
from django.contrib import admin

from student.models import ExamStatus,Answer
from website.models import OnlineApplying
from .models import *
# Register your models here.

admin.site.register(User)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name','email')
    search_fields=('branch_name',)
admin.site.register(Branch,BranchAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields=('name',)
admin.site.register(Teacher,TeacherAdmin)



class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','email')
    search_fields=('first_name',)
admin.site.register(Student,StudentAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('couse_name','course_id')
    search_fields=('couse_name',)
admin.site.register(Courses,CoursesAdmin)

class BatchAdmin(admin.ModelAdmin):
    list_display = ('starting_date','ending_date')
admin.site.register(Batch,BatchAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_name','exam_date')
admin.site.register(Exam,ExamAdmin)


class InstructionsAdmin(admin.ModelAdmin):
    list_display = ('exam_id','instructions')
admin.site.register(Instructions,InstructionsAdmin)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question','type','exam_id')
admin.site.register(Questions,QuestionsAdmin)


class ExamStatusAdmin(admin.ModelAdmin):
    list_display = ('student','status')
admin.site.register(ExamStatus,ExamStatusAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('student','question')
admin.site.register(Answer,AnswerAdmin)


class OnlineApplyingAdmin(admin.ModelAdmin):
    list_display = ('first_name','phone','course')
admin.site.register(OnlineApplying,OnlineApplyingAdmin)