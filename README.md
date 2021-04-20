# Opalo Pruebas

Este repositorio está enfocado a resolver la prueba de selección, de una forma profesional, rápida y bonita. Siempre teniendo las buenas prácticas de autopep8 y una buena arquitectura en los archivos.

## Requisitos
- docker
- docker-compose

## Las reglas
Uno de puntos a resolver en el reto era crear un crud para dos tablas, una de ellas llamada
"tasas_gen" y la otra "mercados". 
La forma en que se resolvió este punto fue usar a "django-rest-framework" que serializara
los modelos y expusiera la api de ambas tablas. Esta api se combino con la clase 
Paginator de django para no saturar el response con miles de datos, lo que permite regresar
bloques que se irán recorriendo como si fueran páginas de un libro.
Por ejemplo: la base de datos tiene 100 registros, si se usa limit=25, se creará un paginator con 4 bloques de 25 registros cada uno. 
Así el performance no se ve afectado. Por default el limit es 15 (se puede cambiar a mas o menos dependiendo cual sea el requerimiento).


API en postman: https://www.getpostman.com/collections/2450e93c4845691181a2

Link al proyecto (instancia ec2 de AWS): [seco-dev.com][link al dominio]

Admin del proyecto: [seco-dev.com/admin][link al dominio admin] ------ {user: opalo, password: opalo123}

La api está estructurada de la siguiente forma:

```bash
- [GET] {{host}}/api/v1/mercados/ => Regresa todos los registros en la base de datos
- [GET] {{host}}/api/v1/tasas-gen/ => Regresa todos los registros en la base de datos
- [DELETE] {{host}}/api/v1/tasas-gen/{{pk}}/ => Regresa el pk del registro eliminado, en otro caso, un error
- [DELETE] {{host}}/api/v1/tasas-gen/{{pk}} => Regresa el pk del registro eliminado, en otro caso, un error
```

Una variante a los GET anteriores es usar la variable limit:

```bash
- [GET] {{host}}/api/v1/mercados/?limit=2 => Regresa bloques de 2 registros cada uno
- [GET] {{host}}/api/v1/tasas-gen/?limit=60 => Regresa bloques de 60 registros cada uno
```

Los siguientes endpoints reciben los mismos parámetros de entrada y el único campo obligatorio para crear un registro es la "fecha". 
Todos los demás son opcionales y se setearan en "null" como dato inicial.


```bash
- [POST] {{host}}/api/v1/mercados/
- [PUT] {{host}}/api/v1/mercados/{{pk}}/

- [POST] {{host}}/api/v1/tasas-gen/
- [PUT] {{host}}/api/v1/tasas-gen/{{pk}}/
```

Ejemplo sencillo de las variable del post y el response que regresa en la tabla mercados:
```json
{
    "fecha": "2021-04-21",
    "tesoros_30_y": 123.456,
    "us_tips_7y": 12.345,
    "colombia_1_y": 1234.5678
}
```

Response:
```json
{
    "id": 9,
    "created": "2021-04-20T07:01:30.049982Z",
    "modified": "2021-04-20T07:01:30.050011Z",
    "fecha": "2021-04-21",
    "pk_control": null,
    "us_2y": null,
    "tesoros_3_y": null,
    "tesoros_5_y": null,
    "tesoros_7_y": null,
    "us_10y": null,
    "tesoros_30_y": "123.45600",
    "us_tips_5y": null,
    "us_tips_7y": "12.34500",
    "us_tips_10y": null,
    "us_tips_20y": null,
    "us_tips_30y": null,
    "german_10y": null,
    "german_2y": null,
    "colombia_10_y": null,
    "colombia_1_y": "1234.56780",
    "deuda_internacional_d_soberanos": null,
    "deuda_internacional_d_crédito": null,
    "d_intl_soberanos": null,
    "d_intl_credito": null,
    "acciones_colombia": null,
    "us_sp_500": null,
    "euro_stoxx_50": null,
    "acciones_intl_asia": null,
    "global_oh": null,
    "acciones_emergentes": null,
    "mex_cds_usd_sr_5y_d14_corp": null,
    "brazil_cds_usd_sr_5y_d14_corp": null,
    "colom_cds_usd_sr_5y_d14_corp": null,
    "chile_cds_usd_sr_5y_d14_corp": null,
    "wti": null,
    "laci_index": null,
    "clp_regn_curncy": null,
    "pen_curncy": null,
    "dxy": null,
    "euro": null,
    "cad": null,
    "nok": null,
    "rub": null,
    "mxn_curncy": null,
    "brl_curncy": null,
    "vix_index": null,
    "emerging_markets_currency": null,
    "gold": null,
    "italy_10y": null,
    "italy_2y": null,
    "france_10y": null,
    "france_2y": null,
    "us_federal_funds_effective_rat": null,
    "us_generic_govt_1_month_yield": null,
    "us_3m": null,
    "us_generic_govt_6_month_yield": null,
    "us_generic_govt_12_month_yield": null,
    "us_generic_govt_2_year_yield": null,
    "usd_libor_3m": null,
    "german_3m": null,
    "german_treasury_bill_6m": null,
    "german_government_bills_1_yr": null,
    "ftse_mib": null,
    "expectativa": false,
    "liquidez_local": null
}
```

Como adicional se creó un endpoint en la raíz del proyecto que permite hacer "cargas masivas". 
Es un formulario en html, con poco css y jquery para que el usuario ingrese un archivo csv, la tabla donde se 
guardará la información y un campo opcional llamado "campo umbral".
El objetivo de este endpoint es que el usuario pueda agregar/modificar grandes cantidades 
de registros sin necesidad de ir uno por uno usando la api.



## Uso

### Local
Al ser un proyecto "dockerizado" basta con ejecutar el comando:
``` bash
docker-compose -f local.yml up --build
```

Esto inicializa todos los servicios correspondientes y abrirá a django
en el puerto 8002. Puerto en el cual se podrá jugar con la api y el "cargado masivo".


### Producción

Se tiene que contar con un dominio propio porque se tiene que configurar los DNS
para que dos registros de tipo A (www y *) apunten a la ip publica del servidor.

Y después de tener los registros creados basta con correr:

``` bash
docker-compose -f production.yml up --build
```

## Reto #2
Reto de programación con uso de dataframes, la solución está en:

```py
python prueba2/main.py
```
[link al dominio]: https://seco-dev.com/
[link al dominio admin]: https://seco-dev.com/admin
