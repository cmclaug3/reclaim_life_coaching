from django.contrib import admin
from member.models import Member, Space, MemberSpace


admin.site.register(Member)
admin.site.register(Space)
admin.site.register(MemberSpace)
