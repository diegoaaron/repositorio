// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.7.0;

import "hardhat/console.sol"; // para que sirve esta importación...

contract Contador {
    uint256 count;

    //constructor
    constructor(uint256 _count) {
        count = _count;
    }

    //funciones getter y setter
    function setCount(uint256 _count) public {
        count = _count;
    }

    function incrementCount() public {
        count += 1;
    }

    function getCount() public view returns(uint256) { // esta función de tipo view no consume gas
        return count;
    }

    function getNumber() public pure returns(uint256) { // esta función de tipo view no consume gas
        return 34;
    }
}