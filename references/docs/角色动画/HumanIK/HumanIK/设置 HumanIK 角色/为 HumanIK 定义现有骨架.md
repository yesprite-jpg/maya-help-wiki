# 为 HumanIK 定义现有骨架

完成角色映射过程主要有两种方法，具体取决于是否为角色的骨骼使用标准命名约定。

对于这两种方法，您可以按如下方式做好准备：

1. 加载骨架。在尝试创建定义之前，请确保已遵循[为 HumanIK 准备现有骨架](为%20HumanIK%20准备现有骨架.md)中的指导方针，并且已按照 [HumanIK 角色结构](../HumanIK%20角色结构.md)中所述的内容对角色进行设置。

2. 打开 [HumanIK 窗口](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-9921EDE1-05E2-4062-9F0D-4BADECA29226.htm)（“窗口 > 动画编辑器 > HumanIK”(Windows > Animation Editors > HumanIK)），然后单击[“开始”(Start)窗格](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-708BB8DD-C29F-4112-8704-730716E538C9.htm)中的“创建角色定义”(Create Character Definition)。

3. （可选）要重命名角色，请单击 ![图：（可选）要重命名角色，请单击 “重命名角色”(Rename Character)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-39B60BBD-A9DF-46CA-8078-B4277C4CD703.png) <!-- baize:img-hook downloaded=false reason="正文 1660 字 ≥300，非承重" --> >“重命名角色”(Rename Character)。

4. 请选择下列方法之一来映射角色的结构：

  - [手动映射骨骼](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-33859AA1-887B-4F8A-8360-F881C28EF351.htm#GUID-33859AA1-887B-4F8A-8360-F881C28EF351__WS1A9193826455F5FF219F8B8B1249CF2CB82-5295)

  - [根据命名模板自动映射骨骼](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-33859AA1-887B-4F8A-8360-F881C28EF351.htm#GUID-33859AA1-887B-4F8A-8360-F881C28EF351__GUID-BB662CCD-59E5-48F9-A933-3F14C4D0B560)

手动映射骨骼

1. 请执行下列操作之一以开始将骨骼映射到[“角色”(Character)视图](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C3ECEC71-6AE0-4DC9-8149-2EFD86F12FA9.htm)：

  - 从“定义”(Definition)选项卡转到骨架：在**“角色”(Character)**视图中双击单元（单元在单击时将变为蓝色），然后单击场景中对应的骨骼。（例如，您还可以在“大纲视图”(Outliner)或“Hypergraph”中选择骨骼。）

  - 从骨架转到“定义”(Definition)选项卡：选择骨骼，然后在**“角色”(Character)**视图中的相应单元上单击鼠标右键，然后选择“指定选定骨骼”(Assign Selected Bone)。

    **“角色”(Character)**视图中的骨骼将变为绿色，以指示每个有效的骨骼指定。

  有关哪些骨骼映射到哪些节点的详细信息，请参见 [HumanIK 角色结构](../HumanIK%20角色结构.md)。

  **注**

  提示：

  如果已使用标准的左/右命名约定并启用

  “镜像匹配”(Mirror Matching)

  选项，且映射（例如）右腿的骨骼，该工具将自动映射左腿的骨骼。另请参见

  配置镜像匹配

  和

  激活并配置镜像匹配

  。

  继续映射，直到定义完所有需要的骨骼为止。映射所有需要的骨骼之后，[验证状态](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C3ECEC71-6AE0-4DC9-8149-2EFD86F12FA9.htm#GUID-C3ECEC71-6AE0-4DC9-8149-2EFD86F12FA9__SECTION_C7453CA20E144C6FA494686CA1B95BBE)指示器将变为绿色。

  ![图：请执行下列操作之一以开始将骨骼映射到“角色”(Character)视图： 从“定义”(Definition)选项卡转到骨…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-8917065C-B91B-4F6C-A022-734BC12406C3.png) <!-- baize:img-hook downloaded=false reason="正文 1660 字 ≥300，非承重" -->

2. （可选）展开**“角色”(Character)**视图的附加区域，可以映射其他可选关节（如其他脊椎关节或侧滚骨骼）。

3. （可选）映射引用骨骼。

  **注**

  映射引用对象是可选操作，但强烈建议执行该操作。

  若要快速创建引用对象，请创建一个定位器（创建 > 定位器(Create > Locator)），并将该定位器设置为角色骨架层级的根的父对象。然后，您可以将该定位器映射为角色的“引用”(Reference)。

根据命名模板自动映射骨骼

1. 选择要指定的第一个骨骼。

2. 单击“定义”(Definition)选项卡工具栏中的**“加载骨架定义”(Load Skeleton Definition)**按钮 ![图：单击“定义”(Definition)选项卡工具栏中的“加载骨架定义”(Load Skeleton Definition)…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-EDB5F6E6-B284-4BE8-8E62-1A8EFC54A1FD.png) <!-- baize:img-hook downloaded=false reason="正文 1660 字 ≥300，非承重" -->。

3. 在出现的[“加载骨架定义”(Load Skeleton Definition)窗口](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-866266D0-2CB4-4FBA-9490-F7FEFE4482D9.htm)中，从“模板”(Template)下拉列表中选择要应用的命名模板。

  默认情况下，该列表包含“HumanIK”提供的所有模板以及已创建的任何模板。若要导航并选择未列出的模板，请选择 <“浏览”(Browse)>。

  例如，如果角色关节是根据 HumanIK 命名约定（在[名称匹配](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-C3ECEC71-6AE0-4DC9-8149-2EFD86F12FA9.htm#GUID-C3ECEC71-6AE0-4DC9-8149-2EFD86F12FA9__SECTION_8CD666A1D45C4DF7A2A6AB04A89624E5)视图中已列出）命名的，则可以使用 HIK 模板自动完成映射过程。

  **注**

  提示：

  您也可以选择

  >

  “编辑 > 编辑角色定义 > 加载角色定义模板”(Edit > Edit Character Definition > Load Character Definition Template)

  以应用您自己的命名模板。

4. （可选）如果要限制模块仅与与骨架中的骨骼子集匹配，请选择这些骨骼。

5. 设置名称匹配的范围。

  选择“使用前缀匹配所有骨骼”(Match all bones with prefix)选项，可以映射其名称中包含该字段中显示的前缀以及映射模板中所含后缀的所有骨骼。建议的前缀是从选定的骨骼中获取的。如果建议的前缀与要定义的骨架使用的前缀不匹配，则可以更改该前缀。选择“仅匹配选定的骨骼”(Match only selected bones)选项，以限制后缀仅与选定的骨骼匹配。

6. 单击“确定”(Ok)。

## 相关主题

- [“定义”(Definition)选项卡](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-630B5349-213C-414D-B6C9-D283CE319472.htm)

- [创建 HumanIK 骨架定义](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-AC690ECF-D5B7-4759-AD71-C1FEFD7CF7A8.htm)

- [“HumanIK”窗口](../../HumanIK.md)
