# “关键帧”(Key)菜单

位于“动画”(Animation)菜单集中。

有关设置关键帧的信息，请参见[设置关键帧](../../../关键帧动画/关键帧动画/设定关键帧.md)和[使用自动关键帧](../../../关键帧动画/关键帧动画/设定关键帧/使用自动关键帧.md)。

## 设置(Set)

#### 设置关键帧(Set Key)

在时间轴中当前时间指示器所在的时间位置插入关键帧。

如果在“设置关键帧”(Set Key)选项中启用“设置 IK/FK 关键帧”(Set IK/FK Keys)，则随后可以将“关键帧 > 设置关键帧”(Key > Set Key)用作“关键帧 > IK/FK 关键帧 > 设置 IK/FK 关键帧”(Key > IK/FK Keys > Set IK/FK Key)的一种替代方法。（如果对不是 IK 控制柄的对象、由 IK 控制柄控制的关节或连接到 IK 控制柄的对象选择“关键帧 > 设置关键帧”(Key > Set Key)，则会忽略“设置 IK/FK 关键帧”(Set IK/FK Keys)选项。）

选择“关键帧 > 设置关键帧”(Key > Set Key) > ![图：选择“关键帧 设置关键帧”(Key Set Key) ，以设置设置关键帧选项(Set Key Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> ，以设置[设置关键帧选项(Set Key Options)](“关键帧”%28Key%29菜单/设置关键帧选项%28Set%20Key%20Options%29.md)。

#### 设置动画关键帧(Set Key on Animated)

使用此选项可在已有关键帧的通道上以独占方式设置关键帧。

#### 设置平移/旋转/缩放关键帧(Set Key on Translate/Rotate/Scale)

使用这些选项可在选定对象的 X、Y 和 Z 平移通道上，在当前时间添加常规关键帧。

#### 设置受控关键点关键帧(Set Breakdown Key)

有关“受控关键点”(Breakdowns)的详细信息，请参见[受控关键点](../../../关键帧动画/关键帧动画/受控关键点.md)。

**注**

没有任何相邻关键帧的“受控关键点”(Breakdowns)未绑定。当您放置、编辑和移动时，这些受控关键点的表现方式类似于常规关键帧。

选择“关键帧 > 设置受控关键点关键帧”(Key > Set Breakdown Key) > ![图：选择“关键帧 设置受控关键点关键帧”(Key Set Breakdown Key) ，以设置设置受控关键点选项(Set …](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> ，以设置[设置受控关键点选项(Set Breakdown Options)](../../../关键帧动画/关键帧动画/受控关键点/设置受控关键点/“设置受控关键点”%28Set%20Breakdown%29选项.md)。

#### 设置受驱动关键帧(Set Driven Key)

此菜单包括“设置”(Set)、“转到上一个”(Go to Previous)和“转到下一个”(Go to Next)选项。

单击“设置”(Set)选项可显示[“设置受驱动关键帧”(Set Driven Key)窗口](../../../关键帧动画/关键帧动画/受驱动关键帧/“设置受驱动关键帧”%28Set%20Driven%20Key%29窗口.md)。请参见[使用“设置受驱动关键帧”(Set Driven Key)来链接属性](../../../关键帧动画/关键帧动画/设定关键帧/使用“设置受驱动关键帧”%28Set%20Driven%20Key%29来链接属性.md)。

单击“转到上一个”(Go to Previous)和“转到下一个”(Go to Next)选项可针对当前对象的受驱动属性循环所有关键帧，并在每个关键帧上查看对象的状态。另请参见[使用“设置受驱动关键帧”(Set Driven Key)来链接属性](../../../关键帧动画/关键帧动画/设定关键帧/使用“设置受驱动关键帧”%28Set%20Driven%20Key%29来链接属性.md)和[查看受驱动关键帧关系](../../../关键帧动画/关键帧动画/受驱动关键帧/查看受驱动关键帧关系.md)。

#### 设置融合变形目标权重关键帧(Set Blend Shape Target Weight Keys)

为当前融合形变变形的目标形状融合变形权重设置关键帧。

选定该菜单项时，可以执行以下操作：

- 如果仅选定了基本形状，将对其所有目标形状权重设置关键帧。

- 如果仅选定了目标形状，将对选定目标形状的权重设置关键帧。

- 如果选定了基础形状和目标形状，将仅对选定目标形状的权重设置关键帧。

另请参见[设置绘制的融合变形权重的动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-950716A4-19CF-4C14-96F1-FD6B4D48663C)。

## 插入(Insert)

#### 插入关键帧(Insert Key)

在当前时间插入固定关键帧，同时保留曲线形状和关键帧在任意一侧的切线形状。如果在“曲线图编辑器”(Graph Editor)中未选择任何内容，并且选择了“插入关键帧”(Insert Key)，则将在视口中选定对象的每个通道上的当前时间插入固定关键帧。如果在“曲线图编辑器”(Graph Editor)中选择了曲线或关键帧，并且选择了“插入关键帧”(Insert Key)，则将在当前时间在选定关键帧上插入固定关键帧。热键：Alt + I

#### 在平移时插入关键帧(Insert Key on Translate)

在平移通道上的当前时间插入固定关键帧，同时保留曲线形状和关键帧在任意一侧的切线形状。如果在“曲线图编辑器”(Graph Editor)中未选择任何内容，并且选择了“在平移时插入关键帧”(Insert Key on Translate)，则将在视口中选定对象的每个平移通道上的当前时间插入固定关键帧。如果在“曲线图编辑器”(Graph Editor)中选择了曲线或关键帧，并且选择了“在平移时插入关键帧”(Insert Key on Translate)，则在当前时间在选定曲线上插入固定关键帧。热键：Ctrl + Shift + W

#### 在旋转时插入关键帧(Insert Key on Rotate)

在旋转通道上的当前时间插入固定关键帧，同时保留曲线形状和关键帧在任意一侧的切线形状。如果在“曲线图编辑器”(Graph Editor)中未选择任何内容，并且选择了“在旋转时插入关键帧”(Insert Key on Rotate)，则将在视口中选定对象的每个旋转通道上的当前时间插入固定关键帧。如果在“曲线图编辑器”(Graph Editor)中选择了曲线或关键帧，并且选择了“在旋转时插入关键帧”(Insert Key on Rotate)，则在当前时间在选定曲线上插入固定关键帧。热键：Ctrl + Shift + E

#### 在缩放时插入关键帧(Insert Key on Scale)

在缩放通道上的当前时间插入固定关键帧，同时保留曲线形状和关键帧在任意一侧的切线形状。如果在“曲线图编辑器”(Graph Editor)中未选择任何内容，并且选择了“在缩放时插入关键帧”(Insert Key on Scale)，则将在视口中选定对象的每个缩放通道上的当前时间插入固定关键帧。如果在“曲线图编辑器”(Graph Editor)中选择了曲线或关键帧，并且选择了“在缩放时插入关键帧”(Insert Key on Scale)，则在当前时间在选定曲线上插入固定关键帧。热键：Ctrl + Shift + R

## 编辑(Edit)

#### 剪切(Cut)

剪切当前关键帧并将其存储在虚拟关键帧剪贴板中。

选择“关键帧 > 剪切”(Key > Cut) > ![图：剪切当前关键帧并将其存储在虚拟关键帧剪贴板中。 选择“关键帧 剪切”(Key Cut) 以打开“剪切关键帧选项”(Cut…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开“剪切关键帧选项”(Cut Keys Options)窗口。此窗口除了包含[复制关键帧选项(Copy Keys Options)](“关键帧”%28Key%29菜单/复制关键帧选项%28Copy%20Keys%20Options%29.md)窗口中的相同选项外，还包含：

| 调整(Adjustment) | 指定在剪切关键帧集之后如何将其复制到关键帧剪贴板（“分段”(Segments)启用时可用）。 |
|---|---|
| 无(None) | 指定剪切处于指定范围内的关键帧。如果存在仍与已删除区域的两端相邻的关键帧，那么产生的动画曲线将在剪切区域中保留关键帧的出切线和入切线。 |
| 收拢(Collapse) | 指定移除指定范围内的关键帧。会将在剪切之前的所有关键帧移动到剪切区域的开始时间，从而有效地向前缓慢移动动画曲线以填充产生的间距。 |
| 连接(Connect) | 调整关键帧剪贴板曲线值，并调整跟随已粘贴分段的原始曲线的分段。这样可防止动画中的不连续（启用“收拢”(Collapse)时可用）。 |

#### 复制(Copy)

将当前关键帧复制到虚拟剪贴板。请参见[复制和粘贴关键帧](../../../关键帧动画/关键帧动画/编辑关键帧/复制并粘贴关键帧.md)和[剪切关键帧](../../../关键帧动画/关键帧动画/编辑关键帧/剪切关键帧.md)。

选择“关键帧 > 复制”(Key > Copy) > ![图：选择“关键帧 复制”(Key Copy) 以打开复制关键帧选项(Copy Keys Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开[复制关键帧选项(Copy Keys Options)](“关键帧”%28Key%29菜单/复制关键帧选项%28Copy%20Keys%20Options%29.md)。

#### 粘贴(Paste)

将当前位于虚拟剪贴板中的关键帧粘贴到当前时间指示器所在的时间线。选择“关键帧 > 粘贴”(Key > Paste) > ![图：将当前位于虚拟剪贴板中的关键帧粘贴到当前时间指示器所在的时间线。选择“关键帧 粘贴”(Key Paste) 以打开粘贴关…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开[粘贴关键帧选项(Paste Key options)](“关键帧”%28Key%29菜单/粘贴关键帧选项%28Paste%20Key%20Options%29.md)。

#### 删除(Delete)

删除当前关键帧。选择“关键帧 > 删除”(Key > Delete) > ![图：删除当前关键帧。选择“关键帧 删除”(Key Delete) 以打开删除关键帧选项(Delete Key Options…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开[删除关键帧选项(Delete Key Options)](“关键帧”%28Key%29菜单/删除关键帧选项%28Delete%20Keys%20Options%29.md)。

#### 缩放(Scale)

使用“缩放关键帧选项”(Scale Keys Options)窗口中的设置缩放当前关键帧。选择“关键帧 > 缩放关键帧”(Key > Scale Keys) > ![图：使用“缩放关键帧选项”(Scale Keys Options)窗口中的设置缩放当前关键帧。选择“关键帧 缩放关键帧”(K…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开并编辑[缩放关键帧选项(Scale Key Options)](“关键帧”%28Key%29菜单/缩放关键帧选项%28Scale%20Keys%20Options%29.md)。

#### 捕捉(Snap)

使用“捕捉关键帧选项”(Snap Keys Options)窗口中的设置捕捉当前关键帧。选择“关键帧 > 捕捉”(Key > Snap) > ![图：使用“捕捉关键帧选项”(Snap Keys Options)窗口中的设置捕捉当前关键帧。选择“关键帧 捕捉”(Key S…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开并编辑[捕捉关键帧选项(Snap Key Options)](“关键帧”%28Key%29菜单/捕捉关键帧选项%28Snap%20Keys%20Options%29.md)。

#### 烘焙动画(Bake Animation)

烘焙当前模拟。选择“关键帧 > 烘焙动画”(Key > Bake Animation) > ![图：烘焙当前模拟。选择“关键帧 烘焙动画”(Key Bake Animation) 以打开并编辑烘焙模拟选项(Bake Si…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开并编辑[烘焙模拟选项(Bake Simulation Options)](“关键帧”%28Key%29菜单/烘焙模拟选项%28Bake%20Simulation%20Options%29.md)。

#### 保持当前关键帧(Hold Current Keys)

“保持当前关键帧”(Hold Current Keys)在当前为选定对象的所有动画属性设置关键帧。此菜单项对“自动关键帧”(Auto Key)最有用，因为“自动关键帧”(Auto Key)只对更改值的属性设置关键帧。详细信息请参见[使用自动关键帧保持当前关键帧](../../../关键帧动画/关键帧动画/设定关键帧/使用自动关键帧.md)。

例如，假设您正在为角色的周期行走制作动画。如果脚踩在地上，其位置必须占几帧。如果单独使用“自动关键帧”(Auto Key)，必须更改值才能设置关键帧。尽管值不变，“保持当前关键帧”(Hold Current Keys)也会为脚设置关键帧。

#### IK/FK 关键帧(IK/FK Keys)

此菜单包括“设置 IK/FK 关键帧”(Set IK/FK Key)、“启用 IK 解算器”(Enable IK Solver)、“连接到 IK/FK”(Connect to IK/FK)和“将 IK 移动到 FK”(Move IK to FK)选项。有关这些选项的详细信息，请参见 [IK/FK 关键帧(IK/FK Keys)菜单](“关键帧”%28Key%29菜单/“IKFK%20关键帧”%28IKFK%20Keys%29菜单.md)。

## 角色集

#### 创建角色集(Create Character Set)

创建一个[角色集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-39A5A681-1BB8-41BA-8139-95E16111B297)。选择“关键帧 > 创建角色集”(Key > Create Character Set) > ![图：创建一个角色集。选择“关键帧 创建角色集”(Key Create Character Set) 以打开创建角色集选项(C…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以打开[创建角色集选项(Create Character Set Options)](“关键帧”%28Key%29菜单/创建角色集选项%28Create%20Character%20Set%20Options%29.md)。另请参见[创建角色集](../../../Maya%20中的非线性动画/Maya%20中的非线性动画/Trax%20编辑器/创建、加载和亮显角色集/创建角色集%28Create%20character%20sets%29.md)。

#### 创建子角色集(Create Subcharacter Set)

可以在以前定义的角色集内创建子角色集。创建子角色集时，Maya 将子角色集添加到当前角色集内。该功能非常有用，因为您可以将 Maya 的角色动画功能的效果应用于角色的部分层级中。

创建子角色集类似于创建角色集：选择您要定义为子角色集的角色对象（例如，构成角色的面的对象），然后选择“关键帧 > 创建子角色集”(Key > Create Subcharacter Set) > ![图：创建子角色集类似于创建角色集：选择您要定义为子角色集的角色对象（例如，构成角色的面的对象），然后选择“关键帧 创建子角色…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 。子角色的创建选项与创建角色的选项相同。请参见[创建子角色集选项(Create Subcharacter Set Options)](“关键帧”%28Key%29菜单/创建子角色集选项%28Create%20Subcharacter%20Set%20Options%29.md)。

#### 角色映射器(Character Mapper)

打开[“角色映射器”(Character Mapper)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-20015023-4D8F-4D09-8F82-15D3A80A1554)。

#### 属性编辑器(Attribute Editor)

打开[属性编辑器(Attribute Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-67A58D31-4722-4769-B3E6-1A35B5B53BED)。

#### 添加到角色集(Add to Character Set)

将选定属性添加到当前的角色集或子角色集。

#### 从角色集中移除(Remove from Character Set)

从当前角色或子角色集中移除选定的属性。

#### 合并角色集(Merge Character Sets)

组合或*合并*选定角色或子角色集。

#### 选择角色集节点(Select Character Set Node)

请参见[选择角色集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7BC4C0A4-0B4E-490F-861F-2E96029EEE08)。

#### 选择角色集成员(Select Character Set Members)

请参见[选择角色集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7BC4C0A4-0B4E-490F-861F-2E96029EEE08)。

#### 选择当前角色集(Select Current Character Set)

请参见[选择角色集](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7BC4C0A4-0B4E-490F-861F-2E96029EEE08)。

#### 重定向(Redirect)

将平移和/或旋转重定向控制添加到当前角色。这些控制将显示在角色原点处。当角色可重定向时，可以更改已创建（例如，运动捕捉）动画的平移和方向。

请参见[重定向角色动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C3DF9BF0-2B41-4A3A-B760-1679D7132515)和[重定向动画角色的运动](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D7EA1F16-4EB2-48C0-8833-82E7A2C54BA0)。

选择“关键帧 > 重定向”(Key > Redirect) > ![图：选择“关键帧 重定向”(Key Redirect) 以查看角色重定向选项(Character Redirection O…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 4703 字 ≥300，非承重" --> 以查看[角色重定向选项(Character Redirection Options)](“关键帧”%28Key%29菜单/角色重定向选项%28Character%20Redirection%20Options%29.md)窗口。

## 时间(Time)

#### 场景时间扭曲(Scene Time Warp)

此菜单提供了用于添加、选择、删除和编辑场景时间扭曲曲线的选项。

有关这些选项的详细信息，请参见[场景时间扭曲(Scene Time Warp)菜单](“关键帧”%28Key%29菜单/“场景时间扭曲”%28Scene%20Time%20Warp%29菜单.md)。
