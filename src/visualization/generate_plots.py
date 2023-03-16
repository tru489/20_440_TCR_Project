import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_stripplot(ov_df, xslice, yslice, ylabel, filename, show=False):
    """
    Plot stripplot given dataframe and x and y column names

    Args:
        ov_df (pd.DataFrame): dataframe with data for plotting
        xslice (str): dataframe column to use for x values
        yslice (str): dataframe column to use for y values
        ylabel (str): label for y axis
        filename (str): filename to which file will be saved
        show (bool, optional): toggles whether plot will be shown after 
            plotting. Defaults to False.
    """
    plt.figure()
    sns.stripplot(data=ov_df, x=xslice, y=yslice)
    plt.xlabel('')
    plt.ylabel(ylabel)

    plt.savefig(os.path.join('fig', 'main_fig', filename), bbox_inches='tight')
    
    if show: plt.show()