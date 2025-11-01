from typing import Tuple, Any


def demo_creation() -> Tuple[Any, ...]:
    """Show how to create tuples."""
    t1 = (1, 2, 3)
    t2 = 'a', 'b', 'c'          # tuple packing without parentheses
    t3 = (42,)                  # single-element tuple needs a trailing comma
    print("demo_creation:")
    print("  t1 =", t1)
    print("  t2 =", t2)
    print("  t3 =", t3)
    print()
    return t1


def demo_indexing_slicing(t: Tuple[Any, ...]) -> None:
    """Indexing and slicing examples."""
    print("demo_indexing_slicing:")
    print("  original:", t)
    print("  t[0] ->", t[0])
    print("  t[-1] ->", t[-1])
    print("  t[1:3] ->", t[1:3])
    print()


def demo_packing_unpacking() -> None:
    """Packing and unpacking tuples."""
    print("demo_packing_unpacking:")
    packed = 10, 20, 30
    a, b, c = packed
    print("  packed ->", packed)
    print("  unpacked a, b, c ->", a, b, c)
    # extended unpacking
    head, *middle, tail = (1, 2, 3, 4, 5)
    print("  extended unpacking head, *middle, tail ->", head, middle, tail)
    print()


def demo_immutability() -> None:
    """Show that tuples are immutable and safe to use as dict keys."""
    print("demo_immutability:")
    t = (1, 2, 3)
    print("  tuple t:", t)
    try:
        # This will raise a TypeError
        t[0] = 100  # type: ignore
    except TypeError as e:
        print("  trying to modify raises:", type(e).__name__)
    d = {t: 'a valid dictionary key'}
    print("  tuples can be dict keys:", d)
    print()


def demo_methods_conversion() -> None:
    """Tuple methods (count/index) and converting to/from lists."""
    print("demo_methods_conversion:")
    t = (1, 2, 2, 3)
    print("  t:", t)
    print("  t.count(2) ->", t.count(2))
    print("  t.index(3) ->", t.index(3))
    # conversion
    lst = list(t)
    lst.append(4)
    t2 = tuple(lst)
    print("  converted to list and back ->", t2)
    print()


def demo_nested_and_returning() -> Tuple[int, Tuple[str, int]]:
    """Nested tuple example and function returning multiple values as tuple."""
    nested = ("point", (10, 20))
    print("demo_nested_and_returning:")
    print("  nested:", nested)
    # function returning a tuple (common pattern)
    def get_user() -> Tuple[str, int]:
        return ("Alice", 30)

    user = get_user()
    print("  get_user() ->", user)
    print()
    return 0, nested


def run_all_demos() -> None:
    """Run every demo in sequence."""
    t = demo_creation()
    demo_indexing_slicing(t)
    demo_packing_unpacking()
    demo_immutability()
    demo_methods_conversion()
    demo_nested_and_returning()


if __name__ == '__main__':
    print("Python Tuples — small workshop\n")
    run_all_demos()
