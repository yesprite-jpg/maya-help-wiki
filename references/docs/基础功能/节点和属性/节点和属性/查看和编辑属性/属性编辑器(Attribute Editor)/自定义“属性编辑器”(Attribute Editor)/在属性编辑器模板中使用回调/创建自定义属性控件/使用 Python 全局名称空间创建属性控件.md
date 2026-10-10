# 使用 Python 全局名称空间创建属性控件

若要使用 Python 全局名称空间创建属性控件，请完成以下步骤：

- [创建属性控件](使用%20Python%20全局名称空间创建属性控件.md#GUID-F4411BAF-9F15-46C1-9D75-C535D3FB3A67__SECTION_2D1243DBC43147378192B1FA5CF68DC1)

- [定义 Python 程序](使用%20Python%20全局名称空间创建属性控件.md#GUID-F4411BAF-9F15-46C1-9D75-C535D3FB3A67__SECTION_9CD59D3C07134718B4B7E37CCEE698CF)

- [定义对 Python 程序的回调](使用%20Python%20全局名称空间创建属性控件.md#GUID-F4411BAF-9F15-46C1-9D75-C535D3FB3A67__SECTION_C2AB1346705F40D49F0C795EA1D8833D)

## **创建属性控件**

在下面的示例中，将使用 Python 全局名称空间方法创建一个滑块控件。回调名为 AEFloatSliderGlobal。此程序会创建 floatSlider 控件，然后该控件使用更改命令 AEaddFloatSliderGlobalCB。

```text
def AEaddFloatSliderGlobalCB( plug, slider ):
	val = cmds.floatSlider( slider, q=1, v=1 )
	cmds.setAttr( plug, val )

def AEaddFloatSliderGlobal( plug, sliderLabel, annot ):
	cmds.rowLayout( nc=2 )
	val = cmds.getAttr( plug )
	cmds.text( label=sliderLabel )
	slider = cmds.floatSlider( annotation=annot, v=val )
	cmds.floatSlider( slider, e=1, cc=('AEaddFloatSliderGlobalCB( \"' + plug + '\", \"' + slider + '\" )' ) )
	cmds.setParent( u=1 )
```

该程序中使用下列参数：

- plug 是栓，即控件使用的节点和属性。

- label 是属性的标签。

- annot 属性的注释。

## 定义 Python 程序

您必须定义 Python 程序，以便 Maya 可以使用它们。在“脚本编辑器”(Script Editor)的 Python 选项卡中执行上述示例的代码可以完成此操作。

## 定义对 Python 程序的回调

当您创建自定义模板文件时，请将 <description language="cb"> 标志添加至属性声明部分以指定对 Python 程序的回调。默认情况下，回调在模板中采用 MEL 进行指定。

若要在全局名称空间中指定名为 AEaddFloatSliderGlobal 的 Python 回调，声明应为 py.AEaddFloatSliderGlobal。声明采用以下格式： py.<ProcedureName>。

若要将在以上 Python 模块中定义的自定义滑块控件添加至“白炽度绿”(Incandescence Green)属性，请采用以下操作：

```text
<attribute name='incandescenceG' type='maya.float'>
   <label>Incandescence Green</label>
     <description language="cb">py.AEaddFloatSliderGlobal</description>
</attribute>
```

在“属性编辑器”(Attribute Editor)中访问属性视图时，“白炽度绿”(Incandescence Green)属性使用自定义的滑块。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-18EFB9C0-36C7-4F85-B428-DB6A2B387CBC.png) <!-- baize:img-hook downloaded=false reason="正文 1234 字 ≥300，非承重" -->

## 相关主题

- [自定义属性编辑器模板](../../../自定义“属性编辑器”%28Attribute%20Editor%29.md)

- [属性编辑器(Attribute Editor)](../../../../属性编辑器%28Attribute%20Editor%29.md)
