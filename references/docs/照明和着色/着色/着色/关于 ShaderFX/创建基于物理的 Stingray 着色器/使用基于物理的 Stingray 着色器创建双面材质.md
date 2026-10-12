# 使用基于物理的 Stingray 着色器创建双面材质

使用 Stingray PBS 创建双面材质时，必须同时在对象的形状节点上和 Stingray PBS 的“标准基础”(Standard Base)节点上启用“双面”(Double Sided)属性。这样可确保对象使用 Maya 中的正确照明进行渲染。如果只启用前者，则照明对着色器可能不正确。

将 Stingray PBS 材质指定给对象后，执行以下操作：

1. 选择对象。在属性编辑器中，选择对象的形状节点，并确保已启用“双面”(Double Sided)。

2. 在 Stingray PBS 节点属性编辑器中，单击“打开 ShaderFX”(Open ShaderFX)以打开 ShaderFX 编辑器。

3. 选择“标准基础”(Standard Base)节点。

  在属性编辑器中，选择“双面”(Double Sided)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-429BD3A1-115E-4592-83F2-73535CAF2DCC.png) <!-- baize:img-hook downloaded=false reason="正文 329 字 ≥300，非承重" -->
