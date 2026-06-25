from __future__ import annotations

from typing import List, Optional

import config

from models.position import Position
from models.trade import Trade


class Portfolio:
    """
    Хранит состояние торгового счёта.
    """

    def __init__(self):

        self.start_balance = config.START_BALANCE
        self.balance = config.START_BALANCE

        self.long_position: Optional[Position] = None
        self.short_position: Optional[Position] = None

        self.closed_trades: List[Trade] = []

        self.equity_history: List[float] = []

        self.max_equity = self.balance
        self.max_drawdown = 0.0

    # --------------------------------------------------

    @property
    def floating_pnl(self) -> float:

        pnl = 0.0

        if self.long_position:
            pnl += self.long_position.floating_pnl

        if self.short_position:
            pnl += self.short_position.floating_pnl

        return pnl

    # --------------------------------------------------

    @property
    def equity(self) -> float:

        return self.balance + self.floating_pnl

    # --------------------------------------------------

    def has_long(self) -> bool:

        return self.long_position is not None

    # --------------------------------------------------

    def has_short(self) -> bool:

        return self.short_position is not None

    # --------------------------------------------------

    def can_open_long(self) -> bool:

        return not self.has_long()

    # --------------------------------------------------

    def can_open_short(self) -> bool:

        return not self.has_short()

    # --------------------------------------------------

    def update_price(self, price: float):

        if self.long_position:

            self.long_position.floating_pnl = (
                price - self.long_position.entry_price
            ) * self.long_position.qty

        if self.short_position:

            self.short_position.floating_pnl = (
                self.short_position.entry_price - price
            ) * self.short_position.qty

        self._update_statistics()

    # --------------------------------------------------

    def register_trade(self, trade: Trade):

        self.closed_trades.append(trade)

    # --------------------------------------------------

    def _update_statistics(self):

        equity = self.equity

        self.equity_history.append(equity)

        if equity > self.max_equity:
            self.max_equity = equity

        drawdown = self.max_equity - equity

        if drawdown > self.max_drawdown:
            self.max_drawdown = drawdown

    # --------------------------------------------------

    @property
    def trade_count(self):

        return len(self.closed_trades)

    # --------------------------------------------------

    @property
    def net_profit(self):

        return self.balance - self.start_balance