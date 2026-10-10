# 使用 OpenSubdiv 平滑网格

使用“网格 > 平滑”(Mesh > Smooth)平滑网格或创建细分曲面代理时，OpenSubdiv 是默认的细分方法。

使用 OpenSubdiv 平滑网格

1. 选择要平滑的网格或面。

2. 选择“网格 > 平滑”(Mesh > Smooth) > ![图：选择“网格 平滑”(Mesh Smooth) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 700 字 ≥300，非承重" -->。

3. 在显示的“平滑选项”(Smooth Options)窗口中，设置 [OpenSubdiv Catmull-Clark](../../../多边形建模参考/“建模”%28Modeling%29菜单集/“网格”%28Mesh%29菜单/平滑选项%28Smooth%20Options%29.md#GUID-4D094DC4-9027-4422-9083-6C9D2FE4036E__SECTION_9968881EA5124F759D9786EB9D638050) 选项。

4. 单击“平滑”(Smooth)。

  Maya 通过添加新的多边形，然后平滑顶点及其连接的边来平滑网格。

5. 在“属性编辑器”(Attribute Editor)中，选择“polySmoothFace”选项卡 >“OpenSubdiv 控件”(OpenSubdiv Controls)。

  使用 [OpenSubdiv 控件(OpenSubdiv Controls)](../../../多边形建模参考/多边形节点/polySmoothFace.md#GUID-EF5DE1E7-329D-4354-9D9E-BE8AFD1BE3A6__SECTION_9968881EA5124F759D9786EB9D638050)调整平滑网格。

使用 OpenSubdiv 创建细分曲面代理网格

1. 选择您要平滑的网格。

2. 选择“网格 > 平滑代理 > 细分曲面代理”(Mesh > Smooth Proxy > Subdiv Prox) > ![图：选择“网格 平滑代理 细分曲面代理”(Mesh Smooth Proxy Subdiv Prox) 。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/images/GUID-23B160F6-E1FB-4E29-94B2-7323BFE33726.png) <!-- baize:img-hook downloaded=false reason="正文 700 字 ≥300，非承重" -->。

3. 在显示的“细分曲面代理选项”窗口中，设置 [OpenSubdiv Catmull-Clark](../../../多边形建模参考/“建模”%28Modeling%29菜单集/“网格”%28Mesh%29菜单/平滑选项%28Smooth%20Options%29.md#GUID-4D094DC4-9027-4422-9083-6C9D2FE4036E__SECTION_9968881EA5124F759D9786EB9D638050) 选项。

4. 单击“平滑”(Smooth)。

  Maya 会平滑选定的网格，并将其放置在原始的未平滑网格（代理）中。Maya 还会创建包含两种网格的新组，并为每个网格创建新层。

5. 在“属性编辑器”(Attribute Editor)中，选择“polySmoothProxy”选项卡 >“OpenSubdiv 控件”(OpenSubdiv Controls)。

  使用 [OpenSubdiv 控件(OpenSubdiv Controls)](../../../多边形建模参考/多边形节点/polySmoothProxy.md#GUID-954CB56E-A40D-415B-A1D4-13EDFAED01D3__SECTION_9968881EA5124F759D9786EB9D638050)调整平滑网格。

## 相关主题

- [OpenSubdiv 概述](../OpenSubdiv%20概述.md)

- [使用 OpenSubdiv 预览平滑网格](使用%20OpenSubdiv%20预览平滑网格.md)
