# Prueba Lilab
Sistema desarrollado principalmente con Python, Django y REST Framework para el manejo de solicitudes de aprobación de créditos.

## Instalación

* Verifica que tengas instalado docker y docker-compose
* Pega el archivo .env en la raíz del directorio
* Ejecuta el comando:
```sudo docker-compose build```

* Aplica las migraciones:
```sudo docker-compose run --rm web python3 manage.py migrate```

* Crea un super usuario con el comando:
```sudo docker-compose run --rm web python3 manage.py createsuperuser```

## Uso
* Para correr la aplicación usa el comando:
```sudo docker-compose up```
