"""
Загрузка и объединение данных BTC и OI.
"""

from pathlib import Path
import pandas as pd


class DataLoader:
    def __init__(self, btc_file: Path, oi_file: Path):
        self.btc_file = btc_file
        self.oi_file = oi_file

    def load_btc(self) -> pd.DataFrame:
        """Загрузка свечей BTC."""

        df = pd.read_csv(self.btc_file)

        # Приводим название первой колонки к datetime
        if "datetime" not in df.columns:
            first = df.columns[0]
            df.rename(columns={first: "datetime"}, inplace=True)

        df["datetime"] = pd.to_datetime(df["datetime"])

        df.sort_values("datetime", inplace=True)

        df.drop_duplicates("datetime", inplace=True)

        df.reset_index(drop=True, inplace=True)

        return df

    def load_oi(self) -> pd.DataFrame:
        """Загрузка Open Interest."""

        df = pd.read_csv(self.oi_file)

        df["datetime"] = pd.to_datetime(df["datetime"])

        df.sort_values("datetime", inplace=True)

        df.drop_duplicates("datetime", inplace=True)

        df.reset_index(drop=True, inplace=True)

        return df

    def merge(self) -> pd.DataFrame:
        """
        Объединяет BTC и OI по времени.
        """

        btc = self.load_btc()

        oi = self.load_oi()

        df = pd.merge_asof(
            btc,
            oi,
            on="datetime",
            direction="backward"
        )

        return df