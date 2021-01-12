#### quitar archivo o directorio completo del seguimiento de git
git rm --cached name_file
git rm -r --cached directory_to_delete/


------------------------------------------------------------------------------------------------------------------------------------------------
Scripts utilizados

# clonar un repositorio 
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

# lista las ramas e indica la rama actual 
git branch 

# une a la rama actual, la rama name_branch
git merge name_branch 

# elimina la rama name_branch
git branch -d name_branch 

# cambia a la rama name_branch
git checkout name_branch 

# envia la información de la local_branch hacia remote_branch
git push -u remote_branch local_branch 

# muestra los registros de las acciones de git
git log 

# elimina de git la carpeta/archivo indicado
git rm -r --cached name_dir 

# inicializa un proyecto git dentro del repositorio que se encuentra
git init 

# agregando un repositorio remoto
git remote add origin git@github.com:diegoaaron/prj_dj_uno.git 

# actualizar repositorio local desde el repositorio remoto
git pull remote_branch local_branch


------------------------------------------------------------------------------------------------------------------------------------------------
Documentos y guías ya revisadas

# Configuración de SSH en equipo
https://docs.github.com/es/github/authenticating-to-github/connecting-to-github-with-ssh

# Configuración de comandos básicos de github
https://docs.github.com/es/free-pro-team@latest/github/creating-cloning-and-archiving-repositories


