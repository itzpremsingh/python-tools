from re import MULTILINE, findall
from subprocess import run


def commander(command: str) -> tuple[str, int]:
    """Execute command on bash"""
    outcode = run(
        command,
        shell=True,
        capture_output=True,
    )

    returnCode = outcode.returncode

    if returnCode == 0:
        output = outcode.stdout.decode()
        return output, returnCode

    error = outcode.stderr.decode()
    return error, returnCode


command = input("Enter Command:")
pattern = input("Enter Pattern\n")


output, rcode = commander(command)

if rcode == 0:
    for match in findall(pattern, output, MULTILINE):
        print(match)

else:
    print("Error:", output)
