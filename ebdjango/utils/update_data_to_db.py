from django.core.wsgi import get_wsgi_application
import os
import sys
import environ

# root django
DJANGO_DIR = os.path.abspath(os.path.join(__file__, '../../..'))
print(DJANGO_DIR)
# ROOT_DIR = environ.Path(__file__) - 3
# APPS_DIR = ROOT_DIR.path('ebdjango')

# print(APPS_DIR)

# django route
sys.path.append(DJANGO_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

# # ======================
# # ====================== CODE
# # ======================
from core import models as mod_core
import MasiveLoader as ml

ml_market = ml.MasiveLoader(mod_core.Market)
ml_rategen = ml.MasiveLoader(mod_core.RateGen)

# # ======================
# # ====================== (1) insert initial data
# # ======================
# # ======================== (1.1) markets
path_file = os.path.abspath(os.path.join(
    DJANGO_DIR, '../data/csv/02datos_actualizar_mercado.csv'))
ml_market.insert_or_update_marker(path_file, 'fecha')

# # ======================== (1.2) rate_gen
path_file = os.path.abspath(os.path.join(
    DJANGO_DIR, '../data/csv/02datos_actualizar_tasas_gen.csv'))
ml_rategen.insert_or_update_rate_gen(path_file, 'id_historico_tasas_gen')
