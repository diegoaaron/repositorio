const { expect } = require("chai");
const { ethers } = require("hardhat");
const { isCallTrace } = require("hardhat/internal/hardhat-network/stack-traces/message-trace");

describe("My Token", function(){
    it("Should return the new", async function(){
        const MyToken = await ethers.getContractFactory("MyToken");
        const mytoken = await MyToken.deploy("0x7dd4640271b84f7D023946AFB2b85E7964C21FA1", 1000);

        await mytoken.deployed();

        expect(await mytoken.name()).to.equal("My Token");
        expect(await mytoken.symbol()).to.equal("MYT");
        expect(await mytoken.decimals()).to.equal(18);
        expect(await mytoken.totalSupply()).to.equal(1000);

        await mytoken.mint(10000);
    });
});