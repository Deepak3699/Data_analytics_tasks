# dataset_generator.py
import numpy as np
import pandas as pd
import random

# ============================================================
# GENERATING SYNTHETIC WEBSITE TRAFFIC DATA
# ============================================================

def generate_website_traffic_data(seed=42):
    """
    Generate synthetic A/B test data for a website.
    
    Scenario:
    ---------
    An e-commerce website wants to test a NEW button color (Green)
    vs the OLD button color (Blue) to see which drives more conversions.
    
    Group A = Control Group   → OLD design (Blue Button)
    Group B = Treatment Group → NEW design (Green Button)
    """
    
    np.random.seed(seed)
    random.seed(seed)
    
    # ── Parameters ──────────────────────────────────────────
    n_visitors_A = 1000   # Visitors who saw OLD design
    n_visitors_B = 1000   # Visitors who saw NEW design
    
    conv_rate_A  = 0.10   # 10% conversion rate (baseline)
    conv_rate_B  = 0.13   # 13% conversion rate (new design - slightly better)
    
    # ── Generate Group A (Control) ───────────────────────────
    group_A = pd.DataFrame({
        'visitor_id'      : [f'A_{i:04d}' for i in range(n_visitors_A)],
        'group'           : 'A (Control)',
        'design'          : 'Blue Button',
        'converted'       : np.random.binomial(1, conv_rate_A, n_visitors_A),
        'time_on_page_sec': np.random.normal(120, 30, n_visitors_A).clip(10, 300),
        'pages_visited'   : np.random.poisson(3.5, n_visitors_A).clip(1, 15),
        'revenue'         : np.where(
                                np.random.binomial(1, conv_rate_A, n_visitors_A),
                                np.random.normal(50, 15, n_visitors_A).clip(10, 150),
                                0
                            )
    })
    
    # ── Generate Group B (Treatment) ────────────────────────
    group_B = pd.DataFrame({
        'visitor_id'      : [f'B_{i:04d}' for i in range(n_visitors_B)],
        'group'           : 'B (Treatment)',
        'design'          : 'Green Button',
        'converted'       : np.random.binomial(1, conv_rate_B, n_visitors_B),
        'time_on_page_sec': np.random.normal(135, 28, n_visitors_B).clip(10, 300),
        'pages_visited'   : np.random.poisson(4.0, n_visitors_B).clip(1, 15),
        'revenue'         : np.where(
                                np.random.binomial(1, conv_rate_B, n_visitors_B),
                                np.random.normal(55, 15, n_visitors_B).clip(10, 150),
                                0
                            )
    })
    
    # ── Combine & Save ───────────────────────────────────────
    df = pd.concat([group_A, group_B], ignore_index=True)
    df.to_csv('website_traffic_data.csv', index=False)
    
    print("✅ Dataset Generated Successfully!")
    print(f"   Total Records : {len(df)}")
    print(f"   Group A Size  : {len(group_A)}")
    print(f"   Group B Size  : {len(group_B)}")
    print(f"   Columns       : {list(df.columns)}")
    print(f"\n   Preview:")
    print(df.head(10).to_string(index=False))
    
    return df


if __name__ == "__main__":
    df = generate_website_traffic_data()