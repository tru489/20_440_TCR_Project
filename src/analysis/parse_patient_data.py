import pandas as pd
import os
import numpy as np

def parse_patients(ov_df, metric_fn, metric_col, ov_new_col):
    """
    Calculate metrics for patient data files and put them in a new column in 
    the overview dataframe, given a metric with which each patient's data will 
    be quantified

    Args:
        ov_df (pd.DataFrame): preprocessed sample overview dataframe
        metric_fn (function): function that calculates metric values from 
            individual patient files
        metric_col (str): column in patient data from which metrics will be 
            calculated
        ov_new_col (str): name of new column to which new datapoints, one for
            each patient, will be added to sample overview dataframe

    Returns:
        pd.DataFrame: dataframe with new column for the metrics calculated 
            for each patient
    """
    # Initialize data for new column
    new_col_arr = np.zeros(len(ov_df))

    # Iterate through each patient (columns in sample overview df) and apply 
    # metric function 
    for i, samp in enumerate(ov_df['sample_name']):
        pt_path = os.path.join('data', 'raw', 'ChemoProjTCRs', samp + '.tsv')
        patient_df = pd.read_csv(pt_path, sep='\t', low_memory=False)
        new_col_arr[i] = metric_fn(patient_df, metric_col)
    
    # Save data to new column in sample overview df
    ov_df[ov_new_col] = new_col_arr
    return ov_df