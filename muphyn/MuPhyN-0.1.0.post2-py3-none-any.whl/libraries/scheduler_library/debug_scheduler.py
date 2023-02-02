#-----------------------------------
# Imports
#-----------------------------------

import os
import time
import pandas as pd
from typing import Any

from muphyn.packages.core.plci_core_scheduler import Scheduler
from muphyn.packages.core.utils.file import CreateDirectory

#-----------------------------------
# Methods
#-----------------------------------

def _execute_box (scheduler: Scheduler, event, box) -> None :
    
    new_events = box.function(event)

    if scheduler.is_scheduler_exception(new_events) :
        return new_events

    for event in new_events :
        
        scheduler.append_event(event)

        if event.signal in scheduler.diagram.linked_signals :
            for signal in scheduler.diagram.linked_signals[event.signal] :
                scheduler.append_event(scheduler.construct_signal_event(signal, event.box, event.new_signal_data))

def _default_scheduler_method (scheduler: Scheduler) -> Any :
    
    b_bis = None
    event = None
    b = None

    # Init pandas table 
    timings = {
        "box": [], "box_start_time": [], "box_end_time": [], "scheduler_start_exception_time": [], "scheduler_end_exception_time": []
    }

    # Global start time
    global_start_time = time.perf_counter()

    try :

        while scheduler.should_simulation_continue :
            
            for b in scheduler.diagram.boxes :
                timings["box"].append(f"{b.name}_{b.index}")
                
                # Execute box
                timings["box_start_time"].append(time.perf_counter())
                new_events = _execute_box(scheduler, scheduler.construct_event(), b)

                # Scheduler Exception time
                scheduler_exception_start_time = time.perf_counter()
                timings["box_end_time"].append(scheduler_exception_start_time)
                timings["scheduler_start_exception_time"].append(scheduler_exception_start_time)

                # Scheduler Exception
                if scheduler.is_scheduler_exception(new_events) :
                    return new_events
                    
                # Scheduler Exception time
                timings["scheduler_end_exception_time"].append(time.perf_counter())

                while scheduler.are_events_left :
                    
                    event = scheduler.get_event(0)
                    event.signal.data = event.new_signal_data

                    if event.signal in scheduler.diagram.box_inputs :
                    
                        for b_bis in scheduler.diagram.box_inputs[event.signal] :
                            timings["box"].append(f"{b_bis.name}_{b_bis.index}")
                            
                            # Execute box
                            timings["box_start_time"].append(time.perf_counter())
                        
                            new_events = _execute_box(scheduler, scheduler.construct_event(event), b_bis)

                            # Scheduler Exception time
                            scheduler_exception_start_time = time.perf_counter()
                            timings["box_end_time"].append(scheduler_exception_start_time)
                            timings["scheduler_start_exception_time"].append(scheduler_exception_start_time)
                            
                            if scheduler.is_scheduler_exception(new_events) :
                                return new_events

                            # Scheduler Exception time
                            timings["scheduler_end_exception_time"].append(time.perf_counter())
                            
                    scheduler.remove_event(event)

            scheduler.stepping_time()

    except Exception as err :
        return scheduler.construct_exception(b, b_bis, event, err)

    
    # Global end time
    global_end_time = time.perf_counter()

    # Convert to dataframe
    pd_timings = pd.DataFrame(timings)

    # 
    pd_timings["box_duration"] = pd_timings["box_end_time"] - pd_timings["box_start_time"]
    pd_timings["scheduler_duration"] = pd_timings["scheduler_end_exception_time"] - pd_timings["scheduler_start_exception_time"]

    # Create directory if doesn't exists
    directory = "LOGS/Time"
    CreateDirectory(directory)

    # Save timing report
    pd_timings.to_csv(os.path.join(directory, f"Log_time_{time.strftime('%Y_%m_%j_%H_%M_%S')}.csv"), sep=";", decimal=",")