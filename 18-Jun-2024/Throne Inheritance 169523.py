# Problem: Throne Inheritance - https://leetcode.com/problems/throne-inheritance/

class ThroneNode:
    def __init__(self, name):
        self.name = name
        self.childs = []

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.kingNode = ThroneNode(kingName)
        self.childArray = {}
        self.childArray[kingName] = self.kingNode.childs

        self.deadPersons = set()

    def birth(self, parentName: str, childName: str) -> None:
        newNode = ThroneNode(childName)
        self.childArray[parentName].append(newNode)
        self.childArray[childName] = newNode.childs

    def death(self, name: str) -> None:
        self.deadPersons.add(name)

    def getInheritanceOrder(self) -> List[str]:
        path = []
        stack = [self.kingNode]
        while stack:
            node = stack.pop()
            if node.name not in self.deadPersons:
                path.append(node.name)
            for child in reversed(node.childs): 
                stack.append(child)
        return path

        # # def dfs(node):
        # #     if not node:
        # #         return
        # #     if node.name not in self.deadPersons:
        # #         path.append(node.name)
        # #     for child in node.childs:
        # #         dfs(child)
        # # dfs(self.kingNode)
        # return path


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()