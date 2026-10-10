# “渲染设定”(Render Setup)编辑器的“场景”(Scene)设置中的“渲染设置”(Render Settings)、“AOVs”(AOV)和“灯光”(Lights)选项卡

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

- 双击“渲染设置”(Render Settings)选项卡，以打开“渲染设置”(Render Settings)窗口。

- 双击“AOVs”(AOV)选项卡，以打开显示 AOV 设置的“渲染设置”(Render Settings)窗口。

- 双击“灯光”(Lights)选项卡，以打开“灯光编辑器”(Light Editor)。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-58B3AE08-02F6-4FFE-B8F0-541D38328988.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

![图：也可以通过“渲染设置”(Render Setup)编辑器中的“首选项”(Preferences)菜单打开“渲染设置”(R…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" --> 也可以通过“渲染设置”(Render Setup)编辑器中的“首选项”(Preferences)菜单打开“渲染设置”(Render Settings)和 AOV 设置。

如果在查看场景层时打开“渲染设置”(Render Settings)，将显示场景的“渲染设置”(Render Settings)。如果您正在查看任一层（如 layer1），那么将显示 layer1 的“渲染设置”(Render Settings)。这同样适用于“AOVs”(AOV)和“灯光”(Lights)选项卡。

![图：如果通过“渲染设置”(Render Setup)编辑器中的“首选项”(Preferences)菜单打开“渲染设置”(Re…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" --> 如果通过“渲染设置”(Render Setup)编辑器中的“首选项”(Preferences)菜单打开“渲染设置”(Render Settings) 和 AOV 设置，则同样适用。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-9515E4AB-21A8-431B-B0E8-50B6D9FFB28E.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

## 创建覆盖

通过这些编辑器，您可以创建渲染设置、AOV 或灯光覆盖。示例如下所示。

此示例说明了如何创建渲染设置覆盖。系统会自动在您的渲染层中创建“渲染设置”(Render Settings)集合，以及相应的覆盖。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-03A9BF05-20D0-4BA8-8EC5-FA0F738C102D.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

在此示例中，将创建一个 AOV 覆盖，让您可以为您的渲染层禁用漫反射 AOV。系统也会自动创建“AOVs”(AOV)集合。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-970293B6-2A50-4C4E-8869-A0D28FBEDAB4.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

在此示例中，将基于点光源的“颜色”(Color)和“强度”(Intensity)属性创建覆盖。同时也创建“灯光”(Lights)集合。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-F092B039-ED66-4ADC-96D4-1BDC8334F97C.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

您还可以手动将**“渲染设置”(Render Settings)、“AOVs”(AOV)或“灯光”(Lights)**集合添加到渲染层，方法是将其从“场景”(Scene)设置拖放到图层。通常不需要执行此步骤，但如果您要[创建渲染设置子集合](为渲染层创建渲染设置覆盖.md#GUID-B3690107-63E5-45C6-818D-5BDD158693A4__SECTION_78B5C75D4FD44143A9F23188C838B146)以对您的覆盖进行排序以及创建多个“渲染设置”(Render Settings)组合，此步骤可能会很有用。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-21194ED7-CF90-4230-B893-9939CDB5E889.png) <!-- baize:img-hook downloaded=false reason="正文 899 字 ≥300，非承重" -->

## 相关主题

- [为渲染层创建渲染设置覆盖](为渲染层创建渲染设置覆盖.md)

- [使用渲染设置创建 AOV 覆盖](使用渲染设置创建%20AOV%20覆盖.md)

- [在渲染层中创建灯光覆盖](在渲染层中创建灯光覆盖.md)
