#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2023/1/9
"""

from fast_tracker import config, ComponentType, Layer
from fast_tracker.trace.carrier import Carrier
from fast_tracker.trace.context import get_context
from fast_tracker.trace.tags import Tag
from fast_tracker.utils import functions


def install():
    from rq.job import Job
    from rq.queue import Queue

    _job_perform = Job.perform

    def _fast_job_perform(this: Job):
        context = get_context()
        carrier = Carrier()
        trace_id_name = config.get_trace_id_name()
        trace_id = this.meta.get(trace_id_name)
        span_pid = this.meta.get("span_id")
        for item in carrier:
            if type(item) is Carrier and trace_id:
                item.set_frontend_trace_id(trace_id)
        functions.log("job info %s %s", this.kwargs, this.meta)
        with context.new_entry_span(op="RQ/" + this.func_name, carrier=carrier) as span:
            span.extract(carrier)
            span.pid = span_pid
            span.layer = Layer.Http
            span.component = ComponentType.RQ
            span.tag(Tag(key="RQ JOB", val=this.func_name))
            return _job_perform(this)

    Job.perform = _fast_job_perform

    _enqueue_call = Queue.enqueue_call

    def _fast_enqueue_call(this: Queue, func, **kwargs):
        context = get_context()
        trace_id_name = config.get_trace_id_name()
        trace_id = ""
        with context.new_exit_span(op=ComponentType.Falcon, peer="enqueue job") as span:
            carrier = span.inject()
            span.Layer = Layer.Http
            span.component = ComponentType.RQ
            span.tag(Tag(key="RQ QUEUE", val=func.__name__))
            for item in carrier:
                if getattr(item, "trace_id", None):
                    trace_id = item.trace_id
                    break
            meta = kwargs.get("meta")
            if not meta:
                kwargs["meta"] = {trace_id_name: trace_id, "span_id": span.sid}
            else:
                kwargs["meta"].update({trace_id_name: trace_id, "span_id": span.sid})

        return _enqueue_call(this, func, **kwargs)

    Queue.enqueue_call = _fast_enqueue_call
