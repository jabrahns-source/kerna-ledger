#!/usr/bin/env python3
"""
Vercel serverless entry-point stub for the Kerna-Ledger umbrella.

Production serverless handlers live in the dedicated runtime repositories
(vera-enterprise-engine, Q-Reg, GridPulse). This file prevents 404s for
legacy Vercel project configurations while making the relocation explicit.
"""

def handler(request):
    return {
        "statusCode": 301,
        "headers": {
            "Location": "https://github.com/jabrahns-source/vera-enterprise-engine",
            "Content-Type": "text/plain",
        },
        "body": "Kerna-Ledger production surface moved to vera-enterprise-engine and Q-Reg.",
    }

# For local testing
if __name__ == "__main__":
    print(handler(None))
