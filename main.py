from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, BoxAnnotation

from bokeh.plotting import figure
from bokeh.models import CategoricalColorMapper,Slider,HoverTool, Select,Label
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row

import pandas as pd

df1=pd.read_csv("1.csv")
df2=pd.read_csv("2.csv")
df3=pd.read_csv("3.csv")
df4=pd.read_csv("4.csv")
df5=pd.read_csv("5.csv")
df6=pd.read_csv("6.csv")
df7=pd.read_csv("7.csv")
df8=pd.read_csv("8.csv")
df9=pd.read_csv("9.csv")
df10=pd.read_csv("10.csv")
df11=pd.read_csv("11.csv")
df12=pd.read_csv("12.csv")

df21=pd.read_csv("21.csv")
df22=pd.read_csv("22.csv")
df23=pd.read_csv("23.csv")
df24=pd.read_csv("24.csv")
df25=pd.read_csv("25.csv")
df26=pd.read_csv("26.csv")
df27=pd.read_csv("27.csv")
df28=pd.read_csv("28.csv")
df29=pd.read_csv("29.csv")
df210=pd.read_csv("210.csv")
df211=pd.read_csv("211.csv")
df212=pd.read_csv("212.csv")

df31=pd.read_csv("31.csv")
df32=pd.read_csv("32.csv")
df33=pd.read_csv("33.csv")


df1=df1.set_index("DAY")
df2=df2.set_index("DAY")
df3=df3.set_index("DAY")
df4=df4.set_index("DAY")
df5=df5.set_index("DAY")
df6=df6.set_index("DAY")
df7=df7.set_index("DAY")
df8=df8.set_index("DAY")
df9=df9.set_index("DAY")
df10=df10.set_index("DAY")
df11=df11.set_index("DAY")
df12=df12.set_index("DAY")

df21=df21.set_index("DAY")
df22=df22.set_index("DAY")
df23=df23.set_index("DAY")
df24=df24.set_index("DAY")
df25=df25.set_index("DAY")
df26=df26.set_index("DAY")
df27=df27.set_index("DAY")
df28=df28.set_index("DAY")
df29=df29.set_index("DAY")
df210=df210.set_index("DAY")
df211=df211.set_index("DAY")
df212=df212.set_index("DAY")

df31=df31.set_index("DAY")
df32=df32.set_index("DAY")
df33=df33.set_index("DAY")


columns = list(df1.columns)
units = list(range(int(columns[0]), int(columns[-1])))
rename_dict = dict(zip(columns, units))

df1 = df1.rename(columns=rename_dict)
df2 = df2.rename(columns=rename_dict)
df3 = df3.rename(columns=rename_dict)
df4 = df4.rename(columns=rename_dict)
df5 = df5.rename(columns=rename_dict)
df6 = df6.rename(columns=rename_dict)
df7 = df7.rename(columns=rename_dict)
df8 = df8.rename(columns=rename_dict)
df9 = df9.rename(columns=rename_dict)
df10 = df10.rename(columns=rename_dict)
df11= df11.rename(columns=rename_dict)
df12= df12.rename(columns=rename_dict)

df21 = df21.rename(columns=rename_dict)
df22 = df22.rename(columns=rename_dict)
df23 = df23.rename(columns=rename_dict)
df24 = df24.rename(columns=rename_dict)
df25 = df25.rename(columns=rename_dict)
df26 = df26.rename(columns=rename_dict)
df27 = df27.rename(columns=rename_dict)
df28 = df28.rename(columns=rename_dict)
df29 = df29.rename(columns=rename_dict)
df210 = df210.rename(columns=rename_dict)
df211= df211.rename(columns=rename_dict)
df212= df212.rename(columns=rename_dict)

df31 = df31.rename(columns=rename_dict)
df32 = df32.rename(columns=rename_dict)
df33 = df33.rename(columns=rename_dict)

source = ColumnDataSource(data={
    'x'       : list(df1.index),
    'y'       : df1[1].tolist(),
    'z':df1[1].abs().tolist(),
    
})

plot=figure()

label = Label(x=0, y=-20, text=str(units[0]), text_font_size='70pt', text_color='#eeeeee')

plot.add_layout(label)
plot.circle(x='x', y='y',size='z', source=source)
plot.add_tools(HoverTool(tooltips="@y", show_arrow=False, point_policy='follow_mouse'))
plot.title.text = "Disturbance storm time (Dst) index"
plot.title.align = "left"
plot.title.text_color = "black"
plot.title.text_font_size = "25px"


plot.xaxis.axis_label ='DAY'
plot.legend.location = 'top_right' 
# Set the y-axis label
plot.yaxis.axis_label = 'Dst value'

   

def update_plot(attr, old, new):
    # set the `slv` name to `slider.value` and `source.data = new_data`
    slv = slider.value
    m=month_select.value
    yr=year_select.value
    label.text = str(slv)+"nT"
    # Set new_data
    if yr=='2016':
        if m=='JANUARY':
         new_data= {
         'x'       : list(df1.index),
         'y'       : df1[slv].tolist(),
         'z':df1[slv].abs().tolist()
                           }
        elif m=='FEBRUARY':
          new_data={
         'x'       : list(df2.index),
         'y'       : df2[slv].tolist(),
         'z':df2[slv].abs().tolist()
                            }
        elif m=='MARCH':
          new_data={
          'x'       : list(df3.index),
          'y'       : df3[slv].tolist(),
          'z':df3[slv].abs().tolist()
                            }
        elif m=='APRIL':
          new_data={
          'x'       : list(df4.index),
          'y'       : df4[slv].tolist(),
          'z':df5[slv].abs().tolist()
                            }
        elif m=='MAY':
          new_data={
          'x'       : list(df5.index),
          'y'       : df5[slv].tolist(),
          'z':df5[slv].abs().tolist()
                            }
        elif m=='JUNE':
           new_data={
           'x'       : list(df6.index),
           'y'       : df6[slv].tolist(),
           'z':df6[slv].abs().tolist()
                            }
        elif m=='JULY':
           new_data={
           'x'       : list(df7.index),
           'y'       : df7[slv].tolist(),
           'z':df7[slv].abs().tolist()
                            }

        elif m=='AUGUST':
            new_data={
            'x'       : list(df8.index),
            'y'       : df8[slv].tolist(),
            'z':df8[slv].abs().tolist()
                            }

        elif m=='SEPTEMBER':
            new_data={
            'x'       : list(df9.index),
            'y'       : df9[slv].tolist(),
            'z':df9[slv].abs().tolist()
                            }
        elif m=='OCTOBER':
            new_data={
            'x'       : list(df10.index),
            'y'       : df10[slv].tolist(),
            'z':df10[slv].abs().tolist()
                            }
        elif m=='NOVEMBER':
            new_data={
            'x'       : list(df11.index),
            'y'       : df11[slv].tolist(),
            'z':df11[slv].abs().tolist()
                            }
        else:
            new_data={
            'x'       : list(df12.index),
            'y'       : df12[slv].tolist(),
            'z':df12[slv].abs().tolist()
                            }

    elif yr=='2017':
        if m=='JANUARY':
            new_data= {
            'x'       : list(df21.index),
            'y'       : df21[slv].tolist(),
            'z':df21[slv].abs().tolist()
                           }
        elif m=='FEBRUARY':
            new_data={
            'x'       : list(df22.index),
            'y'       : df22[slv].tolist(),
            'z':df22[slv].abs().tolist()
                            }
        elif m=='MARCH':
            new_data={
            'x'       : list(df23.index),
            'y'       : df23[slv].tolist(),
            'z':df23[slv].abs().tolist()
                            }
        elif m=='APRIL':
            new_data={
            'x'       : list(df24.index),
            'y'       : df24[slv].tolist(),
            'z':df24[slv].abs().tolist()
                            }
        elif m=='MAY':
            new_data={
            'x'       : list(df25.index),
            'y'       : df25[slv].tolist(),
            'z':df25[slv].abs().tolist()
                            }
        elif m=='JUNE':
            new_data={
            'x'       : list(df26.index),
            'y'       : df26[slv].tolist(),
            'z':df26[slv].abs().tolist()
                            }
        elif m=='JULY':
            new_data={
            'x'       : list(df27.index),
            'y'       : df27[slv].tolist(),
            'z':df27[slv].abs().tolist()
                            }

        elif m=='AUGUST':
            new_data={
            'x'       : list(df28.index),
            'y'       : df28[slv].tolist(),
            'z':df28[slv].abs().tolist()
                            }

        elif m=='SEPTEMBER':
            new_data={
            'x'       : list(df29.index),
            'y'       : df29[slv].tolist(),
            'z':df29[slv].abs().tolist()
                            }
        elif m=='OCTOBER':
            new_data={
            'x'       : list(df210.index),
            'y'       : df210[slv].tolist(),
            'z':df210[slv].abs().tolist()
                            }
        elif m=='NOVEMBER':
            new_data={
            'x'       : list(df211.index),
            'y'       : df211[slv].tolist(),
            'z':df211[slv].abs().tolist()
                            }
        else:
            new_data={
            'x'       : list(df212.index),
            'y'       : df212[slv].tolist(),
            'z':df212[slv].abs().tolist()
                            }
    else:
        if m=='JANUARY':
            new_data= {
            'x'       : list(df31.index),
            'y'       : df31[slv].tolist(),
            'z':df31[slv].abs().tolist()
                           }
        elif m=='FEBRUARY':
            new_data={
            'x'       : list(df32.index),
            'y'       : df32[slv].tolist(),
            'z':df32[slv].abs().tolist()
                            }
        elif m=='MARCH':
            new_data={
            'x'       : list(df33.index),
            'y'       : df33[slv].tolist(),
            'z':df33[slv].abs().tolist()
                            }
       
        else:
            new_data={
            'x'       : list(df31.index),
            'y'       : df31[slv].tolist(),
            'z':df3[slv].abs().tolist()
                            }


    # Assign new_data to sour ce.data
    source.data = new_data
    # Set the range of all axes
  

# Make a slider object: slider
slider = Slider(start=1, end=24, step=1, value=1, title='unit=nT')


# Make a row layout of widgetbox(slider) and plot and add it to the current document
month_select = Select(
    options=['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL','MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'],
    value='JANUARY',
    title='MONTH'
)

year_select = Select(
    options=['2016', '2017','2018'],
    value='2016',
    title='YEAR'
)

# Attach the update_plot callback to the 'value' property of month_select
year_select.on_change('value', update_plot)
month_select.on_change('value', update_plot)
# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select

layout = row( plot,widgetbox(year_select, month_select,slider))


# Add the plot to the current document and add a title
curdoc().add_root(layout)
curdoc().title = ' Hourly Equatorial Dst Values (REAL-TIME)'


