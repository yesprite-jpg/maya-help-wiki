# 将 PSD 网络用作 Maya 中的纹理

通过“PSD 文件”节点，可以将 PSD 文件用作 Maya 中的纹理网络。它类似于 Maya 的“文件纹理”节点，但仅适用于 PSD 文件。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-0077025F-18CE-4200-8692-E404D71C0421.png) <!-- baize:img-hook downloaded=false reason="正文 1113 字 ≥300，非承重" -->

默认情况下，Maya 会将 PSD 文件链接到包含在 PSD 文件中的合成图像。Maya 只能读取图像和向量层，因此在 PSD 节点链接到 Adobe Photoshop 的合成图像（默认情况）时，Maya 会支持 Adobe Photoshop 支持的所有内容，包括（例如）层样式、调整层、文本等。

但是，您可以选择将 PSD 节点链接到层集，在这种情况下，不支持层样式和调整层，应在 Maya 中读取 PSD 文件之前对其进行光栅化。

## 带有层集的 PSD 文件的优点

带有层集的 PSD 文件有助于进行迭代绘制：

- Adobe Photoshop 艺术工作者可以在保持 Maya 中的连接的同时添加、修改或删除层集中任意数量的层（请参见[在 Maya 中创建包含层集的 PSD 文件](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-B750BF4E-2343-4AA0-A09F-C7FA5F270B95.htm)）。

- Maya 艺术工作者可以将 PSD 节点转化为“分层纹理”(Layered Texture)，并将层集视为连接到“Hypershade”中的分层纹理的多个“PSD 文件纹理”(PSD File Texture)。

  **注**

  Maya 会将层集中的所有层视为单个展平图像。

使用 Maya 中现有的 PSD 文件

1. 在“Hypershade”中，使用新的“PSD 文件纹理”(PSD File Texture)节点加载 PSD 图像文件（“创建 > 2D 纹理 > PSD 文件”(Create > 2D textures > PSD File)）。

  PSD 文件将链接到 Adobe Photoshop 的合成图像。

2. 如果该文件具有多个遮罩通道，可以选择要查看的通道。从“属性编辑器”(Attribute Editor)中的“要使用的 Alpha”(Alpha to Use)属性选择遮罩。

3. 如果 PSD 文件具有层集，则可以选择要链接到的层集。从“属性编辑器”(Attribute Editor)中的“链接到层集”(Link to Layer Set)属性选择层。

4. 与 Maya 中的任何“文件纹理”(File Texture)一样，您可以设置任何“PSD 文件纹理”(PSD File Texture)属性。

  请参见[文件属性](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-648C6045-45B5-49FB-9FA5-77A8D67835FF.htm#WS17956D7ADBC6E736-51D3585C117AE33DCFA-7F89)。

将带有层集的现有 Adobe Photoshop“文件纹理”(File Texture)转化为“分层纹理”(Layered Texture)

1. 在“Hypershade”中，执行以下操作之一：

  - 在“PSD 文件纹理”(PSD File Texture)上单击鼠标右键，然后选择“转化为分层纹理”(Convert to Layered Texture)。

  - 选择[编辑 > 将 PSD 转化为分层纹理(Edit > Convert PSD to Layered Texture)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/files/GUID-EF6DFB31-CFCF-428D-8961-3D96CE673F99.htm#GUID-EF6DFB31-CFCF-428D-8961-3D96CE673F99__GUID-A0332172-AC9F-4439-8FD5-761BB6B362D6)。

2. 若要查看连接到分层纹理的多个层集，请对分层纹理重新制图。
