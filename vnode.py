from dataclasses import dataclass
from typing import Type, Union, TYPE_CHECKING
from tabulate import tabulate


if TYPE_CHECKING:
    from html_elem import Div, Body

HTML_ELEM_TYPE = Union["Div", "Body"]


@dataclass()
class Vnode:
    dtype: HTML_ELEM_TYPE  # choose any type among the list of  html element type

    def __init__(self, dtype: Type[HTML_ELEM_TYPE]):
        from html_elem import Div, Body

        self.dtype = dtype
        if not isinstance(dtype, type) or not issubclass(dtype, (Div, Body)):
            raise TypeError(f"dtype must be a subclass of Div or Body, got {dtype}")

    def print_tree(self):
        print(
            tabulate(
                [
                    ["Sun", 696000, 1989100000],
                    ["Earth", 6371, 5973.6],
                    ["Moon", 1737, 73.5],
                    ["Mars", 3390, 641.85],
                ],
                headers=["Planet", "R (km)", "mass (x 10^29 kg)"],
            )
        )
