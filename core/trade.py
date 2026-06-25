from dataclasses import dataclass
from datetime import datetime

from core.enums import Side
from core.enums import ExitReason


@dataclass
class Trade:

    side: Side

    entry_time: datetime

    exit_time: datetime

    entry_price: float

    exit_price: float

    qty: float

    pnl: float

    commission: float

    exit_reason: ExitReason