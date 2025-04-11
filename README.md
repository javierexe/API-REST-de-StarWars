
# Star Wars Blog API

Esta es una API RESTful desarrollada con Flask y SQLAlchemy que simula el backend de un blog inspirado en Star Wars. Permite consultar personajes, planetas y vehículos, además de gestionar usuarios y sus favoritos.

## 🚀 Tecnologías utilizadas

- Python 3
- Flask
- SQLAlchemy
- Flask-Migrate
- PostgreSQL (o SQLite para pruebas)
- Flask-Admin

## 🧠 Funcionalidades principales

- Consultar personajes, planetas y vehículos
- Consultar detalle de cada entidad
- Gestionar usuarios
- Agregar y eliminar favoritos por usuario

## 📦 Instalación y uso

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/starwars-blog-api.git
cd starwars-blog-api
```

2. Instalar dependencias:

```bash
pipenv install
pipenv shell
```

3. Configurar base de datos en `.env` (opcional, usa SQLite por defecto).

4. Crear y aplicar migraciones:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Ejecutar la app:

```bash
python src/app.py
```



## 📡 Endpoints disponibles

| Método | Ruta                              | Descripción                           |
|--------|-----------------------------------|---------------------------------------|
| GET    | `/people`                         | Listar personajes                     |
| GET    | `/people/<id>`                    | Detalle de personaje                  |
| GET    | `/planets`                        | Listar planetas                       |
| GET    | `/planets/<id>`                   | Detalle de planeta                    |
| GET    | `/vehicles`                       | Listar vehículos                      |
| GET    | `/vehicles/<id>`                  | Detalle de vehículo                   |
| GET    | `/users`                          | Listar usuarios                       |
| GET    | `/users/favorites?user_id=1`      | Favoritos del usuario                 |
| POST   | `/favorite/planet/<id>?user_id=1` | Agregar planeta favorito              |
| POST   | `/favorite/people/<id>?user_id=1` | Agregar personaje favorito            |
| DELETE | `/favorite/planet/<id>?user_id=1` | Eliminar planeta favorito             |
| DELETE | `/favorite/people/<id>?user_id=1` | Eliminar personaje favorito           |

## 🧑‍💻 Autor

- javierexe, Ing. Agrónomo | Científico de Datos | Desarrollador Fullstack  
- Proyecto desarrollado como parte del curso de 4Geeks Academy

---

¡Que la fuerza te acompañe! 😝
