import pandas as pd
import matplotlib.pyplot as plt
from .colors import cnc_rgb

# TODO: to complete
trans_dict = {
    'red': 'hong',
    'grey': 'hui',
    'gray': 'hui',
    'purple': 'zi',
    'yellow': 'huang',
    'cyan': 'qing',
    'green': 'lv',
    'blue': 'lan',
    'white': 'bai',
    'brown': 'zong',
    'black': 'hei',
}


def show_color(clr_name=None):
    print(f'Reference: http://zhongguose.com/#{clr_name}')
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.set_title(f'Name: {clr_name}; RGB: {cnc_rgb[clr_name]}')
    ax.scatter(1, 1, c=cnc_rgb[clr_name], s=1e4, marker='s')

def show(clr_name=None, ncol=3, fs=15, figsize=[10, 20]):
    print(f'Reference: http://zhongguose.com')
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis('off')
    i_row, i_col = 0, 0
    if clr_name is None:
        clr_dict = cnc_rgb
    else:
        clr_name = trans_dict[clr_name] if clr_name in trans_dict else clr_name
        clr_dict = {k: v for k, v in cnc_rgb.items() if clr_name in k}

    for k, v in clr_dict.items():
        ax.scatter(i_col, i_row, c=v, s=1e2, marker='s', edgecolor='k')
        ax.text(i_col+0.1, i_row, k, color='k', fontsize=fs, verticalalignment='center')
        i_col -= 1
        if i_col == -ncol:
            i_row -= 1
            i_col = 0

def to_df():
    df = pd.DataFrame(cnc_rgb.items(), columns=['name', 'rgb'])
    print(f'Reference: http://zhongguose.com')
    return df




