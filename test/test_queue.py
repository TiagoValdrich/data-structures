from data_structures.queue import Queue


class TestQueue:
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        assert len(queue) == 2
        assert queue.front() == 1

        queue.enqueue([3, 4, 5])

        assert len(queue) == 5
        assert queue.front() == 1

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("item1")

        assert len(queue) > 0
        assert queue.front() == "item1"

        dequeued_value = queue.dequeue()

        assert dequeued_value == "item1"
        assert len(queue) == 0
        assert queue.front() == None

        dequeued_value = queue.dequeue()

        assert dequeued_value == None
        assert len(queue) == 0
        assert queue.front() == None
