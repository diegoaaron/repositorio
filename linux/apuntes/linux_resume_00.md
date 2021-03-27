# Comandos de referencia I

**tree**: lista elementos utilizando una estructura de arbol

lista carpetas con una profundidad de 5 y evitando el directorio 'env' `tree -d -L 5 -I env`

**cp**: copiar archivos

copiar carpetas enteras `cp -r carpeta_origen/ carpeta_destino/`

**tar**: comprime archivos

comprimir archivos de una carpeta `tar -czvf empaquetado.tar.gz /carpeta/a/empaquetar/`

# copiar archivos del servidor hacia el equipo
scp -i "servidor_testing.pem" ubuntu@compute-1.amazonaws.com:/home/ubuntu/django/prj_dj_uno_bk2/prj_dj_uno.tar.gz /home/diego/Documentos/django/prj_dj_uno_bk2/prj_dj_uno.tar.gz

# copiar archivos del equipo al servidor
scp -i "servidor_testing.pem" /home/diego/Documentos/django/prj_dj_uno_bk/prj_dj_uno_1update.tar.gz ubuntu@compute-1.amazonaws.com:/home/ubuntu/django/

# mostrar los logs del último inicio
journalctl -b

# mostrar la lista de reinicios guardados
journalctl --list-boots
# 

