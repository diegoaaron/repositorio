# ver la fecha y hora
date

# copiar carpetas enteras
cp -r carpeta_origen/ carpeta_destino/

# comprimir archivos
tar -czvf empaquetado.tar.gz /carpeta/a/empaquetar/ 

# copiar archivos del servidor hacia el equipo
scp -i "servidor_testing.pem" ubuntu@ec2-35-173-247-127.compute-1.amazonaws.com:/home/ubuntu/django/prj_dj_uno_bk2/prj_dj_uno.tar.gz /home/diego/Documentos/django/prj_dj_uno_bk2/prj_dj_uno.tar.gz

# copiar archivos del equipo al servidor
scp -i "servidor_testing.pem" /home/diego/Documentos/django/prj_dj_uno_bk/prj_dj_uno_1update.tar.gz ubuntu@ec2-35-173-247-127.compute-1.amazonaws.com:/home/ubuntu/django/

# mostrar los logs del último inicio
journalctl -b

# mostrar la lista de reinicios guardados
journalctl --list-boots
# 

------------------------------------------------------------------------------------------------------------------------------------------------
Documentos y guías ya revisadas

# Explicación sobre el comando eval
https://www.ediciones-eni.com/open/mediabook.aspx?idR=30685667a4a8c4fa17440d77e57a0694

# Explicación sobre el funcionamiento de ssh-keygen, ssh-agent y ssh-add 
http://rabexc.org/posts/using-ssh-agent

# Explicación sobre las diferentes arquitecturas de PC
https://www.thinkinvirtual.com/2017/03/diferencias-entre-i386-x86-x64-amd64-e.html

# Configuración básica para conectarse a instancia EC2
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

# Agregar directorio al PATH
https://www.howtogeek.com/658904/how-to-add-a-directory-to-your-path-in-linux/

# Grupos y usuarios linux
https://www.solvetic.com/tutoriales/article/4943-como-anadir-usuario-grupo-o-grupo-secundario-linux/

# Solución de driver de wifi en laptop asus
https://www.youtube.com/watch?v=EZ85K7VrRUo&lc=UgwfBi4cuA0zdTzPkyt4AaABAg.9GTQKB4g29j9GTSAEIrV8X

# Resolver problema de depencias con dpkg
https://www.linuxito.com/gnu-linux/nivel-medio/1335-resolver-problemas-de-dependencias-faltantes-al-instalar-paquetes-con-dpkg-en-debian-y-derivados

# 



