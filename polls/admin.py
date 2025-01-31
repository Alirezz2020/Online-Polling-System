from django.contrib import admin


from polls.models import *


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
