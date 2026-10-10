# 使用 MEL/Python 或 API 进行分析

## 使用 MEL/Python 命令进行分析

可以使用 MEL/Python profiler 和 profilerTool 命令在分析器中开始/停止录制，查询事件信息，搜索事件，以及检测过程以进行分析。检测是对程序的修改，用于收集信息进行分析。

必须在编辑模式下使用以下 profilerTool 标志：

- categoryView

- cpuView

- frameAll

- frameSelected

- matchWholeWord

- showAllEvent

- showSelectedEvents

- showSelectedEventsRepetition

- threadView

必须在查询模式下使用以下 profilerTool 标志：

- exists

- searchEvent

### 使用 MEL

#### 录制

使用 profiler 命令 -sampling (-s) 标志启用和禁用事件录制；如下所示：

```text
profiler -s true;
polyCube;
profiler -s false;
```

#### 添加类别

若要添加分析类别，请使用 -addCategory 标志；如下所示：

```text
int $melCategoryIndex = `profiler -addCategory "MEL Scripts"`;
```

**注**

当前，不支持包含本地化字符（即大写 ASCII 字符和双字节字符）的类别名称。

#### 检测过程

定义 MEL 过程，然后使用 -instrumentMel 标志检测此过程。以下示例演示了如何启用称为 *Factorial* 的过程的检测。

```text
profiler -instrumentMel true -procedureName "Factorial" -categoryIndex $melCategoryIndex -colorIndex 8 -procedureDescription "FactorialDesc" ;
```

您可以禁用一个或多个过程的检测。若要禁用特定过程的检测，请将 -instrumentMel 设置为 False，并提供要禁用检测的过程的名称：

```text
profiler -instrumentMel false -procedureName "Factorial" -categoryIndex $melCategoryIndex;
```

若要同时禁用所有检测，请使用 -clearAllMelInstrumentation 标志：

```text
profiler -clearAllMelInstrumentation;
```

有关上文提到的标志以及其他有用标志（例如：-eventCount，用于查询缓冲区中的事件计数；或 -reset，用于重置“分析器”(Profiler)的数据）的详细信息，请参见 profiler MEL 命令文档。

有关如何与“分析器”(Profiler)的主视图交互的信息，请参见 profilerTool MEL 命令文档。例如，可以在视图之间切换，或者隔离特定的分段。

### 使用 Python

#### 录制

若要启用和禁用事件录制，请将采样分别设置为 True 和 False，如下所示：

```text
cmds.profiler(sampling = True)
cmds.polyCube()
cmds.profiler(sampling = False)
```

#### 添加类别

若要添加分析类别，请调用 OpenMaya.MProfiler.addCategory()，如下所示：

```text
categoryIndex = OpenMaya.MProfiler.addCategory("Python Scripts")
```

#### 检测过程

若要检测过程，请在过程定义中调用 OpenMaya.MProfilingScope()；如下所示：

```text
def Factorial(number):
    # Instrument this procedure
    profiler = OpenMaya.MProfilingScope(categoryIndex, OpenMaya.MProfiler.kColorE_L1, "Factorial", "FactorialDesc")

    result = 1
    for i in range(1, number+1):
        result = result * i
    return result
```

有关上文提到的标志以及其他有用标志（例如：eventCount，用于查询缓冲区中的事件计数；或 reset，用于重置“分析器”(Profiler)的数据）的详细信息，请参见 profiler Python 命令文档。Python 可以使用 -instrumentMel 标志来检测 MEL 过程。

**注**

如果执行大量的 Python 命令，可能会出现性能问题。如果发生这种情况，请在环境中定义 MAYA_RETAIN_PYTHON_GIL。（MAYA_RELEASE_PYTHON_GIL 已弃用。它默认为 true，并且可被 MAYA_RETAIN_PYTHON_GIL 覆盖。）

此外，使用自定义 Python 节点对其他线程求值时，也有可能会出现 Python 性能问题。

有关如何与“分析器”(Profiler)的主视图交互的信息，请参见 profilerTool Python 命令文档。例如，可以在视图之间切换，或者隔离特定的分段。

## 在您的插件中检测函数

可以在插件中调用 MProfiler::addCategory() 方法，向“分析器”(Profiler)中添加类别。调用 MProfilingScope::MProfilingScope() 以检测要分析的函数。详细信息请参见 MProfiler 和 MProfilingScope C++ API 参考文档，以及 Maya 开发人员帮助中的 *Autodesk Maya 2015 Extension 新特性*。

## 检测过程并注册关联的 DG 节点

使用 Python 或 C++ 检测过程时，也可以注册关联的 DG 节点。这样，在分析器图表中选择检测到的事件时，在属性编辑器、大纲视图或节点编辑器中也会选择并显示其关联的 DG 节点。

为此，在 Python 脚本或 C++ 插件中调用 MProfilingScope::MProfilingScope() 时，将关联的 DG 节点作为 MObject（输入参数之一）提供。MObject 输入参数必须指向 DG 节点，而不能指向属性或组件。

详细信息请参见 OpenMaya::MProfilingScope() C++ API 参考文档，以及 Maya 开发人员帮助中的“Autodesk Maya 2016 新特性”。

## 相关主题

- [分析器](分析器.md)

- [分析器标记菜单](分析器/分析器标记菜单.md)

- [分析器菜单](分析器/分析器菜单.md)
