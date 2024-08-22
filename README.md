# beeware_gate

El objetivo es crear una aplicación usando python para activar un actuador de la puerta.
Para ello se utilizara beeware que permite crear aplicaciones para android y iPhone.


## BeeWare 

En la siguiente página viene muy bien documentado los primeros pasos para crear una app pero
uno de los principales problemas es que no se puede compilar para iPhone sin un macOS.
info: https://docs.beeware.org/en/latest/tutorial/tutorial-1.html

Comandos principales:
Run the app in developer mode
- briefcase dev
Creates application
- briefcase create
Builds application
- briefcase build
Runs application
- briefcase run
Builds installer
- briefcase package

La solución para compilar en en macOS puede ser con Github actions:

## Usar un Servicio de CI/CD en la Nube (como GitHub Actions o CircleCI)

Pasos:

    1. Configurar un repositorio de GitHub con tu proyecto BeeWare.

    2. Configurar un workflow de GitHub Actions:
        Usa un runner de macOS disponible en GitHub Actions para compilar tu aplicación iOS.
        Puedes definir un archivo YAML para que se encargue de la compilación de tu proyecto.

    3. Descargar el artefacto: Después de la compilación, puedes descargar el paquete .ipa (la aplicación iOS) desde la página de GitHub Actions.
