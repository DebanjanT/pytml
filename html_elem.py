from uuid import uuid4
from vnode import Vnode


MAX_ALLOWED_ATTR = 50


class Div:
    content: Vnode  # nested vnode support
    id = uuid4()  # autogen id for the every div element


class Body:
    content: Vnode  # nested vnode support
    id = uuid4()  # autogen id for the every div element
