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
    DJANGO_DIR, '../data/csv/01TablasSQL_historico_tasas_gen.csv'))

df = pd.read_csv(path_file)

# ======================
# ====================== TRATAMIENTO DE DATOS
# ======================

# replace spaces with underscore in names columns
df.columns = df.columns.str.replace(' ','_')

# lowercase in names columns
df.columns = df.columns.str.lower()

# rename - the word 'global' conflicts with the reserved words
df = df.rename({'global': 'global_oh'}, axis=1)
df = df.replace(to_replace={'[NULL]': 0})
df = df.fillna(0)


for row in df.itertuples():
    obj = mod_core.create_or_update_obj(
        mod_core.RateGen,
        row.pk_control,
        row.fecha,
        id_historico_tasas_gen=row.id_historico_tasas_gen,
        tasa=strings.convert_float(row.tasa),
        nodo=row.nodo,
        curva=row.curva,
        expectativa=strings.convert_bool(row.expectativa),
        precio=strings.convert_float(row.precio),
        duracion=row.duracion,
    )
