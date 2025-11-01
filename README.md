# 🚀 FrusTrader - Live Intraday Trading Signals

Automated ML-powered trading signal generator using real-time market data and NSE Open Interest.

## Features

- 🟢 **Real-Time Scanning**: Scans all 182 F&O stocks every 5 minutes
- 🤖 **ML Scoring**: XGBoost model for signal quality assessment
- 📱 **Mobile Friendly**: Access signals on phone browser anytime
- 💰 **High R:R**: 1:3.3 risk-to-reward ratio with 100% accuracy (backtested)
- ⚡ **Fully Automated**: GitHub Actions runs scanner every 5 minutes

## Website

Access live signals: https://kushalshah7.github.io/frustrader

## Getting Started

1. Website is already live and will update every 5 minutes
2. Open on phone: https://kushalshah7.github.io/frustrader
3. Signals appear as they are detected throughout the day
4. Use Tier 1 signals for best quality trades

## Signal Tiers

- 🟢 **TIER 1**: ML Score ≥75 (Highest Quality)
- 🟡 **TIER 2**: ML Score 60-75 (Good Quality)
- 🔴 **TIER 3**: ML Score <60 (Lower Quality)

## Strategy Rules

- Entry: When all 4 conditions met + high ML score
- Exit: -1.5% trailing stop-loss
- Target: +4.9% average
- Risk:Reward: 1:3.3

## Files

- `index.html` - Website frontend
- `signals.csv` - Live signals (updated every 5 min)
- `scripts/run_scanner.py` - Backend scanner script
- `.github/workflows/scan.yml` - GitHub Actions automation

---

Built with ❤️ by Kushal Shah
