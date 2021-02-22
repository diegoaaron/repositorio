//SPDX-License-Identifier: Unlicense
pragma solidity 0.7.5;

import "hardhat/console.sol";

contract Greeter {
    string greeting;

    constructor(string memory _greeting) {
        console.log("Desplegando el contrato Greeter", _greeting);
        greeting = _greeting;
    }

    function greet() public view returns (string memory) {
        return greeting;
    }

    function setGreeting(string memory _greeting) public {
        console.log("Cambiando el estado from '%s' por '%s'", greeting, _greeting);
        greeting = _greeting;
    }
}