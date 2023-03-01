import sys
from typing import Any, ClassVar
from typing_extensions import Literal, final

# _tkinter is meant to be only used internally by tkinter, but some tkinter
# functions e.g. return _tkinter.Tcl_Obj objects. Tcl_Obj represents a Tcl
# object that hasn't been converted to a string.
#
# There are not many ways to get Tcl_Objs from tkinter, and I'm not sure if the
# only existing ways are supposed to return Tcl_Objs as opposed to returning
# strings. Here's one of these things that return Tcl_Objs:
#
#    >>> import tkinter
#    >>> text = tkinter.Text()
#    >>> text.tag_add('foo', '1.0', 'end')
#    >>> text.tag_ranges('foo')
#    (<textindex object: '1.0'>, <textindex object: '2.0'>)
@final
class Tcl_Obj:
    @property
    def string(self) -> str: ...
    @property
    def typename(self) -> str: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __eq__(self, __other): ...
    def __ge__(self, __other): ...
    def __gt__(self, __other): ...
    def __le__(self, __other): ...
    def __lt__(self, __other): ...
    def __ne__(self, __other): ...

class TclError(Exception): ...

# This class allows running Tcl code. Tkinter uses it internally a lot, and
# it's often handy to drop a piece of Tcl code into a tkinter program. Example:
#
#    >>> import tkinter, _tkinter
#    >>> tkapp = tkinter.Tk().tk
#    >>> isinstance(tkapp, _tkinter.TkappType)
#    True
#    >>> tkapp.call('set', 'foo', (1,2,3))
#    (1, 2, 3)
#    >>> tkapp.eval('return $foo')
#    '1 2 3'
#    >>>
#
# call args can be pretty much anything. Also, call(some_tuple) is same as call(*some_tuple).
#
# eval always returns str because _tkinter_tkapp_eval_impl in _tkinter.c calls
# Tkapp_UnicodeResult, and it returns a string when it succeeds.
@final
class TkappType:
    # Please keep in sync with tkinter.Tk
    def adderrorinfo(self, __msg): ...
    def call(self, __command: Any, *args: Any) -> Any: ...
    def createcommand(self, __name, __func): ...
    if sys.platform != "win32":
        def createfilehandler(self, __file, __mask, __func): ...
        def deletefilehandler(self, __file): ...

    def createtimerhandler(self, __milliseconds, __func): ...
    def deletecommand(self, __name): ...
    def dooneevent(self, __flags: int = 0): ...
    def eval(self, __script: str) -> str: ...
    def evalfile(self, __fileName): ...
    def exprboolean(self, __s): ...
    def exprdouble(self, __s): ...
    def exprlong(self, __s): ...
    def exprstring(self, __s): ...
    def getboolean(self, __arg): ...
    def getdouble(self, __arg): ...
    def getint(self, __arg): ...
    def getvar(self, *args, **kwargs): ...
    def globalgetvar(self, *args, **kwargs): ...
    def globalsetvar(self, *args, **kwargs): ...
    def globalunsetvar(self, *args, **kwargs): ...
    def interpaddr(self): ...
    def loadtk(self) -> None: ...
    def mainloop(self, __threshold: int = 0): ...
    def quit(self): ...
    def record(self, __script): ...
    def setvar(self, *ags, **kwargs): ...
    if sys.version_info < (3, 11):
        def split(self, __arg): ...

    def splitlist(self, __arg): ...
    def unsetvar(self, *args, **kwargs): ...
    def wantobjects(self, *args, **kwargs): ...
    def willdispatch(self): ...

# These should be kept in sync with tkinter.tix constants, except ALL_EVENTS which doesn't match TCL_ALL_EVENTS
ALL_EVENTS: Literal[-3]
FILE_EVENTS: Literal[8]
IDLE_EVENTS: Literal[32]
TIMER_EVENTS: Literal[16]
WINDOW_EVENTS: Literal[4]

DONT_WAIT: Literal[2]
EXCEPTION: Literal[8]
READABLE: Literal[2]
WRITABLE: Literal[4]

TCL_VERSION: str
TK_VERSION: str

@final
class TkttType:
    def deletetimerhandler(self): ...

if sys.version_info >= (3, 8):
    def create(
        __screenName: str | None = None,
        __baseName: str = "",
        __className: str = "Tk",
        __interactive: bool = False,
        __wantobjects: bool = False,
        __wantTk: bool = True,
        __sync: bool = False,
        __use: str | None = None,
    ): ...

else:
    def create(
        __screenName: str | None = None,
        __baseName: str | None = None,
        __className: str = "Tk",
        __interactive: bool = False,
        __wantobjects: bool = False,
        __wantTk: bool = True,
        __sync: bool = False,
        __use: str | None = None,
    ): ...

def getbusywaitinterval(): ...
def setbusywaitinterval(__new_val): ...
