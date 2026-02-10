# COVID-19 Research Analysis Dashboard

## Brief Report of Findings

This project analyzes a subset of COVID-19 research papers, including information on paper titles, abstracts, journals, publication dates, and sources. Key findings from the dataset are:

- **Publication Trends:** Papers are published across multiple years. From the subset analyzed, we observed peaks in publication activity corresponding to 2020 and 2021.
- **Top Publishing Journals:** The most frequent journals publishing COVID-19 research in this subset are:
  - Vaccine Research
  - COVID Therapeutics
  - Critical Care Medicine
- **Common Words in Titles:** Frequent words appearing in paper titles include `COVID-19`, `vaccine`, `treatment`, `research`, and `mask`.
- **Distribution by Source:** Papers originate from multiple sources, with some sources contributing more heavily to the dataset.
- **Abstract Analysis:** Word counts in abstracts vary across papers, providing insight into the level of detail in reporting.

## Challenges Faced

- **Missing Values:** Several columns, such as `journal` and `abstract`, contained missing data that needed careful handling to avoid errors in analysis.
- **Date Parsing:** Converting `publish_time` to a datetime object and extracting publication year required attention to handle inconsistencies.
- **Visualization Integration:** Combining Matplotlib figures with Streamlit for interactive visualization posed challenges in ensuring charts display correctly.
- **File Naming Conflicts:** Initially, naming the script `streamlit.py` caused module import issues that had to be resolved.

## Learning Outcomes

- Gained experience in **cleaning and preprocessing real-world datasets** using Pandas.
- Learned to generate **visualizations** using Matplotlib and WordCloud to extract insights from textual and numeric data.
- Built an **interactive Streamlit dashboard** allowing users to filter papers by source and publication year, and view plots and sample data dynamically.
- Developed the ability to **integrate data analysis and visualization** into a web-based application for practical presentation.

## How to Use the Dashboard

1. Ensure all dependencies are installed:
   ```bash
   pip install pandas matplotlib wordcloud streamlit
