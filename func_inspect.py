from inspect import getfullargspec

def inspectFunction(__func__):
    """
    Extract details about a function.

    Returns a dict with:
      - name: function name
      - args: list of arguments
      - default: dict of default arguments (if any)
      - varargs: variable arguments (*args)
      - varkw: keyword arguments (**kwargs)
      - annotation: type annotations
    """
    allData: dict = {}
    allData["name"] = __func__.__name__

    fullargs = getfullargspec(__func__)

    argument = fullargs.args
    allData["args"] = argument

    defaultValue = fullargs.defaults
    if defaultValue:
        defaultLen = len(defaultValue)
        defaultArgs = fullargs.args[::-1][:defaultLen][::-1]
        defaultDict = {}

        for key, value in zip(defaultArgs, defaultValue):
            defaultDict[key] = value

        allData["default"] = defaultDict

    if fullargs.varargs:
        allData["varargs"] = fullargs.varargs
    if fullargs.varkw:
        allData["varkw"] = fullargs.varkw

    allData["annotation"] = fullargs.annotations
    return allData

if __name__ == "__main__":
    def test(arg1: int, arg2: str = "Arg2") -> str:
        return arg2 * arg1

    print(inspectFunction(test))
