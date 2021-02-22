const hre = require("hardhat");

async function main() {
    const Greeter = await hre.ethers.getContractFactory("Greeter");
    const greeter = await Greeter.deploy("ENTENDIENDO HARDAT");

    await greeter.deployed();

    console.log("El contrato Greeter ha sido desplegado en la dirección: ", greeter.address);
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.log(error);
        process.exit(1);
    });
