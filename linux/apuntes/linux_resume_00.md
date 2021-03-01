## Comandos de referencia



# ver la fecha y hora
date

# copiar carpetas enteras
cp -r carpeta_origen/ carpeta_destino/

# comprimir archivos
tar -czvf empaquetado.tar.gz /carpeta/a/empaquetar/ 

# copiar archivos del servidor hacia el equipo
scp -i "servidor_testing.pem" ubuntu@compute-1.amazonaws.com:/home/ubuntu/django/prj_dj_uno_bk2/prj_dj_uno.tar.gz /home/diego/Documentos/django/prj_dj_uno_bk2/prj_dj_uno.tar.gz

# copiar archivos del equipo al servidor
scp -i "servidor_testing.pem" /home/diego/Documentos/django/prj_dj_uno_bk/prj_dj_uno_1update.tar.gz ubuntu@compute-1.amazonaws.com:/home/ubuntu/django/

# mostrar los logs del último inicio
journalctl -b

# mostrar la lista de reinicios guardados
journalctl --list-boots
# 





#### Primera explicación 



## Artículos y guías