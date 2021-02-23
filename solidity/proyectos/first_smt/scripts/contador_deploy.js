const hre = require("hardhat");

async function main() {
    const Contador = await hre.ethers.getContractFactory("Contador");
    const contador = await Contador.deploy(100);

    await contador.deployed();

    console.log("El contrato de Contador, ha sido desplegado en la dirección: ", contador.address);
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.log(error);
        process.exit(1);
    });