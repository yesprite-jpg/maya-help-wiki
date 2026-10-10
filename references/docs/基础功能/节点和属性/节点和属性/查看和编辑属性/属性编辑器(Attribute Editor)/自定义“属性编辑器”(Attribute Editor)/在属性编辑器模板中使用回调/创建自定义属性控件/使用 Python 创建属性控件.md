# 使用 Python 创建属性控件

若要使用 Python 模块中定义的回调创建属性控件，请完成以下步骤：

- [创建属性控件](使用%20Python%20创建属性控件.md#GUID-C71F52F9-5437-45AD-A6B6-B43D6D95E93A__SECTION_2D1243DBC43147378192B1FA5CF68DC1)

- [指定 Python 模块的位置](使用%20Python%20创建属性控件.md#GUID-C71F52F9-5437-45AD-A6B6-B43D6D95E93A__SECTION_9CD59D3C07134718B4B7E37CCEE698CF)

- [定义对 Python 程序的回调](使用%20Python%20创建属性控件.md#GUID-C71F52F9-5437-45AD-A6B6-B43D6D95E93A__SECTION_C2AB1346705F40D49F0C795EA1D8833D)

## **创建属性控件**

在下面的示例中，floatSlider 控件是由 Python 程序 AEaddFloatSliderModule 创建的，并使用了更改命令 AEaddFloatSliderModuleCB。回调 AEFloatSliderModule 在模块 AEaddFloatSlider.py 中定义。

```text
import maya.cmds as cmds

def AEaddFloatSliderModule(	plug, sliderLabel, annot ):

	cmds.rowLayout( nc=2 )
	val = cmds.getAttr( plug )
	cmds.text( label=sliderLabel )
	slider = cmds.floatSlider( annotation=annot, v=val )
	def AEaddFloatSliderModuleCB( *args ):
		val = cmds.floatSlider( slider, q=1, v=1 )
		cmds.setAttr( plug, val )
	cmds.floatSlider( slider, e=1, cc=AEaddFloatSliderModuleCB )
	cmds.setParent( u=1 )
```

Python 程序使用了以下参数：

- plug 是栓，即控件使用的节点和属性。

- label 是属性的标签。

- annot 属性的注释。

## 指定 Python 模块的位置

此步骤为 Maya 提供包含 Python 模块的目录的路径。将 PYTHONPATH 环境变量设置为模块的路径和位置。

## 定义对 Python 程序的回调

创建模板文件时，将 <description language="cb"> 标记添加到属性声明或视图定义中，以指定 Python 程序的回调。

若要指定 Python 模块 AEaddFloatSlider.py 中的 Python 回调 AEaddFloatSliderModule，声明应为 py.AEaddFloatSlider.AEaddFloadSliderModule。声明采用以下格式： py.<ModuleName>。<ProcedureName>。

若要将上述 Python 模块中定义的自定义滑块控件添加至“白炽度蓝色”(Incandescence Blue)属性，请执行如下操作：

```text
<attribute name='incandescenceB' type='maya.float'>
    <label>Incandescence Blue</label>
      <description language="cb">py.AEaddFloatSlider.AEaddFloatSliderModule</description>
</attribute>
```

在“属性编辑器”(Attribute Editor)中访问属性视图时，“白炽度蓝色”(Incandescence Blue)属性会使用自定义的滑块。

![图：（图旁无可取正文，Maya 手册 img 无 alt）](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Basics/images/GUID-676B13E1-BDA2-42DB-AA45-1B04616B0C46.png) <!-- baize:img-hook downloaded=false reason="正文 1269 字 ≥300，非承重" -->

## 相关主题

- [自定义属性编辑器模板](../../../自定义“属性编辑器”%28Attribute%20Editor%29.md)

- [属性编辑器(Attribute Editor)](../../../../属性编辑器%28Attribute%20Editor%29.md)
