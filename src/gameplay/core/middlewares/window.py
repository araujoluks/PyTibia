import re
import win32gui
from ...typings import Context


def setTibiaWindowMiddleware(context: Context):
    if context['window'] is None:
        windowsList: list = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windowsList)
        windowsNames = list(map(lambda hwnd: win32gui.GetWindowText(hwnd), windowsList))
        regex = re.compile(r'Tibia - .*')
        windowsFilter = list(filter(lambda windowName: regex.match(windowName), windowsNames))
        if len(windowsFilter) > 0:
            context['window'] = windowsFilter[0]
    return context