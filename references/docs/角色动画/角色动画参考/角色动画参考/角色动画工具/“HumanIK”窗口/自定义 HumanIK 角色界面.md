# 自定义 HumanIK 角色界面

您可以通过在基本文本编辑器（如记事本或 [Programmer's Notepad](https://www.pnotepad.org/)）中编辑 *CharacterControls.xml* 文件，自定义 [HumanIK 窗口](../“HumanIK”窗口.md) 的“控制”(Controls)和“自定义绑定”(Custom Rig)选项卡。您可以通过更改布局来编辑 HumanIK 选项卡的外观，以适应您的工作流或动画绑定。

CharacterControls XML 配置文件位于 CharacterControls 目录 (C:\Program Files\Autodesk\<Maya 版本>\resources\CharacterControls) 中。有关可自定义区域的描述，请参见[编辑 HumanIK 角色控制布局](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3C94CA89-F43E-4A0A-B41C-102FCEAF8F7B.htm)。

根据“控制”(Controls)选项卡（全身、手和脚）和“自定义绑定”(Custom Rig)选项卡（全身、脊椎和颈部）中的视图构建配置文件：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-783CC8B1-3032-47D8-A8B1-AE476002602E.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

## 打开角色控制配置文件

打开配置文件以便您可以对其进行编辑

1. 在文本或 XML 编辑器中，导航到：

  - **Windows**：C:\Program Files\Autodesk\<Maya 版本>\resources\CharacterControls

  - **Mac OS X**：/Applications/Autodesk/<Maya 版本>/Maya.app/Contents/resources/CharacterControls

  - **Linux**：/usr/autodesk/Maya/resources/CharacterControls

  **注**

  默认情况下，在安装期间 CharacterControlsConfig.xml 和 CustomRigControlsConfig.xml 在此目录中创建。这些文件用于创建“控制”(Controls)和“自定义绑定”(Custom Rig)选项卡的默认布局。

2. 选择要编辑的配置文件。

  **注**

  每次在外部编辑器中编辑配置文件时，都必须在

  Maya

  中加载该文件才能看到所做的更改。请参见

  保存并加载 HumanIK 角色布局

  。

## HumanIK 角色控制配置文件描述

下图显示了 CharacterControlsConfig.xml 文件中的全身视图并亮显其主区域和元素。

有关如何更改此文件的说明，请参见[编辑 HumanIK 角色控制配置文件](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-3C94CA89-F43E-4A0A-B41C-102FCEAF8F7B.htm)。

**注**

CustomRigControlsConfig.xml

文件包含相同的主元素。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-E5F5D4F0-290F-458E-A84C-16BB5FF8AA8E.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

### 主元素

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-9C67C4C2-9408-4BB9-AB56-A391EFAAD79D.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

配置文件中的每个部分都使用以下资源元素，例如 <View resource="FullBody">：对应于特定于全身的资源，<View resource="LeftHand">：对应于特定于左手的资源，<View resource="RightFoot">：对应于特定于右脚的资源，等等。

如果要使用存储在非默认位置的图像，需要修改相应的资源元素，使其指向正确的文件夹。请参见

| 元素 | 说明 |
|---|---|
| <ResourcePath> | 标识包含图像资源的目录。 |
| <View resource> | 包含视图的所有元素并标识背景图像。 |

### 定位点

配置文件基于定位点、二维 X 和 Y 坐标（用于定义布局中其他元素的位置）的概念构建。 定位点已链接到其他元素。因此，定位点坐标确定这些元素在布局中的位置。

您可以向定位点附加导航器资源或 IK 效应器。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-C2D9DFF6-1B94-4918-A83C-ABC5373BC283.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

| 属性 | 说明 |
|---|---|
| <name> | 为定位点提供一个名称。 |
| <x> | 定位点的 X 坐标。 |
| <y> | 定位点的 Y 坐标。 |

### 导航器资源

导航器资源表示用于在布局中打开一个不同视图的按钮。例如，向下箭头 ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-5F3CFCD8-AB75-4028-9FEB-27DF5D127EC5.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->，用于展开以查看角色布局的详细分段，如手或脚。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-60E23320-E3D5-4145-AB14-5F0E03B7297B.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

| 属性 | 说明 |
|---|---|
| <name> | 为该导航器资源提供一个名称。 |
| <goto> | 此数字标识已连接到导航器资源的视图。 |
| <layer> | 此数字与指定给导航器资源的层对应。 提示： 分层系统可以让您在布局中将不同的元素彼此层叠。 |
| <resource> | 用于导航器资源的图像的名称。 |
| <tooltip> | 导航器资源的注释文本。当您将光标悬停在布局中的导航器按钮上方时会显示此文本。 |

### IK 效应器

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-5BD3AC0A-F899-441B-BB53-5230119372E6.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

| 属性 | 说明 |
|---|---|
| <anchor> | 标识定义 IK 效应器位置的定位点。 |
| <body_part> | 标识 IK 效应器的身体部位关键帧组。例如，左腿、右腿、右臂或左臂。请参见[操纵和关键帧模式](“控制”%28Controls%29选项卡/“控制”%28Controls%29选项卡工具栏.md#GUID-735DF85A-331C-4049-8C70-E53EFCDB4B73__SECTION_448E393B3A904F939192EF2FA4C7EF0B)。 |
| <id> | IK 效应器的内部 ID。 |
| <layer> | 此数字与指定给 IK 效应器的层对应。 |
| <resource> | 用于 IK 效应器的图像的名称。 |
| <tooltip> | IK 效应器的注释文本。当您将光标悬停在布局中的 IK 效应器上方时会显示此文本。 |

您可以向 IK 效应器附加效应器控制柄。<Expander> 元素具有以下属性：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-8FB90A40-4872-425E-BA4C-C06EDF6C0205.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

| 属性 | 说明 |
|---|---|
| <anchor> | 标识定义效应器控制柄位置的定位点。 |
| <item_offset> | 此数字表示附加效应器控制柄和第一个附加效应器之间的偏移（以像素为单位）。 |
| <direction> | 指示控制柄在哪个方向展开：上、下、右或左。 |
| <max_shown> | 设置可以添加到展开的控制柄的附加效应器的最大数目。 |
| <resource> | 用于效应器控制柄的图像的名称。 |
| <layer> | 此数字与指定给 IK 效应器的层对应。 |

### FK 效应器

FK 效应器是程序效应器，且不基于图像。使用两个定位点来定义效应器的起点和终点。

**注**

提示：

您可以通过将 FK 效应器附加到与 IK 效应器相同的定位点来重用定位点。这样，当 IK 效应器移动时，FK 效应器也会随之移动。以下示例将重用

ikRWrist0

定位点，该定位点也在上述 IK 效应器定义中使用。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-CD6FA4D7-A5C9-4765-9500-2948895B877A.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

| 属性 | 说明 |
|---|---|
| <anchor1> | 在布局中定义效应器开始位置的定位点。 |
| <anchor2> | 在布局中定义效应器结束位置的定位点。 |
| <body_part> | FK 效应器的身体部位关键帧组。例如，左腿、右腿、右臂、左臂。请参见[操纵和关键帧模式](“控制”%28Controls%29选项卡/“控制”%28Controls%29选项卡工具栏.md#GUID-735DF85A-331C-4049-8C70-E53EFCDB4B73__SECTION_448E393B3A904F939192EF2FA4C7EF0B)。 |
| <id> | 此数字是指定给 FK 效应器的内部 ID。 |
| <layer> | 此数字与指定给 FK 效应器的层对应。 |
| <tooltip> | FK 效应器的注释文本。当您将光标悬停在布局中的 FK 效应器上方时会显示此文本。 |

### 按钮

CustomRigControlsConfig.xml 文件中使用 <Button> 元素，而不是 <IK> 元素，但二者有很多相同的属性：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-42BBE341-1867-4BCD-B88B-FBB5C57C2E1D.png) <!-- baize:img-hook downloaded=false reason="正文 2624 字 ≥300，非承重" -->

| 属性 | 说明 |
|---|---|
| <anchor> | 标识定义按钮位置的定位点。 |
| <id> | 按钮的内部 ID。 |
| <layer> | 此数字与指定给按钮的层对应。 |
| <resource> | 单元未被选中时使用的图像。请参见[单元状态](“自定义装备”%28Custom%20Rig%29选项卡/“自定义装备”%28Custom%20Rig%29角色表示.md#GUID-79F46233-F567-4F7E-87AE-716609F6DED1__SECTION_31E9A907CB9A4178A6FA20CE1F6A6BCD)。 |
| <resource_selected> | 单元被选中时使用的图像。请参见[单元状态](“自定义装备”%28Custom%20Rig%29选项卡/“自定义装备”%28Custom%20Rig%29角色表示.md#GUID-79F46233-F567-4F7E-87AE-716609F6DED1__SECTION_31E9A907CB9A4178A6FA20CE1F6A6BCD)。 |
| <resource_active> | 单元被指定时使用的图像。请参见[单元状态](“自定义装备”%28Custom%20Rig%29选项卡/“自定义装备”%28Custom%20Rig%29角色表示.md#GUID-79F46233-F567-4F7E-87AE-716609F6DED1__SECTION_31E9A907CB9A4178A6FA20CE1F6A6BCD)。 |
| <tooltip> | 按钮的注释文本。当您将光标悬停在布局中的按钮上方时会显示此文本。 |
