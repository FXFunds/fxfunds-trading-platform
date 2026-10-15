#!/usr/bin/env node
/**
 * @fxfunds/fxfunds-trading-platform
 * FXFunds Trading Platform reference data — library and CLI.
 *
 * Returns company-reported public information about FXFunds
 * (https://fxfunds.com/): profile, market categories, payment status
 * and a verify-before-trading checklist.
 *
 * All data is company-reported and NOT independently verified.
 * No trading functionality. Not financial advice.
 */

export const VERSION = "1.0.0";
export const WEBSITE = "https://fxfunds.com/";
export const DOCS = "https://fxfunds-trading-platform.readthedocs.io";
export const REPO = "https://github.com/fxfunds/fxfunds-trading-platform";

export type Status =
  | "verified"
  | "company-reported"
  | "company-described"
  | "pending"
  | "not-confirmed"
  | "not-published";

export interface Market {
  market: string;
  label: string;
  coverage: string;
  status: Status;
}

export interface Payment {
  method: string;
  coins: string;
  networks: string;
  fees: string;
  status: Status;
}

export const PROFILE = {
  name: "FXFunds",
  alternateName: "Fxfunds",
  website: WEBSITE,
  description:
    "FXFunds describes itself as a digital trading platform focused on multi-asset markets, stablecoin-based transactions and blockchain-related financial technology.",
  location: "United States (company-reported; subject to verification)",
  dataStatus: "company-reported" as Status,
  docs: DOCS,
  repository: REPO,
};

export const MARKETS: Market[] = [
  { market: "forex", label: "Forex", coverage: "Currency pair trading", status: "company-reported" },
  { market: "commodities", label: "Commodities", coverage: "Commodity markets including gold and oil", status: "company-reported" },
  { market: "stocks", label: "Stocks", coverage: "Equity markets", status: "company-reported" },
  { market: "indices", label: "Indices", coverage: "Stock index markets", status: "company-reported" },
  { market: "crypto", label: "Cryptocurrencies", coverage: "Digital asset markets", status: "company-reported" },
  { market: "gold", label: "Gold", coverage: "Headline market on the website", status: "company-reported" },
  { market: "oil", label: "Oil", coverage: "Headline market on the website", status: "company-reported" },
];

export const PAYMENTS: Payment[] = [
  { method: "stablecoins", coins: "pending", networks: "pending", fees: "pending", status: "company-described" },
  { method: "bank-transfer", coins: "n/a", networks: "n/a", fees: "pending", status: "not-confirmed" },
  { method: "cards", coins: "n/a", networks: "n/a", fees: "pending", status: "not-confirmed" },
];

export const PENDING: string[] = [
  "Registered legal entity and jurisdiction",
  "Regulatory authorisation and licence numbers",
  "Instrument type (spot / CFD / futures)",
  "Leverage, spreads, commissions and fees",
  "Account types and minimum deposit",
  "Supported stablecoins and networks",
  "Technical whitepaper and security audit",
];

export const CHECKLIST: string[] = [
  "Find the registered legal entity, registration number and jurisdiction.",
  "Look up that entity on the regulator's own public register.",
  "Read the risk disclosure and client agreement in full.",
  "Read independent reviews, not platform-published testimonials.",
  "Make a small test withdrawal before depositing more.",
  "Confirm the exact coin and network before sending any stablecoin.",
];

export const STATUS_LEGEND: Record<string, string> = {
  verified: "Confirmed with supporting evidence",
  "company-reported": "Stated by FXFunds, not independently checked",
  pending: "Not yet supplied by FXFunds",
  "not-published": "No public document exists",
};

export const getProfile = () => ({ ...PROFILE });
export const getMarkets = (): Market[] => MARKETS.map((m) => ({ ...m }));
export const getMarket = (key: string): Market | undefined =>
  MARKETS.find((m) => m.market === key.toLowerCase().trim());
export const getPayments = (): Payment[] => PAYMENTS.map((p) => ({ ...p }));
export const getPending = (): string[] => [...PENDING];
export const getChecklist = (): string[] => [...CHECKLIST];
export const toJSON = (): string =>
  JSON.stringify(
    { version: VERSION, profile: PROFILE, markets: MARKETS, payments: PAYMENTS, pending: PENDING, checklist: CHECKLIST, statusLegend: STATUS_LEGEND },
    null,
    2
  );

const USAGE = `FXFunds Trading Platform — reference data (company-reported)

Usage: npx fxfunds-info <command> [arg]

Commands:
  profile          Company profile
  markets          Market categories listed by FXFunds
  market <key>     One market (forex, commodities, stocks, indices, crypto, gold, oil)
  payments         Payment methods and status
  pending          Items awaiting confirmation
  checklist        Verify-before-trading checklist
  json             All data as JSON
`;

export function main(argv: string[] = process.argv.slice(2)): number {
  const cmd = (argv[0] || "help").toLowerCase();
  switch (cmd) {
    case "profile":
      Object.entries(PROFILE).forEach(([k, v]) => console.log(`${k.padEnd(15)} ${v}`));
      break;
    case "markets":
      MARKETS.forEach((m) => console.log(`${m.label.padEnd(17)} ${m.coverage.padEnd(42)} [${m.status}]`));
      break;
    case "market": {
      const m = argv[1] ? getMarket(argv[1]) : undefined;
      if (!m) {
        console.log("Unknown market. Try: " + MARKETS.map((x) => x.market).join(", "));
        return 1;
      }
      console.log(JSON.stringify(m, null, 2));
      break;
    }
    case "payments":
      PAYMENTS.forEach((p) => console.log(`${p.method.padEnd(14)} coins=${p.coins.padEnd(8)} networks=${p.networks.padEnd(8)} [${p.status}]`));
      break;
    case "pending":
      PENDING.forEach((x, i) => console.log(`${i + 1}. ${x}`));
      break;
    case "checklist":
      CHECKLIST.forEach((x, i) => console.log(`${i + 1}. ${x}`));
      break;
    case "json":
      console.log(toJSON());
      break;
    default:
      console.log(USAGE);
      return ["help", "-h", "--help"].includes(cmd) ? 0 : 1;
  }
  console.log(`\nCompany-reported, not independently verified. Website: ${WEBSITE}`);
  return 0;
}

if (require.main === module) {
  process.exitCode = main();
}
