# 颜色管理和基于图像的照明 (IBL)

用于渲染 3D CG 图形的算法需要场景线性颜色；希望进行基于图像的照明的图像通常作为已是场景线性的 HDR 或 OpenEXR 图像提供。但是，这些图像可能仍需要一些颜色管理。

如果用于 IBL 的图像编码所使用的主颜色与用于渲染的工作空间不匹配，则可以手动指定 primaries/ 目录中的一个或多个变换来转化图像。例如，如果图像使用 Adobe RGB 主颜色并且您希望使用 UHDTV (Rec.2020) 主颜色渲染，那么可以应用 LinearAdobeRGB_to_CIE-XYZ，后跟 CIE-XYZ_to_LinearUHDTV。
