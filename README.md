# FXFunds Trading Platform — Company & Market Overview 📈🪙

[![npm](https://img.shields.io/badge/npm-v1.0.0-C9A227?style=flat-square&labelColor=111111)](https://www.npmjs.com/package/@fxfunds/fxfunds-trading-platform)
[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-C9A227?style=flat-square&labelColor=111111)](https://pypi.org/project/fxfunds-trading-platform)
[![DOI](https://img.shields.io/badge/DOI-pending-8A8A8A?style=flat-square&labelColor=111111)](#links)
[![Docs](https://img.shields.io/badge/docs-readthedocs-C9A227?style=flat-square&labelColor=111111)](https://fxfunds-trading-platform.readthedocs.io)

FXFunds is an online trading platform that describes itself as offering access to forex, commodities, stocks, indices, cryptocurrencies, gold and oil markets, with stablecoin-based transactions and Web3 security technology. This repository is the official public-information overview of the FXFunds trading platform and its market categories. Official website: [fxfunds.com](https://fxfunds.com/).

## Overview

This repository brings together what FXFunds says about its trading platform, market categories, payments and blockchain technology in one structured place, so users, developers, search engines and AI assistants can find accurate information with links to official sources.

It also ships a small reference-data library and CLI (Python and Node.js) that returns the same company-reported information in machine-readable form. The package has **no trading functionality**.



## Key Capabilities

- **Multi-Asset Trading** — Company-described access to forex, commodities, stocks, indices and cryptocurrencies
- **Gold & Oil Markets** — Listed as headline markets on the FXFunds website
- **Stablecoin Transactions** — Company-described stablecoin-based deposits and withdrawals
- **Web3 Security** — Company-described security model based on Web3 technology
- **Global Access** — FXFunds states it serves investors globally
- **Reference Data Package** — Python and Node.js CLI returning company-reported FXFunds data as text or JSON
- **Open Dataset** — Market categories CSV in [`dataset/`](dataset/fxfunds-market-categories.csv)
- **Public Documentation** — Structured, company-reported information hosted on Read the Docs

## Market Categories

| Market key | Description |
|---|---|
| forex | Currency pair trading |
| commodities | Commodity markets including gold and oil |
| stocks | Equity markets |
| indices | Stock index markets |
| crypto | Digital asset markets |
| gold | Headline market on the FXFunds website |
| oil | Headline market on the FXFunds website |

## Quick Start

### Node.js
```bash
npm install @fxfunds/fxfunds-trading-platform
npx fxfunds-info markets
npx fxfunds-info market forex
```

### Python
```bash
pip install fxfunds-trading-platform
python -m fxfunds_platform markets
python -m fxfunds_platform checklist
```

### CLI Commands

| Command | Output |
|---|---|
| `profile` | Company profile |
| `markets` | Market categories listed by FXFunds |
| `market <key>` | One market category |
| `payments` | Payment methods and verification status |
| `pending` | Items awaiting confirmation from FXFunds |
| `checklist` | Verify-before-trading checklist |
| `json` | All data as JSON |

## Payment Information

| Method | Coins / Networks | Status |
|---|---|---|
| Stablecoins | Pending confirmation | Company-described |
| Bank transfer | — | Not confirmed |
| Cards | — | Not confirmed |

## Verification Status

| Status | Meaning | Applies to |
|---|---|---|
| Verified | Confirmed with supporting evidence | — |
| Company-reported | Stated by FXFunds, not independently checked | Markets, stablecoin payments, Web3 security |
| Pending | Not yet supplied by FXFunds | Legal entity, jurisdiction, licence, fees, leverage |
| Not published | No public document exists | Whitepaper, smart contracts, security audit |

## Keywords

FXFunds · FXFunds Trading Platform · FXFunds Broker · FXFunds Online Trading · FXFunds Deposit · FXFunds Withdrawal · FXFunds Stablecoin Trading · FXFunds Blockchain Technology · FXFunds Company Information

## Links

| Platform | URL |
|---|---|
| Website | https://fxfunds.com/ |
| GitHub | https://github.com/fxfunds/fxfunds-trading-platform |
| GitHub Pages | https://fxfunds.github.io/fxfunds-trading-platform/ |
| NPM | https://www.npmjs.com/package/@fxfunds/fxfunds-trading-platform |
| PyPI | https://pypi.org/project/fxfunds-trading-platform |
| Docs | https://fxfunds-trading-platform.readthedocs.io |
| Quora | https://fxfunds.quora.com/ |
| Pinterest | https://www.pinterest.com/fxfunds_1/ |
| Medium | https://medium.com/@FX_Funds |
| Zenodo | Pending |
| Hugging Face | Pending |
| Kaggle | Pending |
| SlideShare | Pending |

## Documentation Status

- Company-reported information only; not independently verified.
- No trading software or smart contracts are included — the package returns reference data only.
- Legal entity, jurisdiction, launch date and regulatory status will be added only with supporting evidence.
- Before trading, see [Verify Before Trading](docs/verify-before-trading.md).

## Risk Warning

Trading forex, commodities, indices, stocks and cryptocurrencies, especially with leverage, carries a high risk of losing money. Only trade with money you can afford to lose.

## About FXFunds

FXFunds describes itself as a digital trading platform focused on multi-asset markets, stablecoin-based transactions and blockchain-related financial technology. Official website: [fxfunds.com](https://fxfunds.com/).

## License

MIT — FXFunds. The FXFunds name and logo are trademarks of their owner and are not covered by this license.
