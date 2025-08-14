from inspect import getfullargspec, isclass
from io import StringIO
from sys import argv
from urllib.request import Request, urlopen


def getFuncDetail(__func__):
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
            defaultDict.setdefault(key, value)

        allData["default"] = defaultDict

    varargs = fullargs.varargs
    varkw = fullargs.varkw

    annotation = fullargs.annotations

    if varargs:
        allData["varargs"] = varargs
    if varkw:
        allData["varkw"] = varkw
    allData["annotation"] = annotation

    return allData


def buildDoc(__func__: object, read: bool = False) -> str:
    __doc__ = StringIO()
    _default = False
    write = __doc__.write
    extra = ""
    index = 1

    detail = getFuncDetail(__func__)
    if read:
        write("Function name: ")

    write(detail["name"])

    if not read:
        write(": __description__")

    write("\n")

    write("\nArgument:\n")
    for args in detail["args"]:
        __type = detail["annotation"].get(args, "Unknown")

        if isclass(__type):
            __type = __type.__name__

        if "default" in detail:
            default = detail["default"].get(args, "<unknown>")
            if default != "<unknown>":
                _default = True
                extra = f" Default is {default!r}."

        if _default:
            __type = f"{__type}, optional"

        write(
            f'   {args} ({__type}): {" __summary__." if not read else f"parameter {index}."}{extra}\n'
        )

        index += 1

    returnType = detail["annotation"].get("return", "<unknown>")

    if returnType != "<unknown>":
        if isclass(returnType):
            returnType = returnType.__name__

        write(f'\nReturns: {returnType if read else ""}')

        if not read:
            write(f"\n   {returnType}: __summary__.")

    return __doc__.getvalue()


def args(file: str) -> str | None:
    if argv[1::]:
        return argv[1]

    else:
        print(f'usage: python {file.split("/")[-1]} __argument__')


def fetch(url: str, headers={}) -> str:
    # headers.setdefault(
    #    "User-Agent",
    #   "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    # )
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read().decode()
