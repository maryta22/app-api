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

    def get(self, request):
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
            datos = {'cliente':clients}
        else:
            datos = {'mensaje':'No se han encontrado clientes'}
        return JsonResponse(datos)

    def post(self, request):
        try:
            data = json.loads(request.body)
            reponse = {'mensaje':'Exito'}
        except:
            reponse = {'mensaje':'Está mal el formato enviado'}
        return JsonResponse(reponse)

    def put(self, request):
        pass

    def delete(self, request):
        pass
