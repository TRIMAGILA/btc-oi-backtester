"""
Broker

Отвечает за исполнение сделок.
"""

from __future__ import annotations

from datetime import datetime

import config

from core.enums import Side, ExitReason
from models.position import Position
from models.trade import Trade


class Broker:

    def __init__(self, portfolio):

        self.portfolio = portfolio

    def _calc_qty(self, price: float) -> float:

        return config.POSITION_SIZE / price

    def _commission(self) -> float:

        return config.POSITION_SIZE * config.COMMISSION

    # --------------------------------------------------

    def open_long(self, dt: datetime, price: float):

        if self.portfolio.long_position is not None:
            return False

        qty = self._calc_qty(price)

        commission = self._commission()

        self.portfolio.balance -= commission

        self.portfolio.long_position = Position(
            side=Side.LONG,
            entry_time=dt,
            entry_price=price,
            qty=qty,
            margin=config.MARGIN,
            leverage=config.LEVERAGE,
            commission=commission,
        )

        return True

    # --------------------------------------------------

    def open_short(self, dt: datetime, price: float):

        if self.portfolio.short_position is not None:
            return False

        qty = self._calc_qty(price)

        commission = self._commission()

        self.portfolio.balance -= commission

        self.portfolio.short_position = Position(
            side=Side.SHORT,
            entry_time=dt,
            entry_price=price,
            qty=qty,
            margin=config.MARGIN,
            leverage=config.LEVERAGE,
            commission=commission,
        )

        return True

    # --------------------------------------------------

    def close_long(
        self,
        dt: datetime,
        price: float,
        reason: ExitReason,
    ):

        pos = self.portfolio.long_position

        if pos is None:
            return

        pnl = (price - pos.entry_price) * pos.qty

        commission = self._commission()

        self.portfolio.balance += pnl

        self.portfolio.balance -= commission

        trade = Trade(
            side=Side.LONG,
            entry_time=pos.entry_time,
            exit_time=dt,
            entry_price=pos.entry_price,
            exit_price=price,
            qty=pos.qty,
            pnl=pnl,
            commission=pos.commission + commission,
            exit_reason=reason,
        )

        self.portfolio.closed_trades.append(trade)

        self.portfolio.long_position = None

    # --------------------------------------------------

    def close_short(
        self,
        dt: datetime,
        price: float,
        reason: ExitReason,
    ):

        pos = self.portfolio.short_position

        if pos is None:
            return

        pnl = (pos.entry_price - price) * pos.qty

        commission = self._commission()

        self.portfolio.balance += pnl

        self.portfolio.balance -= commission

        trade = Trade(
            side=Side.SHORT,
            entry_time=pos.entry_time,
            exit_time=dt,
            entry_price=pos.entry_price,
            exit_price=price,
            qty=pos.qty,
            pnl=pnl,
            commission=pos.commission + commission,
            exit_reason=reason,
        )

        self.portfolio.closed_trades.append(trade)

        self.portfolio.short_position = None