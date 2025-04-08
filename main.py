import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data() -> pd.DataFrame:
    df = pd.read_csv("pokemon.csv")
    return df

def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    return df

def wide_to_long_format(df:pd.DataFrame) -> pd.DataFrame:
    stats_df = df.drop(["#","Total", "Generation", "Legendary"], axis=1)
    #melted_stats = pd.melt(stats_df, id_vars=["Name", "Type 1", "Type 2"], value_vars=["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], var_name="Stat", value_name="Value")
    melted_df = stats_df.melt(id_vars=["Name", "Type 1", "Type 2"], value_vars=["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], var_name="Stat", value_name="Value")
    return melted_df


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)


    # Long format ( changeing all different stats[attributes] to long format[one column])
    """
    df = wide_to_long_format(df)
    print(df)
    """
    
    # Stripplot
    """
    sns.stripplot(x="Stat", y="Value", hue="Type 1", data=df)
    """

    # Swarmplot
    """
    sns.swarmplot(x="Stat", y="Value", hue="Type 1", data=df)# takes a while to load and to respond
    plt.ylim(0, 260)
    plt.legend(bbox_to_anchor=(1, 1), loc=2)
    """

    
    # Single plot (Attack)
    """
    x = np.sort(df["Attack"])
    y = np.array(range(1, len(x)+1)) / len(x)

    g = plt.plot(x, y, marker=".", linestyle="None")
    g = plt.xlabel("Attack")
    g = plt.ylabel("ECDF")
    
    plt.margins(0.02)
    """


    # Multiple plots (Attack, Defense, Speed)
    """
    attack = np.sort(df["Attack"])
    defense = np.sort(df["Defense"])
    speed = np.sort(df["Speed"])

    y = np.array(range(1, df.shape[0]+1)) / df.shape[0]

    g = plt.plot(attack, y, marker=".", linestyle="None")
    g = plt.plot(speed, y, marker=".", linestyle="None")
    g = plt.plot(defense, y, marker=".", linestyle="None")
    
    
    g = plt.xlabel("Stats")
    g = plt.ylabel("ECDF")
    plt.margins(0.02)
    """
    

    # Heatmap
    """
    corr = df.drop(["#", "Total", "Generation", "Legendary", "Name", "Type 1", "Type 2"], axis=1).corr()
    sns.heatmap(corr)#, annot=True, cmap="Blues")
    """


    # Countplot
    """
    sns.countplot(x="Type 1", data=df)
    plt.xticks(rotation=45)
    """



    # Jointplot
    """
    sns.jointplot(x="Attack", y="Defense", data=df)
    """



    plt.show()