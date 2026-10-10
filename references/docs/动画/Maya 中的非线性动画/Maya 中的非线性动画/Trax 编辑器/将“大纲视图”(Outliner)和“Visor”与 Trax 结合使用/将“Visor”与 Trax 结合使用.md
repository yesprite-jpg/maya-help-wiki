# 将“Visor”与 Trax 结合使用

从“Trax 编辑器”(Trax Editor)打开“Visor”

1. 执行下列操作之一：

  - 在 Trax 菜单栏中，选择“文件 > Visor”(File > Visor)。

  - 在 [Trax 工具栏](../Trax%20工具栏.md)中，单击“Visor” ![图：在 Trax 工具栏中，单击“Visor” 按钮。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DB059130-6C3C-4B62-9D2A-B5B846C4BB07.png) <!-- baize:img-hook downloaded=false reason="正文 1493 字 ≥300，非承重" -->按钮。

2. 执行下列操作之一：

  - 单击“角色片段”(Character Clips)或“角色姿势”(Character Poses)选项卡以显示已应用于场景中的角色的片段或姿势。

  - 单击“未使用的片段”(Unused Clips)或“未使用的姿势”(Unused Poses)选项卡以显示未应用于场景中的角色的片段或姿势。

  例如，如果从另一个场景导入一个片段，则可以通过“Visor”中的“未使用的片段”(Unused Clips)选项卡来访问该片段。

在“Visor”中复制源片段并将其粘贴到“Trax 编辑器”(Trax Editor)中的角色

1. 打开 [Visor](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-0065E2FA-EC3E-4BBD-A896-043621AD35D2)，然后切换到“角色片段”(Character Clips)或“未使用的角色片段”(Unused Character Clips)选项卡。

2. 执行下列操作之一：

  - 在要复制的源片段上单击鼠标中键，并将它从“Visor”拖到所需的角色、轨迹和位置上。

    表示要插入的片段的白色框会显示在轨迹视图区域中的鼠标指针下。该白色框与要复制的源片段长度相同。

    另外，如果鼠标指针在轨迹之间，那么将会出现一条黑线，指示将在轨迹之间创建一条新轨迹以容纳要复制的片段。有关将轨迹添加到角色、组或子角色的详细信息，请参见[选择、添加和移除轨迹](../选择、添加和移除轨迹.md)。

    ![图：在要复制的源片段上单击鼠标中键，并将它从“Visor”拖到所需的角色、轨迹和位置上。 表示要插入的片段的白色框会显示在轨…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-DEBC2EF4-8D60-4A0B-B74B-7FCB799F19E2.png) <!-- baize:img-hook downloaded=false reason="正文 1493 字 ≥300，非承重" -->

    释放鼠标按钮之后，在白色框的位置（Trax 时间轴中的轨迹和点）将出现该源片段的一个实例。

  - 在“Visor”中右键单击需要的源片段，从显示的弹出菜单中选择“复制”(Copy)，然后在所需角色下方的“Trax”轨迹视图区域中单击鼠标右键并选择“粘贴片段”(Paste Clip)。

    在轨迹中的角色下方，会显示选定源片段的一个实例。

    如果将片段粘贴到相同角色集中的某一个角色上，Maya 将创建该片段的实例。请参见[复制片段](../创建片段和姿势/复制片段.md)。

    如果将片段粘贴到一个不同的角色集，并且在源片段的角色集与将片段拖动到的角色集之间存在角色贴图，那么 Maya 会使用该角色贴图粘贴该片段。请参见[在角色之间映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AAF92442-CDC0-46C2-B55C-276D75D292DE)。

    否则，Maya 将用“按节点名称”(By Node Name)粘贴方法来粘贴角色中的片段。如果要使用一种不同的方法（如“按属性名称”(By Attribute Name)）粘贴，请在“粘贴片段选项”(Paste Clip Options)窗口（“Edit > Paste”(Edit > Paste) > ![图：否则，Maya 将用“按节点名称”(By Node Name)粘贴方法来粘贴角色中的片段。如果要使用一种不同的方法（如“…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1493 字 ≥300，非承重" -->）中选择所需的方法。

将片段从磁盘导入到“Visor”中

1. 在“Visor”中，选择“文件 > 导入”(File > Import)。

  将显示“导入”(Import)文件浏览器。

2. 导航到包含要导入到“Visor”中的一个或多个片段的 .ma 或 .mb 文件，选择文件，然后单击“导入”(Import)。

  这些片段会显示在“Visor”的“未使用的片段”(Unused Clips)选项卡中。

将片段从“Visor”导出到磁盘

1. 在“Visor”中，选择“文件 > 导出选定网络”(File > Export Selected Network)，或在某个片段或某组选定片段上单击鼠标右键并从显示的弹出菜单中选择“导出”(Export)。

  将显示“导出”(Export)文件浏览器。

2. 导航到要将片段导出到的硬盘上的文件夹，然后单击“导出”(Export)。

  会将在“Visor”中选择的片段放置在一个 .ma 或 .mb 文件中，并将这些片段导出到磁盘上指定的目录和文件夹中。

将片段从磁盘复制到场景

1. 有关将片段从操作系统的文件浏览器复制到 Maya 场景的信息，请参见[剪切、复制和粘贴片段](../创建片段和姿势/剪切、复制和粘贴%20Trax%20片段.md)。
