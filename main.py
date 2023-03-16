import os
import pandas as pd

from src.data.preprocess_overview import preprocess_overview
from src.analysis.parse_patient_data import parse_patients
from src.util.helper_functions import get_richness_vdj
from src.visualization.generate_plots import plot_stripplot

def main():
    """
    Main file in driver script from which all code is run
    """
    # Determine whether to load precalculated data or calculate
    load_precalculated = False
    
    saved_df_path = os.path.join('data', 'processed', 'precalculated.tsv')
    if not load_precalculated:
        # Parse overview tsv file
       samp_overview_path = './data/analysis/SampleOverview.tsv'
       ov_df = preprocess_overview(samp_overview_path)

       # Calculate from patient sequencing data
       ov_df = parse_patients(ov_df, 
                            get_richness_vdj, 'vdjGenes', 'richness_vdjgene')
       ov_df.to_csv(saved_df_path, sep="\t")
    else:
       ov_df = pd.read_csv(saved_df_path, sep="\t")

    ## Plotting
    plot_stripplot(ov_df, 'group_label', 'richness_vdjgene', 
           'Number of Unique V, D, J-gene Combinations', 
           'rich_vdjgene_violin.jpg')
    

if __name__ == "__main__":
    # Run main function when driver script is run in bash
    main()