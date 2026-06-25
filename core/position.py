from dataclasses import dataclass
from datetime import datetime

from core.enums import Side


@dataclass
class Position:

    side: Side

    entry_time: datetime

    entry_price: float

    qty: float

    margin: float

    leverage: int

    commission: float

    floating_pnl: float = 0.0