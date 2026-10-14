#This file is not completely finished yet.
#The purpose of this file is to automatically test whether functions work correctly.

# test_finance_commands.py
import pytest
from finance_commands import fetch_realtime_price 

# Test 1: Testing a successful outcome
def test_fetch_realtime_price_success():
    print("Starting real time ticker price testing...")
    # 1. ARRANGE
    ticker = "AAPL"
    
    # 2. ACT
    price = fetch_realtime_price(ticker)
    
    # 3. ASSERT
    assert price is not None       # Ensure we didn't get nothing back
    assert type(price) == float    # Ensure the price is a decimal number
    assert price > 0               # Ensure Apple's stock price is above $0
    print("Testing completed, no errors found")

# Test 2: Testing an expected failure
def test_fetch_realtime_price_invalid_ticker():
    print("Starting real time invalid price testing...")
    # 1. ARRANGE
    bad_ticker = "FAKE12345"
    
    # 2. ACT & ASSERT
    with pytest.raises(ValueError):
        fetch_realtime_price(bad_ticker)
    print("Testing completed, no errors found")

# Test 3: Testing multiple metals correctly
def test_fetch_realtime_metal_price_success():
    print("Starting real time metal price testing...")
    metal_tickers = ["GC=F", "SI=F", "HG=F", "PA=F", "PL=F"]
    
    # Loop directly over the items in the list
    for ticker in metal_tickers:
        price = fetch_realtime_price(ticker)
        assert price is not None, f"Failed to get price for {ticker}"
        assert type(price) == float, f"Price for {ticker} is not a float"
        assert price > 0, f"Price for {ticker} is zero or negative"
        
    print("Testing completed, no errors found")
