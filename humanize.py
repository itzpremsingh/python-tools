from typing import Optional


def time_format(sec, _format=0, _sort=0, _round=2):
    hours = 0
    minute = 0

    if sec > 3599:
        hours += sec // 3600
        sec = sec % 3600

    if sec > 59:
        minute += sec // 60
        sec = sec % 60

    sec = round(sec, _round)

    if _sort:
        hours = str(hours) + " h "
        minute = str(minute) + " m "
        sec = str(sec) + " s"

    if _format:
        if sec and minute == "0 m ":
            return sec

        elif minute and hours == "0 h ":
            return minute, sec

    return hours, minute, sec


def size_format(byte, _round=1):
    kb = 1024
    mb = 1048576
    gb = 1073741824
    tb = 1099511627776
    size: Optional[float] = None
    byte = int(byte)
    if byte < kb:
        return byte, "B"

    elif kb <= byte < mb:
        size, unit = (byte / kb), "KB"

    elif mb <= byte < gb:
        size, unit = (byte / mb), "MB"

    elif gb <= byte < tb:
        size, unit = (byte / gb), "GB"

    elif tb <= byte:
        size, unit = (byte / tb), "TB"

    _size = round(float(size), _round)

    return _size, unit


def direction(windDir: str) -> str:
    windDirLen = len(windDir)
    if windDirLen > 3 or not windDir:
        return "Unknown"

    windDir = windDir.lower()
    newWindDir = ""

    allDir: dict = {
        "e": "east",
        "w": "west",
        "n": "north",
        "s": "south",
    }

    first = True

    for oneWindDir in windDir:
        if oneWindDir in allDir:
            extractedDir = allDir[oneWindDir]

            if first:
                extractedDir = extractedDir.title()
                first = False

            newWindDir += extractedDir

            if windDirLen == 3:
                newWindDir += "-"
                windDirLen = None

        else:
            return "Unknown"

    return newWindDir
