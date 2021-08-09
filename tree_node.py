class Tree:
    def __init__(self, argv1=0):
        self.data = argv1
        self.left = None
        self.right = None
        self.visited = False

    def get(self):
        return self.data
