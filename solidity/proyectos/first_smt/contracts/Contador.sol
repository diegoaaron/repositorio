//SPDX-License-Identifier: Unlicense
pragma solidity 0.7.5;

import "hardhat/console.sol";

contract Contador {
    uint256 count;

    constructor (uint256 _count) {
        count = _count;
        console.log("El valor del contador al desplegar es: ", count);
    }

    function setCount(uint256 _count) public {
        count = _count;
        console.log("El nuevo valor del contador es: ", count);
    }

    function incrementCount() public {
        count += 1;
        console.log("El contador despues de incrementar es: ", count);
    }

    function getCount() public view returns (uint256) {
        console.log("el valor actual del contador es: ", count);
        return count;
    }

    function getNumber() public pure returns (uint256) {
        return 34;
    }
    
}