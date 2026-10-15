"""
fxfunds_platform — FXFunds Trading Platform reference data.

A small, dependency-free library and CLI that returns company-reported public
information about FXFunds (https://fxfunds.com/): platform profile, market
categories, payment information status and a verify-before-trading checklist.

All data is company-reported and NOT independently verified.
This package contains no trading functionality and is not financial advice.
"""

import json
import sys

__version__ = "1.0.0"

WEBSITE = "https://fxfunds.com/"
DOCS = "https://fxfunds-trading-platform.readthedocs.io"
REPO = "https://github.com/fxfunds/fxfunds-trading-platform"

PROFILE = {
    "name": "FXFunds",
    "alternate_name": "Fxfunds",
    "website": WEBSITE,
    "description": (
        "FXFunds describes itself as a digital trading platform focused on "
        "multi-asset markets, stablecoin-based transactions and "
        "blockchain-related financial technology."
    ),
    "location": "United States (company-reported; subject to verification)",
    "data_status": "company-reported",
    "docs": DOCS,
    "repository": REPO,
}

MARKETS = [
    {"market": "forex", "label": "Forex", "coverage": "Currency pair trading", "status": "company-reported"},
    {"market": "commodities", "label": "Commodities", "coverage": "Commodity markets including gold and oil", "status": "company-reported"},
    {"market": "stocks", "label": "Stocks", "coverage": "Equity markets", "status": "company-reported"},
    {"market": "indices", "label": "Indices", "coverage": "Stock index markets", "status": "company-reported"},
    {"market": "crypto", "label": "Cryptocurrencies", "coverage": "Digital asset markets", "status": "company-reported"},
    {"market": "gold", "label": "Gold", "coverage": "Headline market on the website", "status": "company-reported"},
    {"market": "oil", "label": "Oil", "coverage": "Headline market on the website", "status": "company-reported"},
]

PAYMENTS = [
    {"method": "stablecoins", "coins": "pending", "networks": "pending", "fees": "pending", "status": "company-described"},
    {"method": "bank-transfer", "coins": "n/a", "networks": "n/a", "fees": "pending", "status": "not-confirmed"},
    {"method": "cards", "coins": "n/a", "networks": "n/a", "fees": "pending", "status": "not-confirmed"},
]

PENDING = [
    "Registered legal entity and jurisdiction",
    "Regulatory authorisation and licence numbers",
    "Instrument type (spot / CFD / futures)",
    "Leverage, spreads, commissions and fees",
    "Account types and minimum deposit",
    "Supported stablecoins and networks",
    "Technical whitepaper and security audit",
]

CHECKLIST = [
    "Find the registered legal entity, registration number and jurisdiction.",
    "Look up that entity on the regulator's own public register.",
    "Read the risk disclosure and client agreement in full.",
    "Read independent reviews, not platform-published testimonials.",
    "Make a small test withdrawal before depositing more.",
    "Confirm the exact coin and network before sending any stablecoin.",
]

STATUS_LEGEND = {
    "verified": "Confirmed with supporting evidence",
    "company-reported": "Stated by FXFunds, not independently checked",
    "pending": "Not yet supplied by FXFunds",
    "not-published": "No public document exists",
}


def get_profile():
    """Return the company-reported FXFunds profile."""
    return dict(PROFILE)


def get_markets():
    """Return the market categories FXFunds lists."""
    return [dict(m) for m in MARKETS]


def get_market(key):
    """Return one market category by key (e.g. 'forex'), or None."""
    key = key.lower().strip()
    for m in MARKETS:
        if m["market"] == key:
            return dict(m)
    return None


def get_payments():
    """Return payment method information and its verification status."""
    return [dict(p) for p in PAYMENTS]


def get_pending():
    """Return items still awaiting confirmation from FXFunds."""
    return list(PENDING)


def get_checklist():
    """Return the verify-before-trading checklist."""
    return list(CHECKLIST)


def to_json():
    """Return all reference data as a JSON string."""
    return json.dumps(
        {
            "version": __version__,
            "profile": PROFILE,
            "markets": MARKETS,
            "payments": PAYMENTS,
            "pending": PENDING,
            "checklist": CHECKLIST,
            "status_legend": STATUS_LEGEND,
        },
        indent=2,
    )


USAGE = """FXFunds Trading Platform — reference data (company-reported)

Usage: python -m fxfunds_platform <command> [arg]

Commands:
  profile          Company profile
  markets          Market categories listed by FXFunds
  market <key>     One market (forex, commodities, stocks, indices, crypto, gold, oil)
  payments         Payment methods and status
  pending          Items awaiting confirmation
  checklist        Verify-before-trading checklist
  json             All data as JSON
"""


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    cmd = args[0].lower() if args else "help"

    if cmd == "profile":
        for k, v in PROFILE.items():
            print(f"{k:15} {v}")
    elif cmd == "markets":
        for m in MARKETS:
            print(f"{m['label']:17} {m['coverage']:42} [{m['status']}]")
    elif cmd == "market":
        m = get_market(args[1]) if len(args) > 1 else None
        if not m:
            print("Unknown market. Try: " + ", ".join(x["market"] for x in MARKETS))
            return 1
        print(json.dumps(m, indent=2))
    elif cmd == "payments":
        for p in PAYMENTS:
            print(f"{p['method']:14} coins={p['coins']:8} networks={p['networks']:8} [{p['status']}]")
    elif cmd == "pending":
        for i, item in enumerate(PENDING, 1):
            print(f"{i}. {item}")
    elif cmd == "checklist":
        for i, item in enumerate(CHECKLIST, 1):
            print(f"{i}. {item}")
    elif cmd == "json":
        print(to_json())
    else:
        print(USAGE)
        return 0 if cmd in ("help", "-h", "--help") else 1

    print(f"\nCompany-reported, not independently verified. Website: {WEBSITE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
