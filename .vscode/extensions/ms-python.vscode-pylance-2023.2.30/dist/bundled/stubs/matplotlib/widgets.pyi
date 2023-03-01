from ast import Str
from tkinter import Image
import numpy as np
from typing import Callable, Literal, Sequence
from ._typing import *
from .text import Text
from .patches import Circle
from .backend_bases import (
    DrawEvent,
    Event,
    FigureCanvasBase,
    KeyEvent,
    MouseButton,
    MouseEvent,
)
from .lines import Line2D
from .figure import Figure
from .axes import Axes
from .artist import Artist

class LockDraw:
    def __init__(self) -> None: ...
    def __call__(self, o: "Lasso") -> None: ...
    def release(self, o: "Lasso") -> None: ...
    def available(self, o: "Lasso") -> bool: ...
    def isowner(self, o: "Lasso") -> bool: ...
    def locked(self) -> bool: ...

class Widget:

    drawon = ...
    eventson = ...

    def set_active(self, active: Widget): ...
    def get_active(self) -> bool: ...
    active = ...
    def ignore(self, event: Event) -> bool: ...

class AxesWidget(Widget):
    def __init__(self, ax: Axes) -> None: ...
    def connect_event(self, event: str, callback: Callable) -> None: ...
    def disconnect_events(self) -> None: ...

class Button(AxesWidget):
    def __init__(
        self,
        ax: Axes,
        label: Str,
        image: Image | ArrayLike = ...,
        color: Color = ...,
        hovercolor: Color = ...,
    ) -> None: ...
    def on_clicked(self, func: Callable) -> int: ...
    def disconnect(self, cid): ...

class SliderBase(AxesWidget):
    def __init__(
        self,
        ax: Axes,
        orientation: Literal["horizontal", "vertical"],
        closedmin: bool,
        closedmax: bool,
        valmin: float,
        valmax: float,
        valfmt: str | None,
        dragging: bool,
        valstep: float | ArrayLike | None,
    ) -> None: ...
    def disconnect(self, cid: int): ...
    def reset(self): ...

class Slider(SliderBase):

    val: float

    def __init__(
        self,
        ax: Axes,
        label: str,
        valmin: float,
        valmax: float,
        valinit: float = ...,
        valfmt: str | None = ...,
        closedmin: bool = True,
        closedmax: bool = True,
        slidermin: Slider | None = None,
        slidermax: Slider | None = None,
        dragging: bool = True,
        valstep: float | ArrayLike | None = None,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        *,
        initcolo: Color = "r",
        track_color: Color = "lightgrey",
        handle_style: dict = ...,
        **kwargs
    ) -> None: ...
    def set_val(self, val: float) -> None: ...
    def on_changed(self, func: Callable) -> int: ...

class RangeSlider(SliderBase):

    val: tuple[float, ...]

    def __init__(
        self,
        ax: Axes,
        label: str,
        valmin: float,
        valmax: float,
        valinit: Sequence[float] | None = None,
        valfmt: str | None = None,
        closedmin: bool = True,
        closedmax: bool = True,
        dragging: bool = True,
        valstep: float | None = None,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        track_color: Color = "lightgrey",
        handle_style: dict = ...,
        **kwargs
    ) -> None: ...
    def set_min(self, min: float): ...
    def set_max(self, max: float): ...
    def set_val(self, val: Sequence[float]): ...
    def on_changed(self, func: Callable) -> int: ...

class CheckButtons(AxesWidget):
    def __init__(
        self, ax: Axes, labels: Sequence[str], actives: Sequence[bool] = ...
    ) -> None: ...
    def set_active(self, index: int): ...
    def get_status(self) -> tuple[bool, ...]: ...
    def on_clicked(self, func: Callable) -> int: ...
    def disconnect(self, cid) -> None: ...

class TextBox(AxesWidget):

    DIST_FROM_LEFT = ...
    def __init__(
        self,
        ax: Axes,
        label: str,
        initial: str = ...,
        color: Color = ...,
        hovercolor: Color = ...,
        label_pad: float = ...,
        textalignment: Literal["left", "center", "right"] = ...,
    ) -> None: ...
    @property
    def text(self) -> str: ...
    def set_val(self, val: str) -> None: ...
    def begin_typing(self, x): ...
    def stop_typing(self) -> None: ...
    def position_cursor(self, x: float): ...
    def on_text_change(self, func: Callable): ...
    def on_submit(self, func: Callable) -> int: ...
    def disconnect(self, cid): ...

class RadioButtons(AxesWidget):

    ax: Axes
    activecolor: Color
    labels: list[Text]
    circles: list[Circle]
    value_selected: str

    def __init__(
        self,
        ax: Axes,
        labels: Sequence[Text],
        active: int = ...,
        activecolor: Color = ...,
    ) -> None: ...
    def set_active(self, index: int): ...
    def on_clicked(self, func: Callable) -> int: ...
    def disconnect(self, cid): ...

class SubplotTool(Widget):
    def __init__(self, targetfig: Figure, toolfig: Figure) -> None: ...

class Cursor(AxesWidget):
    def __init__(
        self,
        ax: Axes,
        horizOn: bool = True,
        vertOn: bool = True,
        useblit: bool = False,
        **lineprops
    ) -> None: ...
    def clear(self, event: DrawEvent) -> None: ...
    def onmove(self, event: Event): ...

class MultiCursor(Widget):
    def __init__(
        self,
        canvas: FigureCanvasBase,
        axes: Sequence[Axes],
        useblit: bool = True,
        horizOn: bool = False,
        vertOn: bool = True,
        **lineprops
    ) -> None: ...
    def connect(self) -> None: ...
    def disconnect(self): ...
    def clear(self, event: DrawEvent) -> None: ...
    def onmove(self, event: Event): ...

class _SelectorWidget(AxesWidget):
    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        useblit: bool = ...,
        button=...,
        state_modifier_keys=...,
        use_data_coordinates=...,
    ) -> None: ...

    eventpress = ...
    eventrelease = ...
    state = ...
    state_modifier_keys = ...
    def set_active(self, active): ...
    def update_background(self, event: DrawEvent) -> None: ...
    def connect_default_events(self) -> None: ...
    def ignore(self, event: Event): ...
    def update(self) -> bool: ...
    def press(self, event: Event): ...
    def release(self, event: Event): ...
    def onmove(self, event: Event): ...
    def on_scroll(self, event: Event): ...
    def on_key_press(self, event: KeyEvent) -> None: ...
    def on_key_release(self, event: Event): ...
    def set_visible(self, visible: bool) -> None: ...
    def clear(self): ...
    @property
    def artists(
        self,
    ) -> tuple[Artist, ...]: ...
    def set_props(self, **props): ...
    def set_handle_props(self, **handle_props): ...
    def add_state(self, state: str): ...
    def remove_state(self, state: str): ...

class SpanSelector(_SelectorWidget):
    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        direction: Literal["horizontal", "vertical"],
        minspan: float = 0,
        useblit: bool = False,
        props: dict = ...,
        onmove_callback: Callable = ...,
        interactive: bool = False,
        button: MouseButton | Sequence[MouseButton] = ...,
        handle_props: dict = ...,
        grab_range: float = 10,
        state_modifier_keys: dict = ...,
        drag_from_anywhere: bool = False,
        ignore_event_outside: bool = False,
        snap_values: ArrayLike = ...,
    ) -> None: ...

    rect = ...
    rectprops = ...
    active_handle = ...
    pressv = ...
    span_stays = ...
    prev = ...
    def new_axes(self, ax: Axes): ...
    def connect_default_events(self) -> None: ...
    @property
    def direction(self): ...
    @direction.setter
    def direction(self, direction): ...
    @property
    def extents(self): ...
    @extents.setter
    def extents(self, extents): ...

class ToolLineHandles:
    def __init__(
        self,
        ax: Axes,
        positions: ArrayLike,
        direction: Literal["horizontal", "vertical"],
        line_props: dict = ...,
        useblit: bool = True,
    ) -> None: ...
    @property
    def artists(self) -> tuple[Line2D, Line2D]: ...
    @property
    def positions(self): ...
    @property
    def direction(self) -> str: ...
    def set_data(self, positions: tuple): ...
    def set_visible(self, value): ...
    def set_animated(self, value): ...
    def remove(self): ...
    def closest(self, x: float, y: float) -> tuple[int, float]: ...

class ToolHandles:
    def __init__(
        self,
        ax: Axes,
        x: ArrayLike,
        y: ArrayLike,
        marker: str = "o",
        marker_props: dict = ...,
        useblit: bool = True,
    ) -> None: ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def artists(self) -> tuple[Line2D, ...]: ...
    def set_data(self, pts: Sequence[float], y: Sequence[float] = ...) -> None: ...
    def set_visible(self, val): ...
    def set_animated(self, val): ...
    def closest(self, x: float, y: float) -> tuple[int, float]: ...

class RectangleSelector(_SelectorWidget):
    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        drawtype=...,
        minspanx=...,
        minspany=...,
        useblit=...,
        lineprops=...,
        props=...,
        spancoords=...,
        button=...,
        grab_range=...,
        handle_props=...,
        interactive=...,
        state_modifier_keys=...,
        drag_from_anywhere=...,
        ignore_event_outside=...,
        use_data_coordinates=...,
    ) -> None: ...

    to_draw = ...
    drawtype = ...
    active_handle = ...
    interactive = ...
    maxdist = ...
    @property
    def corners(self): ...
    @property
    def edge_centers(self): ...
    @property
    def center(self) -> tuple[float, float]: ...
    @property
    def extents(self): ...
    @extents.setter
    def extents(self, extents): ...
    @property
    def rotation(self) -> float: ...
    @rotation.setter
    def rotation(self, value: float): ...

    draw_shape = ...
    @property
    def geometry(self) -> np.ndarray: ...

class EllipseSelector(RectangleSelector):

    draw_shape = ...

class LassoSelector(_SelectorWidget):
    def __init__(
        self,
        ax: Axes,
        onselect: Callable = ...,
        useblit: bool = True,
        props: dict = ...,
        button: MouseButton | Sequence[MouseButton] = ...,
    ) -> None: ...
    def onpress(self, event): ...
    def onrelease(self, event): ...

class PolygonSelector(_SelectorWidget):
    def __init__(
        self,
        ax: Axes,
        onselect: Callable,
        useblit: bool = True,
        props: dict = ...,
        handle_props: dict = ...,
        grab_range: float = 10,
        *,
        draw_bounding_box: bool = ...,
        box_handle_props: dict = ...,
        box_props: dict = ...
    ) -> None: ...

    line = ...
    vertex_select_radius = ...
    def onmove(self, event: Event): ...
    @property
    def verts(self): ...
    @verts.setter
    def verts(self, xys): ...

class Lasso(AxesWidget):
    def __init__(
        self,
        ax: Axes,
        xy: Sequence[float],
        callback: Callable = ...,
        useblit: bool = True,
    ) -> None: ...
    def onrelease(self, event: MouseEvent) -> None: ...
    def onmove(self, event: MouseEvent) -> None: ...
