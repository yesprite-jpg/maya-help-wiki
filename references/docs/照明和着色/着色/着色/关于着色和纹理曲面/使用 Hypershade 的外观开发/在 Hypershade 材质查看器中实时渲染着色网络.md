# 在 Hypershade  材质查看器中实时渲染着色网络

通过“材质查看器”(Material Viewer)，可以轻松地可视化子网络和未连接的网络，因此优化了合成和着色器开发工作流。

“材质查看器”(Material Viewer)基于在 Hypershade 工作区中所绘制内容的上下文，显示任何着色网络（包括材质、纹理和工具）。红色边界亮显了在“材质查看器”(Material Viewer)中当前渲染的节点。

调整着色网络时，材质查看器会实时更新。

在使用 Maya 硬件 2.0 渲染器进行渲染或使用已注册的任何其他插件渲染器（如 Arnold for Maya）进行渲染之间做出选择。

**注**

可以使用 MPxRenderer 类实现第三方渲染器，以便在“材质查看器”(Material Viewer)中进行渲染。详细信息请参见 Maya 开发人员帮助中的“C++ API 参考”。

## 渲染着色器网络

在此示例中，可以选择图表中的任何节点，以在材质查看器中查看网络 (phong1) 的下游结果。在“材质查看器”(Material Viewer)中渲染的节点由红色边界表示。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-5854D328-B8A4-4737-9872-5ABD726AD7F8.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->

**注**

在

“材质查看器”(Material Viewer)

中使用硬件渲染器时，Maya 使用在

“渲染设置”(Render Settings)

窗口中

“Maya 硬件 2.0”(Maya Hardware 2.0)

选项卡中选择的透明度算法。如果发现透明度结果与预期不符，则选择其他透明度算法。

### 在您的网络中渲染纹理

若要查看特定的纹理，请单击文件节点上的 S 图标以单放节点。有关 solo 的详细信息，请参见[关于单放](关于单放.md)。也可以在“浏览器”(Browser)的“纹理”(Textures)选项卡中选择您的纹理，然后在“材质查看器”(Material Viewer)中渲染它们。渲染纹理时，“材质查看器”(Material Viewer)样例将出现在平面视图中。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-FAF9A070-C563-47A1-B3B5-62F7774263BE.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->

## 渲染没有材质节点的网络

可以渲染具有或没有材质节点的网络。这样就可以构建纹理网络，而无需将每个网络指定给材质。

在此示例中，checker1 是在“材质查看器”(Material Viewer)中渲染的。若要在“材质查看器”(Material Viewer)中查看草参考纹理，请单放文件节点。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-CBAC26B5-A4AA-4127-AED6-AA8FC1C5DC6C.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->

纹理由 www.cgtextures.com 提供。

## 渲染凹凸贴图

可以在“材质查看器”(Material Viewer)中渲染凹凸贴图，它将显示为 3d 几何体样例，以允许您更好地检查照明影响下的凹凸。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-20652A12-AA59-422F-9550-8733BBC70571.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->

## 识别在“材质查看器”(Material Viewer)中渲染的节点

通过 Hypershade 工作区，可以同时绘制多个着色网络，每个着色网络在不同的选项卡中进行绘制。可以通过其红色边界识别正在渲染的节点。如果单放了某个节点，则它始终显示有红色边界，且已在“材质查看器”(Material Viewer)中渲染。如果未单放节点，则在“材质查看器”(Material Viewer)中渲染的节点的轮廓为红色。在大多数情况下，这是上次选择的着色网络的下游结果。

## 材质样例选项

也可从多个样例形状中选择，例如：“球体”(Sphere)、“布料”(Cloth)、“茶壶”(Teapot)、“玻璃泼墨”(Glass Splash)等。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-947BA4BC-7287-4DF1-A386-8F608D9534FF.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->

## 添加环境照明

也可以在预设或自定义环境背景中渲染材质。从预设环境列表中进行选择，或者添加自己的环境。详细信息请参见[在材质查看器中通过预设或自定义环境添加基于图像的照明](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-35DC6688-1D1B-44BA-8DFD-9BB5C764A835.htm)。

## 移动和旋转摄影机

您可以在“材质查看器”(Material Viewer)中移动和旋转摄影机。在 3D 视图中，您可以像在视口中一样执行翻滚、平移和推拉等操作；而在 2D 平面视图中（例如，单放纹理时），您可以平移和缩放。

从 3D 视图切换至 2D 视图（例如，通过单放纹理切换）、然后再重新切换回至 3D 视图时，系统将保存 3D 摄影机的位置。另一方面，系统不会保存 2D 视图的摄影机位置。关闭并重新打开“材质查看器”(Material Viewer)时，也会重置摄影机的设置。

单击“材质查看器”(Material Viewer)工具栏中的 ![图：单击“材质查看器”(Material Viewer)工具栏中的 ，可将摄影机重置到其原始位置。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-AF011479-C2C5-453B-9C00-0187A834306B.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->，可将摄影机重置到其原始位置。

## Hypershade 中的颜色管理

全局颜色管理设置（“首选项”(Preferences)窗口中的“颜色管理”(Color Management)首选项）适用于“材质查看器”(Material Viewer)样例，以及“浏览器”(Browser)和工作区中的样例。

此外，可以使用提供的控件调整“材质查看器”(Material Viewer)的曝光和 Gamma，以及选择从显示的工作颜色空间转化颜色的视图变换。有关颜色管理控件的详细信息，请参见[渲染视图工具栏](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-83161023-275E-4E57-A0D8-9C9E255944AE)。

## 暂停材质查看器

单击“材质查看器”(Material Viewer)工具栏中的 ![图：单击“材质查看器”(Material Viewer)工具栏中的 ，可暂停更新。如果“材质查看器”(Material Vi…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" -->，可暂停更新。如果“材质查看器”(Material Viewer)设置为使用硬件渲染器，则所有使用 Viewport 2.0 渲染器的编辑器（例如，视口和 UV 编辑器）也会暂停。暂停的编辑器以红色边界显示，且文本“暂停”(Paused)指示其暂停状态。如果存在上次缓存渲染的图像，则“材质查看器”(Material Viewer)将显示此图像来代替文本“暂停”(Paused)。

允许您在场景中进行更改，而不必等待“材质查看器”(Material Viewer)更新。这特别适用于复杂场景。

再次单击 ![图：再次单击 可解除暂停，并且使用暂停期间进行所有更改更新“材质查看器”(Material Viewer)。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" --> 可解除暂停，并且使用暂停期间进行所有更改更新“材质查看器”(Material Viewer)。

请参见[在 Hypershade 中暂停 Viewport 2.0 和材质查看器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-5326458C-E6AA-45F8-ACAF-D32FAAA613E3)

### 材质查看器的挂起

如果两个渲染同时出现（例如，“渲染视图”(Render View)和“材质查看器”(Material Viewer)），启动 IPR 渲染将挂起“材质查看器”(Material Viewer)，且“材质查看器”(Material Viewer)周围将出现红色边界，以指示其挂起状态。若要解除挂起，请停止 IPR 渲染且“材质查看器”(Material Viewer)再次处理活动状态。但是，必须手动触发重新渲染（例如，通过更改属性值或摄影机角度手动触发）。此行为与单击 ![图：如果两个渲染同时出现（例如，“渲染视图”(Render View)和“材质查看器”(Material Viewer)），…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-A856707B-0550-4DFA-AEB1-590B0FF7D219.png) <!-- baize:img-hook downloaded=false reason="正文 2471 字 ≥300，非承重" --> 略有不同，后者在解除暂停后始终会重新渲染。
