from django.core.wsgi import get_wsgi_application
import os
import sys
import pandas as pd

# root django
DJANGO_DIR = os.path.abspath(os.path.join(__file__, '../..'))

# django route
sys.path.append(DJANGO_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebdjango.settings')
application = get_wsgi_application()

# ======================
# ====================== CODE
# ======================
from core import models as mod_core
from utils import strings


# leer csv
path_file = os.path.abspath(os.path.join(
    DJANGO_DIR, '../data/csv/02datos_actualizar_tasas_gen.csv'))

df = pd.read_csv(path_file)

# ======================
# ====================== TRATAMIENTO DE DATOS
# ======================
df = strings.clean_dataframe(df)

for row in df.itertuples():
    obj = mod_core.create_or_update_obj(
        mod_core.RateGen,
        row.id_historico_tasas_gen,
        row.fecha,
        search_by='id_historico_tasas_gen',
        tasa=row.tasa,
        nodo=row.nodo,
        curva=row.curva,
        expectativa=row.expectativa,
        precio=row.precio,
        duracion=row.duracion,
    )
