from django.http.response import JsonResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import View
from omnibus.api import publish

from core.models import ChatUser, ChatRoom, ChatMessage


class HomeView(View):
    template = "chat_upik/home.html"
    def get(self, request, *args, **kwargs):
        return render_to_response(self.template, {}, RequestContext(request))

class ApiCreateNewUserView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name");
        chat_user = ChatUser()
        chat_user.name = name
        chat_user.save()

        return JsonResponse(chat_user.to_dict())

class ApiCreateNewRoomView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name");
        chat_room = ChatRoom()
        chat_room.name = name
        chat_room.save()
        return JsonResponse(chat_room.to_dict())

class ApiRoomListView(View):
    def get(self, request, *args, **kwargs):
        rooms = ChatRoom.objects.all().order_by("-creation_date")
        rooms_list = [];

        for room in rooms:
            rooms_list.append(room.to_dict())

        print(rooms_list);

        return JsonResponse(rooms_list, safe=False)

class ApiSendMessageView(View):
    def post(self, request, *args, **kwargs):
        chat_user_id = request.POST.get("user_id");
        chat_room_id = request.POST.get("room_id");
        message = request.POST.get("message");

        chat_message = ChatMessage()

        chat_message.chat_user_id = int(chat_user_id);
        chat_message.chat_room_id = int(chat_room_id);
        chat_message.message = message
        chat_message.save()

        publish(
            'chat',
            'message',
            chat_message.to_dict(),
            sender=None
        )

        return JsonResponse(chat_message.to_dict(), safe=False)