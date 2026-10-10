# 导出预合成选项(Export Pre-Compositing Options)

使用这些选项可查看在选择“渲染 > 导出预合成”(Render > Export Pre-Compositing) > ![图：使用这些选项可查看在选择“渲染 导出预合成”(Render Export Pre-Compositing) 时发生的情况…](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-96432FB8-EBE9-4D1A-8DED-5173E032EBC0.png) <!-- baize:img-hook downloaded=false reason="正文 1196 字 ≥300，非承重" --> 时发生的情况。

使用“导出预合成”(Export Pre-Compositing)窗口中的选项，可以：

- 将所有渲染层、渲染过程和摄影机导出到合成中的预合成文件

- 将选定的渲染层、渲染过程和摄影机导出到合成中的预合成文件

“导出预合成”(Export Pre-compositing)编辑器可分为以下三种选项卡：“摄影机”(Cameras)、“渲染层”(Render Layers)和“渲染过程”(Render Passes)。根据要导出的元素，选择适当的选项卡。

使用 ![图：使用 图标可展开渲染层，渲染摄影机或渲染过程层次。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-533C04FB-C389-4177-8FA2-6DCCE1ADFCE0.png) <!-- baize:img-hook downloaded=false reason="正文 1196 字 ≥300，非承重" --> 图标可展开渲染层，渲染摄影机或渲染过程层次。

## 导出元素

![图：图标表示正在导出所有元素。 图标表示正在导出部分元素。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-DF480517-FF4D-497A-8082-FAFC8954AB60.png) <!-- baize:img-hook downloaded=false reason="正文 1196 字 ≥300，非承重" --> 图标表示正在导出所有元素。![图：图标表示正在导出所有元素。 图标表示正在导出部分元素。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-7EC1333D-B2B3-4895-9E91-5926390A5477.png) <!-- baize:img-hook downloaded=false reason="正文 1196 字 ≥300，非承重" --> 图标表示正在导出部分元素。

以下示例中，仅导出漫反射和白炽度过程。因此，Bob（渲染层）旁边的 ![图：以下示例中，仅导出漫反射和白炽度过程。因此，Bob（渲染层）旁边的 图标表示只有部分元素正在导出。](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-7EC1333D-B2B3-4895-9E91-5926390A5477.png) <!-- baize:img-hook downloaded=false reason="正文 1196 字 ≥300，非承重" --> 图标表示只有部分元素正在导出。

**注**

通过更改摄影机父对象（建立父子关系和断开父子关系），可以更改摄影机的唯一名称并打断预合成工作流程。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Rendering/images/GUID-A96FF658-B7F0-4CF4-973E-F055D8DA2E52.png) <!-- baize:img-hook downloaded=false reason="正文 1196 字 ≥300，非承重" -->

单击“导出全部”(Export All)或“导出当前选择”(Export Selection)按钮，以便将渲染层、过程和摄像机导出到“合成”中。此时将打开“导出预合成文件”(Export PRECOMP file)窗口，以允许您为导出的文件输入文件名。

### 预合成场景定位点

使用“预合成场景锚点”(Pre-Compositing Scene Anchor)，以便将 Maya 场景连接到一个合成的场景合成。场景中的所有元素均与场景定位点相关联。场景名可能会发生变化，例如，从版本 1 变为版本 2；与此不同的是，场景定位点不会发生变化。属于同一合成的所有元素，例如，摄影机、渲染过程、渲染层等，应具有相同的场景定位点。

从“导出预合成”(Export Pre-Compositing)窗口选择“导出全部”(Export All)或“导出当前选择”(Export Selection)后，合成将开始查找具有定位点名称的场景合成。如果这样的合成不存在，新的合成将建立。如果该合成存在，随后其将在合成中更新（根据合成中的导入选项；有不同的更新/创建/重新创建模式）。

**注**

没有适当的、规定的场景，定位点将无法执行导出。未在“预合成场景定位点”(Pre-Compositing Scene Anchor)字段中输入名称的情况下，单击“导出全部”(Export All)或“导出当前选择”(Export Selection)按钮后，系统将提示您定义一个定位点或使用场景名作为定位点。应避免使用场景名作为场景定位，因为它会断开 Maya 场景与合成项目中场景合成之间的唯一连接关于此规则，有一个例外情况是，只要导出一次，并且将来不打算更新合成。例如，如果只是要在合成中创建预合成模板，则不需要场景定位点文件，因为场景定位点仅用于更新现有的场景合成。

### 场景预合成注释

通过该区域可标识预合成文件中的更改。
