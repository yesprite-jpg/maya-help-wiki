# 匹配选项(Matching options)

打开匹配选项(Matching Options)

- 在动画片段上单击鼠标右键，然后选择“重新定位 > 匹配重定位器”(Relocate > Match Relocators)。

  **注**

  若要执行匹配，必须存在两个具有重定位器的片段。请参见

  使用时间编辑器重定位器匹配姿势

  。

使用“匹配选项”(Matching Options)可将片段相互匹配。匹配两个片段时，一个片段的匹配对象与该片段在轨迹上之前或之后的同一对象保持一致。有关如何匹配片段的信息，请参见[使用时间编辑器重定位器匹配姿势](../使用时间编辑器重定位器匹配姿势.md)。

使用时间编辑器操纵动画序列中的片段时，您可以使用片段的匹配选项根据指定的对象自动对齐片段。因此，片段必须并排放在相同轨迹上。

有关创建有效姿势匹配的提示，请参见[姿势匹配最佳实践](姿势匹配最佳实践.md)。

#### 匹配对象(Matching Object)

使用“匹配对象”(Matching Object)菜单可以选择轨迹内容的哪一部分要用于片段匹配。单击列表旁边的 ![图：使用“匹配对象”(Matching Object)菜单可以选择轨迹内容的哪一部分要用于片段匹配。单击列表旁边的 ，将默认…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-A8D6C4CC-5A01-4A92-B124-67B4662112AA.png) <!-- baize:img-hook downloaded=false reason="正文 1902 字 ≥300，非承重" -->，将默认对象替换为选定对象。

#### 根对象(Root Objects)

用于设置不是默认指定的根对象。默认情况下，“在片段中使用根对象”(Use root objects in clip)部分包含可在片段的名单中找到的根对象。

如果要设置非默认根对象，请禁用“在片段中使用根对象”(Use root objects in clip)，然后选择更适合匹配的对象。单击列表旁边的 ![图：如果要设置非默认根对象，请禁用“在片段中使用根对象”(Use root objects in clip)，然后选择更适合…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-A8D6C4CC-5A01-4A92-B124-67B4662112AA.png) <!-- baize:img-hook downloaded=false reason="正文 1902 字 ≥300，非承重" -->，将默认对象替换为选定对象。 您可以使用 ![图：如果要设置非默认根对象，请禁用“在片段中使用根对象”(Use root objects in clip)，然后选择更适合…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-A8D6C4CC-5A01-4A92-B124-67B4662112AA.png) <!-- baize:img-hook downloaded=false reason="正文 1902 字 ≥300，非承重" --> 按钮直接在视口或大纲视图中选择根对象，从而将自定义根添加到列表中。

**注**

根对象应当是可移动角色全局位置的关节/控制器。请参见

姿势匹配最佳实践

。

#### 匹配片段(Matching Clip)

使用“匹配选项”(Match Options)对话框中的“匹配片段”(Match Clip)选项，可以选择要匹配的片段。

##### 上一个(Previous)

将选定片段与其在轨迹上之前的片段匹配。

##### 下一个(Next)

将选定片段与其在轨迹上之*后*的片段匹配。

#### 匹配时间(Matching Time)

使用“匹配时间”(Match Time)选项，可以选择选定片段在交叉融合的哪个点匹配。

**注**

匹配片段时，选定片段是指在视口中播放的片段。

“匹配时间”(Match Time)菜单包含以下选项：

##### 当前帧(Current Frame)

在当前时间将选定片段的开头与上一个片段匹配。

##### 第一个片段末尾(End of First Clip)

将选定片段的开头与第一个片段的末尾匹配。如果片段之间没有交叉融合，则选定片段的开头将与上一个片段的末尾匹配。

##### 中间帧的片段(Inbetween Clips)

将选定片段与融合中间的上一个片段匹配。如果片段之间没有交叉融合，则选定片段的开头将与上一个片段的末尾匹配。

##### 第二个片段开头(Start of Second Clip)

将选定片段的末尾与第二个片段的开头匹配。

#### 匹配姿势(Matching Pose)

使用“匹配姿势”(Matching Pose)选项，可以通过选择“无”(None)、“完全 XYZ”(Full XYZ)或“沿全局 Y 轴(重力)投影”(Projected along GlobalY (Gravity))，确定片段的匹配对象是否以及如何平移和旋转，以便与另一个片段的动画匹配。

**平移/旋转(Translation/Rotation)**

##### 无(None)

匹配片段时，忽略变换值注意事项。

##### 完全(XYZ) (Full (XYZ))

将选定片段的匹配对象平移或旋转到与上一个片段的匹配对象相同的位置或方向。

##### 沿全局 Y 轴(重力)投影(Projected along GlobalY (Gravity))

在同一角色之间匹配姿势时，重力效果最佳。在不同大小的角色之间匹配姿势可能会产生意外结果，从而导致目标角色的脚伸到空中，与较大角色的姿势匹配。为获得最佳结果，请在不同大小的角色之间匹配姿势时禁用“沿全局 Y 轴(重力)投影”(Projected along GlobalY (Gravity))。

当您希望角色的脚悬浮于空中时，如果要匹配姿势，也可以禁用“重力”(Gravity)选项。禁用“重力”(Gravity)时，可以在不考虑地板的情况下实现精确匹配。

#### 上方向轴(Up Axis)

如果流水线配置为使用 Z 轴作为上方向向量，请禁用“使用场景首选项”(Use Scene Preferences)以覆盖 Maya 默认设置（在“首选项”(Preferences)窗口中设置），从而定义自定义上方向向量进行匹配。在以下字段中输入特定的值。请参见“设置”(Settings)首选项中的[世界坐标系](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4D653DC9-57AA-4D8B-987A-5B7A9735CAF0#GUID-4D653DC9-57AA-4D8B-987A-5B7A9735CAF0__WS73099CC142F487553B93539F117EA10CE8F30A5)。

**注**

这些更改仅适用于

“时间编辑器”(Time Editor)

。

#### 变换偏移(Transform Offset)

如果单击“应用”(Apply)，则显示匹配对象值不断变化。
