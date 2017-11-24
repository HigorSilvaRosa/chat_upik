from django.db import models


class ChatUser(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=50)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    class Meta:
        verbose_name = "Usuário do bate-papo"
        verbose_name_plural = "Usuários do bate-papo"


class ChatRoom(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=50)
    creation_date = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name="Data de modificação", auto_now=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    class Meta:
        verbose_name = "Sala do bate-papo"
        verbose_name_plural = "Salas do bate-papo"


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, verbose_name="Sala")
    chat_user = models.ForeignKey(ChatUser, verbose_name="Chat")
    message = models.TextField(verbose_name="Mensagem")

    creation_date = models.DateTimeField(verbose_name="Data de criação", auto_now_add=True)
    modification_date = models.DateTimeField(verbose_name="Data de modificação", auto_now=True)

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "chat_room": self.chat_room.to_dict(),
            "chat_user": self.chat_user.to_dict(),
        }

    class Meta:
        verbose_name = "Mensagem do bate-papo"
        verbose_name_plural = "Mensagens do bate-papo"