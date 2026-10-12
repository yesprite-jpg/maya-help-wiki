# 调整(tweak)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-18F963A9-A2D7-4CA7-B4B1-EDBC323666BF.png) <!-- baize:img-hook downloaded=false reason="正文 489 字 ≥300，非承重" -->

存储当前蒙皮的顶点的变换信息。当您操纵角色的骨架时，“调整”(Tweak)还将确保正确转换蒙皮顶点。当删除“调整”(tweak)节点时，将擦除受影响关节和对象所影响的顶点的所有转换信息。删除“调整”(tweak)节点是从蒙皮移除变形的一种简单方法。

## 组件标记和调整节点

使用[组件标记](../../../../变形效果/变形效果/变形器参考/变形器节点/组件标记.md)时，不会向变形添加任何调整节点。但是，有时您可能需要通过添加调整节点使组件标记形状的行为与已弃用的 GroupID 形状相同。

如果要继续使用调整节点，有下面一些选项：

- 如果希望在向场景添加变形器时创建调整节点，请在[“动画”(Animation)首选项（在“设置”(Settings)下）](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0817C74B-C95C-4E5F-BCFA-26DEE1D7747F)中激活**“创建调整”(Create Tweak)**（“绑定”(Rigging)区域）

- 若要在创建调整节点后将其添加到变形中，请在“属性编辑器”(Attribute Editor)中选择变形器，然后从[“变形”(Deform)菜单](../../../../变形效果/变形效果/变形器参考/“变形”%28Deform%29菜单.md)选项中选择**“添加调整”(Add Tweak)**

- 使用 deformableShapes 命令中的 -createTweakNode 元素：

  deformableShape

  -createTweakNode TagShape;
