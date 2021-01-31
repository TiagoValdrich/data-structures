from data_structures.priority_queue import PriorityItem, PriorityQueue


class TestQueue:
    def test_enqueue(self):
        queue = PriorityQueue()
        priority_item_one = PriorityItem("item1", 1)
        priority_item_two = PriorityItem("item2", 1)

        queue.enqueue(priority_item_one)
        queue.enqueue(priority_item_two)
        front = queue.front()

        assert len(queue) == 2
        assert front.value == priority_item_one.value
        assert front.priority == priority_item_one.priority

        priority_item_three = PriorityItem("item3", 2)
        queue.enqueue(priority_item_three)
        front = queue.front()

        assert len(queue) == 3
        assert front.value == priority_item_three.value
        assert front.priority == priority_item_three.priority

    def test_dequeue(self):
        queue = PriorityQueue()
        priority_item_one = PriorityItem("item1", 1)
        priority_item_two = PriorityItem("item2", 3)
        priority_item_three = PriorityItem("item3", 99)
        queue.enqueue(priority_item_one)
        front_item = queue.front()

        assert len(queue) == 1
        assert front_item.value == priority_item_one.value
        assert front_item.priority == priority_item_one.priority

        dequed_value = queue.dequeue()

        assert len(queue) == 0
        assert dequed_value.value == priority_item_one.value
        assert dequed_value.priority == priority_item_one.priority
        assert queue.dequeue() == None

        queue.enqueue(priority_item_three)
        queue.enqueue(priority_item_one)
        queue.enqueue(priority_item_two)

        assert queue.dequeue().value == priority_item_three.value
        assert queue.dequeue().value == priority_item_two.value
        assert queue.dequeue().value == priority_item_one.value
