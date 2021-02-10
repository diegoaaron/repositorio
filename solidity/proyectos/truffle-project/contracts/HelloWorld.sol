// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract HelloWorld {

  // Variables
  uint storedInt;
  string storedString;
  
  // Eventos

  // Modificadores

  // Constructor
  constructor() public {
    storedString = "Hola mundo!";
  }

  // Funciones
  function setInt(uint _storedInt) public {
    storedInt = _storedInt;
  }

  function getInt() public view returns (uint) {
    return storedInt;
  }

  function getString() public view returns (string memory) {
    return storedString;
  }

}

// Crear un contrato con dos funciones guardar una variable que guarde un valor numerico, 
// otra funcion que lo retorne y una variable publica de string con la palabra Hola mundo.
