from enum import Enum


class WidgetType(str, Enum):
    TEXT = "text"
    BUTTON = "button"
    IMAGE = "image"
    ICON = "icon"
    INPUT = "input"
    SWITCH = "switch"
    SLIDER = "slider"
    GAUGE = "gauge"
    INDICATOR = "indicator"
    CHART = "chart"
    TIMER = "timer"
    VIDEO = "video"
    CONTAINER = "container"
    CUSTOM = "custom"


class LayoutType(str, Enum):
    FREE = "free"
    ROW = "row"
    COLUMN = "column"
    GRID = "grid"
    STACK = "stack"


class ScreenType(str, Enum):
    STANDARD = "standard"
    DASHBOARD = "dashboard"
    CONTROL = "control"
    MONITOR = "monitor"
    FORM = "form"
    KIOSK = "kiosk"
    DIALOG = "dialog"


class ActionType(str, Enum):
    NONE = "none"
    NAVIGATE = "navigate"
    COMMAND = "command"
    AUTOMATION = "automation"
    SET_VALUE = "set_value"
    OPEN_DIALOG = "open_dialog"
    CLOSE_DIALOG = "close_dialog"
