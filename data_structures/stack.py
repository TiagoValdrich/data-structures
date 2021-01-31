from typing import Any, Optional


class Stack:
    def __init__(self) -> None:
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def __iter__(self):
        for item in self._stack:
            yield item

    def __repr__(self) -> str:
        result = "["

        if self._stack:
            for (i, item) in enumerate(self._stack):
                if not isinstance(item, str):
                    result += str(item)
                else:
                    result += item

                if i < len(self._stack) - 1:
                    result += ", "

        result += "]"

        return result

    def peek(self) -> Optional[Any]:
        if self._stack:
            return self._stack[-1]

        return None

    def push(self, element: Any) -> None:
        self._stack.append(element)

    def pop(self) -> Optional[Any]:
        if self._stack:
            return self._stack.pop()

        return None

    def clear(self) -> None:
        self._stack = []
