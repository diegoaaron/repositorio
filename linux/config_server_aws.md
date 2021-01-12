# Configuración servidor AWS 

Despues de crear una instancia EC2 en AWS, configurar el puerto 22 en el firewall y las llaves para el logueo 


#### DNS público - servidor AWS
ec2-35-173-247-127.compute-1.amazonaws.com

#### Usuario por defecto para la instancia Ubuntu 20.04
ubuntu

#### Palabra utilizada para crear la llave pública
servidor_testing

#### Configurar el permiso de la llave (para poder utilizarla, despues de descargarla)
`chmod 400 servidor_testing.pem`

#### Conectarnos a la instancia EC2 (desde la ruta donde se encuentra la llave)
`ssh -i "servidor_testing.pem" ubuntu@ec2-35-173-247-127.compute-1.amazonaws.com`

#### 