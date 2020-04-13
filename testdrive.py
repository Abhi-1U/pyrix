import sys
import Matrix as M


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


d = [[2, 3, 9], [2, 11, 5]]
st = [[2, 4, 2], [2, 1, 1], [2, 1, 4]]
nrow = 2
ncol = 3
z = M.Matrix(nrow=nrow, ncol=ncol, data=d)
p = M.Matrix(nrow=nrow, ncol=ncol, data=d)
r = M.Matrix(nrow=3, ncol=3, data=st)
try:
    print(r)
    f = r.determinantValue()
    print(f)
except M.incompaitableTypeException as e:
    print(e)
except M.nonInvertibleException as e:
    print(e)
