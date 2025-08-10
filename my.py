# -*- coding: utf-8 -*-
import os
import sys
import argparse
from termcolor import colored

# os.environ.setdefault("TESTING_ZVT", "True")
# os.environ.setdefault("SQLALCHEMY_WARN_20", "1")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "./src")))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--zvt",
        help="zvt main",
        action="store_true",
    )
    parser.add_argument(
        "--server",
        help="zvt server",
        action="store_true",
    )
    parser.add_argument(
        "--plugin",
        help="zvt plugin",
        action="store_true",
    )
    parser.add_argument(
        "--test",
        help="test",
        action="store_true",
    )
    args = parser.parse_args()

    if args.zvt:
        from src.zvt.main import main as zvt_main

        zvt_main()
    elif args.server:
        from src.zvt.zvt_server import main as zvt_server_main

        zvt_server_main()
    elif args.plugin:
        from src.zvt.plugin import main as plugin_main

        plugin_main()
    elif args.test:
        # print(colored("stock", "cyan"))
        # from zvt.domain import Stock
        # Stock.record_data()
        # df = Stock.query_data()
        # print(df.tail())

        print(colored("tradable entity schema map", "cyan"))
        from zvt.contract import zvt_context
        print(zvt_context.tradable_schema_map)

        # print(colored("stock hk", "cyan"))
        # from zvt.domain import Stockhk
        # Stockhk.record_data()
        # df = Stockhk.query_data(index='code')
        # print(df.tail())

        print(colored("StockInstitutionalInvestorHolder", "cyan"))
        from zvt.domain import StockInstitutionalInvestorHolder
        # entity_ids = ["stock_sz_000338", "stock_sz_000001"]
        entity_ids = None
        StockInstitutionalInvestorHolder.record_data(entity_ids=entity_ids)
        df = StockInstitutionalInvestorHolder.query_data(entity_ids=entity_ids)
        # print(df.tail())
        print(df)

        print(colored("Stock1dHfqKdata", "cyan"))
        from zvt.domain import Stock1dHfqKdata
        entity_ids = ["stock_sz_000338", "stock_sz_000001"]
        Stock1dHfqKdata.record_data(entity_ids=entity_ids, provider="em")
        df = Stock1dHfqKdata.query_data(entity_ids=entity_ids, provider="em")
        print(df)
        print(Stock1dHfqKdata.get_storages())

        print(colored("IntervalLevel", "cyan"))
        from zvt.contract import IntervalLevel
        for level in IntervalLevel:
            print(level.value)

        print(colored("AdjustType", "cyan"))
        from zvt.contract import AdjustType
        for adjust_type in AdjustType:
            print(adjust_type.value)

        print(colored("Stock1dHfqKdata", "cyan"))
        from zvt.domain import Stock1dHfqKdata
        Stock1dHfqKdata.record_data(code='000338', provider='em')
        df = Stock1dHfqKdata.query_data(code='000338', provider='em')
        print(df)

        from zvt.domain import Stock5mKdata
        Stock5mKdata.record_data(code='000338', provider='em')
        df = Stock5mKdata.query_data(code='000338', provider='em')
        print(df)

        print(colored("FinanceFactor", "cyan"))
        from zvt.domain import FinanceFactor
        FinanceFactor.record_data(code='000338')
        df = FinanceFactor.query_data(code='000338', 
                                      columns=FinanceFactor.important_cols(),
                                      index='timestamp')
        print(df)

        print(colored("Country", "cyan"))
        from zvt.domain import Country
        Country.record_data()
        df = Country.query_data()
        print(df[df['income_level'] == 'High income'])

        # print(colored("TreasuryYield", "cyan"))
        # from zvt.domain import TreasuryYield
        # from zvt.api.intent import compare
        # TreasuryYield.record_data()
        # compare(codes=["US"], schema=TreasuryYield, columns=["yield_2", "yield_10", "yield_30"])

    else:
        parser.print_help()
    pass


if __name__ == "__main__":
    main()
