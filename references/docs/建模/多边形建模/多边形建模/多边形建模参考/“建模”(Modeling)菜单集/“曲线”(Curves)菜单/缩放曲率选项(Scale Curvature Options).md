# 缩放曲率选项(Scale Curvature Options)

使用以下选项可设置在选择“曲线 > 缩放曲率”(Curves > Scale Curvature)时发生的情况。

#### 比例因子(Scale Factor)

确定会将选定曲线的每个分段拉直的程度或使其现有曲率扩大的程度。“比例因子”(Scale Factor)越高，效果越显著。在包含较多 CV 的曲线上的效果将比在包含较少 CV 的曲线上的效果更显著，因为“比例因子”(Scale Factor)会影响每个分段。

如果“比例因子”(Scale Factor)小于 1，那么选定曲线将变得更直。

如果“比例因子”(Scale Factor)大于 1，那么选定曲线将使其现有曲率扩大（通过按与其现有曲率相同的方向扩大每个分段的曲率）。

#### 最大曲率(Max Curvature)

控制相邻分段之间所允许的最大角度。

如果“最大曲率”(Max Curvature)为 1，那么相邻分段之间所允许的最大角度为 180 度。如果“最大曲率”(Max Curvature)为 0.5，那么相邻分段之间所允许的最大角度为 90 度。

**注**

如果选定曲线已经有角度大于“最大曲率”(Max Curvature)值所允许的角度的相邻分段，并且应用了“比例因子”(Scale Factor)大于 1 的“缩放曲率”(Scale Curvature)（即，扩大曲线的曲率），那么曲线实际上可能会变得更直。这是因为“最大曲率”(Max Curvature)值将减小相邻分段之间的角度。

## 相关主题

- [拉直、平滑、卷曲或弯曲曲线](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Modeling/files/GUID-C050D5F6-661E-4C3F-87B4-4DD4DFD1E94E.htm)
