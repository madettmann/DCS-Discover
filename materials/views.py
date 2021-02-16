from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from .models import Material
import os
from bokeh.models import ColumnDataSource, MultiLine
from bokeh.io import show, curdoc, output_file
from bokeh.models.widgets import Button, TextInput
from bokeh.layouts import layout, widgetbox, row, column
from .PlotINS import GetXY
from bokeh.plotting import figure
from bokeh.models import CheckboxButtonGroup, CustomJS
from jsmol_bokeh_extension import JSMol
from bokeh.resources import CDN
from bokeh.embed import components
import plotly.graph_objects as go
import plotly.offline as opy



    
def get_layout(material):
    data_folder = os.getcwd()
    exp_data_x, exp_data_y, exp_max = GetXY(data_folder+material.experimental_data_file, type="exp")    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=exp_data_x, y=exp_data_y, mode='lines', name='Experimental'))
    offset = exp_max
    if material.dft_data_file:
        dft_data_x, dft_data_y, max_dft = GetXY(data_folder+material.dft_data_file, type="fdsm")
        dft_scaler = exp_max/max_dft 
        dft_data_y = [(val * dft_scaler)+offset for val in dft_data_y]
        offset += exp_max
        fig.add_trace(go.Scatter(x=dft_data_x, y=dft_data_y, mode='lines', name='DFT'))
    if material.dftb_data_file:
        dftb_data_x, dftb_data_y, dftb_max = GetXY(data_folder+material.dftb_data_file, type="fdsm")
        dftb_scaler = exp_max/dftb_max
        dftb_data_y = [(val * dftb_scaler) + offset for val in dftb_data_y]
        offset += exp_max
        fig.add_trace(go.Scatter(x=dftb_data_x, y=dftb_data_y, mode='lines', name='DFTB+')) 
    if material.chimes_data_file:
        chimes_data_x, chimes_data_y, chimes_max = GetXY(data_folder+material.chimes_data_file, type="fdsm")
        chimes_scaler = exp_max/chimes_max
        chimes_data_y = [(val * chimes_scaler) + offset for val in chimes_data_y]
        fig.add_trace(go.Scatter(x=chimes_data_x, y=chimes_data_y, mode='lines', name='DFTB+ w/ ChIMES'))
    fig.update_xaxes(range=[10, 1500], title_text='Energy (cm<sup>-1</sup>)')
    fig.update_yaxes(range=[0, (exp_max*1.1 + offset)], title_text='Intensity (AU)')
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ),
    margin=dict(l=20, r=20, t=20, b=20))
    div = opy.plot(fig, auto_open=False, output_type='div')
    return div


# Create your views here.
def material_list_view(request):
    my_materials = get_list_or_404(Material)
    cwd = os.getcwd()
    context = {"materials_list": my_materials, "my_cwd": cwd }
    return render(request, "materials.html", context)

def material_detail_view(request, id=None):
    my_material = get_object_or_404(Material, id=id)
    layout = get_layout(my_material)
    context = {"material": my_material, "layout": layout}
    return render(request, "material-detail.html", context)

def search_results_view(request):
    query = request.GET.get('q')
    my_materials = Material.objects.filter(Q(compound_name__icontains=query) | Q(iupac_name__icontains=query))
    cwd = os.getcwd()
    context = {"materials_list": my_materials, "my_cwd": cwd}
    return render(request, "materials.html", context)

def about_view(request):
    context = {}
    return render(request, "about.html", context)
