
import queue
import time
import traceback
from typing import Any, List, Optional
from dataclasses import dataclass
from threading import Thread, Condition, Event

from typeguard import typechecked
from .base import BaseModel


class ItemFuture:
    def __init__(self, cancellation_token: Optional[Event]=None):
        self._condition = Condition()
        self._flag_done = False
        self._flag_cancelled = False
        self._external_ct = cancellation_token
        self._exception: Optional[Exception] = None
        self._result: Any = None
    
    def get_result(self, timeout: Optional[float]=None) -> Any:
        ''' Return the result of task future
            Args:
                timeout: the number of seconds to wait for result
                         raise PredictTimeoutError on timeout
                         Default: None, will never timeout
            Raises:
                PredictTimeoutError: If the future is not done before timeout
                PredictCancelledError: If the future is cancelled
        '''
        with self._condition:
            if self._flag_cancelled:
                raise PredictCancelledError('predict cancelled')
            if not self._flag_done:
                self._condition.wait(timeout)
                if self._flag_cancelled:
                    raise PredictCancelledError('predict cancelled')
                if not self._flag_done:
                    raise PredictTimeoutError('predict timeout')
            # from here, _flag_done == True
            if self._exception:
                raise self._exception
            return self._result

    def set_cancelled(self):
        ''' Try to mark cancelled for the task future. Won't actuallly 
            interrupt the process if the task has already started running
        '''
        with self._condition:
            if self._flag_done or self._flag_cancelled:
                return
            self._flag_cancelled = True
            self._condition.notify_all()
            
    def is_cancelled(self) -> bool:
        ''' Return if future is cancelled
        '''
        with self._condition:
            return self._flag_cancelled
        
    def is_external_ct_set(self) -> bool:
        ''' Return if external cancallation token is set
        '''
        return self._external_ct is not None and self._external_ct.is_set()

    def set_result(self, result: Any):
        ''' Set result for the future and mark it done.
            Should only be used by Promise holder
        '''
        with self._condition:
            if self._flag_done:
                return
            self._result = result
            self._flag_done = True
            self._condition.notify_all()
    
    def set_excepted(self, e: Exception):
        ''' Set exception for the future and mark it done.
            Should only be used by Promise holder
        ''' 
        with self._condition:
            if self._flag_done:
                return
            self._exception = e
            self._flag_done = True
            self._condition.notify_all()


@dataclass
class ItemMessage:
    future: ItemFuture
    item: Any


class PredictCancelledError(Exception):
    pass


class PredictTimeoutError(Exception):
    pass


class DynamicBatchModel:
    ''' Wrapped Model for dynamic batching automatically.
    
    A backend thread will serve all the callers. It merges data 
    inputs from multiple calls, and process batchly. Then return 
    corresponding results to each callers.
    
    '''
    
    @typechecked
    def __init__(
        self, 
        model: BaseModel, 
        max_batch_size: int = 12,
        idle_batch_size: int = 5,
        max_batch_interval: float = 0.002,
    ):
        '''
        Args: 
            model: Subclass of BaseMode, to provide business logic
            max_batch_size: Max size of each processing batch
            idle_batch_size: If there's no more data in queue, a new batch will be launched when size reaches this value
            max_batch_interval: Max interval in seconds to wait for items. When waiting time exceeds, will launch a batch immediately.

        '''
        assert idle_batch_size <= max_batch_size

        self.model = model
        self.max_batch_size = max_batch_size
        self.idle_batch_size = idle_batch_size
        self.max_batch_interval = max_batch_interval
        
        self.alive = True
        self.q: queue.Queue[ItemMessage] = queue.Queue()
        self.worker = Thread(target=self._worker_run, daemon=True)
        self.worker.start()
        
    
    @typechecked
    def predict(
        self,
        items: List[Any],
        timeout: Optional[float] = 1.0,
        raise_timeout: bool = True,
        cancellation_token: Optional[Event] = None,
    ) -> List[Any]:
        ''' Predict with dynamic batching
        
        Args:
            items: model input list
            timeout: A floating point number specifying a timeout for the operation in seconds, or None 
                    indicating to wait without timeout
            raise_timeout: When timeout, True: raise PredictTimeoutError; False: set to None for 
                    no result items and return.
            cancellation_token: A event for cancellation. If the event is set, will try to cancel and skip
                    the calculation in downstream batch process. Default: None.
            
        Returns:
            predict output list
        
        '''
        # get futures & put messsage into queue
        futurelist: List[ItemFuture] = []
        for item in items:
            future = ItemFuture(cancellation_token)
            msg = ItemMessage(future, item)
            self.q.put_nowait(msg)
            futurelist.append(future)
        
        # get results
        rs = []
        start_time = time.perf_counter()
        for future in futurelist:
            if timeout is None:
                time_left = None
            else:
                time_left = timeout - (time.perf_counter() - start_time)
            try:
                result = future.get_result(timeout=time_left)
            except PredictTimeoutError:
                future.set_cancelled()
                if raise_timeout:
                    raise
                else:
                    result = None
            rs.append(result)
        return rs


    @typechecked
    def predict_one(
        self,
        item: Any,
        timeout: Optional[float] = 1.0,
        raise_timeout: bool = True,
        cancellation_token: Optional[Event] = None,
    ) -> Any:
        ''' Predict for a single item, with dynamic batching
        
        Args:
            item: model input, a single item
            timeout: A floating point number specifying a timeout for the operation in seconds, or None 
                    indicating to wait without timeout
            raise_timeout: When timeout, True: raise PredictTimeoutError; False: set to None for 
                    no result items and return.
            cancellation_token: A event for cancellation. If the event is set, will try to cancel and skip
                    the calculation in downstream batch process. Default: None.
            
        Returns:
            single predict output
        
        '''
        rs = self.predict(
            [item], 
            timeout=timeout, 
            raise_timeout=raise_timeout, 
            cancellation_token=cancellation_token,
        )
        return rs[0]

    
    def close(self):
        self.alive = False
        
        
    def __del__(self):
        self.close()
        
        
    def _worker_run(self):
        ''' If _worker_inner failed somehow, sleep some time and retry
        '''
        while self.alive:
            try:
                self._worker_inner()
            except Exception:
                # unexpected error
                traceback.print_exc()
                time.sleep(0.1)
                
                
    def _worker_inner(self):
        ''' condition to trigger a batch run:
            1. [batch size] >= self.max_batch_size
            2. queue is empty && [batch size] >= self.idle_batch_size
            3. [now] - [last run time] >= self.max_batch_interval
        '''
        batch: List[ItemMessage] = []          # cached batch items
        last_run_time = time.perf_counter()    # last batch run time
        
        while self.alive:
            # get from q without block & check empty
            try:
                msg = self.q.get_nowait()
                # handle cancellation
                if msg.future.is_external_ct_set():
                    msg.future.set_cancelled()
                    continue
                elif msg.future.is_cancelled():
                    continue
                else:
                    batch.append(msg)
            except queue.Empty:
                msg = None

            # here msg is None means q is empty, idle
            # idle && size >= idle_batch_size, trigger batch run
            if msg is None and len(batch) >= self.idle_batch_size:
                self._worker_run_batch(batch)
                batch = []
                last_run_time = time.perf_counter()
                continue

            # q is empty and still have time left, get from q with timeout
            if msg is None:
                timeout = self.max_batch_interval - (time.perf_counter() - last_run_time)
                if timeout > 0:
                    try:
                        msg = self.q.get(block=True, timeout=timeout)
                        # handle cancellation
                        if msg.future.is_external_ct_set():
                            msg.future.set_cancelled()
                            continue
                        if msg.future.is_cancelled():
                            continue
                        else:
                            batch.append(msg)
                    except queue.Empty:
                        msg = None

            # here msg is None means timeout
            # timeout or batch reached max size, trigger batch run
            if msg is None or len(batch) >= self.max_batch_size:
                if batch:
                    self._worker_run_batch(batch)
                    batch = []
                last_run_time = time.perf_counter()
            
            
    def _worker_run_batch(self, batch: List[ItemMessage]):
        # preprocess & predict
        try:
            input = [msg.item for msg in batch]
            output_preprocess = self.model.preprocess(input)
            output_predict = self.model.predict(output_preprocess)
            
            if len(output_predict) != len(batch):
                raise Exception(f'model output size is {len(output_predict)} while input size is {len(batch)}')
            
        except Exception as e:
            for msg in batch:
                msg.future.set_excepted(e)
            return
        
        # set result for each
        for msg, result in zip(batch, output_predict):
            msg.future.set_result(result)
