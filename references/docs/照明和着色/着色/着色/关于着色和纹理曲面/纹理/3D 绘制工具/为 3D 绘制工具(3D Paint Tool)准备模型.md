# 为 3D 绘制工具(3D Paint Tool)准备模型

开始绘制之前，请考虑以下事项：

- 多边形曲面和细分曲面必须具有适配纹理空间中 0 到 1 范围的非重叠 UV。通常，“自动映射”(Automatic Mapping)会产生可用于绘制的 UV。有关详细信息，请参见[多边形建模](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-7941F97A-36E8-47FE-95D1-71412A3B3017)和“细分曲面建模”([www.autodesk.com/maya-docs-archive](http://www.autodesk.com/maya-docs-archive))。

- NURBS 模型通常由多个面片组成，而多边形模型通常仅由单个网格组成。指定纹理时，每个 NURBS 面片都会接收一个纹理，但在默认情况下，多边形仅接收整个网格的一个纹理。这会导致没有足够的纹理分辨率来获取有关多边形网格的细节。将纹理大小增加到最大值会降低性能，并且可能仍无法提供足够的分辨率。

  一种解决方案是划分模型并指定多种材质（例如，一种用于头，一种用于躯干，一种用于肢体）。然后，网格上的每种材质均接收其自己的纹理。这种解决方案还有一个好处是一次可以处理网格的一部分。此外，您还可以根据需要为模型的不同部分指定不同大小的纹理。

  **注**

  “3D 绘制工具”(3D Paint Tool)

  不会正确处理非流形几何体。

为模型的某个部分指定材质

1. 选择要为其指定材质的模型的某个部分。

2. 打开 Hypershade（“窗口 > 渲染编辑器 > Hypershade”(Windows > Rendering Editors > Hypershade)）。

3. 在 Hypershade 中，在材质上单击鼠标右键，然后选择“为当前选择指定材质”(Assign Material to Selection)。
