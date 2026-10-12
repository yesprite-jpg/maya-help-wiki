# “控制”(Control)菜单

位于“装备”(Rigging)[菜单集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D90A2BDB-FD05-4528-8A95-C33A02D15129)中。

## 控制器

#### 标记为控制器(Tag as Controller)

将选定对象标记为动画控制器。单击装备控制器并选择“标记为控制器”(Tag as Controller)，可以创建连接到装备控制器对象的控制器节点。

#### 父控制器(Parent Controller)

将选定对象指定为控制器，并将最后一个选定对象设为控制器父对象。例如，如果一只手的手指具有关节链，请分别在其上下方选择一个手指关节。选择“父控制器”(Parent Controller)将这两个关节标记为控制器，层次较高的手指关节将成为较低关节的父对象。

**注**

对于 Viewport 2.0，您可以在“显示”(Display) >

显示(Show)

子菜单中过滤控制器对象的场景，而不考虑其类型（NURBS、定位器或形状）。请参见

使用 Viewport 2.0

。

## HumanIK

#### 创建控制装备(Create Control Rig)

为角色创建控制装备。详细信息请参见[创建控制装备](../../../HumanIK/HumanIK/设置%20HumanIK%20角色/创建控制装备.md)。

## 角色集

#### 创建角色集(Create Character Set)

使用已设置动画的对象、对象的各个部分或所选属性创建角色集。详细信息请参见[创建角色集](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-A2AAF7B8-4187-4E1B-8BC5-98F84474C0EF.htm)。

选择“控制 > 创建角色集”(Control > Create Character Set) > ![图：选择“控制 创建角色集”(Control Create Character Set) 以设置创建角色集选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1319 字 ≥300，非承重" --> 以设置[创建角色集选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C344110A-440B-43B5-A26F-06480298006A)。

#### 创建子角色集(Create Subcharacter Set)

使用所选的相关角色集属性包创建子角色集。

选择“控制 > 创建子角色集”(Control > Create Subcharacter Set) > ![图：选择“控制 创建子角色集”(Control Create Subcharacter Set) 以设置创建子角色集选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1319 字 ≥300，非承重" --> 以设置[创建子角色集选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DB982EA4-8450-45D6-A375-D7761194A1AA)。

#### 角色映射器(Character Mapper)

打开角色映射器窗口，该窗口提供了将动画从源角色映射到目标角色的选项。

有关选项的详细信息，请参见[角色映射器](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-20015023-4D8F-4D09-8F82-15D3A80A1554.htm)。

#### 属性编辑器(Attribute Editor)

显示选定对象上的属性。详细信息请参见[属性编辑器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)。

#### 添加到角色集(Add to Character Set)

将选定属性添加到当前的角色集或子角色集。

#### 从角色集中移除(Remove from Character Set)

从当前角色或子角色集中移除选定的属性。

#### 合并角色集(Merge Character Sets)

组合选定的角色集或子角色集。

#### 选择角色集节点(Select Character Set Node)

此子菜单列出了所有的已定义角色集。从列表中选择角色集。

**注**

角色集中的对象不处于选定状态。

#### 选择角色集成员(Select Character Set Members)

此子菜单仅列出构成角色集的对象。

#### 设置当前角色集(Set Current Character Set)

此子菜单列出了所有的已定义角色集。从列表中选择角色集以将其设置为当前角色集。

选择“关系编辑器”(Relationship Editor)以打开关系编辑器窗口。在角色编辑模式下，使用关系编辑器选择角色集，以便它在工作区中当前处于选定状态。

#### 重定向(Redirect)

将平移和/或旋转重定向控制添加到当前角色。这些控制将显示在角色原点处。当角色可重定向时，可以更改已创建（例如，运动捕捉）动画的平移和方向。

详细信息请参见[重定向角色动画](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C3DF9BF0-2B41-4A3A-B760-1679D7132515.htm)和[重定向动画角色的运动](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-D7EA1F16-4EB2-48C0-8833-82E7A2C54BA0.htm)。

选择“控制 > 重定向”(Control > Redirect) > ![图：选择“控制 重定向”(Control Redirect) 以设置角色重定向选项。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1319 字 ≥300，非承重" --> 以设置[角色重定向选项](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-10957ABA-B9A5-45D3-8A0C-2F5822BE3BC0)。
