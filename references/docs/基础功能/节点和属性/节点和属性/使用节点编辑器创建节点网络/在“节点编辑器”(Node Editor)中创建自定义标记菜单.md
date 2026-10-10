# 在“节点编辑器”(Node Editor)中创建自定义标记菜单

可以自定义节点标记菜单。以下是使用 Python 将自定义节点标记菜单项添加到 plusMinusAverage 节点的示例。

在“节点编辑器”(Node Editor)中创建 plusMinusAverage 节点，然后在“脚本编辑器”(Script Editor)中运行以下脚本。

```text
from maya.app.general import nodeEditorMenus
from maya import cmds

def addPMAMenuItems(ned, node):
    """
    Check for plusMinusAverage node and create necessary menu items
    """
    type = cmds.nodeType(node)
    if type == 'plusMinusAverage':
        def doSomething(*args):
            cmds.confirmDialog(title="Something", message="Ok?")
        cmds.menuItem(label="PlusMinusAverage! Do something!", c = doSomething)
        return True
    else:
        return False

# register the custom callback with nodeEditor
#
nodeEditorMenus.customInclusiveNodeItemMenuCallbacks.append(addPMAMenuItems)
```

plusMinusAverage 节点现在包括自定义菜单项“PlusMinusAverage! Do something!”。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-5A5A38B9-47C6-4624-A647-EFA7A3ED3312.png) <!-- baize:img-hook downloaded=false reason="正文 688 字 ≥300，非承重" -->

## 相关主题

- [节点编辑器标记菜单](节点编辑器%28Node%20Editor%29/“节点编辑器”%28Node%20Editor%29标记菜单.md)
