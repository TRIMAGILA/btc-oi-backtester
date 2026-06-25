from abc import ABC
from abc import abstractmethod

from core.enums import Signal


class BaseStrategy(ABC):

    @abstractmethod
    def check(self, df, i) -> Signal:
        pass