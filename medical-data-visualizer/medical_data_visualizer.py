import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) **2 > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
#print(df)

# 4
def draw_cat_plot():
    
    # 5
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    #print(df_cat)
    
    # 6
    df_cat = df_cat.groupby(['cardio' , 'variable', 'value']).size().reset_index(name='total')
    df_cat['value'] = df_cat['value'].astype(str)
    #print(df_cat)


    # 8
    fig = sns.catplot(data=df_cat, x='variable', y='total', kind='bar', hue='value', col='cardio').fig
    """
    # 5
    df_cat = pd.melt(pd, id_vars='cardio', value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    # 6
    df_cat['value'] = df_cat['value'].astype(str)
    # 7
    # 8
    fig = sns.catplot(data=df_cat, x='variable', kind='count', hue='value' ,hue_order=['0', '1'], col='cardio')
    fig.set_axis_labels(None, 'total')
    """
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    """
    print(pd_data['height'].quantile(0.025), 
    pd_data['height'].quantile(0.975), 
    pd_data['weight'].quantile(0.025), 
    pd_data['weight'].quantile(0.975))
    """
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))]
    
    """
    print(df_heat[df_heat['height'] > 180])
    print(df_heat[df_heat['height'] < 150])
    print(df_heat[df_heat['height'] > 108.0])
    print(df_heat[df_heat['height'] < 51.0])
    """

    # 12
    corr = df_heat.corr()
    #print(corr)

    # 13
    mask = np.triu(np.ones((14, 14))).astype(bool)
    #print(mask)



    # 14
    fig, ax = plt.subplots()
    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        annot_kws={'fontsize':6}, 
        vmax=0.32, 
        vmin=-0.16, 
        center=0, 
        linewidths=0.5)

    # 16
    plt.savefig('heatmap.png')
    return fig

if __name__ == '__main__':
    draw_cat_plot()
    draw_heat_map()