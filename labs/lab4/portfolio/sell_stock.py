
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    #Ensure symbol exists (use _find_position())
    pos = _find_position(self, sym)
    if pos is None:
        print(f"{sym} not found in portfolio.")
        return
    
    #Ensure shares <= owned
    owned = pos.get("shares", 0) #gets how many shares the client owns
    if shares > owned: #if the number of shares is more than what the client owns then prints error message
        print(f"Not enough shares to sell. You own {owned} shares of {sym}.")
        return 

    #Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    price_map = _prices.get_last_close_map([sym])
    last_close = price_map.get(sym) #price for the specific stock

    #Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    proportion = shares / pos["shares"]
    cost_reduction = pos["cost"] * proportion #amt of cost is removed by proportion of stock sold
    pos["shares"] = pos["shares"] - shares
    pos["cost"] = pos["cost"]-cost_reduction

    #Remove the position if shares drop to 0
    if pos["shares"] <= 0:
        self.positions.remove(pos)

    #Increase self.cash by proceeds
    proceeds = shares * last_close
    self.cash = self.cash+ proceeds
    return
       
