import pandas as pd

nombres = ["nicolas", "samuel", "mario", "andrres", "camilo"]
estatura = [1.70, 1.72,  1.75,  1.90,  1.68]
peso = [67, 69,  72,  87,  65]
senal_1 = [False, True, True, True, False]
senal_2 = [True, True, False, True, True]

# 1) con los datos anteriorres
#    construya  dicicionarios con la estructura:
#    {nombre: estatrura}
#    {nombre: peso}
#    {nombre: senal_1}
#    {nombre: senal_2}
dict_people = []
for i in range(len(nombres)):
    dict_people.append(
        {
            'name': nombres[i],
            'height': estatura[i],
            'weight': peso[i],
            'signal_1': senal_1[i],
            'signal_2': senal_2[i],
        }
    )
print(f'{"-"*20} 1) \n {dict_people} \n {"-"*20} \n\n')


# 2) construya una funcion en la que se retorne un dicionario
#    con {nombre: IMC} donde:
#    (IMC) indice de masa corporal = peso dividido la estatura
#    al cuadrado
def calculate_imc(height, weight, decimal_points=2):
    return round(weight / (height**2), decimal_points)


for person in dict_people:
    imc = calculate_imc(person['height'], person['weight'])
    person['imc'] = imc
print(f'{"-"*20} 2) \n {dict_people} \n {"-"*20} \n\n')


# 3) con los resultados construlla un df con las
# columnas "nombre" "estatura"  "peso"  "imc"   señal_1 señal_2
df = pd.DataFrame.from_records([person for person in dict_people])
print(f'{"-"*20} 3) \n {df} \n {"-"*20} \n\n')


# 4) construya una funcion que recorra el dataframe
#    y retorne el resultado de multiplicar
#    el "imd" por raiz cuadrada de la "estatura",
#    donde para la la señal_1 ==  True y para la señal_2 sea == False
#    para lo de mas retorne 0
# 5) inserte los resultado del recorridode la
#  funcion en una columna nueva del dataframe con el nombre de "resultado"
def calculate_imc2(imc, height, decimal_points=2):
    return round(imc * (height**0.5), decimal_points)


results = []
for row in df.itertuples():
    imc2 = 0
    if row.signal_1 and not row.signal_2:
        imc2 = calculate_imc2(row.imc, row.height)
    results.append(imc2)

df['resultado'] = results
print(f'{"-"*20} 4-5) \n {df} \n {"-"*20} \n\n')


# 6) separe en un nuevo dataframe los datos de "camilo y de nicolas"
filtered_df = df[df.name.isin(['camilo', 'nicolas'])]
print(f'{"-"*20} 6) \n {filtered_df} \n {"-"*20} \n\n')
