# 颜色、遮罩 (Alpha) 和深度通道

在渲染期间，Maya 软件渲染器可生成一个图像文件，其中包含颜色通道 (RGB)、遮罩通道 (RGBA)、深度通道 (RGBZ) 或这三者的组合 (RGBAZ)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-2454DD0C-9EDB-41BF-8209-E57E083220BF.png) <!-- baize:img-hook downloaded=false reason="正文 901 字 ≥300，非承重" -->

默认情况下，Maya 生成一个包含三个颜色通道和一个遮罩通道的图像文件，但您可以控制在渲染图像文件中包括的通道类型。遮罩和深度通道主要用于合成。如果您不准备合成渲染图像，则无需在渲染过程中生成遮罩或深度通道。如果图像包含遮罩或深度通道，文件大小将增加，计算时间也可能延长。

若要启用或禁用通道，请参见[为渲染图像启用颜色通道、深度通道和遮罩通道](../为渲染调整场景设置/为渲染图像启用颜色通道、深度通道和遮罩通道.md)。

默认情况下，如果使用的是 Arnold for Maya 渲染器，则会以 .exr 格式渲染图像（包括 Alpha (RGBA) 通道）。

## 颜色通道

位图图像中的每个像素都包含三个颜色通道，其中每个颜色通道分别表示图像中红色、绿色或蓝色的量。每个像素也可能具有一个用于实现透明度的 Alpha（遮罩）通道和一个表示与摄影机之间距离的深度通道。某些图像格式不能包含嵌入遮罩或深度通道；在这种情况下，Maya 可以生成单独的遮罩文件或深度文件。

## 遮罩通道

遮罩通道（或 Alpha 通道）定义图像在何处透明，何处不透明。对象的不透明区域为白色，半透明区域为灰色，透明区域为黑色。

可对合成软件使用遮罩通道将图像分层。例如，可以将一个图像的遮罩通道用作蒙版，与另一个图像一起来合成对象（不含背景）。

如果使用的是 **Arnold for Maya**，请参见 [AOV](https://docs.arnoldrenderer.com/display/A5AFMUGCHS/AOV) 和 [Cryptomatte](https://docs.arnoldrenderer.com/display/A5AFMUGCHS/Cryptomatte)。

## 深度通道

深度通道（或 Z 深度或 Z 缓冲区通道）提供图像的 3D 信息。它表示对象与摄影机之间的距离。

深度通道供合成软件使用。例如，可以在保持正确遮挡的同时，使用深度通道正确合成多个层。

Maya 将深度值存储为 -1/z。这些值表示近剪切值和远剪切值。

如果使用的是 **Arnold for Maya**，请参见 [AOV](https://docs.arnoldrenderer.com/display/A5AFMUGCHS/AOV) 和 [Z 深度 AOV](https://support.solidangle.com/display/a5AFMUGCHS/Z+Depth+AOV)。

### 在 3D 空间中依次排列对象

在层中渲染时，合成应用程序必须能够判定各个对象的各个部分的前后顺序。Alpha 通道不包含该信息，因此您可以使用 Maya 中“蒙版不透明度”(Matte Opacity)功能的“黑洞”(Black Hole)模式生成正确合成的裁切区域。请参见[修改遮罩通道](../为渲染调整场景设置/修改遮罩通道.md)。
