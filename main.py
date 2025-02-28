"""
Trying to create simple dom using python.
Target:
    input:
    dom = VDom()
    dom.vnode(type=Div,
    content="Hi",
    {
        "onclick":"alert("Hello from pytml")"
    })

    EXPECTED OUTPUT
    <div onclick={alert("Hello from pytml")}>
        Hi
    </div>

"""

from vnode import Vnode


def main():
    fnode = Vnode(dtype="Div")
    print(fnode)
    print(fnode.print_tree())


main()
