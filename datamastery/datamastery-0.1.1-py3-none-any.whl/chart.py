import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def pie_chart(x: str, data: pd.DataFrame, explode=None, colors=None, autopct=None,
              pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1,
              counterclock=True, wedgeprops=None, textprops=None, center=(0, 0),
              frame=False, rotatelabels=False, figsize=(8, 6)
              ):
    """
    """
    count = []
    perc_list = []
    for i in data[x].value_counts():
        count.append(i)
    count_arr = np.array([count])
    for i in count:
        perc_list.append(int(round(i / count_arr.sum(), 2) * 100))
    label_list = data[x].value_counts().index.to_list()
    plt.figure(figsize=figsize)
    plt.pie(x=perc_list, data=data, labels=label_list, explode=explode,
            colors=colors, autopct=autopct, pctdistance=pctdistance, shadow=shadow,
            labeldistance=labeldistance, startangle=startangle, radius=radius,
            counterclock=counterclock, wedgeprops=wedgeprops, textprops=textprops,
            center=center, frame=frame, rotatelabels=rotatelabels)
    plt.show()
