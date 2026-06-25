"""
Portfolio

Хранит состояние счёта и открытых позиций.
"""

from __future__ import annotations

from typing import List, Optional

import config

from models.position import Position
from models.trade import Trade


class Portfolio:

    def __init__(self):

        # Баланс
        self.start_balance = config.START_BALANCE
        self.balance = config.START_BALANCE

        # Открытые позиции
        self.long_position: Optional[Position] = None
        self.short_position: Optional[Position] = None

        # Закрытые сделки
        self.closed_trades: List[Trade] = []

        # История equity
        self.equity_curve = []

        # Максимальная просадка
        self.max_drawdown = 0.0

        # Максимальный equity
        self.max_equity = self.balance

    # ===================================================
    # POSITION
    # ===================================================

    def has_long(self):

        return self.long_position is not None

    def has_short(self):

        return self.short_position is not None

    def can_open_long(self):

        return not self.has_long()

    def can_open_short(self):

        return not self.has_short()

    # ===================================================
    # FLOATING PNL
    # ===================================================

    def update_price(self, price: float):

        if self.long_position:

            self.long_position.floating_pnl = (
                price -
                self.long_position.entry_price
            ) * self.long_position.qty

        if self.short_position:

            self.short_position.floating_pnl = (
                self.short_position.entry_price -
                price
            ) * self.short_position.qty

        self.update_equity()

    # ===================================================
    # EQUITY
    # ===================================================

    @property
    def floating_pnl(self):

        pnl = 0.0

        if self.long_position:
            pnl += self.long_position.floating_pnl

        if self.short_position:
            pnl += self.short_position.floating_pnl

        return pnl

    @property
    def equity(self):

        return self.balance + self.floating_pnl