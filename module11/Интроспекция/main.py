import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    module = inspect.getmodule(obj)
    if module is None:
        module_name = '__main__'
    else:
        module_name = module.__name__

    other_properties = {}
    if hasattr(obj, '__doc__'):
        other_properties['doc'] = obj.__doc__
    if hasattr(obj, '__class__'):
        other_properties['class'] = obj.__class__.__name__

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name,
        'properties': other_properties
    }

    return info



def main():
    number_info = introspection_info(42)
    print(number_info)

    class_example = introspection_info(int)
    print(class_example)

    custom_class = type('CustomClass', (), {'attr': 'value', 'method': lambda self: 'Hello'})
    custom_obj = custom_class()
    print(introspection_info(custom_obj))
    


if __name__ == "__main__":
    main()