# Página web - Marilin Amaya Asesoria Psicologica

## Archivos incluidos

- `app.py`: página web principal.
- `requirements.txt`: dependencias para desplegar en Streamlit Community Cloud.
- `.streamlit/config.toml`: configuración visual del tema.
- `assets/logo_marilin_amaya.png`: logo del negocio.
- `assets/portada_marilin_amaya.png`: portada del negocio.

## Cómo probar en tu computadora

1. Instalar Python 3.10 o superior.
2. Abrir una terminal dentro de esta carpeta.
3. Ejecutar:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Cómo publicarlo gratis en Streamlit Community Cloud

1. Crear una cuenta en GitHub.
2. Crear un repositorio nuevo, por ejemplo: `marilin-amaya-psicologia`.
3. Subir todos estos archivos al repositorio.
4. Entrar a Streamlit Community Cloud.
5. Elegir el repositorio, la rama principal y el archivo `app.py`.
6. Presionar **Deploy**.
7. Opcionalmente configurar el subdominio, por ejemplo: `marilin-amaya-psicologia.streamlit.app`.

## Datos que puedes personalizar en `app.py`

Busca estas variables al inicio del archivo:

```python
BUSINESS_NAME = "Marilin Amaya"
PROFESSION = "Psicóloga"
PHONE_DISPLAY = "+51 934 386 532"
PHONE_WHATSAPP = "51934386532"
INSTAGRAM_URL = "https://www.instagram.com/psico._marilin?igsh=MXF0dnlrdHpob25yaA=="
```

Reemplaza Instagram y Facebook por los enlaces reales cuando estén disponibles.

## Recomendación profesional

Agregar el número de colegiatura y condición de habilitación profesional si corresponde. Evitar recibir historias clínicas o información altamente sensible por formularios públicos.
