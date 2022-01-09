'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang
@Date          : June 2021

@Student Name  : Humaira Qadeer

https://github.com/JECSand/yahoofinancials

'''

from yahoofinancials import YahooFinancials 

class MyYahooFinancials(YahooFinancials):
    '''
    Extended class based on YahooFinancial libary

    '''
    def __init__(self, symbol, freq = 'annual'):
        YahooFinancials.__init__(self, symbol)
        self.freq = freq

    def get_operating_cashflow(self):
        return self._financial_statement_data('cash', 'cashflowStatementHistory', 'totalCashFromOperatingActivities', self.freq)

    def get_capital_expenditures(self):
        return self._financial_statement_data('cash', 'cashflowStatementHistory', 'capitalExpenditures', self.freq)

    def get_long_term_debt(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'longTermDebt', self.freq)

    def get_account_payable(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'accountsPayable', self.freq)

    def get_total_current_liabilities(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'totalCurrentLiabilities', self.freq)

    def get_other_current_liabilities(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'otherCurrentLiab', self.freq)

    def get_cash(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'cash', self.freq)

    def get_short_term_investments(self):
        return self._financial_statement_data('balance', 'balanceSheetHistory', 'shortTermInvestments', self.freq)
    
    def get_market_cap(self):
        return super().get_market_cap()

    def get_total_assets(self):
        return self._financial_statement_data('balance','balanceSheetHistory','totalAssets',self.freq)
    


    def get_beta(self):
        return super().get_beta()

    def get_pe_ratio(self):
        return super().get_pe_ratio()

def _test():
    symbol = 'AAPL'
    
    yfinance = MyYahooFinancials(symbol)

    print("Getting Financial Data for {}".format(symbol))
    print("Long Term Debt: ", yfinance.get_long_term_debt())
    print("Market Cap:" , yfinance.get_market_cap())
    print("Total Assets: " ,yfinance.get_total_assets())
    print("Total Debt:", yfinance.get_long_term_debt() + (yfinance.get_total_current_liabilities() - yfinance.get_account_payable() - yfinance.get_other_current_liabilities()))
    print("Free Cash: ", yfinance.get_operating_cashflow() + yfinance.get_capital_expenditures())
    print("Beta: ", yfinance.get_beta())
    print("P/E Ratio: ", yfinance.get_pe_ratio())


if __name__ == "__main__":
    _test()
