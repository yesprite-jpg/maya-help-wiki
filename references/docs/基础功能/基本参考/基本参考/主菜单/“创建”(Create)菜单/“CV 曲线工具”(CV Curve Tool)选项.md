# “CV 曲线工具”(CV Curve Tool)选项

使用这些选项可设置在选择“创建 > 曲线工具 > CV 曲线工具”(Create > Curve Tools > CV Curve Tool)时创建的工具属性。另请参见[绘制 NURBS 曲线](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-2B521AD9-1CB2-43C9-8385-388D118A5AF3)。

#### 曲线次数(Curve Degree)

“曲线次数”(Curve Degree)越高，曲线越平滑。默认设置（“3 立方”(3 Cubic)）适用于大多数曲线。您创建的 CV（控制顶点）至少要比“曲线次数”(Curve Degree)多 1。例如，需要至少 6 个 CV 才能完成 5 次曲线：

![图：“曲线次数”(Curve Degree)越高，曲线越平滑。默认设置（“3 立方”(3 Cubic)）适用于大多数曲线。您…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-211DC719-1E33-458A-8AEB-DDFEA786CD38.png) <!-- baize:img-hook downloaded=false reason="正文 632 字 ≥300，非承重" -->

详细信息请参见[次数](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-84AD4364-96CA-48B5-BBBE-D0BF082CAB2F#WS17956D7ADBC6E73629BB7D5D117AE32BD12-7FFE)。

#### 结间距(Knot Spacing)

结间距的类型用于设置 Maya 将 U 位置值指定给编辑点（结）的方式。“弦长”(Chord length)结间距可以更好地分布曲率。如果使用曲线构建曲面，则曲面可能会更好地显示纹理。

“一致”(Uniform)结间距可以创建更便于预测的曲线 U 位置值。详细信息请参见 [NURBS 曲线和曲面参数化](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-275E0E44-2E4B-4A53-B329-B9F5688730A3)。

#### 多端结(Multiple End Knots)

启用此设置时，曲线的末端编辑点（结）将在末端 CV 上重合。通常，这使曲线的末端区域更易于控制。

![图：启用此设置时，曲线的末端编辑点（结）将在末端 CV 上重合。通常，这使曲线的末端区域更易于控制。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-A9F9004A-28CE-4C22-85E0-3B369CBACA56.png) <!-- baize:img-hook downloaded=false reason="正文 632 字 ≥300，非承重" -->

如果在“多端结”(Multiple End Knots)禁用的情况下创建一对曲线，则可以使用“捕捉到点”功能对齐每条曲线的第二个 CV（末端 CV 旁边），以便在两条曲线之间创建切线连续性。

**注**

与 Maya 中的所有工具一样，可以在创建对象后更改选项。选择曲线，然后打开“通道盒”或“属性编辑器”。

## 相关主题

- [NURBS 曲线组件](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-3C709643-E723-4518-84B7-45EB07778AD2)

- [“EP 曲线工具”(EP Curve Tool)选项](“EP%20曲线工具”%28EP%20Curve%20Tool%29选项.md)

- [NURBS 选项](../“显示”%28Display%29菜单/NURBS%20选项.md)
