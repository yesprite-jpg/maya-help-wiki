# “Trax 编辑器”(Trax Editor)  “文件”(File)菜单

#### 导入动画片段(Import Animation Clip)

打开“导入”(Import)文件浏览器。该窗口用于浏览要导入的动画片段文件。“导入片段”(Import Clip)将选定动画片段导入到当前亮显的角色。请参见[导入或导出动画片段](../操纵片段/导入或导出动画片段.md)。可以导入以下文件格式的动画片段：

- mayaAscii (.ma)

- mayaBinary (.mb)

- mel (mel)

- OBJ (.obj)

- 音频（.wav、.aif、.aiff）

- 影片 (.mov)

- EPS (.eps)

- Adobe® Illustrator ® (.AI)

**注**

Trax 编辑器(Trax Editor)

不支持 .atom 动画文件。（请参见

原子文件格式(ATOM file format)

。）

#### 将动画片段导入角色(Import Animation Clip to Characters)

打开“导入”(Import)文件浏览器。该窗口用于浏览要导入到已加载角色的动画片段文件。“将动画片段导入角色”(Import Animation Clip to Character)可将选定动画片段导入到 Trax 中的所有已加载角色。可以导入以下文件格式的动画片段：

- mayaAscii (.ma)

- mayaBinary (.mb)

- mel (mel)

- OBJ (.obj)

- 音频（.wav、.aif、.aiff）

- 影片 (.mov)

- EPS (.eps)

- Adobe® Illustrator ® (.AI)

  ##### 片段(Clip)

  设定下列选项之一：

  ###### 仅将片段放在 Visor 中(Put Clip in Visor Only)

  将要导入的动画片段添加到“Visor”。

  ###### 将片段放在 Trax 编辑器和 Visor 中(Put Clip in Trax Editor and Visor)

  将要导入的动画片段添加到“Trax 编辑器”(Trax Editor)和“Visor”中。

  **注**

  将片段放入

  “Visor”

  时，可以从

  “大纲视图”(Outliner)

  访问该片段。有关在

  “大纲视图”(Outliner)

  中查看片段的信息，请参见

  将大纲视图与 Trax 结合使用(Use the Outliner with Trax)

  。

#### 导入音频(Import Audio)

打开“导入”(Import)文件浏览器。该窗口用于浏览要导入到当前场景“声音轨迹”(Soundtrack)的音频文件。可以导入以下格式的音频文件：

- WAV (.wav)

- 音频交换文件格式（.aif、.aiff）

#### 导入缓存(Import Cache)

打开“导入”(Import)文件浏览器。该窗口用于浏览并选择要附加到当前对象的现有几何体或 nCloth 缓存文件。如果当前对象已具有几何体或 nCloth 缓存，浏览并选择的缓存文件将替换原始缓存，但不会从磁盘中删除它。请参见[创建和编辑几何缓存](../../../../几何缓存/几何缓存/创建和编辑几何缓存.md)。

#### 导出动画片段(Export Animation Clip)

打开“导出”(Export)文件浏览器。该窗口用于浏览导出动画片段的位置。可以导出以下文件类型的动画片段：

- mayaAscii (.ma)

- mayaBinary (.mb)

- mov (.mov)

#### 角色映射器(Character Mapper)

打开“角色映射器”(Character Mapper)窗口。请参见[角色映射器](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-20015023-4D8F-4D09-8F82-15D3A80A1554)。

#### 导出角色映射(Export Character Map)

打开“写入”(Write)文件浏览器。该窗口用于浏览要导出角色映射的角色集。可以导出以下文件类型的角色映射：

- maya Ascii (.ma)

- mayaBinary (.mb)

- 影片 (.mov)

- mel (.mel)

##### 映射方法(Map Method)

设定要导出角色映射的格式。所选的“映射方法”(Map Method)选项取决于期望中最容易编辑的贴图类型。在选择“映射方法”(Map Method)之前，首先要知道这两个角色集的属性（和它们的顺序）。

##### 按属性名称(By Attribute Name)

创建一个贴图，使当前角色集的属性值被映射到目标角色集的属性名称。

#### 按属性顺序(By Attribute Order)

创建一个贴图，使当前角色集的属性值根据“通道盒”(Channel Box)中的属性顺序（降序）映射到目标角色集。

#### 按节点名称(By Node Name)

创建一个贴图，使当前角色集的属性值被映射到目标角色集的相应对象和属性名称。

#### 按当前映射(By Current Map)

使用当前映射为选定角色集创建贴图。如果已经导出一个贴图来修复角色映射，且之后需要将新属性添加到角色集，这将会非常有用。如果使用“按当前映射”(By Current Map)，则只能编辑上次校正映射后添加的属性映射。

该选项仅在已导出角色映射并执行了产生的 MEL 脚本后才有用。请参见[在角色之间映射动画](https://beehive.autodesk.com/community/service/rest/cloudhelp/resource/cloudhelpchannel/guidcrossbook/jsonp?v=2022&p=MAYAUL&l=CHS&accessmode=live&guid=GUID-AAF92442-CDC0-46C2-B55C-276D75D292DE)。

#### Visor

打开“Visor”窗口。请参见[什么是 Visor、大纲视图和片段库？](../../../Maya%20中的非线性动画.md#GUID-B90726CA-6C86-4E9B-80F3-1F65745C3B3F__WS17956D7ADBC6E736B6BA507117AE308213-7FFB)。

## 相关主题

- [导入选项(Import Options)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Animation/files/GUID-37B31221-7BBC-40DA-AB33-47C333EF4E14.htm)
