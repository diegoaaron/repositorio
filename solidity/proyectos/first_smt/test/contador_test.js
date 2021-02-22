const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Contador", function() {
    it("Definimos el valor inicial del contador", async function() {
        const Contador = await ethers.getContractFactory("Contador"); 
        const contador = await Contador.deploy(100);

        await contador.deployed();


        expect(await contador.getCount()).to.equal(100); //validando el constructor

        expect(await contador.getNumber()).to.equal(34);
        
        
        
    });
});