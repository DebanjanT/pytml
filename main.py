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
    from html_elem import Div  # Lcoal import

    div = Div()
    print(div.id, "\n")
    fnode = Vnode(dtype=Div)
    print(fnode, "\n")
    print(fnode.print_tree())


main()
