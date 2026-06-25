from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from core.enums import Side


@dataclass
class Position:
    """
    Открытая позиция.
    """

    side: Side

    entry_time: datetime
    entry_price: float

    qty: float

    margin: float
    leverage: float

    commission: float = 0.0

    floating_pnl: float = 0.0

    @property
    def notional(self) -> float:
        return self.qty * self.entry_price

    @property
    def roi(self) -> float:
        if self.margin == 0:
            return 0.0

        return self.floating_pnl / self.margin

    @property
    def liquidation_move_percent(self) -> float:
        """
        Приблизительное движение цены до потери 100% маржи.
        """
        return 100.0 / self.leverage

    @property
    def liquidation_price(self) -> float:

        move = self.entry_price * self.liquidation_move_percent / 100

        if self.side == Side.LONG:
            return self.entry_price - move

        return self.entry_price + move