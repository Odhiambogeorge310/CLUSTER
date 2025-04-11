🎓 Cluster Dashboard
A web-based interactive dashboard for visualizing and analyzing student performance data across various subjects using Streamlit and Plotly.

🚀 Features
📊 Visualizes assessment rubrics for Maths, English, Science & Technology, Kiswahili, Creative Arts, Social Studies (SST), and CRE.

🧍 Gender and grade-based filtering.

📈 Pie charts for subject score distributions.

📊 Bar charts for subject performance levels.

📋 Interactive table view with customizable columns.

🧮 Key performance metrics for learners by gender.

📁 File Structure
result.py: Main dashboard code (Streamlit app).

results.xlsx: Excel file with student data (must be placed in the same directory).

README.md: Project overview and setup instructions.

🛠️ Setup Instructions
1. Clone the repository:

bash
Copy
Edit
git clone <your-repo-url>
cd cluster-dashboard

2.Install dependencies:
pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install streamlit pandas numpy plotly openpyxl streamlit-extras streamlit-option-menu

3.Add your dataset:
Place your results.xlsx file in the project root. Make sure it has the required columns like ID, GENDER, GRADE, and subject scores (MATHS, ENGLISH, etc.).

4.Run the app:
streamlit run result.py

🖼️ Screenshots

✍️ Customization Tips
Modify the result.py script to add new filters or visualizations.

Adjust theme_plotly and styling for personal branding.

Extend to support CSV or database connections for dynamic data loading.

📄 License
MIT License. Feel free to use and adapt!