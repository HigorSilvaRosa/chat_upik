from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from chat_upik import settings
from core import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^api/create-new-user$', csrf_exempt(views.ApiCreateNewUserView.as_view()), name='api-create-new-user'),
    url(r'^api/create-new-room$', csrf_exempt(views.ApiCreateNewRoomView.as_view()), name='api-create-new-room'),
    url(r'^api/room-list$', csrf_exempt(views.ApiRoomListView.as_view()), name='api-room-list'),
    url(r'^api/send-message$', csrf_exempt(views.ApiSendMessageView.as_view()), name='api-send-message'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
