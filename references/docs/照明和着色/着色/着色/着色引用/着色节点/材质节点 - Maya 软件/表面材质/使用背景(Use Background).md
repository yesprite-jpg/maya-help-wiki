# 使用背景(Use Background)

可以使用“useBackground”材质创建自定义阴影和反射过程以捕捉阴影或反射。

如果已渲染阴影过程，则使用包含阴影信息的遮罩通道创建黑色图像。合成器可以使用此通道对阴影的外观进行模糊、变亮、变暗等处理。如果已渲染反射过程，则使用遮罩通道中的白色遮罩创建 RGB 图像。

在[“创建”(Create)选项卡](../../../着色窗口和编辑器/Hypershade%20窗口/“创建”%28Create%29选项卡.md)中找到此材质。

有关将“使用背景”(Use Background)材质用作捕捉器的详细信息，请参见[阴影捕捉](../../../../../../照明/照明/Maya%20中的阴影/阴影捕捉.md)。

**注**

- 阴影颜色不会影响指定给“useBackground”着色器的表面。

- 在通过“useBackground”着色器光线跟踪折射时，在“useBackground”着色曲面可能会出现瑕疵。若要解决此问题，请将折射对象着色器的“折射”属性设定为禁用。

## 使用背景属性(Use Background Attributes)

#### 镜面反射颜色(Specular Color)

定义材质的镜面反射颜色。如果更改此颜色或指定其纹理，场景中的反射将会显示这些更改。例如，如果将棋盘格纹理映射至“镜面反射颜色”(Specular Color)，将会在棋盘格图案中显示反射。如果要查看非常清晰的反射渲染结果，拖动滑块以将“镜面反射颜色”(Specular Color)设定为白色。默认颜色为灰色。

#### 反射率(Reflectivity)

确定多少对象的纹理反射到“使用背景”(Use Background)材质上。例如，如果对象非常有光泽，则增加该值。默认值为 0.5。

#### 反射限制(Reflection Limit)

确定了反射的距离。默认值为 2。

#### 阴影遮罩(Shadow Mask)

确定材质阴影遮罩的密度。如果更改此值，阴影遮罩将变暗或变亮，便于在查看“渲染视图”(Render View)中的遮罩通道时更好地验证场景中的阴影和反射。

![图：确定材质阴影遮罩的密度。如果更改此值，阴影遮罩将变暗或变亮，便于在查看“渲染视图”(Render View)中的遮罩通道…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-LightingShading/images/GUID-9A40C50A-B014-405E-B7AB-A37FDFD23156.png) <!-- baize:img-hook downloaded=false reason="正文 1022 字 ≥300，非承重" -->

默认值为 1.0。如果设定为 0.0，则将不显示阴影。

## 蒙版不透明度(Matte Opacity)

为了在调整这些属性时获得最佳结果，请选择“渲染视图”(Render View)中的“显示 Alpha 通道”(Display Alpha Channel)图标，以便在重新渲染场景时查看遮罩通道。

#### 蒙版不透明度模式(Matte Opacity Mode)

选择下列选项之一：

#### 不透明度增益(Opacity Gain)

同时显示反射和阴影。

#### 匀值蒙版(Solid Matte)

调整“使用背景”(Use Background)材质的密度。

#### 蒙版不透明度(Matte Opacity)

使用滑块或输入值来调整遮罩通道的密度。
