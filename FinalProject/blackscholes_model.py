'''
@project       : Queens College CSCI 365/765 Computational Finance
@Instructor    : Dr. Alex Pang

@Student Name  : Humaira Qadeer, Usman Ali, Shadman Saleh Shahriyar

@Date          : June 2021


'''

import datetime
from math import e, exp, log, pi, sqrt

import numpy as np
from scipy.stats import norm
from scipy.stats.stats import mode

from option import *
from stock import Stock


class BlackScholesModel(object):
    '''
    OptionPricer
    '''

    def __init__(self, pricing_date, risk_free_rate):
        self.pricing_date = pricing_date
        self.risk_free_rate = risk_free_rate

    def calc_parity_price(self, option, option_price):
        '''
        return the put price from Put-Call Parity if input option is a call
        else return the call price from Put-Call Parity if input option is a put
        '''
        S0 = option.underlying.spot_price
        T = option.time_to_expiry
        K = option.strike
        r = self.risk_free_rate
        result = None
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("Price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            if option.option_type == Option.Type.CALL:
                result = option_price + (K * exp(-r * T)) - S0
            elif option.option_type == Option.Type.PUT:
                result = option_price + S0 - (K * exp(-r * T))
        else:
            raise Exception("Unsupported option type")
        # end TODO
        return(result)

    def calc_model_price(self, option):
        '''
        Calculate the price of the option using Black-Scholes model
        '''
        px = None
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            
            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            q = option.underlying.dividend_yield
            r = self.risk_free_rate
            #TODO: implement details here
            d1 = (log(S0/K)+(r+pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            d2 = (log(S0/K)+(r-pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            d2 = d1 - sigma*math.sqrt(T)
            if option.option_type == Option.Type.CALL:
                px = (S0 *(exp((-q) *T)) * norm.cdf(d1)) - (K * exp((-r)*T)*norm.cdf(d2))
            elif option.option_type == Option.Type.PUT:
                px = (K * exp(-r*T)*norm.cdf(-d2)) - (S0 * (exp((-q) * T)) * norm.cdf(-d1))
            #end TODO   
        else:
            raise Exception("Unsupported option type")        
        return(px)

    def calc_delta(self, option):
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            # TODO:
            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            q = option.underlying.dividend_yield
            r = self.risk_free_rate
            d1 = (log(S0/K)+(r+pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            
            if option.option_type == Option.Type.CALL:
                
                result =  (exp((-q) * T)) *norm.cdf(d1)
            elif option.option_type == Option.Type.PUT:
                
                result = (exp((-q) * T)) * (norm.cdf(d1) - 1)
            # end TODO
        else:
            raise Exception("Unsupported option type")

        return result

    def calc_gamma(self, option):

        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            # TODO:
            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            q = option.underlying.dividend_yield
            r = self.risk_free_rate
            d1 = (log(S0/K)+(r+pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            
            if option.option_type == Option.Type.CALL or option.option_type == Option.Type.PUT:
                result = norm.pdf(d1) * (exp((-q) * T))/(S0 * sigma * math.sqrt(T))
    
            # end TODO
        else:
            raise Exception("Unsupported option type")

        return result

    def calc_theta(self, option):
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            # TODO:
            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            q = option.underlying.dividend_yield
            r = self.risk_free_rate
            d1 = (log(S0/K)+(r+pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            d2 =  (log(S0/K)+(r-pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            # TODO:
            if option.option_type == Option.Type.CALL:
               result = - (S0*sigma*norm.pdf(d1))/(2*math.sqrt(T)) - r*K*exp( -r*T)* norm.cdf(d2) + (q *S0* (exp((-q) * T)) * norm.cdf(d1))
            elif option.option_type == Option.Type.PUT:
               result = -(S0*sigma*norm.pdf(d1)) / (2*math.sqrt(T))+ r*K * exp(-r*T) * norm.cdf(-d2) - (q *S0* (exp((-q) * T)) * norm.cdf(-d1))
            # end TODO
        else:
            raise Exception("Unsupported option type")

        return result
    def calc_vega(self, option):
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            q = option.underlying.dividend_yield
            r = self.risk_free_rate
            d1 = (log(S0/K)+(r+pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))
            # TODO:
            if option.option_type == Option.Type.CALL or option.option_type == Option.Type.PUT:
                result = ((1/100) *(S0  * (exp((-q) * T)) * math.sqrt(T)) * norm.pdf(d1))
            # end TODO
        else:
            raise Exception("Unsupported option type")

        return result

    

    def calc_rho(self, option):
        if option.option_style == Option.Style.AMERICAN:
            raise Exception("B\S price for American option not implemented yet")
        elif option.option_style == Option.Style.EUROPEAN:
            # TODO:
            S0 = option.underlying.spot_price
            sigma = option.underlying.sigma
            T = option.time_to_expiry
            K = option.strike
            r = self.risk_free_rate
            
            d2 = (log(S0/K)+(r-pow(sigma, 2)/2)*T)/(sigma * math.sqrt(T))

            # TODO:
            if option.option_type == Option.Type.CALL:
                result = ((1/100) *(K * T * exp((-r) * T))) * norm.cdf(d2)
            elif option.option_type == Option.Type.PUT:
                result = (-1* (1/100) *(K * T * exp((-r) * T)) * norm.cdf(-d2))
            # end TODO
            # end TODO
        else:
            raise Exception("Unsupported option type")
        return result


def _test():

    symbol = 'AAPL'
    pricing_date = datetime.date(2021, 6, 1)

    risk_free_rate = 0.04
    model = BlackScholesModel(pricing_date, risk_free_rate)

    # .... use this as your unit test
    # calculate the B/S model price for a 3-month ATM call

    T = 3/12
    num_period = 2

    dt = T / num_period
    S0 = 130
    K = 130

    sigma = 0.3
    
    stock = Stock(symbol, S0, sigma)
    
    option = EuropeanCallOption(stock, T, K)
    
    model_price = model.calc_model_price(option)

    
    delta = model.calc_delta(option)
    gamma = model.calc_gamma(option)
    theta = model.calc_theta(option)
    vega = model.calc_vega(option)
    rho = model.calc_rho(option)
    parity = model.calc_parity_price(option,model_price)
    
    print("Model price: ",model_price)
    print("delta: ",delta)
    print("gamma: ",gamma)
    print("theta: ",theta)
    print("vega: ",vega)
    print("rho:",rho)
    print("parity: ",parity)

    
    
    
if __name__ == "__main__":
    _test()
    
