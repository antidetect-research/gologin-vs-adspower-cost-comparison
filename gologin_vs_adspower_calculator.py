#!/usr/bin/env python3
"""
GoLogin vs AdsPower Monthly & Coupon Discount Comparison Calculator 2026.
Models coupon savings and annualized profile capacity.
"""
import argparse

def calculate_comparison(gologin_cost, adspower_base, discount_pct):
    discounted_adspower = adspower_base * (1.0 - discount_pct / 100.0)
    monthly_diff = gologin_cost - discounted_adspower
    annual_diff = monthly_diff * 12.0
    return {
        "gologin_cost": gologin_cost,
        "adspower_base": adspower_base,
        "discounted_adspower": discounted_adspower,
        "monthly_diff": monthly_diff,
        "annual_diff": annual_diff
    }

def main():
    parser = argparse.ArgumentParser(description="GoLogin vs AdsPower Cost Comparison")
    parser.add_argument("--gologin-cost", type=float, default=49.0, help="GoLogin Professional monthly fee in USD (default: $49.00)")
    parser.add_argument("--adspower-base", type=float, default=50.0, help="AdsPower Pro base monthly in USD (default: $50.00)")
    parser.add_argument("--discount-pct", type=float, default=20.0, help="Promotional discount percentage (default: 20.0%)")
    args = parser.parse_args()

    res = calculate_comparison(args.gologin_cost, args.adspower_base, args.discount_pct)
    print(f"GoLogin Monthly Cost:    ${res['gologin_cost']:.2f}/mo")
    print(f"AdsPower Discounted Cost:${res['discounted_adspower']:.2f}/mo")
    print(f"Monthly Cost Difference: ${res['monthly_diff']:.2f}/mo")
    print(f"Annual Net Advantage:    ${res['annual_diff']:.2f}/year")

if __name__ == "__main__":
    main()
