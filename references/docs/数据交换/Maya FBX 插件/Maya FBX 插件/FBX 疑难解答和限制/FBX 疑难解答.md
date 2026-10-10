# FBX 疑难解答

本部分包含一些复杂问题的描述，解释了出现这些问题的原因，并提供了解决方法（如果有）。

如果“疑难解答”或“限制”部分中没有任何一个主题对您有所帮助，请在 [FBX 论坛](https://forums.autodesk.com/t5/fbx/ct-p/area-c7?profile.language=zh-CN)上进行搜索。论坛包含正在进行的有关 Maya FBX 插件的讨论以及可以与支持部门进行联系的电子邮件地址。

## FBX 不在“Maya 导入/导出”(Maya Import/Export) 选项中

如果您正在使用的 Maya FBX 插件版本不是与 Maya 一起安装的，可能 Maya FBX 插件未在 Maya 插件管理器中激活。请参见“Customize how Maya works”（自定义 Maya 的工作方式）一章的“Maya's Preferences and customization”（Maya 首选项和自定义）一节中的主题[“Loading or unload Maya plug-ins”（加载或卸载 Maya 插件）](http://download.autodesk.com/global/docs/maya2014/zh_cn/files/PC_Load_or_unload_Maya_plugins.htm)。

## 插件不运行

插件仅能在创建时所基于的 Maya 版本上运行；请确认您要安装的 Maya FBX 插件版本是否适用于正在运行的 Maya 版本。

## MotionBuilder 层怎么不见了？

通过 Maya FBX 插件，可以导入动画层，而无需进行烘焙。否则，动画将烘焙到基础动画层。

若要在 Maya 中将动画层作为单独层保留，请执行以下操作：

在导入 FBX 文件时，请在 Maya FBX 导入器中禁用“烘焙动画层”(Bake Animation Layers)选项。请参见[烘焙动画层](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-72394768-6DD7-4676-857F-B0468509CFF6)。

如果此选项处于活动状态，插件会在导入过程中自动烘焙动画层。

## FBX UI 怎么不见了？

如果在导入或导出 FBX 文件时，“FBX 导入器”(FBX Importer)或“FBX 导出器”(FBX Exporter)窗口不显示，则可能是因为 Maya FBX 插件找不到 FBX 安装程序中包含的 MEL 脚本。这些脚本会自动安装到以下路径：

```text
<Maya version>/scripts/FBX
```

如果删除了这些脚本，FBX 用户界面将不再显示。可通过重新安装插件来恢复这些文件，让界面重新显示。

#### Maya 默认 UI

如果使用的是 Maya 默认 UI 设置，则文件浏览器右侧的 FBX 选项可能会处于收拢状态。将右侧的分隔条拖动到对话框的中心位置可展开 FBX 选项。

## UI 中的“更新动画(已设置关键帧的变换)”(Update animation (keyed transforms))选项位于何处？

如果“FBX 导入”(FBX Import)窗口中缺少“更新动画(已设置关键帧的变换)”(Update animation (keyed transforms))选项，请针对频繁使用的预设文件验证 Maya 导入预设（尤其是 Autodesk Media and Entertainment 导入预设和 Autodesk MotionBuilder 导入预设）的状态。查找“MergeMode”选项。如果找到“MergeMode”选项，请将其复制到活动的预设文件，然后重新启动 Maya。请参见 [FBX 导入选项](../FBX%20导入/FBX%20导入选项.md)主题中的“导入预设选项”。

## 纹理怎么不见了？

如果从关联媒体文件所在位置的相对和绝对路径移动或删除任何纹理，则纹理会从文件中消失。如果您将 FBX 文件给使用另一台计算机的某个人，而这个人没有您的计算机驱动器上该目录下的那种纹理，可能会出现这种情况。

使用“嵌入的媒体”(Embed Media)选项可以使 FBX 插件将关联媒体（如纹理）纳入（嵌入）到 FBX 文件中。然后该插件在导入时将相应的媒体提取到 .fbm 文件夹。该插件将嵌入的媒体复制到与 FBX 文件处于同一位置上的 <文件名>.fbm 文件夹中，并以 FBX 文件命名。

**注**

激活

“嵌入的媒体”(Embed Media)

后，媒体将包含在 FBX 文件本身中，这对文件大小有影响。最好仅在将 FBX 文件传输到接收者再也无法访问其中的原始媒体源的位置时使用该选项。

如果禁用“嵌入的媒体”(Embed Media)选项，FBX 插件将在导出时存储关联媒体文件的相对和绝对路径。如果因故无法再访问路径，那么将导致出现问题。请确保可以访问关联的媒体，以确保能正确导入这些媒体文件。

#### 为什么应该嵌入媒体？

如果在不激活“嵌入的媒体”(Embed Media)选项的情况下将文件导出为 FBX，则在同一台计算机上打开该文件，且场景中使用的所有图像的位置与导出该文件时这些图像所在的位置相同时，不会出现问题。

如果要将 FBX 文件传送给另一个人，则最好嵌入媒体。如果将 FBX 用于存储资源，由于您最后可能会删除参考图像，或将所有文件移动到另一个驱动器或具有不同路径的计算机中，因此最好也使用嵌入。

**注**

如果在 FBX 2010 版及更早版本中将文件导出为 ASCII 格式，则不会嵌入任何纹理。

#### “嵌入的媒体”(Embed Media)处于启用状态，但我仍旧看不到纹理

在先前版本的 Maya FBX 插件中，当在“嵌入的媒体”选项激活的情况下保存 FBX 文件时，会将嵌入的文件提取到与 FBX 文件处于相同位置的文件夹中。如果您没有写入该文件夹的权限，则不会提取媒体文件。通过网络工作时可能会遇到这种缺少写入权限的情况。

在当前版本的 Maya FBX 插件中，如果您没有创建该文件夹所需的写入权限，则媒体文件会改而发送到临时文件夹中。

**注**

如果使用 FBX 2010 版及更早版本将文件导出为 ASCII 格式，则不会嵌入任何纹理。

## 为何摄影机不一致？

如果使用设置为“垂直”(Vertical)或“填充”(Fill)的“适配分辨率门”(Fit Resolution Gate)设置将 Maya 摄影机导入到 3ds Max 中，则效果将有所不同。

要在 3ds Max 中为 Maya 摄影机之间提供更佳支持，请将“适配分辨率门”(Fit Resolution Gate)设置设定为“水平”(Horizontal)，而不是设置为“垂直”(Vertical)或默认值“填充”(Fill)。

**注**

您可以很轻松地将 3ds Max 摄影机导入到 Maya 中；Maya 渲染相同的效果。

## 为何法线在导入时锁定？

如果导入未变形的几何体，则在导入到 Maya 时，法线将锁定。当您在 Maya 中将几何体变形时，这些锁定的法线可能会引起问题。例如，如果导入在 3ds Max 中创建的融合变形目标并之后将它们导出为 FBX，则它们在导入到 Maya 中时其法线处于锁定状态。

如果在 Maya 中解除锁定变形对象的法线，可以解决此问题。若要解除锁定法线，请将几何体导入到 Maya，然后选择“网格显示 > 解除锁定法线”(Mesh Display > Unlock normals)。

#### 原因为何？

如果导入未变形的几何体，则在将该几何体导入到 Maya 时，法线将锁定。

如果法线被 Maya 锁定，则在将导入的对象变形时，法线不会随着几何体移动。如果未解除锁定这些法线，则在应用修改器（如蒙皮修改器或融合变形修改器）时，可能会遇到着色问题。

## MotionBuilder 中的边为什么看上去不一样？

早期版本的 MotionBuilder（2010 版及更早版本）不支持硬边/软边法线，可能会导致 MotionBuilder 出现着色问题。

如果您使用的是早期版本的 MotionBuilder 并遇到了此问题，请激活“逐顶点分割法线”(Split per-vertex normals)选项。激活该选项后，将基于边的连续性分割几何体顶点法线。顶点法线决定了多边形面之间的视觉平滑效果。它们反映了 Maya 如何在平滑明暗处理模式下渲染多边形。

#### 适用原因

使用此选项可在 MotionBuilder 中保持与 Maya 相同的硬边/软边外观。

如果 MotionBuilder 中不需要硬边，则无需使用该选项，因为该操作会复制顶点信息并转化几何体自身。您可以使用 FBX 导入器中的“逐顶点合并法线”(Combine per-vertex Normals)选项执行相反的操作，但是这可能会导致错误的 UV 纹理贴图，请参见此条目下面的注意事项。

如果使用的不是合并回工作流（将 FBX 合并到现有场景），使用此选项可能会导致将 FBX 文件重新导入到 Maya 中时生成错误的 UV 贴图。将您的 FBX 文件导入到原始 Maya 场景，以避免分割几何体存在几何体 UV 问题。

禁用“逐顶点分割法线”(Split per-vertex Normals)选项的情况下进行导出时会在 MotionBuilder 中生成以下效果：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-8407015A-A704-4DEB-83F6-0FFAA7EE50AE.png) <!-- baize:img-hook downloaded=false reason="正文 3740 字 ≥300，非承重" -->

激活“逐顶点分割法线”(Split per-vertex Normals)选项的情况下进行导出时会在 MotionBuilder 中生成以下效果：

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-DataExchange/images/GUID-6C983CEA-F747-4B62-AE72-1F4305BD962D.png) <!-- baize:img-hook downloaded=false reason="正文 3740 字 ≥300，非承重" -->

**注**

使用此选项可以永久改变应用于几何体的 UV 贴图。之后，UV 将正确地重新指定给新分割的几何体。将此几何体导入到空 Maya 场景时，存在 UV 限制：即，使用

“FBX 导入器”(FBX Importer)

中的

“逐顶点合并法线”(Combine per-vertex Normals)

可能会导致错误的 UV 指定。

## 为什么集为空？

这是由限制造成的。详细信息请参见 [FBX 和选择集](FBX%20限制.md#GUID-AA3B8EA4-DDFB-4B0F-9654-2BF6B8781AE7__GUID-018EB7BB-CADB-4AE7-B755-DA72AB8188A2)。

## 为什么 Mudbox 模型渲染错误？

如果您正在导出已用作纹理贴图提取中的源的网格（例如，使用此模型作为源来提取置换贴图），请注意任何提取的纹理贴图都将自动使用您的模型导出。

这可能会在将模型导入其他应用程序时造成意外变形，因为纹理贴图会在导入时自动指定给该模型。如果遇到此问题，您可以在导入该模型后，从关联通道（例如置换或凹凸通道）移除所有不需要的纹理贴图。
