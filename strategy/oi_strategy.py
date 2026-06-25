import config

from core.enums import Signal
from strategy.base import BaseStrategy


class OIStrategy(BaseStrategy):

    def check(self, df, i):

        if i == 0:
            return Signal.NONE

        oi = df.iloc[i]["oi"]
        oi_prev = df.iloc[i - 1]["oi"]

        delta = oi - oi_prev

        close = df.iloc[i]["Close"]
        prev_close = df.iloc[i - 1]["Close"]

        volume = df.iloc[i]["Volume"]
        prev_volume = df.iloc[i - 1]["Volume"]

        if (
            delta < -config.OI_THRESHOLD
            and close > prev_close
            and volume > prev_volume
        ):
            return Signal.LONG

        if (
            delta > config.OI_THRESHOLD
            and close < prev_close
            and volume > prev_volume
        ):
            return Signal.SHORT

        return Signal.NONE