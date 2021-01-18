## Comandos de referencia

#### inicializa un proyecto git dentro del directorio que se encuentra
`git init`

#### clonar un repositorio 
`git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

#### lista las ramas e indica la rama actual 
`git branch`

#### elimina la rama name_branch
`git branch -d name_branch`

#### cambiar a la rama name_branch
`git checkout name_branch` 

##### envia la información de la local_branch hacia remote_branch
`git push -u remote_branch local_branch` 

#### muestra los registros de las acciones de git
`git log` 

#### agregando un repositorio remoto
`git remote add origin git@github.com:USERNAME/NAME_REPOSITORY.git` 

#### actualizar repositorio local desde el repositorio remoto
`git pull remote_branch local_branch`

#### quitar carpetas del repositorio sin eliminarlo del archivo original
`git rm -r --cached nombre_directorio`

#### quitar archivo del repositorio sin eliminarlo del archivo original
`git rm --cached nombre_archivo`

#### une a la rama actual, la rama name_branch
`git merge name_branch`

## Artículos y guías

[Configuración de SSH](https://docs.github.com/es/github/authenticating-to-github/connecting-to-github-with-ssh)

[Configuración de comandos básicos de github](https://docs.github.com/es/free-pro-team@latest/github/creating-cloning-and-archiving-repositories)

[Referencias sobre Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 