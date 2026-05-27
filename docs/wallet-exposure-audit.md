# Wallet Exposure Audit Guidance

This document replaces unsafe public framing around "key extraction" with a defensive exposure-audit model.

## Allowed Public Scope

- Explain how public keys may appear in normal blockchain activity.
- Review whether a public address has visible suspicious transactions.
- Document whether a user shared a seed phrase, private key, or wallet file with anyone.
- Help users classify risk without collecting secret material.

## Not Allowed In Public Tooling

- Extracting private keys
- Requesting seed phrases
- Uploading wallet backup files
- Bypassing wallet protections
- Automating unauthorized access
- Publishing exploit instructions

## Safer User-Facing Language

Use "wallet exposure audit" or "key exposure risk review" instead of phrases that suggest extracting private keys or secrets.
