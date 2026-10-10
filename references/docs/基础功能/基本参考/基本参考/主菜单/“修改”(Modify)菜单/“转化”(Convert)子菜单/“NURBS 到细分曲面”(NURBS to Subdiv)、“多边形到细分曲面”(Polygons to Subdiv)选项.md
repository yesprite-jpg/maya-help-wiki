# “NURBS 到细分曲面”(NURBS to Subdiv)、“多边形到细分曲面”(Polygons to Subdiv)选项

使用下面的选项来设置选择“修改 > 转化 > NURBS 到细分曲面”(Modify > Convert > NURBS to Subdiv)或“修改 > 转化 > 多边形到细分曲面”(Modify > Convert > Polygons to Subdiv)时发生的情况。两种转化操作均由相同的选项控制。

#### 最大基础网格面数(Maximum Base Mesh Faces)

设置原始曲面可拥有的最大面数，以便成功将该曲面转化为细分曲面。

例如，如果原始曲面具有 900 个面，且“最大基础网格面数”(Maximum Base Mesh Faces)值为 1000，则将成功完成转化，但是如果曲面具有 1200 个面，则转化将失败。

根据原始对象的复杂性，生成的曲面可能以较少的面表示。

#### 最大每顶点边数(Maximum Edges Per Vertex)

设置原始曲面中每个顶点可以拥有的最大边数，以便成功转化为细分曲面。

#### 保持原始(Keep Original)

创建细分曲面时保持原始对象。启用“保持原始”(Keep Original)后，可为细分曲面选择初始编辑模式。禁用该选项之后，原始对象将替换为细分曲面。

#### 细分曲面模式(Subdivision Surface Mode)

仅当“保持原始”(Keep Original)处于启用状态时，才可以使用这些选项。为细分曲面选择初始编辑模式。

## 热键

| ` (在 1 键旁边加上左侧单引号) | 打开/关闭原始曲面或转化细分曲面的显示。 |
|---|---|
| Shift + ` | 同时显示原始曲面和转化的细分曲面。 |
| Alt + ` | 如果已选择 NURBS 曲面：修改 > 转化 > NURBS 到细分曲面(Modify > Convert > NURBS to Subdiv) 如果已选择多边形曲面：修改 > 转化 > 多边形到细分曲面(Modify > Convert > Polygons to Subdiv) |
| Alt + Shift + ` | 如果已选择 NURBS 曲面：修改 > 转化 > NURBS 到细分曲面(Modify > Convert > NURBS to Subdiv) > ![图：如果已选择 NURBS 曲面：修改 转化 NURBS 到细分曲面(Modify Convert NURBS to Sub…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 958 字 ≥300，非承重" --> 如果已选择多边形曲面：修改 > 转化 > 多边形到细分曲面(Modify > Convert > Polygons to Subdiv) > ![图：如果已选择多边形曲面：修改 转化 多边形到细分曲面(Modify Convert Polygons to Subdiv)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 958 字 ≥300，非承重" --> |
| Page Up 键 | 增加细分曲面的“显示级别”(Display Level)（处于细分曲面标准模式时）。 |
| Page Down 键 | 降低细分曲面的“显示级别”(Display Level)（处于细分曲面标准模式时）。 |
