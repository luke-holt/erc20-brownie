// contracts/GLDToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract LukeToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Luke", "L") {
        _mint(msg.sender, initialSupply);
    }
}
