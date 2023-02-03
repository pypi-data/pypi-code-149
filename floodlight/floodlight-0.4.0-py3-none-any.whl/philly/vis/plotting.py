def plot_all_passes(events):
    all_pass_events = events.select(conditions=[
        ("eID", 1),
        ("outcome", 1),
    ])
    all_pass_events.reset_index(drop=True, inplace=True)
    fig, ax = plt.subplots()
    pitch_xy.plot(ax=ax, color_scheme="bw", show_axis_ticks=True)
    for i in events.events.index:
        event = events.events.loc[i]
        x = [event["at_x"], event["to_x"]]
        y = [event["at_y"], event["to_y"]]
        ax.plot(x, y, '--r', markersize=12)



# # plot event
# for i in success_pass_events.index:
#     event = success_pass_events.loc[i]
#     x = [event["at_x"], event["to_x"]]
#     y = [event["at_y"], event["to_y"]]
#     t = event["frameclock"]
#
#     fig, ax = plt.subplots()
#     pitch_xy.plot(ax=ax, show_axis_ticks=True)
#     home_ht1_xy.plot(t=t, ax=ax, color="darkblue")
#     away_ht1_xy.plot(t=t, ax=ax, color="orange")
#     ball_ht1_xy.plot(t=t, ax=ax, ball=True)
#     ax.plot(x, y, '--r', markersize=12)
#     # plt.savefig(f"event_{e_nummer}.png")
#     # plt.close()