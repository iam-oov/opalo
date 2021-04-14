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
    DJANGO_DIR, '../data/csv/02datos_actualizar_historicos_mercado.csv'))

df = pd.read_csv(path_file)

# ======================
# ====================== TRATAMIENTO DE DATOS
# ======================
df = strings.clean_dataframe(df)

for row in df.itertuples():
    obj = mod_core.create_or_update_obj(
        mod_core.Market,
        row.fecha,
        row.fecha,
        search_by='fecha',
        us_2y=strings.convert_float(row.us_2y),
        tesoros_3_y=strings.convert_float(row.tesoros_3_y),
        tesoros_5_y=strings.convert_float(row.tesoros_5_y),
        tesoros_7_y=strings.convert_float(row.tesoros_7_y),
        us_10y=strings.convert_float(row.us_10y),
        tesoros_30_y=strings.convert_float(row.tesoros_30_y),
        us_tips_5y=strings.convert_float(row.us_tips_5y),
        us_tips_7y=strings.convert_float(row.us_tips_7y),
        us_tips_10y=strings.convert_float(row.us_tips_10y),
        us_tips_20y=strings.convert_float(row.us_tips_20y),
        us_tips_30y=strings.convert_float(row.us_tips_30y),
        german_10y=strings.convert_float(row.german_10y),
        german_2y=strings.convert_float(row.german_2y),
        colombia_10_y=strings.convert_float(row.colombia_10_y),
        colombia_1_y=strings.convert_float(row.colombia_1_y),
        deuda_internacional_d_soberanos=strings.convert_float(row.deuda_internacional_d_soberanos),
        deuda_internacional_d_crédito=strings.convert_float(row.deuda_internacional_d_crédito),
        d_intl_soberanos=strings.convert_float(row.d_intl_soberanos),
        d_intl_credito=strings.convert_float(row.d_intl_credito),
        acciones_colombia=strings.convert_float(row.acciones_colombia),
        us_sp_500=strings.convert_float(row.us_sp_500),
        euro_stoxx_50=strings.convert_float(row.euro_stoxx_50),
        acciones_intl_asia=strings.convert_float(row.acciones_intl_asia),
        global_oh=strings.convert_float(row.global_oh),
        acciones_emergentes=strings.convert_float(row.acciones_emergentes),
        mex_cds_usd_sr_5y_d14_corp=strings.convert_float(row.mex_cds_usd_sr_5y_d14_corp),
        brazil_cds_usd_sr_5y_d14_corp=strings.convert_float(row.brazil_cds_usd_sr_5y_d14_corp),
        colom_cds_usd_sr_5y_d14_corp=strings.convert_float(row.colom_cds_usd_sr_5y_d14_corp),
        chile_cds_usd_sr_5y_d14_corp=strings.convert_float(row.chile_cds_usd_sr_5y_d14_corp),
        wti=strings.convert_float(row.wti),
        laci_index=strings.convert_float(row.laci_index),
        clp_regn_curncy=strings.convert_float(row.clp_regn_curncy),
        pen_curncy=strings.convert_float(row.pen_curncy),
        dxy=strings.convert_float(row.dxy),
        euro=strings.convert_float(row.euro),
        cad=strings.convert_float(row.cad),
        nok=strings.convert_float(row.nok),
        rub=strings.convert_float(row.rub),
        mxn_curncy=strings.convert_float(row.mxn_curncy),
        brl_curncy=strings.convert_float(row.brl_curncy),
        vix_index=strings.convert_float(row.vix_index),
        emerging_markets_currency=strings.convert_float(row.emerging_markets_currency),
        gold=strings.convert_float(row.gold),
        italy_10y=strings.convert_float(row.italy_10y),
        italy_2y=strings.convert_float(row.italy_2y),
        france_10y=strings.convert_float(row.france_10y),
        france_2y=strings.convert_float(row.france_2y),
        us_federal_funds_effective_rat=strings.convert_float(row.us_federal_funds_effective_rat),
        us_generic_govt_1_month_yield=strings.convert_float(row.us_generic_govt_1_month_yield),
        us_3m=strings.convert_float(row.us_3m),
        us_generic_govt_6_month_yield=strings.convert_float(row.us_generic_govt_6_month_yield),
        us_generic_govt_12_month_yield=strings.convert_float(row.us_generic_govt_12_month_yield),
        us_generic_govt_2_year_yield=strings.convert_float(row.us_generic_govt_2_year_yield),
        usd_libor_3m=strings.convert_float(row.usd_libor_3m),
        german_3m=strings.convert_float(row.german_3m),
        german_treasury_bill_6m=strings.convert_float(row.german_treasury_bill_6m),
        german_government_bills_1_yr=strings.convert_float(row.german_government_bills_1_yr),
        ftse_mib=strings.convert_float(row.ftse_mib),
        expectativa=strings.convert_bool(str(row.expectativa).replace('"', '').lower()),
        liquidez_local=strings.convert_float(row.liquidez_local),
    )
