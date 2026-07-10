class Liquidity:

    def detect(self, highs, lows):

        if len(highs) < 3 or len(lows) < 3:
            return "NONE"

        # Equal highs → potential buy-side liquidity
        if highs[-1] == highs[-2]:
            return "BUY_SIDE_LIQUIDITY"

        # Equal lows → potential sell-side liquidity
        if lows[-1] == lows[-2]:
            return "SELL_SIDE_LIQUIDITY"

        return "NONE"