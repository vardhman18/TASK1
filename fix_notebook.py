import json

notebook = {
    'cells': [
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['# Student Performance Data Analysis\n\nThis notebook explores student performance using the complete data science workflow:\nLoad → Clean → Analyze → Visualize → Conclude']
        },
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['## 1. Load Dataset']
        },
        {
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': ['import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\ndf = pd.read_csv("student-mat.csv", sep=";")\nprint("Dataset shape:", df.shape)\nprint(df.head())']
        },
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['## 2. Explore Data']
        },
        {
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': ['print("Missing Values:")\nprint(df.isnull().sum())\nprint(f"Duplicates: {df.duplicated().sum()}")']
        },
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['## 3. Clean Data']
        },
        {
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': ['df_cleaned = df.drop_duplicates()\nprint(f"Original: {df.shape} -> Cleaned: {df_cleaned.shape}")']
        },
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['## 4. Analysis']
        },
        {
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': ['avg_grade = df_cleaned["G3"].mean()\nprint(f"Average Grade: {avg_grade:.2f}")\nprint(f"Students above 15: {(df_cleaned[\"G3\"] > 15).sum()}")\n\nif "studytime" in df_cleaned.columns:\n    corr = df_cleaned["studytime"].corr(df_cleaned["G3"])\n    print(f"Correlation: {corr:.4f}")']
        },
        {
            'cell_type': 'markdown',
            'metadata': {},
            'source': ['## 5. Visualizations']
        },
        {
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': ['fig, axes = plt.subplots(1, 3, figsize=(15, 4))\naxes[0].hist(df_cleaned["G3"], bins=15)\naxes[0].set_title("Grade Distribution")\nplt.show()']
        }
    ],
    'metadata': {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'name': 'python',
            'version': '3.8.0'
        }
    },
    'nbformat': 4,
    'nbformat_minor': 4
}

with open('student_performance_analysis.ipynb', 'w') as f:
    json.dump(notebook, f, indent=2)

print('✓ Notebook recreated in proper JSON format!')
