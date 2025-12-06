import pandas as pd
import altair as alt
import numpy as np
from pathlib import Path

def create_gap_chart_data_types(df_brokers, df_survey):
    """
    Prepares data for a gap chart visualizing the disparity between
    data types collected by brokers and those consumers are comfortable with.

    Args:
        df_brokers (pd.DataFrame): DataFrame containing data broker information.
        df_survey (pd.DataFrame): DataFrame containing survey results.

    Returns:
        pd.DataFrame: A DataFrame formatted for Altair, with columns for
                      'Category', 'Source', and 'Percentage'.
    """
    # 1. Process Data Broker Data
    broker_data_types = {
        "Commercial transactions data": "CollectsCommercialData",
        "Employment-related data": "CollectsEmploymentData",
        "Location data": "CollectsAddresses", # Closest proxy for location
        "Biometric data": "CollectsBiometricData",
        "Minors' data": "CollectsMinorsData",
        "Reproductive health-related information": "CollectsReproductiveHealthData",
        "Social Security Number and government ID information": "CollectsSSNGovID",
        "Network data": "CollectsNetworkData"
    }

    broker_percentages = []
    total_brokers = len(df_brokers)

    for consumer_cat, broker_col in broker_data_types.items():
        if broker_col in df_brokers.columns:
            # Count 'Yes' (1) responses, excluding 'Not Reported' (2)
            reported_brokers = df_brokers[df_brokers[broker_col] != 2]
            if not reported_brokers.empty:
                yes_count = reported_brokers[broker_col].sum() # Sum of 1s
                percentage = (yes_count / len(reported_brokers)) * 100
                broker_percentages.append({'Category': consumer_cat, 'Source': 'Data Brokers (Reported)', 'Percentage': percentage})

    # 2. Process Survey Data (Consumer Comfort)
    comfort_col = "3. Which types of your personal data are you comfortable being used for any purpose? (Select all that apply)"
    
    # Standardize survey categories to match broker categories for comparison
    consumer_category_map = {
        "Commercial data (e.g., purchasing and transaction history)": "Commercial transactions data",
        "Employment-related data": "Employment-related data",
        "Location data": "Location data",
        "Biometric data (e.g., fingerprint, voice, facial recognition)": "Biometric data",
        "Personal information of individuals under 18": "Minors' data",
        "Reproductive health-related information": "Reproductive health-related information",
        "Social Security Number and government ID information": "Social Security Number and government ID information",
        "Network data (e.g., IP address, browsing history)": "Network data"
    }

    survey_comfort_counts = {}
    for _cat, short_name in consumer_category_map.items():
        survey_comfort_counts[short_name] = 0

    for responses in df_survey[comfort_col].dropna():
        for category_long_name, category_short_name in consumer_category_map.items():
            if category_long_name in responses:
                survey_comfort_counts[category_short_name] = survey_comfort_counts.get(category_short_name, 0) + 1
    
    total_respondents = len(df_survey)
    consumer_percentages = []
    for category, count in survey_comfort_counts.items():
        percentage = (count / total_respondents) * 100
        consumer_percentages.append({'Category': category, 'Source': 'Consumers', 'Percentage': percentage})

    # Combine and Clean
    combined_df = pd.DataFrame(broker_percentages + consumer_percentages)
    
    # Ensure all categories have both consumer and broker data for charting
    pivoted_df = combined_df.pivot_table(index='Category', columns='Source', values='Percentage').fillna(0)
    combined_df = pivoted_df.reset_index().melt(id_vars='Category', var_name='Source', value_name='Percentage')


    # Sort categories for consistent plotting order
    all_categories = combined_df['Category'].unique()
    
    existing_sort_order = [
        "Commercial transactions data",
        "Employment-related data",
        "Location data",
        "Network data",
        "Minors' data",
        "Biometric data",
        "Reproductive health-related information",
        "Social Security Number and government ID information"
    ]
    
    ordered_categories = [cat for cat in existing_sort_order if cat in all_categories]
    new_categories = sorted([cat for cat in all_categories if cat not in ordered_categories])
    dynamic_sort_order = ordered_categories + new_categories
    
    combined_df['Category'] = pd.Categorical(combined_df['Category'], categories=dynamic_sort_order, ordered=True)
    combined_df = combined_df.sort_values('Category')

    return combined_df

def create_gap_chart_use_cases(df_brokers, df_survey):
    """
    Prepares data for a gap chart visualizing the disparity between
    use cases permitted by brokers and those consumers are comfortable with.

    Args:
        df_brokers (pd.DataFrame): DataFrame containing data broker information.
        df_survey (pd.DataFrame): DataFrame containing survey results.

    Returns:
        pd.DataFrame: A DataFrame formatted for Altair, with columns for
                      'Category', 'Source', and 'Percentage'.
    """
    # 1. Process Data Broker Data (Use Cases - assuming similar Collects pattern or from analysis)
    # The notebook output (Figure 3 in index.md) provides these percentages directly.
    # We will hardcode these based on the analysis output or retrieve from a more structured source if available.
    # For now, let's assume we can get these from the analysis (e.g., from the `create_policy_analysis_chart` function
    # or direct parsing of the notebook's generated data if it were saved.)
    # Given the prompt, we'll use the percentages from the `index.md` text directly.
    broker_use_case_percentages = [
        {'Category': 'Marketing', 'Source': 'Data Brokers (Explicit)', 'Percentage': 95.5},
        {'Category': 'Personalized advertising', 'Source': 'Data Brokers (Explicit)', 'Percentage': 86.0},
        {'Category': 'Employment decisions', 'Source': 'Data Brokers (Explicit)', 'Percentage': 59.0} # from text "59% allow data to be used in employment decisions"
    ]

    # 2. Process Survey Data (Consumer Comfort for Use Cases)
    comfort_col_use_cases = "4. What purposes are you comfortable with your personal data being used for? (Select all that apply)"
    
    # Standardize survey categories to match broker categories for comparison
    consumer_use_case_map = {
        "Marketing": "Marketing",
        "Personalized advertising": "Personalized advertising",
        "Employment decisions (e.g., hiring, promotions)": "Employment decisions",
        # Add other relevant mappings if they exist in survey data but not in broker text example
    }

    survey_comfort_use_cases_counts = {}
    for _cat, short_name in consumer_use_case_map.items():
        survey_comfort_use_cases_counts[short_name] = 0
        
    for responses in df_survey[comfort_col_use_cases].dropna():
        for category_long_name, category_short_name in consumer_use_case_map.items():
            if category_long_name in responses:
                survey_comfort_use_cases_counts[category_short_name] = survey_comfort_use_cases_counts.get(category_short_name, 0) + 1
    
    total_respondents = len(df_survey)
    consumer_use_cases_percentages = []
    for category, count in survey_comfort_use_cases_counts.items():
        percentage = (count / total_respondents) * 100
        consumer_use_cases_percentages.append({'Category': category, 'Source': 'Consumers', 'Percentage': percentage})

    # Combine and Clean
    combined_df = pd.DataFrame(broker_use_case_percentages + consumer_use_cases_percentages)
    
    # Ensure all categories have both consumer and broker data for charting
    pivoted_df = combined_df.pivot_table(index='Category', columns='Source', values='Percentage').fillna(0)
    combined_df = pivoted_df.reset_index().melt(id_vars='Category', var_name='Source', value_name='Percentage')

    # Sort categories for consistent plotting order
    all_categories = combined_df['Category'].unique()
    
    existing_sort_order = [
        "Marketing",
        "Personalized advertising",
        "Employment decisions"
    ]
    
    ordered_categories = [cat for cat in existing_sort_order if cat in all_categories]
    new_categories = sorted([cat for cat in all_categories if cat not in ordered_categories])
    dynamic_sort_order = ordered_categories + new_categories
    
    combined_df['Category'] = pd.Categorical(combined_df['Category'], categories=dynamic_sort_order, ordered=True)
    combined_df = combined_df.sort_values('Category')
    
    return combined_df

def create_dumbbell_chart(data, title, x_label, y_label):
    """
    Creates an Altair dumbbell chart to visualize gaps between two sources.

    Args:
        data (pd.DataFrame): DataFrame with 'Category', 'Source', 'Percentage'.
        title (str): Chart title.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.

    Returns:
        alt.Chart: An Altair dumbbell chart.
    """
    base = alt.Chart(data).encode(
        y=alt.Y('Category:N', title=y_label, sort=alt.EncodingSortField(field="Category", op="min", order='descending')),
    )

    # Lines connecting the points
    lines = base.mark_line(point=True, size=5).encode(
        x=alt.X('Percentage:Q', title=x_label),
        detail='Category:N',
        color=alt.value('lightgray')
    )

    # Points for each source
    points = base.mark_point(size=100, filled=True).encode(
        x=alt.X('Percentage:Q', title=x_label),
        color=alt.Color('Source:N',
                        legend=alt.Legend(title="Source"),
                        scale=alt.Scale(range=['#3498db', '#e74c3c'])), # Blue for Data Brokers, Red for Consumers
        tooltip=[
            alt.Tooltip('Category:N', title=y_label),
            alt.Tooltip('Source:N'),
            alt.Tooltip('Percentage:Q', format='.1f', title='Percentage (%)')
        ]
    )

    text = base.mark_text(
        align='left',
        baseline='middle',
        dx=7 # Nudge text to the right
    ).encode(
        x=alt.X('Percentage:Q'),
        text=alt.Text('Percentage:Q', format='.1f'),
        color=alt.Color('Source:N', scale=alt.Scale(range=['#3498db', '#e74c3c']))
    ).transform_filter(
        # Only label the "Data Brokers (Reported)" point to avoid clutter
        alt.FieldEqualPredicate(field='Source', equal='Data Brokers (Reported)')
    )
    
    chart = (lines + points).properties(
        title=title
    ).interactive()

    return chart

if __name__ == '__main__':
    # Determine the project root dynamically
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Load data
    df_brokers = pd.read_csv(project_root / 'data/cleaned_data/uq-data-brokers.csv')
    df_survey = pd.read_csv(project_root / 'data/raw_data/survey/survey_results.csv')

    # Create and save Data Types chart
    data_types_chart_data = create_gap_chart_data_types(df_brokers, df_survey)
    chart1 = create_dumbbell_chart(
        data_types_chart_data,
        title='Disparity: Data Broker Collection vs. Consumer Comfort (Data Types)',
        x_label='Percentage (%)',
        y_label='Data Type'
    )
    chart1.save(project_root / 'notebooks/imgs/Disparity - Data Types.svg')
    print("Saved ../notebooks/imgs/Disparity - Data Types.svg")

    # Create and save Use Cases chart
    use_cases_chart_data = create_gap_chart_use_cases(df_brokers, df_survey)
    chart2 = create_dumbbell_chart(
        use_cases_chart_data,
        title='Disparity: Data Broker Collection vs. Consumer Comfort (Use Cases)',
        x_label='Percentage (%)',
        y_label='Use Case'
    )
    chart2.save(project_root / 'notebooks/imgs/Disparity - Use Cases.svg')
    print("Saved ../notebooks/imgs/Disparity - Use Cases.svg")
