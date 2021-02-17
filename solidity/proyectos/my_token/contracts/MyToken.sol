// SPDX-License-Identifier: MIT

pragma solidity 0.7.5;

contract MyToken {
    string public name = "My Token";
    string public symbol = "MYT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    constructor(address _owner, uint256 _initialSupply) { //forma correcta de agregar los tokens al crear el contrato
        usersBalance[_owner] = _initialSupply;
        totalSupply = _initialSupply;
    }

    // Hacer una función BUY que permita comprar tokens con ETH
    // Hacer función Burn 



    function mint(uint256 _value) public { // aumentando el total de tokens a un contrato - no recomenando
        usersBalance[msg.sender] = usersBalance[msg.sender] + _value;
        totalSupply += _value;
    }

    mapping(address => uint256) public usersBalance;
    mapping(address => mapping(address => uint256)) public allowance;

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return usersBalance[_owner];
    }

    function transfer(address _to, uint256 _value) external returns (bool success) {
        usersBalance[msg.sender] = usersBalance[msg.sender] - _value;
        usersBalance[_to] = usersBalance[_to] + _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success){
        if(allowance[_from][_to] <= _value) {
            usersBalance[_from] = usersBalance[_from] - _value;
            usersBalance[_to] = usersBalance[_to] + _value;
            allowance[_from][_to] = allowance[_from][_to] - _value;
            return true;
        }  
    }

    function approve(address _spender, uint256 _value) external returns (bool success){
        allowance[msg.sender][_spender] = allowance[msg.sender][_spender] + _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }
event Transfer(address indexed _from, address indexed _to, uint256 _value);
event Approval(address indexed _owner, address indexed _spender, uint256 _value);
}
