from django.contrib import admin
from site.models import Topic


admin.autodiscover()


class TopicAdmin(admin.ModelAdmin):
    class Meta:
        model = Topic

admin.site.register(Topic, TopicAdmin)

admin.autodiscover()
