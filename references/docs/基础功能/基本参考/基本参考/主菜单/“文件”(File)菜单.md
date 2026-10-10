# “文件”(File)菜单

#### 新建场景(New Scene)

清除当前场景并开始新的场景。在清除当前场景之前，会提示您进行保存。

选择“文件 > 新建场景”(File > New Scene) > ![图：选择“文件 新建场景”(File New Scene) ，以设置“新建场景选项”(New Scene Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“新建场景选项”(New Scene Options)](“文件”%28File%29菜单/新建场景选项%28New%20Scene%20Options%29.md)。

#### 打开场景(Open Scene)

打开磁盘中保存的场景。

选择“文件 > 打开场景”(File > Open Scene) > ![图：选择“文件 打开场景”(File Open Scene) ，以设置“打开选项”(Open Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“打开选项”(Open Options)](“文件”%28File%29菜单/打开选项%28Open%20Options%29.md)。

若要打开在早期版本的 Maya 中创建的文件，请确保在“文件/项目”(Files/Projects)首选项中已启用[“忽略版本”(Ignore Version)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8E332DD5-879C-4AFD-8C6C-7C403FEF310F)首选项。

**注**

使用

“文件 > 打开”(File > Open)

打开文件时，会将工作单位（毫米、度等）更改为该文件中指定的单位。如果不希望更改工作单位，请使用

“文件 > 导入”(File > Import)

加载文件。

#### 保存场景(Save Scene)

使用当前名称保存场景。

选择“文件 > 保存场景”(Save Scene) > ![图：选择“文件 保存场景”(Save Scene) ，以设置“保存场景选项”(Save Scene Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“保存场景选项”(Save Scene Options)](“文件”%28File%29菜单/保存场景选项%28Save%20Scene%20Options%29.md)。

#### 场景另存为(Save Scene As)

可用于指定当前场景文件的新名称和位置。

选择“文件 > 场景另存为”(Save Scene As) > ![图：选择“文件 场景另存为”(Save Scene As) ，以设置“场景另存为选项”(Save Scene As Opti…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“场景另存为选项”(Save Scene As Options)](“文件”%28File%29菜单/场景另存为选项%28Save%20Scene%20As%20Options%29.md)。

#### 增量与保存(Increment & Save)

可用来以新的增量名称保存当前文件版本。

默认情况下，增量名称使用以下格式：*<root>.0001.mb*。例如，如果当前文件名为 *MyFile.mb*，则第一个增量文件名为 *MyFile.0001.mb*。另请参见[保存文件版本](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-62B28906-C01A-4A48-8AB7-F8A7FE4D3510)。

#### 归档场景(Archive Scene)

将当前文件连同其相关依存关系一起放置到 .zip 文件中。有关这些依存关系的完整列表，请参见[归档场景](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-C2E5B5A5-7AF1-49B8-B0C1-24CF0AB5C0FD)。

选择“文件 > 归档场景”(File > Archive Scene) > ![图：选择“文件 归档场景”(File Archive Scene) ，以设置“归档场景选项”(Archive Scene O…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“归档场景选项”(Archive Scene Options)](“文件”%28File%29菜单/归档场景选项%28Archive%20Scene%20Options%29.md)。

#### 保存首选项(Save Preferences)

将首选项保存到相应的默认位置。

另请参见[直接修改设置文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-045ADC80-E38A-4F2C-A428-8CE19D51D3A8)。

#### 优化场景大小(Optimize Scene Size)

可让您基于[“优化场景大小选项”(Optimize Scene Size Options)](“文件”%28File%29菜单/优化场景大小选项%28Optimize%20Scene%20Size%20Options%29.md)中的设置从场景中移除空的、无效的或未使用的部分，以减小场景的大小和复杂性。

Maya 优化场景时会显示进度条。按 Esc 键可以中断该操作。可以从“脚本编辑器”(Script Editor)中查看有关所有优化结果的报告。

选择“文件 > 优化场景大小”(File > Optimize Scene Size) > ![图：选择“文件 优化场景大小”(File Optimize Scene Size) 以打开这些选项，并指定在运行“文件 优化…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" --> 以打开这些选项，并指定在运行“文件 > 优化场景大小”(File > Optimize Scene Size)时要移除的信息类型。也可以使用“立即优化”(Optimize Now)按钮执行单项优化。

## 导入/导出(Import/Export)

#### 导入(Import)

将场景文件中的数据加载到现有场景中。

选择“文件 > 导入”(File > Import) > ![图：选择“文件 导入”(File Import) ，以设置导入选项(Import Options)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[导入选项(Import Options)](“文件”%28File%29菜单/导入选项%28Import%20Options%29.md)。

#### 导出全部(Export All)

将所有对象保存到新的场景文件中。

选择“文件 > 导出全部”(File > Export All) > ![图：选择“文件 导出全部”(File Export All) ，以设置导出全部/导出当前选择选项(Export All/Ex…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[导出全部/导出当前选择选项(Export All/Export Selection Options)](“文件”%28File%29菜单/导出全部选项%28Export%20All%20Options%29导出当前选择选项%28Export%20Selection%20Options%29.md)。

#### 导出当前选择(Export Selection)

将选定对象保存到新的场景文件中。

选择“文件 > 导出当前选择”(File > Export Selection) > ![图：选择“文件 导出当前选择”(File Export Selection) ，以设置“导出全部/导出当前选择选项”(Exp…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“导出全部/导出当前选择选项”(Export All/Export Selection Options)](“文件”%28File%29菜单/导出全部选项%28Export%20All%20Options%29导出当前选择选项%28Export%20Selection%20Options%29.md)。

#### 发送到 Flame(Send to Flame)

仅当有匹配的 Maya 和 Flame 版本时可用。将当前场景的内容发送到 Flame。

选择“文件 > 发送到 Flame”(File > Send to Flame) > ![图：选择“文件 发送到 Flame”(File Send to Flame) 可设置发送到 Flame 选项(Send to…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" --> 可设置[发送到 Flame 选项(Send to Flame Options)](“文件”%28File%29菜单/发送到%20Flame%20选项%28Send%20to%20Flame%20Options%29.md)。

#### 发送到 3ds Max

仅当有匹配的 Maya 和 3ds Max 版本时可用。将当前场景的内容发送到 3ds Max。

选择“文件 > 发送到 3ds Max”(File > Send to 3ds Max) > ![图：选择“文件 发送到 3ds Max”(File Send to 3ds Max) ，以设置“发送到 3ds Max”(S…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“发送到 3ds Max”(Send to 3ds Max)选项](“文件”%28File%29菜单/“发送到%203ds%20Max”%28Send%20to%203ds%20Max%29选项.md)。

#### 发送到 MotionBuilder(Send to MotionBuilder)

仅当有匹配的 Maya 和 MotionBuilder 版本时可用。将当前场景的内容发送到 MotionBuilder。

选择“文件 > 发送到 MotionBuilder”(File > Send to MotionBuilder) > ![图：选择“文件 发送到 MotionBuilder”(File Send to MotionBuilder) ，以设置发送到…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[发送到 MotionBuilder 选项(Send to MotionBuilder Options)](“文件”%28File%29菜单/“发送到%20MotionBuilder”%28Send%20to%20MotionBuilder%29选项.md)。

#### 发送到 Mudbox(Send to Mudbox)

仅当有匹配的 Maya 和 Mudbox 版本时可用。将当前场景的内容发送到 Mudbox。

#### 作为新场景发送(Send as New Scene)

在 Mudbox 中打开新场景，并发送选定对象。如果在场景中有选定的对象，则只会发送这些对象；否则，会发送整个场景。

此选项将启动 Mudbox（如果它尚未运行）。如果正在运行，则 Mudbox 将提示您保存当前场景或取消。

#### 更新当前场景(Update Current Scene)

仅在 Mudbox 运行时可用。通过发送当前选择，更新 Mudbox 场景。如果未选择任何对象，则此选项将发送先前发送的相同选择。

#### 添加到当前场景(Add to Current Scene)

仅在 Mudbox 运行时可用。将当前选择发送到 Mudbox。将已发送的全部选定对象都复制至 Mudbox 场景。

#### 选择以前发送的对象(Select Previously Sent Objects)

选择以前发送到 Mudbox 的对象。如果之前同时发送了多个对象，则此选项将选择所有这些对象。但是，如果是分别发送多个对象，则此选项将仅选择最近发送的对象。

该选项可用于方便地查看已共享的对象，并选择要添加到所选项中的对象。

#### 发送到 Unity(Send to Unity)

用于使用 FBX 文件格式将场景直接导出到 Unity 项目。请参见[将场景导出到 Unity](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-01D019BF-4686-469C-98A1-FDA30C75FFAE)。

#### 全部(All)

将所有对象保存到指定的 Unity 项目中的新场景文件。

#### 选择(Selection)

将选定的对象保存到指定的 Unity 项目中的新场景文件。

#### 设置 Unity 项目(Set Unity Project)

用于浏览以选择您想要将所有场景（这些场景是使用其他“文件 > 发送到 Unity”(File > Send To Unity)选项导出的）发送到的有效 Unity 项目。

#### 发送到 Unreal(Send to Unreal)

用于使用 FBX 文件格式将场景直接导出到 Unreal 项目。另请参见[将场景导出到 Unreal](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-51B5F746-12B0-4AB5-9701-A0A740D0ADA5)。

#### 全部(All)

将所有对象保存到指定的 Unreal 项目中的新场景文件。

#### 选择(Selection)

将选定的对象保存到指定的 Unreal 项目中的新场景文件。

#### 设置 Unreal 项目(Set Unreal Project)

用于浏览以选择您想要将所有场景（这些场景是使用其他“文件 > 发送到 Unreal”(File > Send To Unreal)选项导出的）发送到的有效 Unreal 项目。

#### 游戏导出器(Game Exporter)

打开[“游戏导出器”(Game Exporter)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2DB6E7B0-04B8-4585-91E9-7D64B02D0338)，该导出器可使用 FBX 格式有效导出游戏资产。另请参见[使用“游戏导出器”(Game Exporter)导出动画片段](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-31148EE5-CAA8-48F2-9E51-3C9712EE8A14)、[使用“游戏导出器”(Game Exporter)导出模型](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-1D758D66-04CC-40DC-A667-479408AD0AAB)。

#### Adobe(R) After Effects(R) 实时链接

创建[实时链接](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-DB3385DD-F644-458C-B7A3-769E7FA97E69)。

#### 导出到脱机文件(Export to Offline File)

将对场景中的对象（例如连接的节点）所做的编辑导出到指定的文件。然后可以使用“文件 > 指定脱机文件”(File > Assign Offline File)将这些编辑应用于其他场景。

选择“文件 > 导出到脱机文件”(File > Export to Offline File) > ![图：选择“文件 导出到脱机文件”(File Export to Offline File) ，以设置“导出到脱机文件选项”(…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“导出到脱机文件选项”(Export to Offline File Options)](“文件”%28File%29菜单/导出到脱机文件选项%28Export%20to%20Offline%20File%20Options%29.md)。

#### 指定联机文件(Assign Online File)

从所选择的文件引用编辑，并将它们应用于在“大纲视图”(Outliner)或“引用编辑器”(Reference Editor)中选定的引用节点。Maya 通过将编辑文件中的每个 nodename.attribute 与其应用的目标文件匹配来应用编辑。

例如，可以在场景 sphere.ma 中为 pSphere1.translateX 导出一个引用编辑。该编辑会在引用文件中保存为 <main>:sphere_pSphere1.translateX。然后可以将该编辑应用于场景 ball.ma，以便编辑 ball:pSphere1.translateX。

选择“文件 > 指定脱机文件”(File > Assign Offline File) > ![图：选择“文件 指定脱机文件”(File Assign Offline File) ，以设置“指定脱机文件选项”(Assig…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“指定脱机文件选项”(Assign Offline File Options)](“文件”%28File%29菜单/指定脱机文件选项%28Assign%20Offline%20File%20Options%29.md)。另请参见[指定脱机文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D2F8B56-8546-42A7-B31D-A088D1EC2698)。

#### ATOM

此菜单包括“导出动画”(Export Animation)、“导入动画”(Import Animation)、“创建 ATOM 模板”(Create ATOM Template)选项。有关这些选项的详细信息，请参见 [ATOM 菜单](“文件”%28File%29菜单/ATOM%20菜单.md)。

## 引用(References)

#### 创建引用(Create Reference)

将场景内容（包括对象、动画和着色器）导入到当前打开的场景中，而无需将文件导入到场景中。场景中显示的内容是从仍然独立、未打开的已存在文件读取或*引用的*。您可以从 Maya 场景文件 (.ma、mb) 或 Alembic 缓存创建文件引用。

选择“文件 > 创建引用”(File > Create Reference) > ![图：选择“文件 创建引用”(File Create Reference) ，以设置“引用选项”(Reference Opti…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 5017 字 ≥300，非承重" -->，以设置[“引用选项”(Reference Options)](“文件”%28File%29菜单/引用选项%28Reference%20Options%29.md)。

**注**

若要引用在 Maya 的早期版本中创建的文件，请确保在

“文件/项目”(Files/Projects)首选项

中已启用

“忽略版本”(Ignore Version)

首选项。

#### 引用编辑器(Reference Editor)

打开[“引用编辑器”(Reference Editor)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-8D8E0D4A-DE37-4C63-9F59-8D71F00E3367)。

## 视图(View)

#### 查看图像(View Image)

默认情况下，使用“FCheck”查看图像。

**注**

重要：

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。可以在

应用程序首选项

（

“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)

）中选择其他默认图像查看器。

#### 查看序列(View Sequence)

默认情况下，使用“FCheck”查看所选的图像序列。（另请参见[指定默认媒体播放器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-D4284B32-3B66-4712-BAA0-66BA6DB08187)。）

**注**

重要：

自 Maya 2020 起，FCheck 在 macOS 上不再受支持。可以在

应用程序首选项

（

“窗口 > 设置/首选项 > 首选项”(Windows > Settings/Preferences > Preferences)

）中选择其他默认图像查看器。

## 投影(Project)

#### 项目窗口(Project Window)

打开[“项目窗口”(Project Window)](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-A570696B-95A4-4ED7-87EE-A7EAB63156CF)。在“项目窗口”(Project Window)中，可以创建新的 Maya 项目以及编辑现有项目的文件位置和名称。

另请参见[将文件组织到项目中](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9CE78B5A-7E9F-45E6-AB6D-66795E5656F4)。

#### 设置项目(Set Project)

可让您指定的当前要处理的项目。

指定项目可以将一个场景或一组相关场景所需的所有不同文件组合到一起。

## 最近(Recent)

#### 最近的文件(Recent Files)

列出最近保存的场景文件。单击此列表中的场景文件将加载该文件，并关闭当前场景。另请参见[打开最近保存的文件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-699D997C-02C5-4F55-9A3D-6CD68DD0B687)。

**注**

提示：

也可以查看最近打开的文件的列表，方法是在

状态行（工具栏）

的

“打开场景”(Open Scene)

图标上单击鼠标右键。

#### 最近的项目(Recent Projects)

列出最近打开的项目。通过在此列表中选择一个项目文件夹名称，可将该文件夹设置为当前项目。另请参见[将文件组织到项目中](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-9CE78B5A-7E9F-45E6-AB6D-66795E5656F4)。

**注**

提示：

您可以在

“文件/项目”(Files/Projects)首选项

（

“窗口 > 设置/首选项 > 首选项”(Window > Settings/Preferences > Preferences)

）中设置此列表中显示的项目数量。

#### 退出(Exit)

退出 Maya。

如果在选择场景之前刚刚对其进行了保存，将会退出 Maya。如果最近未保存场景，将显示一条消息，提示您在退出之前要先保存。
