import config

from data.loader import DataLoader

from core.engine import Engine

from core.portfolio import Portfolio


def main():

    print("Loading BTC...")

    loader = DataLoader(
        config.BTC_FILE,
        config.OI_FILE,
    )

    print("Loading OI...")

    df = loader.merge()

    print("Rows:", len(df))

    portfolio = Portfolio()

    engine = Engine(df, portfolio)

    engine.run()


if __name__ == "__main__":

    main()