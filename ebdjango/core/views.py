from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.conf import settings

from core import serializers as ser_core
from core import models as mod_core
from utils import MasiveLoader as ml

APPS_DIR = settings.APPS_DIR


def home(request, TEMPLATE='home.html'):
    return render(request, TEMPLATE)


class MasiveLoad(APIView):
    def post(self, request):
        print(request.data)
        table = request.data.get('table', '')
        file_csv = request.data.get('fileCsv', '')
        field_umbral = request.data.get('umbral', '')

        if not (table and file_csv):
            return return_response_error('Parametros invalidos')

        if table not in ['mercado', 'tasagen']:
            return return_response_error('Tabla invalida')

        obj = mod_core.create_file_obj(file_csv)
        file_url = "{}{}".format(APPS_DIR, obj.file.url)
        print('FILE URL', file_url)

        target_field = 'pk_control'
        if field_umbral:
            target_field = field_umbral

        try:
            if table == 'mercado':
                ml_market = ml.MasiveLoader(mod_core.Market)
                ml_market.insert_or_update_marker(file_url, target_field)
            else:
                ml_rategen = ml.MasiveLoader(mod_core.RateGen)
                ml_rategen.insert_or_update_rate_gen(file_url, target_field)
        except Exception as e:
            return return_response_error(str(e))

        return Response({'error': ''}, status=status.HTTP_200_OK)


class MarketViewSet(viewsets.ModelViewSet):
    queryset = mod_core.Market.objects.all()
    serializer_class = ser_core.MarketModelSerializer


class RateGenViewSet(viewsets.ModelViewSet):
    queryset = mod_core.RateGen.objects.all()
    serializer_class = ser_core.RateGenModelSerializer


def return_response_error(error):
    print(error)
    return Response(
        {'error': error},
        status=status.HTTP_412_PRECONDITION_FAILED
    )
