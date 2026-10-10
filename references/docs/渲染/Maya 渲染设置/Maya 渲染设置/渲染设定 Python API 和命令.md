# 渲染设定 Python API 和命令

## 渲染设定 Python API

渲染设定 Python API 作为 Maya 安装的一部分提供，您可在以下文件夹中找到相关文件：..\Python\Lib\site-packages\maya\app\renderSetup。

**注**

目前，渲染设定 Python API 未获得正式支持。随着时间的推移，这一状况可能会有所改变。

若要使用渲染设定 API，您应先按如下所示导入渲染设定模块：

```text
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
```

还应导入 maya.cmds (import maya.cmds)，以便能够使用本地 Maya 命令。

以下示例脚本创建了一个层和两个集合。它使用表达式 mySphere* 将球体添加到第一个集合，然后使用表达式 myCube* 将立方体添加到第二个集合。

创建一个绝对覆盖并将其应用于第一个集合，然后创建一个相对覆盖并将其应用于第二个集合。

该示例最终切换到渲染层，您将在此看到以模板显示模式显示的球体，以及平移的立方体。

```text
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.cmds as cmds

rs = renderSetup.instance()

# Create and append the render layer
rl = rs.createRenderLayer("MyRenderSetupLayer")

# Create and append 2 collections
c1 = rl.createCollection("sphereCollection")
c2 = rl.createCollection("cubeCollection")

# Create a trivial scene with a cube, a sphere and a cylinder
cmds.polySphere(name='mySphere')
cmds.move(2, 'mySphere', y=True)
cmds.polyCube(name='myCube')
cmds.move(5, 'myCube', y=True)
cmds.polyCylinder(name='myCylinder')
cmds.move(10, 'myCylinder', y=True)

# Set up collection 1 to select all spheres using the pattern mySphere*,
# and collection 2 to select all cubes using the pattern myCube*.
c1.getSelector().setPattern('mySphere*')
c2.getSelector().setPattern('myCube*')

# Set up an absolute override on mySphereShape.template with a value of True
ov1 = c1.createAbsoluteOverride('mySphereShape', 'template')
ov1.setAttrValue(True)

# Set up a relative override on myCube.translate with a multiply value of
# [2.0, 2.0, 2.0] and an offset of [0.1, 0.1, 0.1]
ov2 = c2.createRelativeOverride('myCube', 'translate')
ov2.setMultiply([2.0, 2.0, 2.0])
ov2.setOffset([0.1, 0.1, 0.1])

# Set the render layer as visible.
# Only the sphere and the cube are displayed as they are collection members.
rs.switchToLayer(rl)
```

然后，您可以扩展此示例以创建着色器覆盖。在本示例中，将创建两个表面着色器，其中第一个着色器指定给场景层中的立方体。第一个表面着色器设置为红色，第二个着色器设置为蓝色。因此，在场景层中，立方体设置为红色。

然后，创建一个着色器覆盖，以便为立方体指定第二个表面着色器。现在，当您切换渲染层时，将看到立方体为蓝色并已平移。球体以模板显示模式显示。

```text
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.cmds as cmds

# Helper function for creating a shader
def createShader(shaderType):
    """ Create a shader of the given type"""
    shaderName = cmds.shadingNode(shaderType, asShader=True)
    sgName = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=(shaderName + "SG"))
    cmds.connectAttr(shaderName + ".outColor", sgName + ".surfaceShader")
    return (shaderName, sgName)

# Helper function for assigning a material
def assignMaterial(shapeName, shadingGroupName):
    cmds.sets(shapeName, forceElement=shadingGroupName)

# Helper function for setting a color attribute to some color value
def setColor(attr, color):
    cmds.setAttr(attr, color[0], color[1], color[2], type="float3")

rs = renderSetup.instance()

# Create and append the render layer
rl = rs.createRenderLayer("MyRenderSetupLayer")

# Create and append 2 collections
c1 = rl.createCollection("sphereCollection")
c2 = rl.createCollection("cubeCollection")

# Create a trivial scene with a cube, a sphere and a cylinder
cmds.polySphere(name='mySphere')
cmds.move(2, 'mySphere', y=True)
cmds.polyCube(name='myCube')
cmds.move(5, 'myCube', y=True)
cmds.polyCylinder(name='myCylinder')
cmds.move(10, 'myCylinder', y=True)

# Set up collection 1 to select all spheres using the pattern mySphere*,
# and collection 2 to select all cubes using the pattern myCube*.
c1.getSelector().setPattern('mySphere*')
c2.getSelector().setPattern('myCube*')

# Set up an absolute override on mySphereShape.template with a value of True
ov1 = c1.createAbsoluteOverride('mySphereShape', 'template')
ov1.setAttrValue(True)

# Set up a relative override on myCube.translate with a multiply value of
# [2.0, 2.0, 2.0] and an offset of [0.1, 0.1, 0.1]
ov2 = c2.createRelativeOverride('myCube', 'translate')
ov2.setMultiply([2.0, 2.0, 2.0])
ov2.setOffset([0.1, 0.1, 0.1])

# Creates two surface shaders. Makes one red, the other blue and assigns the
# red shader to myCubeShape. Then creates a shader override with the blue
# shader.
shaderName, sgName = createShader("surfaceShader")
shaderName2, sgName2 = createShader("surfaceShader")
assignMaterial("myCubeShape", sgName)
setColor(shaderName + ".outColor", [1.0, 0.0, 0.0])
setColor(shaderName2 + ".outColor", [0.0, 0.0, 1.0])
outColorShaderOvr = c2.createAbsoluteOverride(shaderName2, 'outColor')

# Set the render layer as visible.
# Only the sphere and the cube are displayed as they are collection members.
rs.switchToLayer(rl)
```

**注**

调用 rs.switchToLayer() 方法可确保渲染设定与任何场景更改同步。这相当于以交互方式使用 Maya 时单击层可见性图标 ![图：调用 rs.switchToLayer() 方法可确保渲染设定与任何场景更改同步。这相当于以交互方式使用 Maya 时单…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-7BFB60FC-AB73-409C-8460-0D2945F5E997.png) <!-- baize:img-hook downloaded=false reason="正文 5607 字 ≥300，非承重" --> 更新层成员身份。

## 渲染设定 Python 命令

您可以使用渲染设定命令查询渲染设定成员身份。

若要了解有关以下命令的详细信息：

  renderLayerMembers

  renderSetupFindCollections

  renderSetup

  renderSetupLegacyLayer

请使用 help() 查询文档字符串。

例如，以下 Python 命令可用于查询 renderLayerMembers 命令：

```text
import maya.app.renderSetup.model.modelCmds as modelCmds
help(modelCmds.RenderLayerMembersCmd)
```

您可以通过类似方式查询其他命令的文档字符串。

若要了解有关 renderSetupSelect 命令的详细信息，请在“脚本编辑器”(Script Editor)的“Python”选项卡中输入以下命令：

```text
import maya.app.renderSetup.views.viewCmds as viewCmds
help(viewCmds.RenderSetupSelectCmd)
```

## 在 Python 中导入和导出 .json 文件

您可以按如下所示定义函数，用于在场景中导入和导出渲染设定 .json 文件。

```text
import maya.app.renderSetup.model.renderSetup as renderSetup

import json

# Cannot name function "import", as this is a reserved Python keyword.
def importFile(filename):
    with open(filename, "r") as file:
        renderSetup.instance().decode(json.load(file), renderSetup.DECODE_AND_OVERWRITE, None)

def exportFile(filename):
    with open(filename, "w+") as file:
        json.dump(renderSetup.instance().encode(None), fp=file, indent=2, sort_keys=True)
```
