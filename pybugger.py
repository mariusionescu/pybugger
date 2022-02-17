import inspect


def is_printable(obj):
    return type(obj) in (int, str, list, tuple, set, dict)

def readlines(f):
    with open(f) as f_obj:
        return [l.strip() for l in f_obj.readlines()]

def get_prev(frame):
    frame_info = inspect.getframeinfo(frame)
    lines = readlines(frame_info.filename)
    l = ''
    i = 2
    while not l and lines:
        l = lines[frame_info.lineno - i]
        i += 1
    return l

def debug(message=None):
    message = message or ''
    stack = inspect.stack()
    frame_data = stack[1]
    frame = frame_data[0]

    prev = get_prev(frame)

    print("\n[PYBUGGER] ********************************************************************************")
    print("[PYBUGGER]     line|  {}".format(prev))
    for l_n, l_v in frame.f_locals.items():
        if not l_n.startswith('_') and is_printable(l_v):
            print("[PYBUGGER]    local|  {}: {}".format(l_n, l_v))
    for g_n, g_v in frame.f_globals.items():
        if not g_n.startswith('_') and is_printable(g_v):
            print("[PYBUGGER]   global|  {}: {}".format(g_n, g_v))
    print("[PYBUGGER] ********************************************************************************\n")

