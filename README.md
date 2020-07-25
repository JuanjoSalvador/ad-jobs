# Andalucia Developers: Jobs

> El proyecto Andalucia Developers: Jobs nace a raíz la comunidad homónima, y pretende servir a modo de tablón de anuncios para ofertas de trabajo que los miembros del grupo publican, de forma que no queden enterradas en mensajes y cualquiera puede consultarlas.

En desarrollo, pero puede verse el avance actual desde [Heroku](https://ad-jobs.herokuapp.com/).

![Captura de pantalla de Andalucia Developers: Jobs, en Heroku](https://pbs.twimg.com/media/EdtUgrHWoAMhKFv?format=png&name=large)

## Desarrollo

### Virtualenv

1. Creamos el entorno virtual y lo activamos

#### Linux
```shell
$ virtualenv env -p python3
$ source ./env/bin/activate
```

#### Windows (PowerShell)
```powershell
PS virtualenv env -p python3
PS env/Scripts/activate.ps1
```

2. Instalamos las dependencias

```shell
$ pip install -r requirements.txt
```

3. Ejecutamos el servidor de desarrollo (liveserver) de Flask

#### Linux

```shell
$ ./run.sh
```

#### Windows (PowerShell)
```powershell
PS .\run.ps1
```

La salida tendría que ser algo como esto: 

```
 * Serving Flask app "main.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Docker
Pendiente.

## Tests

Para ejecutar los tests definidos actualmente, asegúrate de tener instalado `pytest` y `pytest-flask` primero.

A continuación solo hay que lanzarlos con

```bash
$ py.test
```