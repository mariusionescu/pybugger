from pybugger import debug

global_var = 'global_value'

a = 1

def ts():
    local_var = 'local_value'
    debug()
    print(1)
    return 2

a = ts()

debug()

print(a)


