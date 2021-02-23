//SPDX-License-Identifier: Unlicense
pragma solidity 0.7.5;

import "hardhat/console.sol";

contract Blockgeeks {

    function name() constant returns (string name) { // Nombre del NFT
        return "Read Blockgeeks";
    }

    function symbol() constant returns (string symbol) { // Symbolo del NFT
        return "BG";
    }

    uint256 private totalSupply = 50;

    function totalSupply() constant returns (uint256 supply) { // Cantidad total de tokens
        return totalSupply; 
    }

    mapping(address => uint) private balances;

    function balanceOf(address _owner) constant returns (uint balance) { // cantidad de bloques asociadas a una dirección
        return balances[_owner];
    }

    mapping(uint256 => address) private tokenOwners;
    mapping(uint256 => bool) private tokenExists;

    function ownerOf(uint256 _tokenId) constant returns (address owner) { // obtener dirección propietara del token
        require(tokenExists[_tokenId]);
        return tokenOwners[_tokenId];
    }

    mapping(address => mapping(address => uint256)) allowed;

    function approve(address _to, uint256 _tokenId) { //delegar autorización de un token a otra persona
        
        require(msg.sender == ownerOf(_tokenId));
        require(msg.sender != _to);

        allowed[msg.sender][_to] = _tokenId;
        Approval(msg.sender, _to, _tokenId);
    }

    function takeOwnership(uint256 _tokenId) {
        require(tokenExists[_tokenId]);

        address oldOwner = ownerOf(_tokenId);
        address newOwner = msg.sender;

        require(newOwner != oldOwner);
        require(allowed[oldOwner][newOwner] == _tokenId);

        balances[oldOwner] -= 1;

        tokenOwners[_tokenId] = newOwner;

        balances[newOwner] += 1;

        Transfer(oldOwner, newOwner, _tokenId);
    }
}