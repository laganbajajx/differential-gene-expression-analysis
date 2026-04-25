# 🧬 Differential Gene Expression Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

**A complete bioinformatics pipeline for identifying, visualizing, and predicting phenotype from gene expression data.**

[Overview](#-overview) · [Dataset](#-dataset-description) · [Pipeline](#-pipeline) · [Results](#-key-outcomes) · [Usage](#-getting-started) · [Roadmap](#-future-improvements)

</div>

---

## 📖 Overview

**Differential Gene Expression (DGE) Analysis** is a cornerstone of modern bioinformatics — identifying genes whose expression levels shift significantly across biological conditions. It underpins disease research, drug target discovery, cancer genomics, and precision medicine.

This project implements a **full end-to-end DGE pipeline** in Python, covering everything from raw data exploration to machine learning-based phenotype prediction. By comparing expression profiles between groups (e.g., healthy vs. diseased), we can uncover:

- 🔬 **Biomarkers** — genes that distinguish disease states
- 🔗 **Molecular pathways** — co-expression and regulatory networks
- 🧪 **Disease mechanisms** — expression changes that drive or reflect pathology

---

## 🗂️ Dataset Description

| Property | Detail |
|---|---|
| **Features** | Gene expression values (thousands of genes per sample) |
| **Samples** | Multiple individuals across biological conditions |
| **Target classes** | Healthy Controls · Diseased Patients · Recovered Patients · Chronic Cases |
| **Format** | Tabular — each row is a sample, each column is a gene |

> Each entry represents the transcriptional activity of a gene under a specific condition, typically measured via microarray or RNA-Seq.

---

## 🔄 Pipeline

```
Raw Gene Expression Data
         │
         ▼
┌─────────────────────────────────────────┐
│  1. EDA & Inspection                    │
│     Missing values · Distributions      │
│     Class balance · Heatmaps            │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  2. Preprocessing                       │
│     Log₂ transform · Normalization      │
│     Standardization · Outlier handling  │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  3. Dimensionality Reduction            │
│     PCA · t-SNE · Variance filtering    │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  4. Clustering                          │
│     K-Means · Hierarchical · Dendrograms│
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  5. Differential Expression Analysis    │
│     Fold change · t-test / ANOVA        │
│     FDR correction · Volcano plot       │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  6. ML Modeling                         │
│     Logistic Regression · Random Forest │
│     SVM · LDA                           │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│  7. Evaluation                          │
│     Accuracy · F1 · ROC-AUC             │
│     Confusion Matrix · Feature Importance│
└─────────────────────────────────────────┘
```

---

## 🧪 Workflow Details

<details>
<summary><b>1. Exploratory Data Analysis (EDA)</b></summary>
<br>

- Missing value detection and handling strategy
- Gene expression distribution analysis (per-sample and per-gene)
- Class balance check across phenotype groups
- Boxplots, histograms, and violin plots
- Correlation heatmaps to identify co-expressed gene clusters

</details>

<details>
<summary><b>2. Data Preprocessing</b></summary>
<br>

- **Log₂ transformation** to stabilize variance across expression ranges
- **Normalization** to correct for technical variation between samples
- **StandardScaler** for zero-mean, unit-variance feature scaling
- Outlier detection and handling

</details>

<details>
<summary><b>3. Dimensionality Reduction</b></summary>
<br>

- **PCA** — Projects thousands of gene dimensions into 2–3 principal components for interpretable visualization
- **t-SNE** — Non-linear embedding for revealing local cluster structure
- **Variance filtering** — Removes low-information genes before modeling

</details>

<details>
<summary><b>4. Clustering Analysis</b></summary>
<br>

- **K-Means Clustering** — Unsupervised grouping of samples
- **Hierarchical Clustering** — Dendrograms revealing nested sample/gene relationships
- Cluster visualizations colored by phenotype label

</details>

<details>
<summary><b>5. Differential Expression Analysis</b></summary>
<br>

Statistical framework for identifying significantly changing genes:

```python
# Per-gene t-test between conditions
stat, p = ttest_ind(group_A[gene], group_B[gene])

# Log2 Fold Change
log2FC = np.log2((mean_B + 1e-6) / (mean_A + 1e-6))

# Multiple testing correction (Benjamini-Hochberg)
from statsmodels.stats.multitest import multipletests
_, p_adj, _, _ = multipletests(p_values, method='fdr_bh')
```

**Outputs:**
- Volcano plot (log2FC vs −log10 p-value)
- Heatmap of top differentially expressed genes
- Ranked gene list with adjusted p-values

</details>

<details>
<summary><b>6. Predictive Modeling</b></summary>
<br>

| Model | Notes |
|---|---|
| `LogisticRegression` | Linear baseline; interpretable coefficients |
| `RandomForestClassifier` | Ensemble method; robust to high dimensionality |
| `SVC (linear kernel)` | Effective in high-dim spaces; margin maximization |
| `LinearDiscriminantAnalysis` | Generative; optimizes class separability |

All models trained on an 80/20 stratified train/test split.

</details>

<details>
<summary><b>7. Model Evaluation</b></summary>
<br>

- Accuracy, Precision, Recall, F1-Score per class
- ROC curves with AUC scores for each classifier
- Confusion matrix visualization
- Feature importance / top predictive genes (Random Forest)

</details>

---

## 🚀 Getting Started

### Clone & Install

```bash
git clone https://github.com/your-username/gene-expression-analysis.git
cd gene-expression-analysis
pip install -r requirements.txt
```

### Run the Notebook

```bash
jupyter notebook gene_expression.ipynb
```

### `requirements.txt`

```
numpy
pandas
scipy
statsmodels
scikit-learn
matplotlib
seaborn
jupyter
```

---

## 🏆 Key Outcomes

| # | Outcome |
|---|---|
| 1 | Identified statistically significant differentially expressed genes with FDR correction |
| 2 | Visualized clear biological separation between phenotype groups via PCA and t-SNE |
| 3 | Built multi-class phenotype prediction models with comparative performance analysis |
| 4 | Produced publication-style plots: volcano plots, heatmaps, ROC curves |
| 5 | Extracted top biomarker genes via Random Forest feature importances |

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| **Language** | Python 3.8+ |
| **Data** | NumPy, Pandas |
| **Statistics** | SciPy, Statsmodels |
| **ML** | Scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook |

---

## 🔭 Future Improvements

- [ ] **RNA-Seq normalization** — DESeq2 / EdgeR-style count normalization
- [ ] **Pathway enrichment analysis** — GSEA, KEGG, Reactome integration
- [ ] **Gene Ontology (GO) mapping** — Functional annotation of top genes
- [ ] **Deep learning models** — 1D CNNs or Transformers for expression classification
- [ ] **Interactive web dashboard** — Plotly Dash or Streamlit deployment

---

## 📁 Project Structure

```
gene-expression-analysis/
├── gene_expression.ipynb      # Main analysis notebook
├── gene_expression_final.csv  # Dataset
├── requirements.txt
└── README.md
```

---

<div align="center">

Made with 🧬 and Python &nbsp;|&nbsp; Contributions welcome

</div>
