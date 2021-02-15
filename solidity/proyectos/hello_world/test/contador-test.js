const { expect } = require("chai");

const { ethers } = require("hardhat"); // la variable 'ethers es de alcance global  pero se puede definir de forma explicita


describe("Contador", function() {
    it("Should return the new greeting once it's changed", async function() {

        const [owner] = await ethers.getSigners();

        const Contador = await ethers.getContractFactory("Contador");
    
        const contador = await Contador.deploy();
    
        const ownerBalance = await contador.balanceOf(owner.address);

});
});


// continuar en https://hardhat.org/tutorial/testing-contracts.html