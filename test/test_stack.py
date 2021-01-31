from data_structures.stack import Stack


class TestStack:
    def test_push_item(self):
        stack = Stack()
        stack.push("item")

        assert len(stack) > 0
        assert stack.peek() == "item"

    def test_pop_item(self):
        stack = Stack()
        stack.push("item")

        assert len(stack) > 0
        assert len(stack) == 1

        value = stack.pop()

        assert value == "item"
        assert len(stack) == 0
        assert stack.peek() == None

    def test_clear_stack(self):
        stack = Stack()
        stack.push("item1")
        stack.push("item2")
        stack.push("item3")

        assert len(stack) > 0
        assert len(stack) == 3

        stack.clear()

        assert len(stack) == 0
