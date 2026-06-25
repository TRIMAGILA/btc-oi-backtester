from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from core.enums import ExitReason, Side


@dataclass
class Trade:
    """
    Закрытая сделка.
    """

    side: Side

    entry_time: datetime
    exit_time: datetime

    entry_price: float
    exit_price: float

    qty: float

    pnl: float

    commission: float

    exit_reason: ExitReason

    @property
    def net_pnl(self) -> float:
        return self.pnl - self.commission

    @property
    def duration(self):
        return self.exit_time - self.entry_time

    @property
    def return_percent(self):

        notional = self.entry_price * self.qty

        if notional == 0:
            return 0.0

        return self.net_pnl / notional * 100