#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass


BTC_BASE58 = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")
BTC_BECH32 = re.compile(r"^bc1[a-z0-9]{25,90}$", re.IGNORECASE)
LTC_BASE58 = re.compile(r"^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$")
LTC_BECH32 = re.compile(r"^ltc1[a-z0-9]{25,90}$", re.IGNORECASE)


@dataclass
class AddressReview:
    chain: str
    address: str
    format_status: str
    explorer_urls: list[str]
    safety_note: str


def review_address(chain: str, address: str) -> AddressReview:
    normalized_chain = chain.lower()
    normalized_address = address.strip()

    if normalized_chain == "btc":
        valid = bool(BTC_BASE58.match(normalized_address) or BTC_BECH32.match(normalized_address))
        urls = [
            f"https://mempool.space/address/{normalized_address}",
            f"https://blockstream.info/address/{normalized_address}",
        ]
    elif normalized_chain == "ltc":
        valid = bool(LTC_BASE58.match(normalized_address) or LTC_BECH32.match(normalized_address))
        urls = [
            f"https://blockchair.com/litecoin/address/{normalized_address}",
            f"https://litecoinspace.org/address/{normalized_address}",
        ]
    else:
        raise ValueError("chain must be btc or ltc")

    return AddressReview(
        chain=normalized_chain,
        address=normalized_address,
        format_status="format-check-pass" if valid else "format-check-review",
        explorer_urls=urls,
        safety_note="Read-only review. Never collect seed phrases, private keys, wallet files, or credentials.",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a defensive BTC/LTC address review record.")
    parser.add_argument("--chain", required=True, choices=["btc", "ltc"])
    parser.add_argument("--address", required=True)
    args = parser.parse_args()

    result = review_address(args.chain, args.address)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
