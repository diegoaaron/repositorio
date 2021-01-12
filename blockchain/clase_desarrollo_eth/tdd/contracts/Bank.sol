// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

contract Bank {
  address payable public owner;

  constructor() public {
    owner = msg.sender;
  }

  function deposit() public payable {}

  function withdraw() public {
    owner.transfer(address(this).balance);
  }
}
