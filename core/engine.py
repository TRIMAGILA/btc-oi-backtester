"""
Backtest Engine
"""

from core.enums import Signal
from strategy.oi_strategy import OIStrategy


class Engine:

    def __init__(self, dataframe, portfolio):

        self.df = dataframe

        self.strategy = OIStrategy()

        self.portfolio = portfolio

        self.current_bar = 0

        self.long_signals = 0

        self.short_signals = 0

    def run(self):

        print()

        print("===================================")
        print("START BACKTEST")
        print("===================================")

        total = len(self.df)

        print(f"Bars: {total}")

        print()

        for i in range(total):

            self.current_bar = i

            row = self.df.iloc[i]

            signal = self.strategy.check(self.df, i)

            if signal == Signal.LONG:

                self.long_signals += 1

                if self.portfolio.can_open_long():

                    self.portfolio.open_long(
                        row["datetime"],
                        row["Close"]
                    )

            elif signal == Signal.SHORT:

                self.short_signals += 1

                if self.portfolio.can_open_short():

                    self.portfolio.open_short(
                        row["datetime"],
                        row["Close"]
                    )

            self.portfolio.update_price(row["Close"])

        print()

        print("BACKTEST FINISHED")

        print(f"Long signals : {self.long_signals}")

        print(f"Short signals: {self.short_signals}")

        print()

        print(f"Equity : {self.portfolio.equity:.2f}")

        print()