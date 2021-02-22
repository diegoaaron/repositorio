require("@nomiclabs/hardhat-waffle");

task("accounts", "Imprime una lista de las cuentas", async () => {
  const accounts = await ethers.getSigners();
  let n = 1;

  for (const account of accounts) {
    console.log(n, "-", account.address);
    n += 1;
  }
});


module.exports = {
  solidity: "0.7.5",
};


