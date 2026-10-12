# Hypershade 的“编辑”(Edit)菜单

#### 删除(Delete)

删除选定的节点。从 Hypershade 中删除节点时，也会将其从会话中删除。

#### 删除未使用节点(Delete Unused Nodes)

删除未指定给几何体或粒子的节点。

#### 删除重复的着色网络(Delete Duplicate Shading Networks)

移除冗余的着色网络。

#### 按类型删除全部(Delete All by Type)

无论是否指定，都将删除所选类型的全部节点。

#### 还原选定样例(Revert Selected Swatches)

将选定样例还原为其默认形状。

#### 按类型全选(Select All by Type)

亮显从该菜单中选择的所有节点样例。

#### 选择具有材质的对象(Select Objects with Materials)

从具有为其指定的材质的对象中亮显所有节点样例。

#### 从对象选择材质(Select Materials from Objects)

亮显选定对象中的所有节点样例。例如，如果要知道哪些材质由对象 A、B、C 使用，可以先选择对象 A、B、C，然后选择该菜单项以选择与 A、B、C 相关的材质。对象 A、B、C 将不再处于选定状态。初始选定对象可以是普通对象，可以是组，也可以是多边形几何体的面。

#### 复制(Duplicate)

复制选定节点或着色网络。若要复制节点但不复制其网络，请选择节点，然后选择“编辑 > 复制 > 无网络”(Edit > Duplicate > Without Network)。若要复制节点并将其连接到同一网络（实际上是共享网络），请选择“编辑 > 复制 > 已连接到网络”(Edit > Duplicate) > With Connections to Network)。

#### 转化为文件纹理(Maya 软件)(Convert to File Texture (Maya Software))

将照明、阴影、着色和纹理转化（渲染）为可用作纹理贴图的文件纹理。

选择“编辑 > 转化为文件纹理(Maya 软件)”(Edit > Convert to File Texture (Maya Software)) > ![图：选择“编辑 转化为文件纹理(Maya 软件)”(Edit Convert to File Texture (Maya S…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1632 字 ≥300，非承重" --> 以打开[转化为文件纹理选项(Convert to File Texture Options)](Hypershade%20的“编辑”%28Edit%29菜单/“转化为文件纹理%28Maya%20软件%29%28Convert%20to%20File%20Texture%20%28Maya%20Software%29”选项.md)窗口。

有关详细信息，请参见[烘焙照明和颜色](../../../../烘焙纹理和预照明/烘焙照明和颜色.md)。

#### 将 PSD 转化为分层纹理(Convert PSD to Layered Texture)

保留 PSD 文件中的层并且将文件转化为对应的分层纹理。

#### 将 PSD 转化为文件纹理(Convert PSD to File Texture)

将 PSD 文件转化为文件纹理，并将所有层压缩到一层。请参见[将 PSD 节点转化为文件纹理](../../../../关于着色和纹理曲面/纹理/将%20PSD%20网络用作%20Maya%20中的纹理/将%20PSD%20节点转化为文件纹理.md)。

#### 创建 PSD 网络(Create PSD Network)

打开[创建 PSD 网络选项(Create PSD Network Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-982EC2B2-64CC-4359-9483-7378760593EB.htm)窗口，该选项可以创建用作纹理贴图的 PSD 纹理网络。请参见[将 PSD 网络用作 Maya 中的纹理](../../../../关于着色和纹理曲面/纹理/将%20PSD%20网络用作%20Maya%20中的纹理.md)

#### 编辑 PSD 网络(Edit PSD Network)

一旦创建了 PSD 网络，可以对其进行编辑。编辑 PSD 网络时，可以在“编辑 PSD 网络选项”(Edit PSD Network Options)窗口中添加或移除属性。有关详细信息，请参见[编辑 PSD 网络](../../../../关于着色和纹理曲面/纹理/将%20PSD%20网络用作%20Maya%20中的纹理/编辑%20PSD%20网络.md)。

#### 更新 PSD 网络(Update PSD Networks)

当修改连接到 Maya PSD 节点（在 Maya 中）的 PSD 文件（在 Adobe Photoshop 中）时，可以更新（刷新）Maya 中的图像以立即显示修改。详细信息请参见[更新 PSD 网络](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2655A075-1B14-4822-94E2-E4F12A25B0DD#GUID-2655A075-1B14-4822-94E2-E4F12A25B0DD__GUID-F2849CC1-79EF-4817-94CB-500B0281E0EA)。

#### 编辑纹理(Edit Texture)

打开默认图像编辑器，并允许编辑纹理。

#### 测试纹理(Test Texture)

请参见[测试纹理（和纹理范围）](../../../../关于着色和纹理曲面/纹理/测试纹理（和纹理范围）.md)。选择“编辑 > 测试纹理”(Edit > Test Texture) > ![图：请参见测试纹理（和纹理范围）。选择“编辑 测试纹理”(Edit Test Texture) 以打开“测试纹理选项”(Te…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1632 字 ≥300，非承重" --> 以打开“测试纹理选项”(Test Texture Options)对话框，然后输入测试纹理的 X 和 Y 分辨率。

#### 渲染纹理范围(Render Texture Range)

选择“编辑 > 渲染纹理范围”(Edit > Render Texture Range) > ![图：选择“编辑 渲染纹理范围”(Edit Render Texture Range) 以打开“渲染纹理范围选项”(Rende…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 1632 字 ≥300，非承重" --> 以打开[“渲染纹理范围选项”(Render Texture Range Options)](Hypershade%20的“编辑”%28Edit%29菜单/渲染纹理范围选项.md)窗口。有关详细信息，请参见[测试纹理（和纹理范围）](../../../../关于着色和纹理曲面/纹理/测试纹理（和纹理范围）.md)。
