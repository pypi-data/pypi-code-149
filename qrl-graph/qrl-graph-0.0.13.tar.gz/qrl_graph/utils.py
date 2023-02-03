import numpy as np
from scipy import optimize
import random
import wandb
import torch
import numpy as np
# the utils function 


##### utils function to construct the graph #####
# graph construction (glued tree)
def contruct_tree_graph(h):
    """contruct the graph for the balanced binary tree with height of h.

    Args:
        h (int): the height of the tree
        
    Returns:
        g (np.array): the graph of the tree
        list_child (list): the index of last layers of the tree
    """
    g = np.zeros((2**h-1, 2**h-1))
    index = 0
    list_parent = []
    list_parent.append(index)
    for _ in range(h-1):
        list_child = []
        for parent in list_parent:
            g[parent, index+1] = 1
            g[parent, index+2] = 1
            list_child.append(index+1)
            list_child.append(index+2)
            index += 2
        list_parent = list_child
    
    g = g + g.T
    return g, list_child

def generate_two_cycles(n):
    """construct the two cycles between the two list of length n.
    
    Args:
        n (int): the length of the two cycles.
        
    Returns:
        list_first_perm (list): the permutation of the first cycles.
        list_second_perm (list): the permutation of the second cycles.
    """

    list_first_perm = list(np.random.permutation(n))
    list_second_perm = []

    list_available = list(range(n))


    # the last element of the first perm must be in the entries before
    index_for_last = random.choice(range(n-1))
    list_available.remove(list_first_perm[-1])

    for i in range(n):
        if i == index_for_last:
            list_second_perm.append(list_first_perm[-1])
        else: 
            # one restriction (can not repeat the first cycle)
            list_available_i = [a for a in list_available if a != list_first_perm[i]]
            index = random.choice(list_available_i)
            list_available.remove(index)
            list_second_perm.append(index)

    return list_first_perm, list_second_perm

def construct_glued_tree_graph(h):
    """contruct the graph for the balanced binary tree with height of h.

    Args:
        h (int): the height of the tree
    """
    n = 2**h-1

    # number of layer double! 
    g = np.zeros((2*n, 2*n))
    g_tree, list_nodes_left = contruct_tree_graph(h)
    
    # reflection (last layer)
    list_nodes_right = [ 2*n-1-i for i in list_nodes_left]
    
    for i in range(n):
        for j in range(n):
            g[i, j] = g_tree[i, j]
            # reflection (binary tree)
            g[2*n-1-i, 2*n-1-j] = g_tree[i, j]
        
    # build the random connection between the two last nodes of the trees. 
    list_perms = generate_two_cycles(len(list_nodes_left))
    
    for perm in list_perms:
        for i, j in enumerate(perm):
            g[list_nodes_left[i], list_nodes_right[j]] = 1
            g[list_nodes_right[j], list_nodes_left[i]] = 1
    
    return g

def construct_linear_graph(n):
    """Construct the linear graph with n nodes.
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.zeros((n, n))
    for i in range(n-1):
        g[i,i+1] = 1
    g = g + g.T
    return g

def construct_actual_fully_connected_graph(n):
    """Construct the actual fully connected graph with n nodes.
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.ones((n, n))
    for i in range(n):
        g[i,i] = 0
    return g

def construct_fully_connected_graph(n):
    """Construct the fully connected graph with n nodes.
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.ones((n, n))
    for i in range(n):
        g[i,i] = 0
    g[0, n-1] = 0
    g[n-1, 0] = 0
    return g

def construct_fully_connected_graph_with_one_out(n):
    """Construct the fully connected graph with n nodes and one edge out to end node. 
    
    Args:
        n (int): the number of nodes.
    
    Returns:
        g (np.array): the graph of the linear graph.
    """
    g = np.ones((n, n))
    for i in range(n):
        g[i,i] = 0
    for i in range(n):
        if i == 1: 
            continue
        else: 
            g[i, n-1] = 0
            g[n-1, i] = 0
    return g

##### utils function for the general graph #####
# general graph utils
def is_graph_connected(g):
    """Here g is an array of length (n-1)n/2, where n is the number of vertices.
    
    Try to find a path from the beginning point to the end point.
    
    Args: g (np.array): an array of length (n-1)n/2, where n is the number of vertices.
    """
    n = int(np.sqrt(2*g.shape[0]+0.25)+0.5)
    g_list_index = []
    for i in range(n-1):
        g0, g = g[:n-1-i], g[n-1-i:]
        index_set = np.where(g0 == 1)[0] + i + 1
        g_list_index.append(index_set)
    
    visited = []
    def dfs(i):
        if i == n-1:
            return True
        for j in g_list_index[i]:
            if j not in visited:
                visited.append(j)
                if dfs(j):
                    return True
                visited.pop()
        return False
    return dfs(0)

def is_start_end_connected(g):
    """Detect whether the start and end vertices are connected.
    
    Args: g (np.array): an array of length (n-1)n/2, where n is the number of vertices.
    """
    n = int(np.sqrt(2*g.shape[0]+0.25)+0.5)
    return g[n-2] == 1

def is_graph_valid(g):
    return is_graph_connected(g) and not is_start_end_connected(g)

def get_index(i, j, n):
    """i is the row index, j is the column index, n is the number of vertices."""
    assert j > i
    return int( (2 * n - 1 - i) * i // 2+ j - i -1 )

def g2adjacent_mat(g):
    """convert from the graph to the adjacent matrix.
    
    The graph is represented by an array of length (n-1)n/2, where n is the number of vertices.
    """
    if isinstance(g, list) or isinstance(g, tuple):
        g = np.array(g)
    n = int(np.sqrt(2*g.shape[0]+0.25)+0.5)
    graph = np.zeros((n, n), dtype=int)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            graph[i, j] = graph[j, i] = g[count]
            count += 1
    assert count == g.shape[0]
    return graph

def adjacent_mat2g(graph):
    """Convert from the adjacent matrix to the graph.
    
    The graph is represented by an array of length (n-1)n/2, where n is the number of vertices.
    """
    n = graph.shape[0]
    g = np.zeros(n * (n-1) // 2, dtype=int)
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            g[count] = graph[i, j]
            count += 1
    assert count == g.shape[0]
    return g


def sample2graph(sample):
    """Convert the sample to the graph.
    
    Note:
        The sample is a string of 0 and 1. The meaning is the choice of the edge 
        for the graph. For example, the sample '1100100'. 
    
    Args:
        sample: str
            The sample of the graph.
    
    Returns:
        g: np.array
            The graph.
    """
    sample_len = len(sample)
    n = 1/2 + np.sqrt(1/4 + 2 * sample_len)
    n = int(n)
    g = np.zeros((n, n))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            g[i, j] = sample[count]
            g[j, i] = g[i, j]
            count += 1
    return g

def str2nparray(string):
    """Convert the string to the np.array.
    
    Args:
        string: str
            The string of the array.
    
    Returns:
        np.array
            The np.array.
    """
    return np.array([int(x) for x in string])

def np2str(array):
    """convert the numpy array into a string. 
    
    Parameters:
    -----------
    array: numpy array
        The numpy array to be converted.
    """
    return [str(i) for i in array]

### utils for the special optimization ### 
def _burnin_modify(data, t_list):
    """modify the data to remove the burnin time
    
    1. remove the negative values
    2. start after the peak
    """
    last_negative = -1
    for i, value in enumerate(data): 
        if value < 0: 
            last_negative = i
    data = data[last_negative + 1: ]
    t_list = t_list[last_negative + 1: ]        
    max_index = np.argmax(data)
    return data[max_index:], t_list[max_index:]

def _postive_filter(data, t_list):
    """modify the data to remove the negative values

    1. remove the negative values
    """
    new_data_list = []
    new_t_list = []
    for value, t in zip(data, t_list): 
        if value > 0:
            new_data_list.append(value)
            new_t_list.append(t)
    return new_data_list, new_t_list

# numbers 
def array2binary(array):
    """Convert the array to binary.
    
    Args:
        array: the array to be converted.
    
    Returns:
        int: the binary representation of the array.
    """
    return int(''.join(map(lambda x: str(int(x)), array)), 2)

### logger
def setup_wandb(config, project_name):
    wandb.init(
            reinit=True,
            config=config,
            project=project_name,
            settings=wandb.Settings(
                start_method="thread",
                _disable_stats=True,
            ),
        )


# optimization (convex)
def three_pts_mod(x, f, delta_x):
    # note that here I have consider the case where the function value is equal
    y1, y2, y3 = f(x - delta_x), f(x), f(x + delta_x)
    if y1 > y2 and y2 > y3: return 'decreasing'
    elif y1 > y2 and y2 < y3: return 'valley'
    elif y1 < y2 and y2 < y3: return 'increasing'
    else:
        assert False

def find_minima_cvx(f, x=1, delta_x=0.1):
    """Find the minima of a convex function"""
    # initial starting points
    # f is the function
    # x is the initial guess
    # delta_x is the step size
    
    # decide the bounds for the optimization
    # two cases: 
    # if x is valley, then the bounds are x - delta_x, x + delta_x
    # otherwise x1, x2, such that x1 is decreasing and x2 is increasing.     
    if three_pts_mod(x, f, delta_x) == 'valley':
        x1 = x - delta_x
        x2 = x + delta_x
    elif three_pts_mod(x, f, delta_x) == 'decreasing':
        x1 = x
        x *= 2
        while three_pts_mod(x, f, delta_x) == 'decreasing':
            x1 = x
            x *= 2
        if three_pts_mod(x, f, delta_x) == 'increasing':
            x2 = x
        elif three_pts_mod(x, f, delta_x) == 'valley':
            x1 = x - delta_x
            x2 = x + delta_x
    elif three_pts_mod(x, f, delta_x) == 'increasing':
        x2 = x
        x /= 2
        delta_x /= 2
        while three_pts_mod(x, f, delta_x) == 'increasing':
            x2 = x
            x /= 2
            delta_x /= 2
        if three_pts_mod(x, f, delta_x) == 'decreasing':
            x1 = x
        elif three_pts_mod(x, f, delta_x) == 'valley':
            x1 = x - delta_x
            x2 = x + delta_x
    else: 
        assert False
    
    res = optimize.minimize_scalar(f, bounds=(x1, x2), method='bounded')
    assert res.success
    return res



# NOTE: this seems to be not working 
# fails to find the global minima 
# ic| self._get_quantum_cost(res.x): 9.578641681287527
# self._get_quantum_cost(t_range[index]): 5.5721808066342415
# res_fun_list: [1.1418684264542784, 1.141863969277414, 7.156687968031823, 1.1418724075585491]
def find_minima_cvx_v2(f):
    """Find the minima of a convex function
    
    The difference between this function and the previous one is that this function does not require that 
    the function is convex! it can have multuple minima and it will find the first minima. 
    """
    # initial starting points
    # f is the function
    # x is the initial guess
    # delta_x is the step size
    
    # hyper parameter
    delta_x = 1e-4
    num_trials = 20
    eps = 1e-3
    
    x1 = 0
    # this is hard code here
    x2 = 10
    
    
    res_x = None
    res_fun = None
    
    res_fun_list = []
    res_list = []
    res_x_list = []
    for i in range(num_trials):
        res = optimize.minimize_scalar(f, bounds=(x1, x2), method='bounded')
        res_fun_list.append(res.fun)
        res_list.append(res)
        res_x_list.append(res.x)
        assert res.success
        x2 = res.x
        if res_x is None:
            res_x = res.x
            res_fun = res.fun
        else:
            # relative function error
            if abs(res_fun - res.fun ) / res.fun < eps: 
                break
            res_x = res.x
            res_fun = res.fun
            
    x2 = 10
    
    res_fun_list_new = res_fun_list.copy()
    res_list_new = res_list.copy()
    res_x_list_new = res_x_list.copy()
        
    for x1 in res_x_list:    
        res = optimize.minimize_scalar(f, bounds=(min(x1 + 0.1, x2), x2+0.01), method='bounded')
        res_fun_list_new.append(res.fun)
        res_list_new.append(res)
        res_x_list_new.append(res.x)
        x2 = x1
            
    index = np.argmin(res_fun_list_new)
    res = res_list_new[index]
    assert three_pts_mod(res.x, f, delta_x) == 'valley'
    return res, res_x_list_new


def find_minima_cvx_refine(f, x, delta_x):
    # refine the minima (local it is a convex function)
    res = optimize.minimize_scalar(f, bounds=(x - delta_x, x + delta_x), method='bounded')
    return res

#####################################
# utils for the graph neural network
#####################################

# batched outer product

def batch_outer(tensor_a, tensor_b):
    """compute outer product of two tensors
    
    Args:
        tensor_a: [batch_size, dim_a]
        tensor_b: [batch_size, dim_b]
    
    Returns:
        outer product: [batch_size, dim_a, dim_b]
    """
    tensor_out = torch.bmm(tensor_a.unsqueeze(2), tensor_b.unsqueeze(1))
    return tensor_out

def get_masked_tensor(prob_matrix, masks): 
    """sample from the matrix (according to the matrix when sampling)
    
    Args:
        prob_matrix: [batch_size, n_node, n_node]


        masks: [batch_size, 2]
            along the batch size dimension, the first index is for the
            index i; and the second index is for the index j.
    
    Returns:
        masked tensor: [batch_size, n_node * (n_node - 1) // 2]
    """
    n_node = prob_matrix.shape[-1]
    B = prob_matrix.shape[0]

    # get the upper triangluar index
    triu_index = torch.triu( torch.ones(n_node, n_node) , 1) == 1

    # scale the prob matrix
    prob_matrix = torch.tanh(prob_matrix) * 10 
    
    
    # the masks only have the masks for each batch
    for mask in masks: 
        prob_matrix[[i for i in range(B)], mask[:, 0], mask[:, 1]] = - np.inf

    # get the vectors for the upper triangle
    # index for the batch version tensor!
    return prob_matrix[:, triu_index]
    
    # probably after that, the prob needs to be normalized 
    
def get_masked_tensor_with_p0(prob_matrix, masks, p0): 
    """sample from the matrix (according to the matrix when sampling)
    
    Args:
        prob_matrix: [batch_size, n_node, n_node]


        masks: [batch_size, 2]
            along the batch size dimension, the first index is for the
            index i; and the second index is for the index j.
            

    
    Returns:
        masked tensor: [batch_size, n_node * (n_node - 1) // 2]
    """
    n_node = prob_matrix.shape[-1]
    B = prob_matrix.shape[0]

    # get the upper triangluar index
    triu_index = torch.triu( torch.ones(n_node, n_node) , 1) == 1


    # the masks only have the masks for each batch
    prob_matrix[[i for i in range(B)], masks[:, 0], masks[:, 1]] = - np.inf


    # get the vectors for the upper triangle
    # index for the batch version tensor!

    p02 = p0 * p0

    return torch.cat([p02, prob_matrix[:, triu_index]], axis=1)
    # probably after that, the prob needs to be normalized 
    
    


# utils function 
# (change the tensor index to the matrix index)  
def tensor_index_2_mat_index(tensor_index, n_node):
    """convert the tensor index to the matrix index
    
    Args:
        tensor_index: [batch_size, 1], where the last index ranges [0, n_node * (n_node - 1) // 2)
        
    Returns:
        matrix index: [batch_size, 2]
    """
    
    tensor2mat_map = dict()
    
    count = 0
    for i in range(n_node):
        for j in range(i + 1, n_node):
            tensor2mat_map[count] = (i, j)
            count += 1
    
    return torch.tensor([tensor2mat_map[i.item()] for i in tensor_index], dtype=torch.long)


def get_one_hot_edge(masks, n_node):
    """"get the one hot edge representation from the 
    edge index representation
    
    Args:
        masks: [batch_size, 2]
        n_node: int
    
    Returns:
        one hot edge: [batch_size, n_node]
    """
    out = torch.zeros(masks.shape[0], n_node)
    
    # one hot encoding of the edge
    for tensor, (i, j) in zip(out, masks):
        tensor[i.item()] = 1
        tensor[j.item()] = 1
    
    return out


def mat2str(mat):
    """convert the matrix to the string representation
    
    Args:
        mat: [n_node, n_node]
    
    Returns:
        string representation: str
    """
    
    n_node = mat.shape[-1]

    # get the upper triangluar index
    triu_index = torch.triu( torch.ones(n_node, n_node) , 1) == 1

    # convert the matrix into tensor representation
    mat_tensor = mat[:, triu_index]
    
    # convert the tensor into string representation
    return [''.join([str(int(i.item())) for i in mt]) for mt in mat_tensor]
    
    
    