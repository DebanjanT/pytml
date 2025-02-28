from dataclasses import dataclass
from typing import Union, TYPE_CHECKING
from tabulate import tabulate

if TYPE_CHECKING:
    from html_elem import Div, Body

HtmlElementType = Union["Div", "Body"]


@dataclass()
class Vnode:
    dtype: HtmlElementType

    def __init__(self, dtype):
        self.dtype = dtype

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
