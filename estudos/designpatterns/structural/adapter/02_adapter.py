"""
Abordagem utilizando herança
"""

from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass


class XboxControl(IControl):
    """
    This is the default control used
    """
    def top(self) -> None:
        print("Y")

    def down(self) -> None:
        print("A")

    def left(self) -> None:
        print("X")

    def right(self) -> None:
        print("B")


class PsControl:
    """
    This is the new control to be used
    """
    def move_top(self) -> None:
        print("Triangulo")

    def move_down(self) -> None:
        print("X")

    def move_left(self) -> None:
        print("Quadrado")

    def move_right(self) -> None:
        print("Bola")


class ControlAdapter(XboxControl, PsControl):
    def top(self) -> None:
        self.move_top()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()


if __name__ == "__main__":
    control = XboxControl()
    control.top()
    control.down()
    control.left()
    control.right()

    print()

    new_control = PsControl()
    control_adapter = ControlAdapter()
    control_adapter.top()
    control_adapter.down()
    control_adapter.left()
    control_adapter.right()
