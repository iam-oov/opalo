from django.db import models

from utils.models import CustomBaseModel


class Market(CustomBaseModel):
    class Meta:
        verbose_name = 'Mercado'
        verbose_name_plural = 'Mercados'

    fecha = models.DateField(
        verbose_name='Fecha'
    )
    pk_control = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    us_2y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    tesoros_3_y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    tesoros_5_y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    tesoros_7_y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_10y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    tesoros_30_y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_tips_5y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_tips_7y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_tips_10y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_tips_20y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_tips_30y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    german_10y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    german_2y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    colombia_10_y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    colombia_1_y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    deuda_internacional_d_soberanos = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    deuda_internacional_d_crédito = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    d_intl_soberanos = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    d_intl_credito = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    acciones_colombia = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_sp_500 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    euro_stoxx_50 = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    acciones_intl_asia = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    global_oh = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    acciones_emergentes = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    mex_cds_usd_sr_5y_d14_corp = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    brazil_cds_usd_sr_5y_d14_corp = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    colom_cds_usd_sr_5y_d14_corp = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    chile_cds_usd_sr_5y_d14_corp = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    wti = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    laci_index = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    clp_regn_curncy = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    pen_curncy = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    dxy = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    euro = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    cad = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    nok = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    rub = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    mxn_curncy = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    brl_curncy = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    vix_index = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    emerging_markets_currency = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    gold = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    italy_10y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    italy_2y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    france_10y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    france_2y = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_federal_funds_effective_rat = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_generic_govt_1_month_yield = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_3m = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_generic_govt_6_month_yield = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_generic_govt_12_month_yield = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    us_generic_govt_2_year_yield = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    usd_libor_3m = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    german_3m = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    german_treasury_bill_6m = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    german_government_bills_1_yr = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    ftse_mib = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    expectativa = models.BooleanField(default=False, blank=True, null=True)
    liquidez_local = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)

    def __str__(self):
        return f'{str(self.pk)} - {self.fecha}'

    def to_dict(self):
        return {
            'hola': self.fecha
        }


class RateGen(CustomBaseModel):
    class Meta:
        verbose_name = 'Tasa Geb'
        verbose_name_plural = 'Tasas Gen'

    id_historico_tasas_gen = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    fecha = models.DateField(
        verbose_name='Fecha'
    )
    tasa = models.DecimalField(
        max_digits=24, decimal_places=16, blank=True, null=True)
    nodo = models.CharField(
        max_length=55,
        blank=True,
        null=True,
    )
    curva = models.CharField(
        max_length=55,
        blank=True,
        null=True,
    )
    expectativa = models.BooleanField(default=False, blank=True, null=True)
    precio = models.DecimalField(
        max_digits=24, decimal_places=16, blank=True, null=True)
    duracion = models.CharField(
        max_length=55,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{str(self.pk)} - {self.fecha}'

    def to_dict(self):
        return {
            'pk': self.pk,
            'tasa': self.tasa
        }


def create_or_update_market(pk_control, date, **kwargs):
    if pk_control:
        obj = get_market_pk_control(pk_control)
        # if object exists: update it
        if obj:
            obj = update_market(obj, fecha=date, **kwargs)
        else:
            obj = create_market(pk_control, fecha=date, **kwargs)
    else:
        # create direct
        obj = create_market(pk_control, fecha=date, **kwargs)
    return obj


def create_market(pk_control, **kwargs):
    obj = Market(
        pk_control=pk_control,
        fecha=kwargs.get('fecha')
    )
    for key, value in kwargs.items():
        setattr(obj, key, value)
    obj.save()
    return obj


def update_market(obj, **kwargs):
    for key, value in kwargs.items():
        setattr(obj, key, value)
    obj.save()
    return obj


def get_market_pk_control(pk_control):
    try:
        obj = Market.objects.get(
            pk_control=pk_control
        )
    except Exception as e:
        obj = None
    return obj
