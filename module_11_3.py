import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)

    def methods():
        return methods.__dir__()

    module = obj.__class__.__module__
    function = inspect.getmembers(obj, inspect.isfunction)

    dictionary = {'type': obj_type, 'attributes': attributes, 'methods': methods(), 'module': module}
    return dictionary


number_info = introspection_info(42)
print(number_info)