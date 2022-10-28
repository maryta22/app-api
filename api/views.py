from django.views import View
from .models import Client, User
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
class ClientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, email = "default"):
        clients = list(Client.objects.values())
        if len(clients)>0:
            for client in clients:
                info = User.objects.get(id = client["id_user_id"])
                client["name"] = info.name
                client["lastname"] = info.lastname
                client["email"] = info.email
                client["password"] = info.password
                client["phone"] = info.phone
                client["gender"] = info.gender
                client["date_of_birthday"] = info.date_of_birthday
                client["state"] = info.state
                client["user"] = info.user
                client["date_register"] = info.date_register
                client["date_modify"] = info.date_modify
                client["longitude_home"] = info.longitude_home
                client["latitude_home"] = info.latitude_home

            if email != "default" :
                client = clients.filter(email = email)
                datos = {'cliente':client}
            else:
                datos = {'clientes':clients}
        else:
            datos = {'mensaje':'No se han encontrado clientes'}

        return JsonResponse(datos)

    def post(self, request):
        try:
            data = json.loads(request.body)
            newuser = User.objects.create(
                name = data["name"],
                lastname = data["lastname"],
                email = data["email"],
                password = data["password"],
                phone = data["phone"],
                gender = data["gender"],
                date_of_birthday = data["date_of_birthday"],
                state = data["state"],
                user = data["user"],
                date_register = data["date_register"],
                date_modify = data["date_modify"],
                longitude_home = data["longitude_home"],
                latitude_home = data["latitude_home"],
            )

            Client.objects.create(
                id_user = newuser,
                date_start = data["date_start"]
            )

            response = {'mensaje':'Exito'}

        except:
            response = {'mensaje':'Esta mal el formato enviado' }

        return JsonResponse(response)


    def put(self, request):
        pass

    def delete(self, request):
        pass
