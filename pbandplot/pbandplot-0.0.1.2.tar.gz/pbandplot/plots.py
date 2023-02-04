import matplotlib.pyplot as plt

def Broken(arr, fre, ticks, EXPORT, labels, figsize, vertical, broken):
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['font.family'] = 'Times New Roman'
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, height_ratios=[broken[2], 1-broken[2]], figsize=figsize)
    fig.subplots_adjust(hspace=0.0)
    ax1.plot(arr,fre.T,color='red',linewidth=1,linestyle='-')
    ax2.plot(arr,fre.T,color='red',linewidth=1,linestyle='-')
    plt.xlim(arr[0], arr[-1])
    if vertical is None:
        vertical = plt.ylim()

    ax1.set_ylim(broken[1], vertical[1])
    ax2.set_ylim(vertical[0], broken[0])
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position(position='none')

    ax1.tick_params(axis='y', which='minor', color='gray')
    ax1.tick_params(axis='y', labelsize='small', labelcolor='dimgray')
    ax2.tick_params(axis='y', which='minor', color='gray')
    ax2.axhline(linewidth=0.4,linestyle='-.',c='blue')

    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i,linewidth=0.4,linestyle='-.',c='gray')
            ax2.axvline(i,linewidth=0.4,linestyle='-.',c='gray')

    diff = len(ticks)-len(labels)
    if diff > 0:
        for i in range(diff):
            labels=labels+['']
    else:
        labels = labels[:len(ticks)]

    plt.xticks(ticks,labels)
    plt.suptitle('Frequency (THz)', rotation=90, x=0.06, y=0.6)
    kwargs = dict(marker=[(-1, -1), (1, 1)], markersize=6,
                  linestyle='', color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0.02, 0.02], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [0.98, 0.98], transform=ax2.transAxes, **kwargs)
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def Nobroken(arr, fre, ticks, EXPORT, labels, figsize, vertical):
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.figure(figsize=figsize)
    plt.plot(arr,fre.T,color='red',linewidth=1,linestyle='-')
    plt.tick_params(axis='y', which='minor', color='gray')
    plt.axhline(linewidth=0.4,linestyle='-.',c='blue')

    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            plt.axvline(i,linewidth=0.4,linestyle='-.',c='gray')

    diff = len(ticks)-len(labels)
    if diff > 0:
        for i in range(diff):
            labels=labels+['']
    else:
        labels = labels[:len(ticks)]

    plt.xticks(ticks,labels)
    plt.xlim(arr[0], arr[-1])
    plt.ylim(vertical)
    plt.ylabel('Frequency (THz)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def BrokenWd(arr, fre, ticks, EXPORT, labels, figsize, vertical, broken, darr, dele, elements):
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['font.family'] = 'Times New Roman'
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, height_ratios=[broken[2], 1-broken[2]], figsize=figsize)
    fig.subplots_adjust(wspace=0.0, hspace=0.0)
    ax1.plot(arr,fre.T,color='red',linewidth=1,linestyle='-')
    ax3.plot(arr,fre.T,color='red',linewidth=1,linestyle='-')
    ax2.plot(dele,darr,linewidth=0.8)
    ax4.plot(dele,darr,linewidth=0.8)
    ax1.set_xlim(arr[0], arr[-1])
    ax3.set_xlim(arr[0], arr[-1])
    if vertical is None:
        vertical = ax1.get_ylim()

    ax1.set_ylim(broken[1], vertical[1])
    ax2.set_ylim(broken[1], vertical[1])
    ax3.set_ylim(vertical[0], broken[0])
    ax4.set_ylim(vertical[0], broken[0])
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax4.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position(position='none')
    ax2.xaxis.set_ticks_position(position='none')
    ax3.xaxis.set_ticks_position(position='none')
    ax4.xaxis.set_ticks_position(position='none')

    ax1.tick_params(axis='y', which='minor', color='gray')
    ax1.tick_params(axis='y', labelsize='small', labelcolor='dimgray')
    ax3.axhline(linewidth=0.4,linestyle='-.',c='blue')
    ax4.axhline(linewidth=0.4,linestyle='-.',c='blue')
    ax2.tick_params(axis='y', which='minor', color='gray')
    ax1.set_xticklabels([])
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax4.set_xticklabels([])
    ax4.set_yticklabels([])
    ax2.axhline(linewidth=0.4,linestyle='-.',c='blue')
    if elements is not None:
        i = dele.shape[1]
        if len(elements) > i:
            elements = elements[:i]
    else:
        elements=[]

    ax2.legend(elements, title='Density of states', title_fontproperties={'style':'italic','size':'x-small'}, frameon=False, prop={'size':'small'})

    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i,linewidth=0.4,linestyle='-.',c='gray')
            ax3.axvline(i,linewidth=0.4,linestyle='-.',c='gray')

    diff = len(ticks)-len(labels)
    if diff > 0:
        for i in range(diff):
            labels=labels+['']
    else:
        labels = labels[:len(ticks)]

    ax3.set_xticks(ticks,labels)
    plt.suptitle('Frequency (THz)', rotation=90, x=0.06, y=0.6)
    kwargs = dict(marker=[(-1, -1), (1, 1)], markersize=6,
                  linestyle='', color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0.02, 0.02], transform=ax1.transAxes, **kwargs)
    ax3.plot([0, 1], [0.98, 0.98], transform=ax3.transAxes, **kwargs)
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')

def NobrokenWd(arr, fre, ticks, EXPORT, labels, figsize, vertical, darr, dele, elements):
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['font.family'] = 'Times New Roman'
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    fig.subplots_adjust(wspace=0.0)
    ax1.plot(arr,fre.T,color='red',linewidth=1,linestyle='-')
    ax2.plot(dele,darr,linewidth=0.8)
    ax1.set_xlim(arr[0], arr[-1])
    if vertical is None:
        vertical = ax1.get_ylim()

    ax1.set_ylim(vertical)
    ax2.set_ylim(vertical)
    ax1.xaxis.set_ticks_position(position='none')
    ax2.xaxis.set_ticks_position(position='none')

    ax1.tick_params(axis='y', which='minor', color='gray')
    ax1.axhline(linewidth=0.4,linestyle='-.',c='blue')
    ax2.tick_params(axis='y', which='minor', color='gray')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.axhline(linewidth=0.4,linestyle='-.',c='blue')
    if elements is not None:
        i = dele.shape[1]
        if len(elements) > i:
            elements = elements[:i]
    else:
        elements=[]

    ax2.legend(elements, title='Density of states', title_fontproperties={'style':'italic','size':'x-small'}, frameon=False, prop={'size':'small'})

    if len(ticks) > 2:
        ticks[0],ticks[-1] = arr[0],arr[-1]
        for i in ticks[1:-1]:
            ax1.axvline(i,linewidth=0.4,linestyle='-.',c='gray')

    diff = len(ticks)-len(labels)
    if diff > 0:
        for i in range(diff):
            labels=labels+['']
    else:
        labels = labels[:len(ticks)]

    ax1.set_xticks(ticks,labels)
    ax1.set_ylabel('Frequency (THz)')
    plt.savefig(EXPORT, dpi=750, transparent=True, bbox_inches='tight')


