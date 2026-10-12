# 子集衰减属性(Subset Falloff Attributes)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-57E9DA6F-DB97-48FB-859F-5FA7A7471DF8.png) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->

在“子集衰减”(Subset Falloff)的“属性编辑器”(Attribute Editor)部分，您可以调整各种特性以控制子集衰减的效果。

访问“子集衰减”(Subset Falloff)的“属性编辑器”(Attribute Editor)构件

- [将变形器衰减应用于几何体](../创建变形器衰减.md)后，在“属性编辑器”(Attribute Editor)的[“变形器属性”(Deformer Attributes)构件](../变形器属性构件.md)中选择“创建子集衰减”(Create Subset Falloff)。在[变形器属性(Deformer Attributes)](../变形器属性构件.md)表的“衰减”(Falloff)列的“子集衰减”(Subset Falloff)单元格中，双击“子集衰减”(Subset Falloff)以切换到“子集衰减属性”(Subset Falloff Attributes)。

#### 使用衰减标记(Use Falloff Tags)

启用此选项后，可使用组件标记定义衰减效果。如果此选项处于非活动状态，则变形将应用于整个几何体。

#### 衰减标记(Falloff Tags)

键入组件标记的名称以定义衰减效果。可以在此字段中使用正则表达式。按 **Enter** 键以应用选择。

如果要确保标记不被更改，请在此字段上单击鼠标右键，然后选择**“锁定属性”(Lock Attribute)**。

#### 在边界内(Within Boundary)

启用此选项后，可在指定标记的限制范围之内或之外约束衰减效果。

![图：启用此选项后，可在指定标记的限制范围之内或之外约束衰减效果。 在立方体的右侧组件标记上切换“在边界内”(Within B…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-C66C5785-095C-47C9-A525-F0AD3F5D5CDD.gif) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->

在立方体的右侧组件标记上切换“在边界内”(Within Boundary)设置。

在“在边界内”(Within Boundary)选项上单击鼠标右键以进行更多选择：

| 选项 | 功能 |
|---|---|
| subsetFalloff_withinboundary.output | 在“属性编辑器”(Attribute Editor)中创建 *subsetFalloff_withinboundary* 构件，您可以在其中调整动画曲线。 |
| **创建新表达式** | 打开[表达式编辑器(Expression Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)，以便创建表达式。 |
| **设置关键帧(Set Key)** | 在由“当前时间指示器”(Current Time Indicator)显示的动画点处，设置关键帧。 |
| **设置受驱动关键帧...(Set Driven Key...) ** | 打开[设置受驱动关键帧(Set Driven Key)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2B1C7EF-F177-4B0E-9E41-B479CFF2AFD4)窗口，以便让属性驱动另一个对象的属性。 |
| 断开连接(Break Connection) | 移除关键帧以及与属性的所有连接。 |
| **锁定属性 ** | 冻结设置，以便无法对其进行更改。 |

#### 使用原始几何体(Use Original Geometry)

使用对象的[原始几何体](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EEF323A6-8692-4D74-8EAA-5481BF437D42.htm)作为变形的影响物。

在“使用原始几何体”(Use Original Geometry)选项上单击鼠标右键以进行更多选择：

| 选项 | 功能 |
|---|---|
| **创建新表达式** | 打开[表达式编辑器(Expression Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)，以便创建表达式。 |
| **设置关键帧(Set Key)** | 在由“当前时间指示器”(Current Time Indicator)显示的动画点处，设置关键帧。 |
| **设置受驱动关键帧...(Set Driven Key...) ** | 打开[设置受驱动关键帧(Set Driven Key)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2B1C7EF-F177-4B0E-9E41-B479CFF2AFD4)窗口，以便让属性驱动另一个对象的属性。 |
| **锁定属性(Lock Attribute) ** | 锁定权重值。Maya 会用灰色背景显示已锁定的属性。 若要解除锁定，请单击鼠标右键，然后选择“解除锁定属性”(Unlock Attribute)。 |

#### 模式(Mode)

选择子集定义衰减的方式：

| 选项 | 功能 |
|---|---|
| **连接** | 根据网格拓扑（而非距离），使用连接级别定义衰减效果。 |
| **体积(Volume)** | 使用对象空间定义衰减效果的距离。 |

#### 开始/结束(Start/End)

用于定义衰减效果的开始和结束，反映在所选组件标记和缩放设置中。

在“开始/结束”(Start/End)字段上单击鼠标右键以进行更多选择：

| 选项 | 功能 |
|---|---|
| **创建新表达式** | 打开[表达式编辑器(Expression Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-251640EA-AACC-4F1B-A341-297F0F4CEFE4)，以便创建表达式。 |
| **设置关键帧(Set Key)** | 在由“当前时间指示器”(Current Time Indicator)显示的动画点处，设置关键帧。 |
| **设置受驱动关键帧...(Set Driven Key...) ** | 打开[设置受驱动关键帧(Set Driven Key)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D2B1C7EF-F177-4B0E-9E41-B479CFF2AFD4)窗口，以便让属性驱动另一个对象的属性。 |
| **创建新纹理...(Create new texture...)** | 打开[“创建渲染节点”(Create Render Node)窗口](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4918C294-FAAD-45B5-A896-92161177EEED)，以便向衰减添加新的纹理节点。 |
| **锁定属性 ** | 冻结设置，以便无法对其进行更改。 |

#### 缩放

使衰减效果倍增。

![图：使衰减效果倍增。 在立方体的右侧组件标记上调整“缩放”(Scale)设置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/images/GUID-E7AF3E7B-209F-4581-8183-20066805C65F.gif) <!-- baize:img-hook downloaded=false reason="正文 1832 字 ≥300，非承重" -->

在立方体的右侧组件标记上调整“缩放”(Scale)设置。
