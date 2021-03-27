# Comandos de referencia I

**tree**: lista elementos utilizando una estructura de árbol

lista carpetas, profundidad 5, evitando archivos y directorios según patrón `tree -d -L 5 -I 'env'`

lista archivos y carpetas, profundidad de 5, evitando archivos y directorios según patrón `tree -L 5 -I '__pycache__|__init__.py'`


**cp**: copiar archivos

copiar carpetas enteras `cp -r carpeta_origen/ carpeta_destino/`


**tar**: comprime archivos

comprimir archivos de una carpeta `tar -czvf empaquetado.tar.gz ~/carpeta_empaquetada/`


**scp**: enviar archivos por utilizando el protocolo scp

copiar archivos del servidor al equipo `scp -i "servidor_testing.pem" ubuntu@aws.com:/home/django/main.tar.gz ~/Documentos/django/backups/`

copiar archivos del equipo al servidor `scp -i "servidor_testing.pem" ~/Documentos/django/backups/main.tar.gz ubuntu@aws.com:/home/django/`


**journalctl**: herramienta para consultar al demonio journal(logs sytemd)

mostrar los logs del último inicio `journalctl -b`

mostrar la lista de reinicios guardados `journalctl --list-boots`

