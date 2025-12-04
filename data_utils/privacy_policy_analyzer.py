"""
Privacy Policy Analysis Utilities
================================

Functions for analyzing LLM-processed privacy policy data and creating
visualizations to understand data broker practices.
"""

import pandas as pd
import numpy as np
import altair as alt
from pathlib import Path


def load_privacy_policy_data(file_path):
    """
    Load privacy policy analysis data from CSV file.
    
    Args:
        file_path (str): Path to the privacy policy CSV file
        
    Returns:
        pd.DataFrame: Loaded privacy policy data
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Privacy policy data loaded successfully: {data.shape[0]} rows, {data.shape[1]} columns")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def parse_llm_responses(data, question_col, category_names, name_col="Name"):
    """
    Parse LLM responses from bracketed format into separate columns.
    
    Args:
        data (pd.DataFrame): Source dataframe
        question_col (str): Column containing LLM responses
        category_names (list): List of category names for new columns
        name_col (str): Column containing entity names
        
    Returns:
        pd.DataFrame: Processed dataframe with parsed categories
    """
    # Create working copy
    result_df = data[[name_col, question_col]].copy()
    
    # Clean and parse the responses
    result_df[question_col] = result_df[question_col].str.strip('[]').str.replace(' ', '')
    
    # Split into separate columns
    split_cols = result_df[question_col].str.split(',', expand=True)
    split_cols.columns = category_names[:len(split_cols.columns)]
    
    # Join back and remove original column
    result_df = result_df.join(split_cols).drop(columns=[question_col])
    
    # Convert to numeric
    for col in category_names:
        if col in result_df.columns:
            result_df[col] = pd.to_numeric(result_df[col], errors='coerce')
    
    return result_df


def create_policy_analysis_chart(data, category_columns, title, xlabel, legend_labels=None, legend_title='Response Type', category_labels_map=None):
    """
    Create a standardized bar chart for privacy policy analysis using Altair.
    
    Args:
        data (pd.DataFrame): Dataframe containing the data to analyze.
        category_columns (list): List of columns to include in the analysis.
        title (str): Chart title.
        xlabel (str): X-axis label.
        legend_labels (list or dict, optional): Mapping from response values to labels.
        legend_title (str, optional): Title for the legend.
        category_labels_map (dict, optional): Dictionary to map snake_case category names to user-friendly labels.
        
    Returns:
        altair.Chart: Generated Altair chart object.
    """
    # Melt the dataframe to long format
    long_df = data[category_columns].melt(var_name='category', value_name='response')
    
    # Apply category label mapping if provided
    if category_labels_map:
        long_df['display_category'] = long_df['category'].map(category_labels_map)
        x_field = 'display_category:N'
        tooltip_category_field = alt.Tooltip('display_category:N', title='Category')
    else:
        default_category_labels_map = {
            "marketing": "Marketing",
            "personalized_ads": "Personalized Ads",
            "employment": "Employment",
            "consumer_finance": "Consumer Finance",
            "law_no_subpoena": "Law Enforcement (No Subpoena)",
            "gov": "Government",
            "corporations": "Corporations",
            "education_research": "Education & Research",
            "access": "Access",
            "correct": "Correct",
            "delete": "Delete",
            "no_discrimination": "No Discrimination",
            "no_targeted_ads": "No Targeted Ads",
            "opt_out_data": "Opt-Out Sharing & Collection"
        }
        long_df['display_category'] = long_df['category'].map(default_category_labels_map).fillna(
            long_df['category'].str.replace('_', ' ').str.title()
        )
        x_field = 'display_category:N'
        tooltip_category_field = alt.Tooltip('display_category:N', title='Category')

    sort_order = None
    # Map response values to labels
    if legend_labels:
        if isinstance(legend_labels, list):
            label_map = {i: label for i, label in enumerate(legend_labels)}
            sort_order = legend_labels
        elif isinstance(legend_labels, dict):
            label_map = legend_labels
            sort_order = [label_map[k] for k in sorted(label_map.keys())]
        else:
            raise TypeError("legend_labels must be a list or dictionary.")
        
        long_df['response_label'] = long_df['response'].map(label_map)
    else:
        long_df['response_label'] = long_df['response']

    # Create the chart
    chart = alt.Chart(long_df).mark_bar().encode(
        y=alt.Y(x_field, title=xlabel, axis=alt.Axis(labelAngle=0), sort=category_columns),
        x=alt.X('count()', stack='normalize', axis=alt.Axis(format='%', title='Percentage')),
        color=alt.Color('response_label:N', title=legend_title, sort=sort_order),
        tooltip=[tooltip_category_field, 'response_label:N', alt.Tooltip('count()', title='Count')]
    ).properties(
        title=title
    )
    
    return chart


def analyze_data_use_practices(llm_data):
    """
    Analyze data use practices from LLM Q1 responses.
    
    Args:
        llm_data (pd.DataFrame): LLM analysis results
        
    Returns:
        tuple: (processed_data, summary_stats)
    """
    category_names = ['marketing', 'personalized_ads', 'employment', 'consumer_finance', 'law_no_subpoena']
    
    # Parse responses
    data_use = parse_llm_responses(llm_data, "LLM Q1", category_names)
    
    # Calculate summary statistics
    summary_stats = {}
    for category in category_names:
        if category in data_use.columns:
            stats = data_use[category].value_counts().sort_index()
            summary_stats[category] = {
                'not_allowed': stats.get(0, 0),
                'allowed': stats.get(1, 0), 
                'not_mentioned': stats.get(2, 0)
            }
    
    return data_use, summary_stats


def analyze_sharing_entities(llm_data):
    """
    Analyze entity sharing practices from LLM Q2 responses.
    
    Args:
        llm_data (pd.DataFrame): LLM analysis results
        
    Returns:
        tuple: (processed_data, summary_stats)
    """
    category_names = ['gov', 'corporations', 'education_research']
    
    # Parse responses  
    entities = parse_llm_responses(llm_data, "LLM Q2", category_names)
    
    # Calculate summary statistics
    summary_stats = {}
    for category in category_names:
        if category in entities.columns:
            stats = entities[category].value_counts().sort_index()
            summary_stats[category] = {
                'not_allowed': stats.get(0, 0),
                'allowed': stats.get(1, 0),
                'not_mentioned': stats.get(2, 0)
            }
    
    return entities, summary_stats


def analyze_user_controls(llm_data):
    """
    Analyze user rights and controls from LLM Q3 responses.
    
    Args:
        llm_data (pd.DataFrame): LLM analysis results
        
    Returns:
        tuple: (processed_data, summary_stats)
    """
    category_names = ['access', 'correct', 'delete', 'no_discrimination', 'no_targeted_ads', 'opt_out_data']
    
    # Parse responses
    controls = parse_llm_responses(llm_data, "LLM Q3", category_names)
    
    # Calculate summary statistics
    summary_stats = {}
    for category in category_names:
        if category in controls.columns:
            stats = controls[category].value_counts().sort_index()
            summary_stats[category] = {
                'no_guarantee': stats.get(0, 0),
                'guaranteed': stats.get(1, 0)
            }
    
    return controls, summary_stats


def generate_analysis_report(data_use_stats, entities_stats, controls_stats):
    """
    Generate a comprehensive analysis report.
    
    Args:
        data_use_stats (dict): Data use analysis results
        entities_stats (dict): Entity sharing analysis results  
        controls_stats (dict): User controls analysis results
        
    Returns:
        str: Formatted analysis report
    """
    report = []
    report.append("=" * 60)
    report.append("PRIVACY POLICY ANALYSIS REPORT")
    report.append("=" * 60)
    
    # Data Use Analysis
    report.append("\n1. DATA USE PRACTICES")
    report.append("-" * 30)
    for category, stats in data_use_stats.items():
        total = sum(stats.values())
        if total > 0:
            allowed_pct = (stats['allowed'] / total) * 100
            report.append(f"{category.replace('_', ' ').title()}:")
            report.append(f"  - Explicitly allowed: {stats['allowed']} ({allowed_pct:.1f}%)")
            report.append(f"  - Not allowed: {stats['not_allowed']}")
            report.append(f"  - Not mentioned: {stats['not_mentioned']}")
    
    # Entity Sharing Analysis
    report.append("\n2. ENTITY SHARING PRACTICES")
    report.append("-" * 35)
    for category, stats in entities_stats.items():
        total = sum(stats.values())
        if total > 0:
            allowed_pct = (stats['allowed'] / total) * 100
            report.append(f"{category.replace('_', ' ').title()}:")
            report.append(f"  - Sharing allowed: {stats['allowed']} ({allowed_pct:.1f}%)")
            report.append(f"  - Not allowed: {stats['not_allowed']}")
            report.append(f"  - Not mentioned: {stats['not_mentioned']}")
    
    # User Controls Analysis
    report.append("\n3. USER RIGHTS AND CONTROLS")
    report.append("-" * 35)
    for category, stats in controls_stats.items():
        total = sum(stats.values())
        if total > 0:
            guaranteed_pct = (stats['guaranteed'] / total) * 100
            report.append(f"{category.replace('_', ' ').title()}:")
            report.append(f"  - Explicitly guaranteed: {stats['guaranteed']} ({guaranteed_pct:.1f}%)")
            report.append(f"  - No guarantee: {stats['no_guarantee']}")
            if 'not_mentioned' in stats and stats['not_mentioned'] > 0:
                report.append(f"  - Not mentioned: {stats['not_mentioned']}")
    
    report.append("\n" + "=" * 60)
    
    return "\n".join(report)


def _build_response_summary(df, question_key, question_labels, response_labels, category_titles):
    """
    Convert wide-format parsed responses into long-form summary suitable for Altair.
    """
    long_df = df.melt(id_vars=["Name"], var_name="category", value_name="response")
    long_df = long_df.dropna(subset=["response"])
    long_df["question"] = question_labels.get(question_key, question_key)
    long_df["response_label"] = long_df["response"].map(response_labels)
    long_df["category_label"] = (
        long_df["category"].map(category_titles)
        .fillna(long_df["category"].str.replace("_", " ").str.title())
    )

    counts = (
        long_df.groupby(["question", "category", "category_label", "response", "response_label"], as_index=False)
        .size()
        .rename(columns={"size": "count"})
    )
    counts["share"] = counts["count"] / counts.groupby(["question", "category"])["count"].transform("sum")
    return counts


def prepare_privacy_policy_summary(llm_data):
    """
    Prepare aggregated summary data for privacy policy visualizations.
    
    Args:
        llm_data (pd.DataFrame): Raw LLM response dataframe.
        
    Returns:
        dict: Summary data and metadata for visualization.
    """
    data_use, _ = analyze_data_use_practices(llm_data)
    entities, _ = analyze_sharing_entities(llm_data)
    controls, _ = analyze_user_controls(llm_data)

    response_labels = {0: "No", 1: "Yes", 2: "Not Mentioned"}
    response_order = ["Yes", "No", "Not Mentioned"]
    response_colors = ["#2ca02c", "#d62728", "#7f7f7f"]

    question_labels = {
        "Q1": "Data Use (Q1)",
        "Q2": "Entity Sharing (Q2)",
        "Q3": "User Rights (Q3)"
    }

    category_titles = {
        "marketing": "Marketing",
        "personalized_ads": "Personalized Ads",
        "employment": "Employment",
        "consumer_finance": "Consumer Finance",
        "law_no_subpoena": "Law Enforcement (No Subpoena)",
        "gov": "Government",
        "corporations": "Corporations",
        "education_research": "Education & Research",
        "access": "Access",
        "correct": "Correct",
        "delete": "Delete",
        "no_discrimination": "No Discrimination",
        "no_targeted_ads": "No Targeted Ads",
        "opt_out_data": "Opt-Out Sharing & Collection"
    }

    summary_frames = [
        _build_response_summary(data_use, "Q1", question_labels, response_labels, category_titles),
        _build_response_summary(entities, "Q2", question_labels, response_labels, category_titles),
        _build_response_summary(controls, "Q3", question_labels, response_labels, category_titles)
    ]

    summary_df = pd.concat(summary_frames, ignore_index=True)
    summary_df["response_label"] = pd.Categorical(
        summary_df["response_label"],
        categories=response_order,
        ordered=True
    )
    summary_df.sort_values(["question", "category", "response_label"], inplace=True)

    summary_records = summary_df.to_dict(orient="records")

    return {
        "summary": summary_records,
        "response_order": response_order,
        "response_colors": response_colors
    }


if __name__ == "__main__":
    # Example usage
    print("Privacy Policy Analysis Utilities")
    print("Use these functions to analyze LLM-processed privacy policy data")
    print("\nAvailable functions:")
    print("- load_privacy_policy_data(): Load data from CSV")
    print("- analyze_data_use_practices(): Analyze data use patterns")
    print("- analyze_sharing_entities(): Analyze entity sharing")
    print("- analyze_user_controls(): Analyze user rights")
    print("- create_policy_analysis_chart(): Create standardized charts")
    print("- generate_analysis_report(): Generate summary report")