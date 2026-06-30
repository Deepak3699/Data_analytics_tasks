# ab_testing.py

# ============================================================
# IMPORTING LIBRARIES
# ============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from statsmodels.stats.power import NormalIndPower
import warnings
warnings.filterwarnings('ignore')

# ── Plot Style ───────────────────────────────────────────────
plt.style.use('seaborn-v0_8-whitegrid')
colors = {'A': '#4C72B0', 'B': '#55A868', 'neutral': '#DD8452'}

print("=" * 60)
print("      A/B TESTING ANALYSIS - WEBSITE TRAFFIC DATA")
print("=" * 60)


# ============================================================
# STEP 1: LOAD DATA
# ============================================================
from dataset_generator import generate_website_traffic_data

df = generate_website_traffic_data()

# Separate Groups
group_A = df[df['group'] == 'A (Control)']
group_B = df[df['group'] == 'B (Treatment)']

print("\n" + "=" * 60)
print("STEP 1: DATA OVERVIEW")
print("=" * 60)
print(df.describe().round(3))
print(f"\nMissing Values:\n{df.isnull().sum()}")


# ============================================================
# STEP 2: EXPLORATORY DATA ANALYSIS
# ============================================================
print("\n" + "=" * 60)
print("STEP 2: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Key Metrics per Group
summary = df.groupby('group').agg(
    Total_Visitors   = ('visitor_id'      , 'count'),
    Total_Conversions= ('converted'       , 'sum'),
    Conversion_Rate  = ('converted'       , 'mean'),
    Avg_Time_on_Page = ('time_on_page_sec', 'mean'),
    Avg_Pages_Visited= ('pages_visited'   , 'mean'),
    Total_Revenue    = ('revenue'         , 'sum'),
    Avg_Revenue      = ('revenue'         , 'mean'),
).round(4)

print("\n📊 Group Summary Statistics:")
print(summary.to_string())

# Conversion counts
conv_A = group_A['converted'].sum()
conv_B = group_B['converted'].sum()
n_A    = len(group_A)
n_B    = len(group_B)
rate_A = conv_A / n_A
rate_B = conv_B / n_B
lift   = ((rate_B - rate_A) / rate_A) * 100

print(f"\n📈 Conversion Summary:")
print(f"   Group A → Conversions: {conv_A}/{n_A} = {rate_A:.2%}")
print(f"   Group B → Conversions: {conv_B}/{n_B} = {rate_B:.2%}")
print(f"   Absolute Lift        : {(rate_B - rate_A):.4f} ({(rate_B - rate_A)*100:.2f}%)")
print(f"   Relative Lift        : {lift:.2f}%")


# ============================================================
# STEP 3: HYPOTHESIS TESTING
# ============================================================
print("\n" + "=" * 60)
print("STEP 3: HYPOTHESIS TESTING")
print("=" * 60)

alpha = 0.05  # Significance level (95% confidence)

print(f"""
📋 Hypotheses:
   H₀ (Null Hypothesis)       : Conversion Rate A = Conversion Rate B
                                 (New design has NO effect)
   H₁ (Alternative Hypothesis): Conversion Rate A ≠ Conversion Rate B
                                 (New design HAS an effect)
   
   Significance Level (α)     : {alpha} (95% Confidence Level)
   Test Type                  : Two-tailed Z-test for Proportions
""")


# ── TEST 1: Z-Test for Proportions ───────────────────────────
print("─" * 50)
print("TEST 1: Z-Test for Proportions (Statsmodels)")
print("─" * 50)

count = np.array([conv_A, conv_B])   # [conversions_A, conversions_B]
nobs  = np.array([n_A, n_B])         # [total_A, total_B]

z_stat, p_value = proportions_ztest(count, nobs)

print(f"   Z-Statistic : {z_stat:.4f}")
print(f"   P-Value     : {p_value:.6f}")
print(f"   Alpha (α)   : {alpha}")
print()

if p_value < alpha:
    print("   ✅ RESULT: REJECT H₀")
    print("   📌 The difference IS statistically significant.")
    print("   📌 The new design (Group B) significantly affects conversion.")
else:
    print("   ❌ RESULT: FAIL TO REJECT H₀")
    print("   📌 The difference is NOT statistically significant.")
    print("   📌 No enough evidence that new design performs differently.")


# ── TEST 2: Chi-Square Test ──────────────────────────────────
print("\n" + "─" * 50)
print("TEST 2: Chi-Square Test (Independence Test)")
print("─" * 50)

# Contingency Table
#               Converted   Not Converted
# Group A       conv_A      n_A - conv_A
# Group B       conv_B      n_B - conv_B

contingency_table = np.array([
    [conv_A, n_A - conv_A],
    [conv_B, n_B - conv_B]
])

print("\nContingency Table:")
print(f"              Converted   Not Converted   Total")
print(f"Group A       {conv_A:<12} {n_A-conv_A:<15} {n_A}")
print(f"Group B       {conv_B:<12} {n_B-conv_B:<15} {n_B}")
print(f"Total         {conv_A+conv_B:<12} {(n_A-conv_A)+(n_B-conv_B):<15} {n_A+n_B}")

chi2, p_chi2, dof, expected = stats.chi2_contingency(contingency_table)

print(f"\n   Chi² Statistic : {chi2:.4f}")
print(f"   P-Value        : {p_chi2:.6f}")
print(f"   Degrees of Freedom: {dof}")

if p_chi2 < alpha:
    print("   ✅ RESULT: REJECT H₀ (Significant difference exists)")
else:
    print("   ❌ RESULT: FAIL TO REJECT H₀")


# ── TEST 3: T-Test (Revenue Comparison) ─────────────────────
print("\n" + "─" * 50)
print("TEST 3: Independent T-Test (Revenue Comparison)")
print("─" * 50)

rev_A = group_A['revenue']
rev_B = group_B['revenue']

t_stat, p_ttest = stats.ttest_ind(rev_A, rev_B)

print(f"   Group A Avg Revenue: ${rev_A.mean():.2f}")
print(f"   Group B Avg Revenue: ${rev_B.mean():.2f}")
print(f"   T-Statistic        : {t_stat:.4f}")
print(f"   P-Value            : {p_ttest:.6f}")

if p_ttest < alpha:
    print("   ✅ Revenue difference IS statistically significant.")
else:
    print("   ❌ Revenue difference is NOT statistically significant.")


# ============================================================
# STEP 4: CONFIDENCE INTERVALS
# ============================================================
print("\n" + "=" * 60)
print("STEP 4: CONFIDENCE INTERVALS (95%)")
print("=" * 60)

# ── CI for Proportions ───────────────────────────────────────
ci_low_A, ci_high_A = proportion_confint(conv_A, n_A, alpha=0.05, method='wilson')
ci_low_B, ci_high_B = proportion_confint(conv_B, n_B, alpha=0.05, method='wilson')

print(f"""
   Group A Conversion Rate: {rate_A:.4f}
   95% CI for Group A     : [{ci_low_A:.4f}, {ci_high_A:.4f}]
   → Interpretation: We are 95% confident that the TRUE
     conversion rate for Group A lies between 
     {ci_low_A:.2%} and {ci_high_A:.2%}

   Group B Conversion Rate: {rate_B:.4f}
   95% CI for Group B     : [{ci_low_B:.4f}, {ci_high_B:.4f}]
   → Interpretation: We are 95% confident that the TRUE
     conversion rate for Group B lies between 
     {ci_low_B:.2%} and {ci_high_B:.2%}
""")

# ── CI for Difference in Proportions ────────────────────────
diff = rate_B - rate_A
se_diff = np.sqrt((rate_A*(1-rate_A)/n_A) + (rate_B*(1-rate_B)/n_B))
z_critical = stats.norm.ppf(0.975)  # 1.96 for 95% CI

ci_diff_low  = diff - z_critical * se_diff
ci_diff_high = diff + z_critical * se_diff

print(f"   Difference (B - A)   : {diff:.4f} ({diff*100:.2f}%)")
print(f"   95% CI for Difference: [{ci_diff_low:.4f}, {ci_diff_high:.4f}]")
print(f"   → [{ci_diff_low*100:.2f}%, {ci_diff_high*100:.2f}%]")

if ci_diff_low > 0:
    print("   ✅ CI entirely above 0 → B is significantly BETTER than A")
elif ci_diff_high < 0:
    print("   ⚠️  CI entirely below 0 → B is significantly WORSE than A")
else:
    print("   ❌ CI includes 0 → No significant difference detected")


# ============================================================
# STEP 5: STATISTICAL POWER & SAMPLE SIZE
# ============================================================
print("\n" + "=" * 60)
print("STEP 5: STATISTICAL POWER ANALYSIS")
print("=" * 60)

effect_size = abs(rate_B - rate_A) / np.sqrt(
    (rate_A * (1-rate_A) + rate_B * (1-rate_B)) / 2
)

analysis = NormalIndPower()
power = analysis.solve_power(
    effect_size = effect_size,
    nobs1       = n_A,
    alpha       = alpha,
    alternative = 'two-sided'
)

required_n = analysis.solve_power(
    effect_size = effect_size,
    power       = 0.80,
    alpha       = alpha,
    alternative = 'two-sided'
)

print(f"   Effect Size           : {effect_size:.4f}")
print(f"   Achieved Power        : {power:.4f} ({power*100:.1f}%)")
print(f"   Required Sample/Group : {int(np.ceil(required_n))}")
print(f"   Actual Sample/Group   : {n_A}")
print(f"   {'✅ Adequately powered!' if power >= 0.8 else '⚠️  Under-powered test!'}")


# ============================================================
# STEP 6: VISUALIZATIONS
# ============================================================
print("\n" + "=" * 60)
print("STEP 6: GENERATING VISUALIZATIONS")
print("=" * 60)

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('A/B Testing Dashboard - Website Traffic Analysis',
             fontsize=16, fontweight='bold', y=1.01)


# ── PLOT 1: Conversion Rates with Error Bars ─────────────────
ax1 = axes[0, 0]
groups    = ['Group A\n(Blue Button)', 'Group B\n(Green Button)']
rates     = [rate_A, rate_B]
ci_errors = [
    [rate_A - ci_low_A, ci_high_A - rate_A],
    [rate_B - ci_low_B, ci_high_B - rate_B]
]
error_vals = np.array(ci_errors).T

bars = ax1.bar(groups, rates,
               color=[colors['A'], colors['B']],
               width=0.5, alpha=0.85, edgecolor='black', linewidth=1.2)

ax1.errorbar(groups, rates,
             yerr=error_vals,
             fmt='none', color='black',
             capsize=8, capthick=2, linewidth=2)

for bar, rate in zip(bars, rates):
    ax1.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.003,
             f'{rate:.2%}',
             ha='center', va='bottom', fontweight='bold', fontsize=12)

ax1.set_title('Conversion Rates with 95% CI', fontweight='bold')
ax1.set_ylabel('Conversion Rate')
ax1.set_ylim(0, max(rates) * 1.35)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))


# ── PLOT 2: Confidence Intervals Visualization ───────────────
ax2 = axes[0, 1]

ci_data = {
    'Group A\n(Control)' : (rate_A, ci_low_A, ci_high_A),
    'Group B\n(Treatment)': (rate_B, ci_low_B, ci_high_B),
}

y_positions = [2, 1]
for (label, (mean, lo, hi)), y_pos, color in zip(
        ci_data.items(), y_positions, [colors['A'], colors['B']]):
    
    ax2.hlines(y_pos, lo, hi, colors=color, linewidth=4, alpha=0.7)
    ax2.plot([lo, hi], [y_pos, y_pos], '|', color=color, markersize=15, mew=3)
    ax2.plot(mean, y_pos, 'o', color=color, markersize=10, zorder=5)
    ax2.text(mean, y_pos + 0.15, f'{mean:.2%}',
             ha='center', fontsize=10, fontweight='bold', color=color)
    ax2.text(lo - 0.001, y_pos, f'{lo:.2%}',
             ha='right', fontsize=8, color='gray')
    ax2.text(hi + 0.001, y_pos, f'{hi:.2%}',
             ha='left', fontsize=8, color='gray')

ax2.set_yticks(y_positions)
ax2.set_yticklabels(list(ci_data.keys()), fontsize=11)
ax2.set_xlabel('Conversion Rate')
ax2.set_title('95% Confidence Intervals\n(Wilson Method)', fontweight='bold')
ax2.set_xlim(0.06, 0.17)
ax2.set_ylim(0.5, 2.7)
ax2.axvline(x=rate_A, color=colors['A'], linestyle='--', alpha=0.4)
ax2.axvline(x=rate_B, color=colors['B'], linestyle='--', alpha=0.4)


# ── PLOT 3: Daily Conversion Distribution (Simulated) ────────
ax3 = axes[0, 2]

# Simulate daily conversion rates for 30 days
np.random.seed(42)
daily_conv_A = np.random.binomial(30, rate_A, 30) / 30
daily_conv_B = np.random.binomial(30, rate_B, 30) / 30
days = range(1, 31)

ax3.plot(days, daily_conv_A, color=colors['A'], label='Group A', 
         marker='o', markersize=4, linewidth=1.5, alpha=0.8)
ax3.plot(days, daily_conv_B, color=colors['B'], label='Group B',
         marker='s', markersize=4, linewidth=1.5, alpha=0.8)
ax3.axhline(y=rate_A, color=colors['A'], linestyle='--', alpha=0.5, linewidth=1)
ax3.axhline(y=rate_B, color=colors['B'], linestyle='--', alpha=0.5, linewidth=1)
ax3.fill_between(days, daily_conv_A, alpha=0.15, color=colors['A'])
ax3.fill_between(days, daily_conv_B, alpha=0.15, color=colors['B'])

ax3.set_title('Daily Conversion Rates (30 Days)', fontweight='bold')
ax3.set_xlabel('Day')
ax3.set_ylabel('Daily Conversion Rate')
ax3.legend()
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.0%}'))


# ── PLOT 4: Revenue Distribution ─────────────────────────────
ax4 = axes[1, 0]

# Only show revenue from converted users
rev_A_converted = group_A[group_A['revenue'] > 0]['revenue']
rev_B_converted = group_B[group_B['revenue'] > 0]['revenue']

ax4.hist(rev_A_converted, bins=25, color=colors['A'],
         alpha=0.6, label=f'Group A (μ=${rev_A_converted.mean():.1f})',
         edgecolor='white')
ax4.hist(rev_B_converted, bins=25, color=colors['B'],
         alpha=0.6, label=f'Group B (μ=${rev_B_converted.mean():.1f})',
         edgecolor='white')
ax4.axvline(rev_A_converted.mean(), color=colors['A'],
            linestyle='--', linewidth=2)
ax4.axvline(rev_B_converted.mean(), color=colors['B'],
            linestyle='--', linewidth=2)

ax4.set_title('Revenue Distribution\n(Converted Users Only)', fontweight='bold')
ax4.set_xlabel('Revenue ($)')
ax4.set_ylabel('Frequency')
ax4.legend()


# ── PLOT 5: Funnel Chart ──────────────────────────────────────
ax5 = axes[1, 1]

funnel_metrics = ['Visitors', 'Engaged\n(>2 pages)', 'Converted']
funnel_A = [n_A,
            (group_A['pages_visited'] > 2).sum(),
            conv_A]
funnel_B = [n_B,
            (group_B['pages_visited'] > 2).sum(),
            conv_B]

x = np.arange(len(funnel_metrics))
width = 0.35

bars_A = ax5.bar(x - width/2, funnel_A, width,
                 label='Group A', color=colors['A'], alpha=0.85,
                 edgecolor='black', linewidth=0.8)
bars_B = ax5.bar(x + width/2, funnel_B, width,
                 label='Group B', color=colors['B'], alpha=0.85,
                 edgecolor='black', linewidth=0.8)

for bar in bars_A:
    ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
             f'{int(bar.get_height())}', ha='center', va='bottom',
             fontsize=9, fontweight='bold')
for bar in bars_B:
    ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
             f'{int(bar.get_height())}', ha='center', va='bottom',
             fontsize=9, fontweight='bold')

ax5.set_title('Conversion Funnel Comparison', fontweight='bold')
ax5.set_xticks(x)
ax5.set_xticklabels(funnel_metrics)
ax5.set_ylabel('Count')
ax5.legend()


# ── PLOT 6: P-Value & Decision Zone ──────────────────────────
ax6 = axes[1, 2]

x_range = np.linspace(-4, 4, 400)
y_normal = stats.norm.pdf(x_range)

ax6.plot(x_range, y_normal, 'k-', linewidth=2, label='Standard Normal')

# Rejection regions
z_crit = 1.96
x_left  = np.linspace(-4, -z_crit, 100)
x_right = np.linspace(z_crit,  4, 100)

ax6.fill_between(x_left,  stats.norm.pdf(x_left),
                 alpha=0.4, color='red', label='Rejection Region (α/2 = 2.5%)')
ax6.fill_between(x_right, stats.norm.pdf(x_right),
                 alpha=0.4, color='red')
ax6.fill_between(x_range[np.abs(x_range) <= z_crit],
                 y_normal[np.abs(x_range) <= z_crit],
                 alpha=0.2, color='green', label='Fail to Reject Region (95%)')

# Plot our Z-statistic
ax6.axvline(x=z_stat, color='blue', linewidth=2.5, linestyle='-.',
            label=f'Z-stat = {z_stat:.3f}')
ax6.axvline(x= z_crit, color='red', linewidth=1.5, linestyle='--', alpha=0.7)
ax6.axvline(x=-z_crit, color='red', linewidth=1.5, linestyle='--', alpha=0.7,
            label=f'Critical Values ±{z_crit}')

ax6.text(z_stat + 0.1, 0.25,
         f'p={p_value:.4f}\n{"REJECT H₀" if p_value < alpha else "FAIL TO REJECT"}',
         fontsize=9, color='blue', fontweight='bold')

ax6.set_title('Hypothesis Test Decision Zone', fontweight='bold')
ax6.set_xlabel('Z-Score')
ax6.set_ylabel('Probability Density')
ax6.legend(fontsize=8)
ax6.set_xlim(-4, 4)

plt.tight_layout()
plt.savefig('ab_test_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Dashboard saved as 'ab_test_dashboard.png'")


# ============================================================
# STEP 7: FINAL REPORT SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("         FINAL A/B TEST REPORT SUMMARY")
print("=" * 60)

print(f"""
╔══════════════════════════════════════════════════════════╗
║              A/B TEST RESULTS SUMMARY                    ║
╠══════════════════════════════════════════════════════════╣
║ Experiment  : Button Color Optimization                  ║
║ Group A     : Blue Button  (Control)   - {n_A} visitors  ║
║ Group B     : Green Button (Treatment) - {n_B} visitors  ║
╠══════════════════════════════════════════════════════════╣
║ CONVERSION RATES:                                        ║
║   Group A Conversion Rate : {rate_A:.2%}                     ║
║   Group B Conversion Rate : {rate_B:.2%}                     ║
║   Absolute Lift           : {(rate_B-rate_A)*100:+.2f}%                   ║
║   Relative Lift           : {lift:+.2f}%                  ║
╠══════════════════════════════════════════════════════════╣
║ STATISTICAL TESTS:                                       ║
║   Z-Statistic    : {z_stat:.4f}                           ║
║   P-Value        : {p_value:.6f}                        ║
║   Significance   : {'YES ✅' if p_value<alpha else 'NO ❌'}                           ║
╠══════════════════════════════════════════════════════════╣
║ CONFIDENCE INTERVALS (95%):                              ║
║   Group A : [{ci_low_A:.4f}, {ci_high_A:.4f}]               ║
║   Group B : [{ci_low_B:.4f}, {ci_high_B:.4f}]               ║
║   Diff CI : [{ci_diff_low:.4f}, {ci_diff_high:.4f}]               ║
╠══════════════════════════════════════════════════════════╣
║ STATISTICAL POWER : {power:.2%}                             ║
╠══════════════════════════════════════════════════════════╣
║ DECISION: {'LAUNCH Group B (Green Button) 🚀' if p_value<alpha else 'CONTINUE TESTING ⏳'}            ║
╚══════════════════════════════════════════════════════════╝
""")