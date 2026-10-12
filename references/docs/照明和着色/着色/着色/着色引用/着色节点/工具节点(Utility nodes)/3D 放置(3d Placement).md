# 3D 放置(3d Placement)

3D 放置节点可定义世界空间中的 3D 纹理或“环境”(Environment)纹理的定位和方向。3D 放置节点能简化多个曲面的纹理放置（就像是放置到一个曲面）。

可以使用 place3dTexture 节点的“属性编辑器”(Attribute Editor)中的数字精度重新定位 3D 纹理，或使用操纵器以交互方式重新定位纹理或标签。

Maya 提供了两种方法在 NURBS 曲面上放置 3D 纹理：“交互式放置”(Interactive Placement)或“适配到组边界框”(Fit to group bbox)（边界框）。根据需要选择最合适的方法。有时兼用这两种方法最有效。

创建 3D 纹理或将纹理投影到对象（而不是将其应用为法线或蒙板）时，一个立方体形状的图标将显示在与曲面上纹理的大小、比例和位置相对应的场景中。尤其对于已设置动画的对象或变形对象，必须保持纹理在对象上的位置正确。（例如，如果对象已设置动画，则可以将几何体作为 3D 图标的父对象。）

在“创建”(Create)选项卡中找到该工具（请参见[“创建”(Create)选项卡](../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)）。

若要使用该工具，请参见[使用“3D 放置”(3d Placement)工具](../../../渲染节点工具/使用“3D%20放置”%283d%20Placement%29工具.md)。

**注**

若要创建没有其对应 place3DTexture 节点的纹理节点，请从

Hypershade

菜单禁用

“创建 > 创建选项 > 包括带纹理的放置”(Create > Create Options > Include Placement with Textures)

。
