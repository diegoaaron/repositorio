const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Greeter", function() {
    it("Devuelve el nuevo saludo despues de cambiar", async function() {
        const Greeter = await ethers.getContractFactory("Greeter");
        const greeter = await Greeter.deploy("HOLA MUNDO XD"); //usando el constructor

        await greeter.deployed();
        expect(await greeter.greet()).to.equal("HOLA MUNDO XD"); //validando si se desplego bien el contrato

        await greeter.setGreeting("habla causita");
        expect(await greeter.greet()).to.equal("habla causita"); //actualizando información del contrato

        const acaracho = await greeter.greet();
        console.log("el valor actual del contrato es:", acaracho);
    });
});