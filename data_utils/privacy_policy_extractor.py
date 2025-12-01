"""
Privacy Policy Data Extraction Utilities
========================================

Functions for processing data broker privacy policies and preparing data
for manual or automated analysis.
"""

import os
import re
import pandas as pd
from pathlib import Path


def clean_name(name):
    """
    Clean and normalize company names for consistency.
    
    Args:
        name (str): Raw company name
        
    Returns:
        str: Cleaned name (lowercase, no spaces)
    """
    if pd.isna(name):
        return ""
    
    name = str(name).lower()
    name = re.sub(r'\s+', '', name)
    return name


def clean_policy_url(policy_url):
    """
    Clean and normalize privacy policy URLs.
    
    Args:
        policy_url (str): Raw privacy policy URL
        
    Returns:
        str: Cleaned URL (lowercase, no spaces)
    """
    if pd.isna(policy_url):
        return ""
        
    policy_url = str(policy_url).lower()
    policy_url = re.sub(r'\s+', '', policy_url)
    return policy_url


def prepare_privacy_policy_dataset(data_path, output_dir=None):
    """
    Prepare data broker dataset for privacy policy analysis.
    
    Args:
        data_path (str): Path to the cleaned data brokers CSV file
        output_dir (str, optional): Directory to save output files
        
    Returns:
        tuple: (clean_dataset, unique_policies_dataset)
    """
    # Load data
    data_brokers = pd.read_csv(data_path)
    
    # Select relevant columns
    policy_data = data_brokers[["Name", "PrivacyPolicyURL"]].copy()
    
    # Remove rows with missing data
    policy_data = policy_data.dropna()
    
    # Clean names and URLs
    policy_data['Name_Clean'] = policy_data['Name'].apply(clean_name)
    policy_data['PrivacyPolicyURL_Clean'] = policy_data['PrivacyPolicyURL'].astype('string').apply(clean_policy_url)
    
    # Remove duplicates based on privacy policy URL (keep last occurrence)
    unique_policies = policy_data.drop_duplicates(subset='PrivacyPolicyURL_Clean', keep='last')
    
    # Reset index
    unique_policies = unique_policies.reset_index(drop=True)
    
    # Shuffle for random sampling (reproducible with seed)
    unique_policies_shuffled = unique_policies.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Create output directory if specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save datasets
        policy_data.to_csv(output_path / 'privacy_policies_cleaned.csv', index=False)
        unique_policies_shuffled.to_csv(output_path / 'privacy_policies_unique_shuffled.csv', index=False)
        
        print(f"Datasets saved to {output_dir}")
        print(f"   All policies: privacy_policies_cleaned.csv ({len(policy_data)} rows)")
        print(f"   Unique policies: privacy_policies_unique_shuffled.csv ({len(unique_policies_shuffled)} rows)")
    
    return policy_data, unique_policies_shuffled


def create_llm_analysis_prompt():
    """
    Generate the standardized prompt for LLM-based privacy policy analysis.
    
    Returns:
        str: Formatted prompt for privacy policy analysis
    """
    prompt = """
We will test what privacy policies mention about data use for the following categories. Only output a list of five numbers {0, 1, or 2} that correspond to the five categories below. Separate them by a comma; for example, respond [0, 1, 0, 0, 2]. 

Categories:

1. Marketing
2. Personalized Ads
3. Employment (influencing employment decisions and opportunities)
4. Consumer Finance (use for loans, credit scores, consumer finance risk calculation, etc.)
5. Law Enforcement Without Subpoena

Indices should correspond to:
0 = Privacy policy explicitly mentions NOT allowing this use case.
1 =  Privacy policy explicitly mentions ALLOWING this use case.
2 = Privacy policy does not explicitly mention this use case.

"""
    return prompt.strip()


def validate_llm_output(llm_response):
    """
    Validate and parse LLM output for privacy policy analysis.
    
    Args:
        llm_response (str): Raw response from LLM
        
    Returns:
        dict: Parsed and validated response, or None if invalid
    """
    try:
        import json
        
        # Try to parse as JSON
        parsed = json.loads(llm_response)
        
        # Check for required keys
        required_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        
        if not all(key in parsed for key in required_keys):
            print(f"Warning: Missing required keys. Expected {required_keys}")
            return None
            
        return parsed
        
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in LLM response")
        return None


if __name__ == "__main__":
    # Example usage
    data_path = "../data/cleaned_data/uq-data-brokers.csv"
    output_dir = "../data/cleaned_data/privacy_policies"
    
    clean_data, unique_policies = prepare_privacy_policy_dataset(data_path, output_dir)
    
    print("\nPrivacy Policy Analysis Workflow:")
    print("1. Use the generated CSV to identify unique privacy policies")
    print("2. Download policies manually or use web scraping")
    print("3. Apply LLM analysis using the standardized prompt")
    print("4. Validate outputs and compile results")
    
    prompt = create_llm_analysis_prompt()
    print(f"\nLLM Analysis Prompt Ready ({len(prompt)} characters)")