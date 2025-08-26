📊 Vendor Performance Analysis – End-to-End Data Pipeline

📌 Project Overview

This project demonstrates the design and implementation of a complete data analytics pipeline for vendor performance.
The pipeline ingests raw transactional data, transforms it into meaningful KPIs, and delivers actionable business insights through Python analysis and Power BI dashboards.

⚙️ Tools & Technologies Used

- Python – Data ingestion, cleaning, transformation, and EDA

- SQLite (SQLAlchemy) – Centralized database storage and querying

- Pandas & NumPy – Data manipulation and aggregation

- Matplotlib & Seaborn – Data visualization and EDA plots

- Logging – Process tracking and debugging

Power BI – Interactive dashboards and business reporting

🔄 Data Pipeline Workflow

Step 1 – Data Ingestion (Python + SQLite)

- Script: ingestion_db.py

- Reads all CSV files from data/ folder

- Loads them into inventory.db as structured tables

- Logging captures ingestion details and runtime

Step 2 – Data Transformation & EDA (Python)

- Script: explotary_data_analysis.py

- Built consolidated vendor_sales_summary table

- Derived KPIs: Gross Profit, Profit Margin, Stock Turnover, Sales-to-Purchase Ratio

- Visualizations: Histograms, Boxplots, Heatmaps

- Insights: Detected brands with low sales but high margins (promotion candidates)

Step 3 – Visualization & Reporting (Power BI)

- Interactive dashboards with vendor and brand-level analysis

- Key metrics included:

Total Vendors: 128

Total Purchases: $321.9M

Total Sales: $451.6M

Gross Profit: $129.7M

Stock Turnover: 18.25K

Top brands analyzed: Jack Daniels, Tito’s, Absolut, Captain Morgan, Ketel One

📈 Key Insights

- Vendors generated $451M in sales from $321M in purchases, yielding $129M gross profit

- Strong correlation between purchases and sales → consistent demand patterns

- High-margin, low-sales brands identified as growth opportunities

- Power BI dashboards provide both executive KPIs and brand-level drilldowns

🚀 Impact

- Automated pipeline from raw CSVs → Database → Insights

- Actionable intelligence for vendor management & promotions

Scalable design: new data files refresh automatically

Reliable, centralized single source of truth

Business-ready dashboards for quick decision-making

<img width="1487" height="813" alt="image" src="https://github.com/user-attachments/assets/2df97728-058f-48d0-a6a5-ca2b0e15ebd2" />
