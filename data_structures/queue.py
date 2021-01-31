from typing import Generator, Optional, Union, Any


class Queue:
    def __init__(self) -> None:
        self._queue = []

    def __len__(self) -> int:
        return len(self._queue)

    def __iter__(self) -> Generator:
        for item in self._queue:
            yield item

    def __repr__(self) -> str:
        result = "["

        if self._queue:
            for (i, item) in enumerate(self._queue):
                if not isinstance(item, str):
                    result += str(item)
                else:
                    result += item

                if i < len(self._queue) - 1:
                    result += ", "

        result += "]"

        return result

    def enqueue(self, items: Union[Any, list]) -> None:
        if isinstance(items, list):
            for item in items:
                self._queue.append(items)
        else:
            self._queue.append(items)

    def dequeue(self) -> Optional[Any]:
        if self._queue:
            return self._queue.pop(0)

        return None

    def front(self) -> Optional[Any]:
        if self._queue:
            return self._queue[0]

        return None
