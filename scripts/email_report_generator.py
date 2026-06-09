import pandas as pd

funds = pd.read_csv("data/processed/top_recommended_funds.csv")

top5 = funds.head(5)

html = """
<html>
<head>
<title>Weekly Mutual Fund Report</title>
</head>
<body>
<h1>Weekly Mutual Fund Performance Summary</h1>

<h2>Top Recommended Funds</h2>

<table border="1">
<tr>
<th>AMFI Code</th>
<th>CAGR</th>
<th>Sharpe Ratio</th>
</tr>
"""

for _, row in top5.iterrows():
    html += f"""
    <tr>
        <td>{row['amfi_code']}</td>
        <td>{row['cagr']:.2f}</td>
        <td>{row['sharpe_ratio']:.2f}</td>
    </tr>
    """

html += """
</table>

<p>Generated automatically by Mutual Fund Analytics Platform.</p>

</body>
</html>
"""

with open("reports/weekly_fund_report.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML report generated successfully.")