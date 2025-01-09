class AsyncRegistryPrinter:
    def __init__(self, val):
        self.val = val

    def to_string (self):
        # return "bla"
        registries = vector_to_list(self.val['registries'])[0]
        return self.val
        # if (self.val == True):
        #     return "ja"
        # else:
        #     return "nein"

def lookup_type (val):
    if str(val.type) == 'arangodb::async_registry::Registry':
        return AsyncRegistryPrinter(val)
    return None

def vector_to_list(std_vector):
    out_list = []
    value_reference = std_vector['_M_impl']['_M_start']
    while value_reference != std_vector['_M_impl']['_M_finish']:
        out_list.append(value_reference.dereference())
        value_reference += 1

    return out_list

gdb.pretty_printers.append (lookup_type)
