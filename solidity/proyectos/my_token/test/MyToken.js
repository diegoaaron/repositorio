const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("My Token", function(){
    it("Should return the new", async function(){
        const [owner, addr1] = await ethers.getSigners();
        const MyToken = await ethers.getContractFactory("MyToken");
        const mytoken = await MyToken.deploy("0x7dd4640271b84f7D023946AFB2b85E7964C21FA1", ethers.utils.parseEther("1000"));

        await mytoken.deployed();

        expect(await mytoken.name()).to.equal("My Token");
        expect(await mytoken.symbol()).to.equal("MYT");
        expect(await mytoken.decimals()).to.equal(18);
        expect(await mytoken.totalSupply()).to.equal(ethers.utils.parseEther("1000"));
        await mytoken.connect(addr1).mint(ethers.utils.parseEther("1"));
        expect(await mytoken.totalSupply()).to.equal(ethers.utils.parseEther("1001"));
        expect(await mytoken.balanceOf("0x7dd4640271b84f7D023946AFB2b85E7964C21FA1")).to.equal(
            ethers.utils.parseEther("1000")
        );

        expect(await mytoken.balanceOf(await addr1.getAddress())).to.equal(
            ethers.utils.parseEther("1")
        );
    });
});

// Contrato de gúia junto al video: https://github.com/crisgarner/sg-erc20

