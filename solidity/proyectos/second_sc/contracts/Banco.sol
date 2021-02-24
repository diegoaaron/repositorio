// SPDX-License-Identifier: MIT

pragma solidity 0.7.5;

contract Bancon {

    constructor () payable {

    }

    function incrementBalance(uint256 _amount) payable public {
        require(msg.value == _amount);
    }

    function getBalance() public {
        msg.sender.transfer(address(this).balance);
    }
}

