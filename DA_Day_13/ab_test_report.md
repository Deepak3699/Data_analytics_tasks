# A/B Testing Report
## Website Traffic Data Analysis

---

## Experiment Details

| Field | Details |
|-------|---------|
| Test Name | Website Design A/B Test |
| Group A | Old Design (Control) |
| Group B | New Design (Treatment) |
| Sample Size | 1000 users each |
| Confidence Level | 95% |

---

## Results

| Metric | Group A | Group B | Significant? |
|--------|---------|---------|-------------|
| Conversion Rate | 9.80% | 12.40% | ✅ YES |
| Avg Time Spent | 120.53 sec | 134.89 sec | ✅ YES |
| Bounce Rate | 58.30% | 52.00% | ✅ YES |

---

## Hypothesis Testing

**Test 1 - Conversion Rate (Z-Test)**
- H0 : Conversion Rate A = Conversion Rate B
- H1 : Conversion Rate A ≠ Conversion Rate B
- P-Value : 0.0289 → ✅ Reject H0

**Test 2 - Time Spent (T-Test)**
- H0 : Mean Time A = Mean Time B
- H1 : Mean Time A ≠ Mean Time B
- P-Value : 0.0000 → ✅ Reject H0

**Test 3 - Bounce Rate (Z-Test)**
- H0 : Bounce Rate A = Bounce Rate B
- H1 : Bounce Rate A ≠ Bounce Rate B
- P-Value : 0.0038 → ✅ Reject H0

---

## Confidence Intervals (95%)

| Group | Conversion Rate | CI Range |
|-------|----------------|----------|
| A | 9.80% | [7.98% - 11.62%] |
| B | 12.40% | [10.40% - 14.40%] |

---

## Conclusion

> **Winner : Group B (New Design)**

- Conversion Rate improved by **+26.53%**
- Users spend **14 more seconds** on site
- Bounce Rate reduced by **6.30%**
- All results are statistically significant at 95% confidence

**Recommendation : Deploy New Design to all users**

---
*Data Analytics Internship — Task 13*