# 导出和导入 AOV

将场景中的 AOV 导出为 .json，然后将此文件导入到新的场景中，以重用 AOV 而不必重新创建它们。可以通过“渲染设置”(Render Settings)窗口或“渲染设置”(Render Setup)编辑器执行此操作。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-4AB6AA8F-094A-422B-981B-D2867DCC6E66.png) <!-- baize:img-hook downloaded=false reason="正文 1023 字 ≥300，非承重" -->

## 导出 AOV

可以通过以下四种方式之一导出 AOV：

  ![图：从“渲染设置”(Render Settings)窗口中，选择“预设 导出 AOV”(Presets Export AOV…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1023 字 ≥300，非承重" --> 从“渲染设置”(Render Settings)窗口中，选择“预设 > 导出 AOV”(Presets > Export AOVs)。

- 在“渲染设置”(Render Setup)编辑器的“场景 > AOV”(Scene > AOVs)部分中单击 ![图：在“渲染设置”(Render Setup)编辑器的“场景 AOV”(Scene AOVs)部分中单击 ，然后选择“导出当…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-15A05717-B953-472A-B6FC-39C64A718DC9.png) <!-- baize:img-hook downloaded=false reason="正文 1023 字 ≥300，非承重" -->，然后选择“导出当前”(Export Current)。

  从“渲染设置”(Render Setup)编辑器中，选择“文件 > 导出场景 AOV”(File > Export Scene AOVs)。

  ![图：从“渲染设置”(Render Setup)编辑器中，选择“文件 导出可见层 AOV”(File Export Visib…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1023 字 ≥300，非承重" --> 从“渲染设置”(Render Setup)编辑器中，选择“文件 > 导出可见层 AOV”(File > Export Visible Layer AOVs)。

默认情况下，AOV .json 文件保存到用户预设位置；即 <Documents>\maya\Presets。有关详细信息，请参见[全局预设和用户预设](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md#GUID-469A3F38-8E0B-4A28-8913-D8A7E3EF0733__SECTION_1B399EB0AAA34C16AA60AD650DC96FC7)。

## 导入 AOV

可以通过以下两种方式之一执行此操作：

  从“渲染设置”(Render Setup)编辑器中，选择“文件 > 导入场景 AOV”(File > Import Scene AOVs)。

  ![图：从“渲染设置”(Render Settings)窗口中，选择“预设 导入 AOV”(Presets Import AOV…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-889B2E93-B1A5-42D7-9CB5-4408CC0D7121.png) <!-- baize:img-hook downloaded=false reason="正文 1023 字 ≥300，非承重" --> 从“渲染设置”(Render Settings)窗口中，选择“预设 > 导入 AOV”(Presets > Import AOVs)。

导入窗口默认为用户预设位置；即 <Documents>\maya\Presets。有关详细信息，请参见[全局预设和用户预设](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md#GUID-469A3F38-8E0B-4A28-8913-D8A7E3EF0733__SECTION_1B399EB0AAA34C16AA60AD650DC96FC7)。

导入时，具有两个选项：

  覆盖(Overwrite)

  当前所有的 AOV 将替换为导入的 AOV。

  合并(Merge)

  如果节点相同（即，具有相同的名称），则将现有的 AOV 替换为导入的 AOV。当前不存在的 AOV 将按原样导入，不加修改。当前位于场景中、但不存在于导入的 .json 文件中的 AOV 将会保留并保持不变。

**注**

提示：

从

“渲染设置”(Render Setup)

编辑器中选择

“首选项 > 渲染首选项”(Preferences > Rendering Preferences)

，可以更改预设的位置。

## 相关主题

- [将“渲染设置”(Render Settings)作为预设导出和导入](将“渲染设置”%28Render%20Settings%29作为预设导出和导入.md)

- [导出场景“渲染设置”(Render Settings)和 AOV 并将其应用于新场景](导出场景“渲染设置”%28Render%20Settings%29和%20AOV%20并将其应用于新场景.md)

- [从可见渲染层导出“渲染设置”(Render Settings)和 AOV 并将其应用于新场景](从可见渲染层导出“渲染设置”%28Render%20Settings%29和%20AOV%20并将其应用于新场景.md)
