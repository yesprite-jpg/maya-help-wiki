# “摄影表”(Dope Sheet)工具栏

## 选择关键帧工具(Select Keyframe Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-3585A107-40FC-42DE-B683-35120B098F17.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

可以使用“选择关键帧工具”(Select Keyframe Tool)，管理“摄影表”(Dope Sheet)中的时间。使用“选择关键帧工具”(Select Keyframe Tool)，可以放置和创建“摄影表操纵器”(Dope Sheet Manipulator)。“摄影表操纵器”(Dope Sheet Manipulator)可用于“摄影表”(Dope Sheet)中选择、移动、缩放、复制、剪切和粘贴时间的空白区域以及包含关键帧的时间区域。该工具适用于移动、缩放、禁用、添加或删除时间区域和关键帧，以及使动画的其他部分移动，以适应时间和关键帧的添加或删除。例如，如果对某个时间区域和关键帧进行剪切，那么动画中的其余时间和关键帧将移动以填充剪切造成的间隙。当稍后粘贴时间和关键帧时，动画将移动以便为粘贴时间和关键帧留出空间。

## 移动最近拾取的关键帧工具(Move Nearest Picked Key Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-67040CD9-FC83-4728-988C-5DD4888CC31A.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该工具可用于使用单一鼠标动作快速操纵单个关键帧和切线。

与“移动工具”(Move Tool)不同，该工具一次只能在一个关键帧上进行操作。无需在图表视图精确地选择关键帧或切线控制柄，即可对活动曲线上最近选定的关键帧进行操作。

### “移动最近拾取的关键帧工具设置”(Move Nearest Picked Key Tool Settings)窗口

双击“移动最近拾取的关键帧工具”(Move Nearest Picked Key Tool)图标，以打开该工具的“工具设置”(Tool Settings)窗口。

直接关键帧选项(移动选项) (DirectKey Options (Move Option))

设定下列选项之一：

#### 仅移动(MoveOnly)

禁用“移动最近拾取的关键帧”(Move Nearest Picked Key)工具的应用，以整个扫描曲线的关键帧（请参见下面的“移过”(MoveOver)）。

#### 移过(MoveOver)

默认设置为启用该工具以沿曲线的关键帧扫描整个活动曲线，从而促进动画曲线的微调。

## 插入关键帧工具(Insert Keys Tool)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-02DF1766-6F61-4938-89C2-F8E485910316.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

选择“插入关键帧工具”(Insert Keys Tool)，以便将新的关键帧放置到现有动画曲线上。若要选择新关键帧要添加到的曲线，请单击曲线。

使用鼠标中键沿动画曲线进行拖动，以确定新关键帧的位置。释放鼠标键时，将放置关键帧。

新的关键帧拥有保留原始动画曲线分段形状的切线。

## “统计信息”(Stats)字段

“统计信息”(Stats)字段以数字表示选定关键帧的时间和值。可使用键盘输入值以明确地进行编辑，或者通过将运算符合并到输入以相对地进行编辑。这些运算符与“通道盒”(Channel Box)中所用运算符相同。有关详细信息，请参见[通道盒](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-4C954FB2-8B6A-4BBD-9695-DF432616D0D2)。

| 运算符 | 功能 |
|---|---|
| **+=value** | 会将输入的值与现有值相加 |
| ***=value** | 会将输入的值与现有值相乘 |
| **-=value** | 会从现有值减去输入的值 |
| **/=value** | 将现有值除以输入的值 |

## 框显全部(Frame all)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-AC8F3337-DCAE-42E6-89BD-B5CC5E392A61.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该图标将框显“摄影表”(Dope Sheet)视图区域中当前动画曲线的所有关键帧。

## 框显播放范围(Frame playback range)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-CA6CD768-52B3-4278-8DD3-3F07760D450D.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该图标将框显“摄影表”(Dope Sheet)视图区域中位于当前“播放范围”(Playback Range)中的所有关键帧。

## 使视图围绕当前时间居中(Center the view about the current time)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-08D37895-563C-4696-A7CD-8EE29CA70A12.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该图标以“摄影表”(Dope Sheet)视图区域中的当前时间为中心。

## 以下层次/无(Hierarchy below/none)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-2EE299F2-BAA5-4CF4-ACA7-E4F075F3D9C1.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该按钮可切换“列表”(List)菜单中可用的“以下层次”(Hierarchy Below)选项。有关详细信息，请参见[以下层次](“摄影表”%28Dope%20Sheet%29菜单栏.md#GUID-FED85068-B947-422D-82C9-8A846EEE4D22__GUID-A00A8350-F46C-47E0-AC4F-D30B22FAADEF)。

### “自动加载摄影表”(Auto Load Dope Sheet)按钮

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-3DC6953D-F691-4166-A023-6A663A4A92DC.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该按钮可切换“列表”(List)菜单中可用的“自动加载选定对象”(Auto Load Selected Objects)选项。有关详细信息，请参见[自动加载选定对象](“摄影表”%28Dope%20Sheet%29菜单栏.md#GUID-FED85068-B947-422D-82C9-8A846EEE4D22__GUID-24AB5704-3EF7-47F1-A622-EBC3A5C40B11)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-1FBDEBFB-5C64-4F93-81B7-B28908FD0901.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该按钮将在未启用“自动加载选定对象”(Auto Load Selected Objects)时，将选定对象加载到“摄影表视图区域”(Dope Sheet View Area)。有关详细信息，请参见[加载选定对象](“摄影表”%28Dope%20Sheet%29菜单栏.md#GUID-FED85068-B947-422D-82C9-8A846EEE4D22__GUID-2AA87618-4D4E-486C-8C47-034888BAA551)。

## 打开曲线图编辑器(Open the Graph Editor)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-F7A48249-70F8-4296-956E-637BBB16AC50.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该图标将打开“曲线图编辑器”(Graph Editor)，并加载当前对象的动画曲线。

## 打开 Trax 编辑器(Open the Trax Editor)

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-EACA869F-C0BC-4F09-99C4-3D859DC9436E.png) <!-- baize:img-hook downloaded=false reason="正文 1867 字 ≥300，非承重" -->

该图标将打开“Trax 编辑器”(Trax Editor)，并加载当前对象的动画片段。
