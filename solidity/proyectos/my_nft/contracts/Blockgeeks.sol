//SPDX-License-Identifier: Unlicense
pragma solidity 0.7.5;

import "hardhat/console.sol";

contract Blockgeeks {

    function name() view returns (string name) { // Nombre del NFT
        return "Read Blockgeeks";
    }

    function symbol() view returns (string symbol) { // Symbolo del NFT
        return "BG";
    }

    uint256 private totalSupply = 50;

    function totalSupply() view returns (uint256 supply) { // Cantidad total de tokens
        return totalSupply; 
    }

    mapping(address => uint) private balances;

    function balanceOf(address _owner) view returns (uint balance) { // cantidad de NFC's asociadas a una dirección
        return balances[_owner];
    }

    mapping(uint256 => address) private tokenOwners;
    mapping(uint256 => bool) private tokenExists;

    function ownerOf(uint256 _tokenId) view returns (address owner) { // obtener dirección propietara del token
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

    function takeOwnership(uint256 _tokenId) { // premite que un tercero saque tokens de la cuenta de otro.
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

    mapping(address => mapping(uint256 => uint256)) private ownerTokens;

    function removeFromTokenList(address owner, uint256 _tokenId) private {
        for(uint256 i=0; ownerTokens[owner][i] != _tokenId; i++) {
            ownerTokens[owner][i] = 0;
        }
    }
    function transfer(address _to, uint256 _tokenId) {
        address currentOwner = msg.sender;

        address newOwner = _to;

        require(tokenExists[_tokenId]);
        require(currentOwner == ownerOf(_tokenId));
        require(currentOwner != newOwner);
        require(newOwner != address(0));

        removeFromTokenList(_tokenId);

        balances[oldOwner] -= 1;

        tokenOwners[_tokenId] = newOwner;

        balances[newOwner] += 1;

        Transfer(oldOwner, newOwner, _tokenId);

    }

    mapping(address => mapping(uint256 => uint256)) private ownerTokens;

    function tokenOfOwnerByIndex(address _owner, uint256 _index) view returns (uint tokenId) {
        return ownerTokens[_owner][_index];
    }

    mapping(uint256 => string) tokenLinks;

    function tokenMetadata(uint256 _tokenId) constant returns (string infoUrl) {
        return tokenLinks[_tokenId];
    }



    event Approval(address indexed _owner, address indexed _approved, uint256 _tokenId);

}

