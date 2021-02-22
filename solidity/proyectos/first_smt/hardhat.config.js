require("@nomiclabs/hardhat-waffle");

task("accounts", "Prints the list of accounts", async () => {
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


