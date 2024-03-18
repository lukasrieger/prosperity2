from typing import List, Tuple
from datamodel import OrderDepth, TradingState, Order

type TraderResult = Tuple[dict[str, list[Order]], int, str]


def run(state: TradingState) -> TraderResult:
    print("traderData: " + state.traderData)
    print("Observations: " + str(state.observations))
    result = {}
    for product in state.order_depths:
        order_depth: OrderDepth = state.order_depths[product]
        orders: List[Order] = []
        acceptable_price = 10  # Participant should calculate this value
        print("Acceptable price : " + str(acceptable_price))
        print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(
            len(order_depth.sell_orders)))

        if len(order_depth.sell_orders) != 0:
            best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
            if int(best_ask) < acceptable_price:
                print("BUY", str(-best_ask_amount) + "x", best_ask)
                orders.append(Order(product, best_ask, -best_ask_amount))

        if len(order_depth.buy_orders) != 0:
            best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
            if int(best_bid) > acceptable_price:
                print("SELL", str(best_bid_amount) + "x", best_bid)
                orders.append(Order(product, best_bid, -best_bid_amount))

        result[product] = orders

    # String value holding Trader state data required. Will be delivered as TradingState.traderData next execution.
    traderData = "SAMPLE"

    conversions = 1
    return result, conversions, traderData


class Trader:
    pass
