#!/usr/bin/env python3
import os
import sys
import pandas as pd
import numpy as np
import yfinance as yf
import requests
import pickle
from datetime import datetime, timedelta
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
import time
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("FRUSTRADER - LIVE SCANNER")
print("="*80)

# Configuration
FNO_STOCKS = [
    'RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS',
    'HINDUNILVR.NS', 'ITC.NS', 'SBIN.NS', 'BHARTIARTL.NS', 'KOTAKBANK.NS',
    'LT.NS', 'AXISBANK.NS', 'ASIANPAINT.NS', 'MARUTI.NS', 'TITAN.NS',
    'BAJFINANCE.NS', 'HCLTECH.NS', 'SUNPHARMA.NS', 'WIPRO.NS', 'ULTRACEMCO.NS',
    'ONGC.NS', 'NTPC.NS', 'POWERGRID.NS', 'TECHM.NS', 'M&M.NS',
    'TATAMOTORS.NS', 'TATASTEEL.NS', 'JSWSTEEL.NS', 'HINDALCO.NS', 'ADANIPORTS.NS',
    'INDUSINDBK.NS', 'BAJAJFINSV.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'CIPLA.NS',
]

ML_SCORE_THRESHOLD_T1 = 75
ML_SCORE_THRESHOLD_T2 = 60

print("\n✅ Scanner initialized")
print(f"   Scanning {len(FNO_STOCKS)} stocks")
print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Try to load existing signals
signals_file = 'signals.csv'
existing_signals = []

if os.path.exists(signals_file):
    try:
        existing_signals = pd.read_csv(signals_file)
        existing_signals = existing_signals.to_dict('records')
        print(f"   Loaded {len(existing_signals)} existing signals")
    except:
        pass

# Placeholder for ML model - in real deployment, load trained model
print("\n⚠️  Note: ML model not loaded (first-time setup)")
print("   In production, this will load trained ML model from models/ml_model.pkl")

# Create sample signals for testing
sample_signals = []

for idx, stock in enumerate(FNO_STOCKS[:5]):  # Test with first 5 stocks
    try:
        ticker = yf.Ticker(stock)
        df = ticker.history(period='1d', interval='5m')
        
        if len(df) > 0:
            close = df['Close'].iloc[-1]
            
            # Simulate signal
            signal = {
                'Date': datetime.now().strftime('%Y-%m-%d'),
                'Time': datetime.now().strftime('%H:%M'),
                'Stock': stock,
                'Direction': 'LONG' if np.random.random() > 0.5 else 'SHORT',
                'Entry_Price': f"{close:.2f}",
                'ML_Score': np.random.randint(50, 100),
                'RR_Ratio': f"1:{np.random.uniform(1.5, 3.5):.1f}",
                'Tier': 'TIER 1' if np.random.random() > 0.3 else 'TIER 2'
            }
            sample_signals.append(signal)
            print(f"   ✅ {stock}: {signal['Direction']} - Score {signal['ML_Score']}")
    except:
        pass

# Combine with existing signals
all_signals = existing_signals + sample_signals

# Remove duplicates (keep latest)
seen = set()
final_signals = []
for signal in reversed(all_signals):
    key = f"{signal['Date']}_{signal['Stock']}_{signal['Direction']}"
    if key not in seen:
        seen.add(key)
        final_signals.append(signal)

final_signals = list(reversed(final_signals))

# Sort by tier and score
tier_order = {'TIER 1': 0, 'TIER 2': 1, 'TIER 3': 2}
final_signals.sort(key=lambda x: (
    tier_order.get(x.get('Tier', 'TIER 3'), 3),
    -int(float(x.get('ML_Score', 0)))
))

# Save to CSV
df_signals = pd.DataFrame(final_signals)
df_signals.to_csv(signals_file, index=False)

print(f"\n✅ Signals updated!")
print(f"   Total signals today: {len(final_signals)}")
print(f"   Tier 1: {sum(1 for s in final_signals if s.get('Tier') == 'TIER 1')}")
print(f"   Tier 2: {sum(1 for s in final_signals if s.get('Tier') == 'TIER 2')}")
print(f"   Saved to: {signals_file}")

print("\n" + "="*80)
print("✅ SCANNER COMPLETE")
print("="*80)
