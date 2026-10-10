# “AE 实时链接”(AE Live Link)窗口

此窗口具有两个版本。

- 在 Maya 中，转到“文件 > Adobe® After Effects® 实时链接”(File > Adobe® After Effects® Live Link)或“窗口 > 常规编辑器 > Adobe® After Effects® 实时链接”(Windows > General Editors > Adobe® After Effects® Live Link)。

- 在 After Effects 中，转到“窗口 > Maya”(Window > Maya)。

## Maya

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-F5BE4AAD-1E31-4A01-9189-7F455F57989A.png) <!-- baize:img-hook downloaded=false reason="正文 869 字 ≥300，非承重" -->

#### 状态栏(Status bar)

显示 Maya 到 After Effects 的连接的当前状态

#### 对象列表(Object list)

列出当前链接到 After Effects 合成的对象。如果此字段为空，则不发送任何信息。

#### 暂停(Pause)

暂停链接。仅当按“推动”(Push)按钮或取消暂停时，才会同步后续更新。

#### 推动更改(Push changes)

将当前对象列表同步到 Maya。

#### 同步时间轴(Sync timeline)

将“时间轴”(Timeline)链接到 After Effects 合成，使二者显示相同的帧。

#### 导入(Import)

从由 After Effects 创建的 .JSON 文件导入数据。

#### 导出(Export)

将数据保存到 .JSON 文件。

### 高级

#### 更改 IP(Change IP)

输入要在该计算机而非当前系统上与 After Effects 链接的本地 IP 地址。

#### 全局比例(Global Scale)

Maya 位置值先乘以该值，然后再发送到 After Effects。

## After Effects

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-MotionGraphics/images/GUID-E6DEE99A-043C-4074-BB41-E103938B9F1B.png) <!-- baize:img-hook downloaded=false reason="正文 869 字 ≥300，非承重" -->

#### 信息/状态(Information/Status)

显示 Maya 中的当前同步场景以及当前连接状态。

#### 对象列表(Object list)

拖到此处的层将发送到 Maya。如果当前没有任何实时链接，则改为打开“导出选定层”(Export selected layers)对话框。

#### 当前合成(Current composition)

将 Maya 同步到当前合成。

#### 导出选定层(Export selected layers)

将任何选定层导出到 Maya

#### 手动导入(Manual import)

用于手动导入 .json 文件。
