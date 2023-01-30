import valueparser
from pydevmgr_core.base import  BaseNode, NodeAlias, NodeAlias1, register

from collections import deque
import time
from  datetime import datetime, timedelta
from typing import Union, List, Dict, Optional, Any
from py_expression_eval import Parser
from dataclasses import dataclass
import math

from pydevmgr_core.base.object_path import PathVar 

_eval_parser = Parser()


__all__ = [
"BaseNode", 
"NodeAlias", 
"NodeAlias1",
"Local", 
"Static", 
"Value", 
"Time", 
"DateTime", 
"UtcTime", 
"Counter", 
"AllTrue","All",  
"AnyTrue","Any", 
"AllFalse", 
"AnyFalse", 
"Oposite", 
"DequeList", 
"Deque", 
"InsideInterval", 
"InsideCircle", 
"PosName", 
"Formula", 
"Formula1", 
"Polynom", 
"Statistics",
"Sum", 
"Mean", 
"Min", 
"Max", 
"Format", 
"Bits", 
"MaxOf", 
"MinOf", 
"MeanOf",
"Rad2Degree", 
"Degree2Rad", 
"Tempo", 
"NoError", 
"Tempo",
"ElapsedTime", 
"Timeout"
]


class __Undefined__:
    pass


@register
class Local(BaseNode):
    """ The node is getting/setting values from the localnode_values dictionary inside the engine

    The localnode_values dictionary is created as part of the base engine. 
    Values are writen inside this dictionary. 
    If not already set, configured default is return 

    Config:
        default (any)
    """
    class Config(BaseNode.Config):
        default: Any = None
        
    def fget(self):
        if self.engine.localnode_values is None:
            return self.config.default                
        return self.engine.localnode_values.get(self.key,self.config.default)
        
    def fset(self, value):
        self.engine.localnode_values[self.key] = value




@register
class Static(BaseNode):
    """ Static node always returning the configured value and cannot be set 

    Config:
        value (any) 
    """
    class Config(BaseNode.Config):    
        value: Any

    def fget(self):        
        return self.config.value    

@register
class Value(BaseNode):
    """ A node storing its own value mostly for test or patch puposes 

    Config:
        value (any) : default is None, a value starting point 
    """
    class Config(BaseNode.Config):    
        value: Any
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = self.config.value 
    
    def fget(self):
        return self._value 

    def fset(self, value):
        self._value = value



class Time(BaseNode):
    """ A basic node returning the float local time  
    
    Args:
        key (optional, str): node key
        delta (optional, float): time shift in seconds 
    
    """
    class Config(BaseNode.Config):
        delta: float = 0.0
    
    def __init__(self, key: str = 'time', config=None, **kwargs):
        super().__init__(key, config=config, **kwargs)
        
    def fget(self) -> float:
        return time.time()+self.config.delta 

@register
class DateTime(BaseNode):
    """ A basic node returning the float local time  
    
    Args:
        key (optional, str): node key
        delta (optional, float): time shift in seconds 
        
    """
    class Config(BaseNode.Config):
        delta: float = 0.0 # delta in seconds 
        
    def __init__(self, key: str = 'datetime', config=None, **kwargs):
        super().__init__(key, config=config, **kwargs)
    
    def fget(self) -> float:
        return datetime.now()+timedelta(seconds=self.config.delta)
        

@register
class UtcTime(BaseNode):
    """ A basic node returning the local UTC as string 
    
    Args:
        key (str, optional): node key
        delta (float, optional): time shift in seconds 
        format (str, optional): Returned format, default is iso 8601 '%Y-%m-%dT%H:%M:%S.%f%z'
    """
    class Config(BaseNode.Config):
        delta: float = 0.0
        format: str = '%Y-%m-%dT%H:%M:%S.%f%z'
        
    def __init__(self, key : str ='utc', config=None, **kwargs):
        super().__init__(key, config=config, **kwargs)
                
    def fget(self) -> str:
        tc = datetime.utcnow()+timedelta(seconds=self.config.delta)   
        return tc.strftime(self.config.format)
    

TimeStamp = valueparser.conparser( valueparser.Timestamp)   
@register
class ElapsedTime(BaseNode):
    """ A basic node returning elapsed seconds since 

    by default the time reference is set at first get unless given 

    Args:
        key (str, optional): default is 'elapsed_time'
        scale (float, optional): scale the time to an other unit than second  
        time_ref (optional, datetime, str iso, float): the time reference. If not given 
            it will be set the first time get is called 
    """
    class Config(BaseNode.Config):
        scale: float = 1.0
        time_ref:  Optional[TimeStamp] = None

    def __init__(self, key : str ='elapsed_time', config=None, **kwargs):
        super().__init__(key, config=config, **kwargs)
        
    def fget(self) -> float:
        tr = self.time_ref
        if tr is None:
            self.config.time_ref = time.time()
            return 0.0
        return (time.time()-tr)*self.config.scale

    def reset(self):
        self.config.time_ref = None


@register
class Tempo(BaseNode):
    """ A node return False until delay seconds occured since the first get 
    
    Parameters:
        time: (float) delay time in seconds
        time_ref (optional, datetime, str iso, float): the time reference. If not given 
            it will be set the first time get is called 

    """

    class Config:
        time: float = 0
        time_ref: Optional[TimeStamp] = None

    def __init__(self, key : str ='tempo', config=None, **kwargs):
        super().__init__(key, config=config, **kwargs)

    def fget(self) -> float:
        time_ref = self.time_ref
        if time_ref is None:
            self.config.time_ref = time.time()
            return False
        return (time.time()-time_ref)>=self.time
    def reset(self):
        self.config.time_ref = None

@register
class Timeout(BaseNode):
    """ A node return False until delay seconds occured then raise RuntimeError
    
    Parameters:
        time: (float) delay time in seconds
        time_ref (optional, datetime, str iso, float): the time reference. If not given 
            it will be set the first time get is called 

    """

    class Config:
        time: float = 0
        time_ref: Optional[TimeStamp] = None

    def __init__(self, key : str ='tempo', config=None, **kwargs):
        super().__init__(key, config=config, **kwargs)

    def fget(self) -> float:
        time_ref = self.time_ref
        if time_ref is None:
            self.config.time_ref = time.time()
            return False

        if  (time.time()-time_ref)>=self.time:
            raise RuntimeError(f"timeout ({self.time} sec)") 
        return False 

    def reset(self):
        self.config.time_ref = None




@register
class Counter(BaseNode):
    """ A simple counter node at each get the counter is increased and returned 
    
    Args:
        start (optional, int): start number 
        
    Example:
    
    ::
       >>> from pydevmgr_core.nodes import Counter 
       >>> c = Counter()
       >>> c.get()
       1
       >>> c.get()
       2
       >>> c.reset()
       >>> c.get()
       1
    """
    class Config(BaseNode.Config):
        start: int  = 0
        step: int = 1
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reset()
    
    def reset(self):
        self._counter = self.config.start
    
    def fget(self):
        self._counter += self.config.step
        return self._counter 



@register
class AllTrue(NodeAlias):
    @staticmethod
    def fget(*nodes):
        return all(nodes)
All = AllTrue

@register
class AnyTrue(NodeAlias):
    @staticmethod
    def fget(*nodes):
        return any(nodes)
Any = AnyTrue

@register        
class AllFalse(NodeAlias):
    @staticmethod 
    def fget(*nodes):
        return not any(nodes)

@register
class AnyFalse(NodeAlias):
    @staticmethod
    def fget(*nodes):
        return not all(nodes)



@register
class Opposite(NodeAlias1):
    """ rNodeAlias1, Return the "not value" of the aliased node """
    @staticmethod
    def fget(value):
        return not value 



@register
class DequeList(NodeAlias):
    """ This is an :class:`NodeAlias` returning at each get a :class:`collections.deque` 
    
    The deque items contains a list of values of the size of the input nodes
    
    Specially handy for live plot and scopes
    
    Args:
       key (string): alias node keyword 
       nodes (list of :class:`UaNode`,:class:`NodeAlias`): 
              List of nodes to get()  
       maxlen (int): maximum len of the dequeu object  
    
    Example:
        
         
    ::
    
        >>> from pydevmgr_core.nodes import Time, Counter, DequeList
        >>> q = DequeList(nodes= [Time(), Counter()] , maxlen=20)
        >>> q.get()
        deque([(1649922096.212783, 1)])
        >>> q.get()
        deque([(1649922096.212783, 1), (1649922104.106418, 2)])
        >>> q.get()
        deque([(1649922096.212783, 1), (1649922104.106418, 2), (1649922106.154751, 3)])
        >>> # etc ....

    .. seealso::
       :class:`Deque` 

        
    """
    class Config(NodeAlias.Config):
        maxlen: int = 10000
        trigger_index: Optional[int] = None
    
    def __init__(self, 
          key: Optional[str] = None, 
          nodes: Optional[Union[BaseNode,List[BaseNode]]] = None, 
          config: Optional[Config] = None,
          **kwargs
        ) -> None: 
        
        if nodes is None:
            raise ValueError("nodes cannot be None")    
        super().__init__(key, nodes, config, **kwargs)        
        
        self._data = deque([], self.config.maxlen)
        self._scalar = not hasattr(nodes, "__iter__")
                
        
    @property
    def data(self):
        return self._data 
    
    @property
    def columns(self):
        return [n.key for n in self.nodes()]
    
        
    def fget(self, *values): 
        if self.config.trigger_index is not None and not values[self.config.trigger_index]:
            return self._data      
        
        if self._scalar:
            self._data.append(values[0])
        else:
            self._data.append(values)
        return self._data
    
    def reset(self, maxlen=None):
        if maxlen is not None:
            self.config.maxlen = maxlen
                
        if self._maxlen != self.config.maxlen:             
            # maxlen has been changed 
            self._maxlen = self.config.maxlen        
            self._data = deque([], self.config.maxlen)
        else:
            self._data.clear()




@register
class Deque(NodeAlias1):
    """ This is an :class:`NodeAlias1` returning at each get a :class:`collections.deque` 
    
    Specially handy for live plot and scopes
    
    Args:
       key (string): alias node keyword 
       node  ( :class:`UaNode`,:class:`NodeAlias`): 
              
       maxlen (int): maximum len of the dequeu object  
    
    .. seealso::
       :class:`DequeList` 
        
    """
    class Config(NodeAlias1.Config):
        maxlen: int = 10000        
    
    def __init__(self, 
          key: Optional[str] = None, 
          node: Optional[Union[BaseNode,List[BaseNode]]] = None, 
          config: Optional[Config] = None,
          **kwargs
        ) -> None: 
        
        super().__init__(key, node, config, **kwargs)
        self._maxlen = self.config.maxlen        
        self._data = deque([], self.config.maxlen)                        
        
    @property
    def data(self):
        return self._data 
        
    def fget(self, value):         
        self._data.append(value)
        return self._data
    
    def reset(self, maxlen=None):
        if maxlen is not None:
            self.config.maxlen = maxlen
                
        if self._maxlen != self.config.maxlen:             
            # maxlen has been changed 
            self._maxlen = self.config.maxlen        
            self._data = deque([], self.config.maxlen)
        else:
            self._data.clear()

@register
class InsideInterval(NodeAlias1):
    """ Bool Node alias to check if a value is inside a given interval 
    
    Args:
        key (str):  node key
        node (:class:`BaseNode`): node returning a float 
        min (float, optional): min value of the interval 
        max (float, optional): max value of the interval
    """
    class Config(NodeAlias1.Config):
        min : Optional[float] = None
        max : Optional[float] = None
            
    def fget(self, value):
        c = self.config
        if c.min is not None and value<c.min:
            return False
        if c.max is not None and value>c.max:
            return False
        return True    

@register
class InsideCircle(NodeAlias):
    """ Bool Node alias to check if a 2d position is inside a circle 
    
    Args:
        key (str): node key
        nodes (list of :class:`BaseNode`): two nodes returning x and y coordinates 
        x0, y0 (float): circle origin  default is (0.0, 0.0)
        r (float): circle radius (default is 1.0)
    
    """
    class Config(NodeAlias.Config):
        x0 : float = 0.0
        y0 : float = 0.0 
        r  : float = 1.0
            
    _n_nodes_required = 2    
    
    def fget(self, x, y):
        c = self.config
        return ((x-c.x0)**2 + (y-c.y0)**2) < (c.r*c.r)        
        
@register    
class PosName(NodeAlias1):
    """ Node alias returning a position name thanks to a list of position and a tolerance 
    
    Args:
        key (str):  node key 
        node (:class:`BaseNode`)
        poses (dict):  name/position pairs
        tol (float): tolerence for each poses
        unknown (str, optional): string for unknown position default is ""
        
    Example:
       
    :: 
       
       posname = PosName(node=motor1.stat.pos_actual, poses={'FREE':0.0, ''}, tol=0.01 )
       posname.get()

    """
    class Config(NodeAlias1.Config):
        poses: Dict[str,float] = None
        tol: float = 0.0 
        unknown: str = ""
        
    def fget(self, value: float) -> str:
        c = self.config
        for name, pos in c.poses.items():
            if abs(pos-value)<c.tol:
                return name
        return c.unknown
         
@register    
class Formula(NodeAlias):
    """ Formula AliasNode computed from several nodes 

    Config:
        formula (str) : mathematical formula. By default the variables corresponding to the 
                        entry nodes are 'x' if only one node is provided or x1, x2, x3, etc 
                        Exemple  ' exp(-x/3.) '  or  ' sqrt(x1**2+ x2**2)'
        varnames (str or list): Alternative var names for the formula  
    """
    class Config(NodeAlias.Config):
        formula : str = "-99.99"
        varnames: Optional[Union[List[str],str]] = None  
    
    def __init__(self, *args, **kwargs):                            
        super().__init__(*args, **kwargs)
        nodes = list(self.nodes())

        if isinstance(self.config.varnames, str):
            varnames = [self.config.varnames]
        else:
            varnames = self.config.varnames
        if varnames is  None:
            if len(nodes)==1:
                varnames = ('x',)
            else:
                varnames = tuple( 'x'+str(i+1) for i in range(len(nodes)) )
        elif len(varnames)!=len(nodes):
            raise ValueError( f"Got {len(nodes)} nodes but configured varnames has size {len(self.config.varnames)}")
                    
        self._parser = _eval_parser.parse(self.config.formula)
        self._inputs = {'nan': math.nan, 'pi': math.pi}
        
        self._varnames = varnames
            
                
    def fget(self, *values):   
        v = {k:x for k,x in zip(self._varnames, values)}
        return self._parser.evaluate(v)


@register    
class Formula1(NodeAlias1):
    """ AliasNode1 similar than Formula but for one single input Node 

    Config:
        formula (str): mathematical formula. Default varname is 'x'
                        exemple: '3.4 + x*12.3'
        varname (str): alternative varname for the formulae (default is 'x') 
    """
    class Config(NodeAlias1.Config):
        formula : str = "-99.99"
        varname: str = 'x' 
    
    def __init__(self, *args, **kwargs):                            
        super().__init__(*args, **kwargs)
                
        self._parser = _eval_parser.parse(self.config.formula)
        self._inputs = {'nan': math.nan, 'pi': math.pi}
        
        self._varname = self.config.varname
                            
    def fget(self, value):          
        return self._parser.evaluate({self._varname:value})

@register
class Polynom(NodeAlias1):
    """ NodeAlias1, Apply a polynome into one single node value input

    Config:
        polynom (list) : list of coefficients (weakest first) 
    """
    class Config(NodeAlias1.Config):
        polynom: List[float] = [0.0,1.0]
        
    
    def fget(self, value):
        if not self.config.polynom:
            return 0.0
        x = self.config.polynom[0]
        for i,c in enumerate(self.config.polynom[1:], start=1):
            x += c*value**i
        return x


@register
class NoError(NodeAlias):
    """ NodeAlias, Return True is all nodes return False or 0 or "" else raise ValueError """
    def fget(self, *error_codes):
        for i,err in enumerate(error_codes):
            if err: raise ValueError(f"Node {i} has return error {err}")
        return True


@register
class Statistics(NodeAlias1):
    """ NodeAlias1, compute the statisitc of one single node value 

    It return a data structure with min, max, sum, mean, sum2 (sum square), rms, n (number of points)

    The statistics is changing at every get(). The reset() method is reseting the statistics. 
   
    Example:

    ::

        >>> from pydevmgr_core.nodes import Statistics, Counter
        >>> s = Statistics( node=Counter() )
        >>> s.get()
        statistics.Stat(min=1, max=1, sum=1, mean=1, sum2=1.0, rms=1, n=1)
        >>> s.get()
        Statistics.Stat(min=1, max=2, sum=3, mean=1.5, sum2=5.0, rms=1.5811388300841898, n=2)
        
        
    """
    class Config(NodeAlias1.Config):
        mean: float = 0.0 # expected mean for Variance and rms computation
        
    @dataclass
    class Stat:
        min  : float = -math.inf
        max  : float =  math.inf
        sum  : float =  math.nan 
        mean : float =  math.nan
        sum2 : float =  math.nan
        rms  : float =  math.nan 
        n    : int = 0
      
    def __init__(self, *args,  **kwargs):                            
        super().__init__(*args, **kwargs)
        self._stat = self.Stat()
        self.reset()
    
    @property
    def data(self):
        return self._stat
    
    def reset(self):
        s = self._stat
        s.min = -math.inf
        s.max =  math.inf
        s.sum =  math.nan 
        s.mean = math.nan
        s.sum2 = math.nan
        s.rms =  math.nan 
        s.n = 0
        
    def fget(self, value):
        s= self._stat
        if not s.n:
            s.min = value 
            s.max = value 
            s.sum = value
            s.mean = value 
            s.sum2 = (value - self.config.mean)**2
            s.var = s.sum2
            s.rms = value 
            s.n = 1
            
        else:
            s.sum = s.sum+value
            s.sum2 = s.sum2 + (value - self.config.mean)**2
            s.n = s.n+ 1
            s.var = s.sum2/s.n
            s.min = min(value, s.min)
            s.max = max(value, s.max)                         
            s.mean = s.sum/s.n
            s.rms = math.sqrt(s.var) 
            
        return s



class _Stat(NodeAlias1):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reset()
    

@register
class Sum(_Stat):
    """ NodeAlias1, sum node values 

    reset() method is reseting to zero

    Example:

    ::

        >>> from pydevmgr_core.nodes import Sum, Counter
        >>> s = Sum( node=Counter())
        >>> s.get()
        1.0 
        >>> s.get()
        3.0 
        >>> s.get() 
        6.0 
        >>> s.get()
        10.0
            
    """
        
    def reset(self):
        self._sum = 0.0
        
    def fget(self, value):
        self._sum += value 
        return self._sum    
        
@register
class Mean(_Stat):
    """ NodeAlias1, mean node values 

    reset() method is reseting to zero

    Example:

    ::
    
        >>> from pydevmgr_core.nodes import Mean, Counter
        >>> m = Mean( node=Counter())
        >>> m.get() 
        1.0 
        >>> m.get() 
        1.5
        >>> m.get()
        3.0
        
        
    """
        
    def reset(self):
        self._sum = 0.0
        self._n = 0
    
    def fget(self, value):
        self._sum += value 
        self._n += 1
        return self._sum / self._n

@register
class Min(_Stat):
    """ NodeAlias1, min for on single node input
    
    reset() method is resetting to +inf 

    Example

    :: 

        >>> from pydevmgr_core.nodes import Min, Value
        >>> v = Value(value=2.0)
        
        >>> m = Min(node=v)  
        >>> m.get()
        2.0 
        >>> v.set(10.0); m.get()
        2.0 
        >>> v.set(1.0) ; m.get()
        1.0
    """
           
    def reset(self):
        self._min = math.inf
            
    def fget(self, value):
        if value < self._min:            
            self._min = value
        return self._min

@register
class Max(_Stat):
    """ NodeAlias1,  max for one single node input

    reset() method is resetting to -inf 

    """
                
    def reset(self):
        self._max = -math.inf
            
    def fget(self, value):
        if value > self._max:            
            self._max = value
        return self._max



@register
class Format(NodeAlias):
    """ NodeAlias, format several incoming node values to strings 

    Config:
        format (str): on the form e.g. : "{0:2.3f} {1!r} ..." 
    """
    class Config(NodeAlias.Config):
        format: str = "{0}"
    def fget(self, *values):
        return self.config.format.format(*values)



@register
class Bits(NodeAlias):
    """ from a list of boolean node build an integer number 

    the node alias works in both way, change a number to switch boolean nodes as bits 

    The weakest weight is the first node of the input list

    Example:

    ::

        >>> from pydevmgr_core.nodes import Value, Bits
        >>> b1, b2, b3 = Value(value=True), Value(value=False), Value(value=True)
        >>> b = Bits( nodes=[b1,b2,b3])
        >>> b.get()
        5
        >>> b.set( 2)
        >>> b1.get(), b2.get(), b3.get()
        (False, True, False)
        
    """
    def fget(self, *bits):
        out = 0 
        for bit in reversed(bits):
            out = (out << 1) | bit
        return out
    def fset(self, num ):
        for i,_ in enumerate(self.nodes()):
            yield bool(num & (1<<i))  
        

@register
class MaxOf(NodeAlias):
    fget = staticmethod(max)
        
@register
class MinOf(NodeAlias):
    fget = staticmethod(min)

@register
class MeanOf(NodeAlias):
    @staticmethod
    def fget(*values):
        return sum(values)/float(len(values))


_r2d =  180.0/math.pi 
_d2r =  math.pi / 180.0
@register
class Rad2Degree(NodeAlias1):
    """ tranform a node with radiant to degree 

    The node also transform degree to radiant at ``.set``
    """
    def fget(self, angle: float)-> float :
        return angle * _r2d 
    def fset(self, angle_deg: float)-> float:
        yield angle_deg * _d2r

        
@register
class Degree2Rad(NodeAlias1):
    """ tranform a node with degree to radiant

    The node also transform radiant to degree at ``.set``
    """

    def fget(self, angle_deg: float)-> float:
        return angle_deg * _d2r 
    def fset(self, angle: float)-> float:
        yield angle * _r2d 
    
    
     
