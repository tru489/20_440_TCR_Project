def get_richness(patient_df, col_name):
    """
    Gets richness (number of unique values) given a dataframe and target column

    Args:
        patient_df (pd.DataFrame): patient dataframe
        col_name (str): column to search through

    Returns:
        int: number of unique values in the specified column of patient_df
    """
    return len(patient_df[col_name].unique())


def get_richness_vdj(patient_df, col_name):
    """
    Gets number of unique combinations of V, D, and J genes given a patient's
    sequencing data dataframe

    Args:
        patient_df (pd.DataFrame): patient dataframe
        col_name (str): destination column to which concatenated V, D, and J
            gene names will be added for quantification

    Returns:
        int: number of unique combinations of V, D, and J genes for a patient
    """
    patient_df[col_name] = patient_df['vGeneName'] + ', ' \
        + patient_df['dGeneName'] + ', ' + patient_df['jGeneName']
    return get_richness(patient_df, col_name)