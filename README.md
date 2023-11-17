# Elecciones 2023

## Enunciado

- En el archivo de `models.py` vas a encontrarte con dos modelos: **PoliticalParties** y **Voters**
- En el archivo de `utils.py` vas a encontrarte dos funciones:
  - **has_voted**
  - **has_voted_percentage**
- Contexto:
  - Este sistema contempla la votaciones para **balotaje**
  - El sitio de ejemplo de votaciones generales: [elecciones 2023](https://resultados.gob.ar/elecciones/1/0/1/-1/-1#agrupaciones)
  - Reglas que podrias tener que utilizar: [clases-de-votos](https://www.argentina.gob.ar/dine/clases-de-votos)
- Requisitos:
  - Pagina para votación
    - Se ingresa el documento y en segun si ya voto o no:
      - si no voto, puede votar las opciones posibles
      - si ya voto, no puede votar
  - Pagina adminsitracion (con permiso) para realizar el cierre de la votación
    - Boton de cierre
    - Confirmacion
    - Muestra de resultados y ganador
  - Pagina de resultados (publica)
    - en caso de no estar cerrada la votación, muestra el % de votantes que ya votaron y el total de votantes
    - en caso de ya cerrada la votación, muestra los resultados y ganador
  - **Se espera poder tener la información suficiente para en caso de necesitarse se pueda obtener el % de votos a favor de cada partido en determinada zona**

## Requisitos previos

### Python

Version 3.11

#### Instalar dependencias de python

```bash
poetry install
```

#### Iniciar el entorno virtual

```bash
poetry shell
```

#### Migrations

```bash
cd ballot

python manage.py migrate
```

#### Carga de datos inicial

```bash
python manage.py load_test_data
```

#### Crear un superuser

```bash
python manage.py createsuperuser
```

#### Iniciar servidor

```bash
python manage.py runserver
```

## Entorno de proyecto

### Herramientas utilizadas

- blue
- flake8
- pre-commit
- pytest

### pre-commit

#### Instalar pre-commit

```bash
pre-commit install
```

## Entorno de testing

### Ejecutar los tests

```bash
pytest ballot
```
