class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self):
        prefix = " " * self.get_level() * 3 + "|__"
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    laptops.add_child(TreeNode("Macbook"))
    laptops.add_child(TreeNode("Surface book"))
    laptops.add_child(TreeNode("Pavilion"))

    cellphones = TreeNode("Cell phones")
    cellphones.add_child(TreeNode("iPhone"))
    cellphones.add_child(TreeNode("OnePlus"))

    tvs = TreeNode("TVS")
    tvs.add_child(TreeNode("LG"))
    tvs.add_child(TreeNode("Onida"))
    tvs.add_child(TreeNode("Samsung"))

    root.add_child(laptops)
    root.add_child(cellphones)
    root.add_child(tvs)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
