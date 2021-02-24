## Comandos de referencia

#### crea el archivo “package.json” para el proyecto con el formato npm (se debe ejecutar dentro de una carpeta vacía)
`npm init`

#### instala en el framework hardhat dentro del proyecto (es instalado como una dependencia para desarrollo, o sea de forma local)
`npm install --save-dev hardhat`
`npm install -D hardhat`

#### crea la plantilla del proyecto Solidity (debe ser llamada desde la carpeta principal del proyecto)
#### cuando el proyecto ya esta creado, sirve para ejecutar comandos del framework sobre el proyecto
`npx hardhat`

#### instalación de componentes adicionales para trabajar con hardhat (se debe ejectuar desde la carpeta principal del proyecto)
`npm install -D @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers ethers`

#### se debe crear las carpetas básicas para programar
`mkdir contracts scripts test`

#### mostras las cuentas creadas por el framework para realizar pruebas
`npx hardhat accounts`

#### compila el código de los smart contracts de todo el proyecto
`npx hardhat compile`

#### ejecuta los test definidos para el smart contract
`npx hardhat test`

#### despliega los contratos compilados
`npx hardhat run scripts/sample-script.js`

#### levanta la blockchain de prueba y despliega el contrato utilizando el script definido
`npx hardhat run scripts/sample-script.js --network localhost`

#### levantar interfaz de la blockchain de prueba creada por hardhat cuando se crea el proyecto (expone una interfaz JSON-RPC)
`npx hardhat node`

#### líneas básicas de un contrato
```
// SPDX-License-Identifier: MIT

pragma solidity 0.7.5;

```