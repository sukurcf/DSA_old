class TreeNode:

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return child

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self, what_to_print, level):
        if self.get_level() > level:
            return
        prefix = " " * self.get_level() * 3 + "|__"
        if what_to_print == "name":
            value = self.name
        elif what_to_print == "designation":
            value = self.designation
        elif what_to_print == "both":
            value = f"{self.name} ({self.designation})"
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(what_to_print, level)


def build_product_tree():
    nilpul = TreeNode("Nilpul", "CEO")
    chinmay = nilpul.add_child(TreeNode("Chinmay", "CTO"))
    vishwa = chinmay.add_child(TreeNode("Vishwa", "Infrastructure Head"))
    vishwa.add_child(TreeNode("Dhaval", "Cloud Engineer"))
    vishwa.add_child(TreeNode("Abhijit", "App Engineer"))
    chinmay.add_child(TreeNode("Aamir", "Application Head"))
    gels = nilpul.add_child(TreeNode("Gels", "HR Head"))
    gels.add_child(TreeNode("Peter", "Recruitment Manager"))
    gels.add_child(TreeNode("Waqas", "Policy Manager"))
    return nilpul


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree("both", 3)
