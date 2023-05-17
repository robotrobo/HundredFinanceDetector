// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;
// import "./ExponentialNoError.sol";


contract HundredFinance {
    uint256 public number;
    uint totalSupply = 10000;
    uint totalBorrows = 1000;
    uint totalReserves = 100;
    // uint expScale = 1e18;

    function getCashPrior() internal pure returns (uint) {
        return 1000;
    }
    function exchangeRateStoredInternal() public pure returns (uint256) {
        // uint _totalSupply = totalSupply;
        // if (_totalSupply == 0) {
        //     /*
        //      * If there are no tokens minted:
        //      *  exchangeRate = initialExchangeRate
        //      */
        //     return 2.0e18;
        // } else {
        //      Unimportant to this test
        // }

        return 25015319085e18;
    }

    function redeemUnderlying(uint256 redeemAmountIn) pure public returns 
    (uint)
    {
        // require(redeemTokensIn == 0 || redeemAmountIn == 0, "one of redeemTokensIn or redeemAmountIn must be zero");

        /* exchangeRate = invoke Exchange Rate Stored() */
        // Exp memory exchangeRate = Exp({mantissa: exchangeRateStoredInternal() });
        uint exchangeRate = exchangeRateStoredInternal();
        uint badRate = 10;
        uint redeemTokens;
        uint good = 1;

        /*
            * We get the current exchange rate and calculate the amount to be redeemed:
            *  redeemTokens = redeemAmountIn / exchangeRate
            *  redeemAmount = redeemAmountIn
            */
        // redeemTokens = div_(redeemAmountIn, exchangeRate);
        // redeemAmount = redeemAmountIn;
        // badRate = badRate % exchangeRate;
        // redeemTokens =  exchangeRate / 1e18;
        // redeemAmountIn = redeemAmountIn % exchangeRate;
        redeemTokens = redeemAmountIn * 1e18 / exchangeRate;


        return redeemTokens;
    }

}
