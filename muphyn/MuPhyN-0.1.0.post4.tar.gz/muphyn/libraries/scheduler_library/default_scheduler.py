#-----------------------------------
# Imports
#-----------------------------------

from typing import Any

from muphyn.packages.core.plci_core_scheduler import Scheduler

#-----------------------------------
# Methods
#-----------------------------------

def _execute_box (scheduler: Scheduler, event, box) -> None :
    
    #if event.signal is None :
    #    print("Running none event to ", box)
    #else : 
    #   print("Running event from ", event.box, " on ", event.signal, " to ", box)

    # print(box.name)
    
    new_events = box.function(event)

    if scheduler.is_scheduler_exception(new_events) :
        return new_events

    for event in new_events :
        
        # print("add event from ", event.box, " on ", event.signal)
        scheduler.append_event(event)

        if event.signal in scheduler.diagram.linked_signals :
            #print("event on ", event.signal, " at time", scheduler.current_time," and it is linked | # of events : ", scheduler.events_count)

            for signal in scheduler.diagram.linked_signals[event.signal] :
                scheduler.append_event(scheduler.construct_signal_event(signal, event.box, event.new_signal_data))
                #print(event.signal, " is connected to ", signal.index," | # of events now : ", scheduler.events_count)

def _default_scheduler_method (scheduler: Scheduler) -> Any :
    
    b_bis = None
    event = None
    b = None

    try :

        while scheduler.should_simulation_continue :
            
            for b in scheduler.diagram.boxes :
                
                new_events = _execute_box(scheduler, scheduler.construct_event(), b)
                if scheduler.is_scheduler_exception(new_events) :
                    return new_events

                while scheduler.are_events_left :
                    
                    event = scheduler.get_event(0)
                    event.signal.data = event.new_signal_data

                    if event.signal in scheduler.diagram.box_inputs :
                    
                        for b_bis in scheduler.diagram.box_inputs[event.signal] :
                            
                            new_events = _execute_box(scheduler, scheduler.construct_event(event), b_bis)
                            if scheduler.is_scheduler_exception(new_events) :
                                return new_events
                    
                    scheduler.remove_event(event)

            scheduler.stepping_time()

    except Exception as err :
        return scheduler.construct_exception(b, b_bis, event, err)