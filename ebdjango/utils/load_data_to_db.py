from django.core.wsgi import get_wsgi_application
import os
import sys
import pandas as pd

# root django
BASE_DIR = os.path.abspath(os.path.join(__file__, '../..'))

# django route
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebdjango.settings')
application = get_wsgi_application()

# ====================== CODE
from core import models as mod_core

# leer csv
path_file_historicos_mercados = os.path.join(
    BASE_DIR, '../data/csv/data_export/01TablasSQL_historico_mercados.csv')
path_file_historicos_tasas_gen = os.path.join(
    BASE_DIR, '../data/csv/data_export/01TablasSQL_historico_tasas_gen.csv')

data_mercados = pd.read_csv(path_file_historicos_mercados)
for row in data_mercados.itertuples():
  print(row)