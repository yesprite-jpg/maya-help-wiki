# “文件路径编辑器”(File Path Editor)浏览器

“文件路径编辑器”(File Path Editor)浏览器显示所有在 Maya 中使用的路径的列表。每个文件路径可以展开以显示其下嵌套的文件。当在浏览器中选择一个文件时，此文件的节点在 Maya 中也被选择。如果在浏览器中选择了一个路径，存在于此路径中的文件的节点将在 Maya 中被选择。

基于文件的不同元素将在浏览器中列出，表示为“nodeName [filename]”。例如，文件 test.ma 的引用节点被列为 testRN [test.ma]。如果文件是图像序列，文件名将显示为序列图案。例如，test.0001.jpg 被列为 test.####.jpg。

## 解析状态

“文件路径编辑器”(File Path Editor)浏览器的顶级指示已解析和未解析文件路径的数量。此外，解析状态图标显示于在浏览器中列出的每个文件路径的左侧。通过这些图标，可以快速查明未解析文件路径。

| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-90F1139F-58CC-499E-BC98-5783F5D00DB1.png) <!-- baize:img-hook downloaded=false reason="正文 447 字 ≥300，非承重" --> | 已解析(Resolved) | 无未解析路径。 |
|---|---|---|
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-63C5803B-0369-4577-87A5-8176B842EE13.png) <!-- baize:img-hook downloaded=false reason="正文 447 字 ≥300，非承重" --> | 警告(Warning) | 某些路径未解析。 |
| ![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-ManagingScenes/images/GUID-82EB3A4A-7BB8-44C2-92F3-921A5F6978DE.png) <!-- baize:img-hook downloaded=false reason="正文 447 字 ≥300，非承重" --> | 未解析(Unresolved) | 所有路径都未解析。 |

## 相关主题

- [管理文件路径](管理文件路径.md)
