def align_data(events, pitch_event):
    """transforms event data from opta pitch to secspec pitch."""
    # shift center of the pitch to origin (0,0)
    events.translate((- pitch_event.center[0], - pitch_event.center[1]))
    # rotate if playing from right to left (opta always left to right)
    if events.direction == 'rl':
        events.rotate(180)
    # rescale axis to pitch length
    events.scale(pitch_event.length / pitch_event.xlim[1], axis='x')
    events.scale(pitch_event.width / pitch_event.ylim[1], axis='y')
