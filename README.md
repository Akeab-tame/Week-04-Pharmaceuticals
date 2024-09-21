Rossmann Pharmaceuticals Sales Forecasting
This project aims to forecast sales across multiple stores using various data features such as promotions, holidays, store type, and more. The analysis includes data exploration, visualizations, and predictive modeling, focusing on understanding customer purchasing behavior, especially around seasonal holidays and promotions.

Project Structure
bash
Copy code
├── data/                 # Contains the dataset used for analysis
├── notebooks/            # Jupyter notebooks for data analysis
├── scripts/              # Python scripts for data cleaning and visualization
├── README.md             # Project documentation
├── requirements.txt      # List of dependencies
└── visuals/              # Saved visualizations from the analysis
Data
The dataset includes:

Store Information: Details of each store (ID, type, etc.).
Sales: Daily sales figures for each store.
Promotions: Information on whether the store had a promotion running.
Holidays: Data on state holidays and other important dates.
Customers: Number of customers visiting each store on a given day.
Analysis Summary
1. Exploratory Data Analysis (EDA)
The EDA section focuses on understanding the key factors influencing sales:

Promotion Impact: Distribution of sales with and without promotions, and a comparison between training and test sets.
Holiday Impact: Sales behavior before, during, and after state holidays.
Seasonal Holidays: Box plot comparison of sales during Christmas and Easter vs non-holiday periods.
2. Key Insights
Promotion Effect: Stores with promotions generally see a spike in sales.
Holiday Impact: Sales tend to rise before holidays and drop afterward. State holidays seem to influence sales patterns.
Seasonal Sales: Significant increase in sales during Christmas and Easter, though with less variability than non-seasonal periods.
3. Visualizations
Promo Distribution in Train vs Test Sets: Highlights the imbalance between sales with promotions in training and test datasets.
Sales During Holidays: Line graph showing sales before, during, and after state holidays.
Sales During Seasonal Holidays: Box plot illustrating sales comparison during major seasonal holidays (Christmas & Easter) vs non-holidays.
Installation and Requirements
To run this project, you'll need to have Python installed along with the following dependencies (listed in requirements.txt):

pandas
numpy
matplotlib
seaborn
scikit-learn
Jupyter notebook
Install the dependencies with:

bash
Copy code
pip install -r requirements.txt
Running the Project
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/rossmann-sales-forecasting.git
Navigate to the project directory:
bash
Copy code
cd rossmann-sales-forecasting
Run the Jupyter notebook for EDA:
bash
Copy code
jupyter notebook notebooks/sales_analysis.ipynb
Explore the visualizations in the visuals/ folder for insights on promotions, holidays, and seasonal sales.
Conclusion
This project highlights important factors influencing sales at Rossmann Pharmaceuticals stores. Understanding these factors can help in building more accurate forecasting models and inform strategic decisions around promotions and holiday-related sales planning.