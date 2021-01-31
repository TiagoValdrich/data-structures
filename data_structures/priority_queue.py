from typing import Any, Generator, List, Optional


class PriorityItem:
    def __init__(self, value: Any, priority: int) -> None:
        self.value = value
        self.priority = priority

    def __repr__(self) -> str:
        return "(" + str(self.value) + "," + str(self.priority) + ")"


class PriorityQueue:
    def __init__(self) -> None:
        self._queue: List[PriorityItem] = []

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
                    result += str(item.value)
                else:
                    result += item.value

                if i < len(self._queue) - 1:
                    result += ", "

        result += "]"

        return result

    def enqueue(self, item: PriorityItem) -> None:
        if not isinstance(item, PriorityItem):
            raise ValueError()

        added = False

        for (index, priority_item) in enumerate(self._queue):
            if item.priority > priority_item.priority:
                added = True
                self._queue.insert(index, item)
                break

        if not added:
            self._queue.append(item)

    def dequeue(self) -> Optional[PriorityItem]:
        if self._queue:
            return self._queue.pop(0)

        return None

    def front(self) -> Optional[PriorityItem]:
        if self._queue:
            return self._queue[0]

        return None
