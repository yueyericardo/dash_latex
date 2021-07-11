import os
import dash
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

###### important for latex ######
import dash_defer_js_import as dji

filepath = os.path.split(os.path.realpath(__file__))[0]

external_stylesheets = ['https://cdn.jsdelivr.net/gh/yueyericardo/simuc@master/apps/dash/resources/dash.css',
                        'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/monokai-sublime.min.css']


app = dash.Dash(name='free_particle',
                external_stylesheets=external_stylesheets)

###### important for latex ######
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                tex2jax: {
                inlineMath: [ ['$','$'],],
                processEscapes: true
                }
            });
            </script>
            {%renderer%}
        </footer>
    </body>
</html>
'''

md_text = open(os.path.join(filepath, "free_particle.md"), "r").read()


def getfig2(k=4, dk=2, xmax=5):
    # Defining functions
    def psi_contour(x, dk):
        return (np.sin(dk*x)/(np.sqrt(np.pi*dk)*x))

    def psi(x, k, dk):
        return psi_contour(x, dk)*(np.cos(k*x)+np.sin(k*x)*1j)

    # calculation (Prepare data)
    x = np.linspace(-xmax, xmax, 900)
    y_real = psi(x, k, dk).real
    y_imag = psi(x, k, dk).imag
    y_prob = (psi(x, k, dk).real)**2+(psi(x, k, dk).imag)**2

    # Plot
    title1 = r'$ \text {Real contribution to } \Psi_{\Delta k}(x)$'
    title2 = r'$ \text {Imaginary contribution to } \Psi_{\Delta k}(x)$'
    title3 = r'$ \text {Probability Density }$'
    fig = make_subplots(
        rows=2, cols=2, subplot_titles=(title1, title2, title3))

    # 1st subplot
    fig.append_trace(go.Scatter(x=x, y=y_real, name="Real",
                                line=dict(color='blue')), row=1, col=1)
    fig.append_trace(go.Scatter(x=x, y=psi_contour(x, dk), showlegend=False, line=dict(
        color='blue', width=1, dash='dash')), row=1, col=1)
    fig.append_trace(go.Scatter(x=x, y=-psi_contour(x, dk), showlegend=False,
                                line=dict(color='blue', width=1, dash='dash')), row=1, col=1)
    fig.update_xaxes(title_text=r"$x (Å)$", row=1, col=1)
    fig.update_yaxes(title_text=r'$\Psi_{\Delta k}(x)$', row=1, col=1)

    # 2nd subplot
    fig.append_trace(go.Scatter(x=x, y=y_imag, name="Imag",
                                line=dict(color='red')), row=1, col=2, )
    fig.append_trace(go.Scatter(x=x, y=psi_contour(x, dk), showlegend=False, line=dict(
        color='red', width=1, dash='dash')), row=1, col=2)
    fig.append_trace(go.Scatter(x=x, y=-psi_contour(x, dk), showlegend=False,
                                line=dict(color='red', width=1, dash='dash')), row=1, col=2)
    fig.update_xaxes(title_text=r"$x (Å)$", row=1, col=2)
    fig.update_yaxes(title_text=r'$\Psi_{\Delta k}(x)$', row=1, col=2)

    # 3rd subplot
    fig.append_trace(go.Scatter(
        x=x, y=y_prob, name="Probability Density", line=dict(color='green')), row=2, col=1)
    fig.update_xaxes(title_text=r"$x (Å)$", row=2, col=1)
    fig.update_yaxes(
        title_text=r'$\left|\Psi_{\Delta k}(x)\right|^2$', row=2, col=1)

    # show
    title = r"$k_o  \pm \Delta k = {} \pm {} Å^{{-1}}$".format(k, dk)
    fig.update_layout(height=600, title_text=title)
    return fig

###### important for latex ######
axis_latex_script = dji.Import(src="https://cdn.jsdelivr.net/gh/yueyericardo/simuc@master/apps/dash/resources/redraw.js")
mathjax_script = dji.Import(src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_SVG")

# fig2
fig2 = dcc.Graph(figure=getfig2(), id="fig2")
sliders2 = html.Div([
    html.Label('The value for $k_0$ (in $ Å^{-\;1} $)'),
    dcc.Slider(id='fig2_k_slider', min=1, max=15, value=4, marks={str(x): str(x) for x in np.arange(1, 16, 1)}, step=1),
    html.Label('The value for $\Delta k$ (in $ Å^{-\;1} $)'),
    dcc.Slider(id='fig2_dk_slider', min=1, max=15, value=2, marks={str(x): str(x) for x in np.arange(1, 16, 1)}, step=1),
    html.Label('the maximum value for x (in Å)'),
    dcc.Slider(id='fig2_xmax_slider', min=1, max=15, value=5, marks={str(x): str(x) for x in np.arange(1, 16, 1)}, step=1),
    ], style={'columnCount': 3, 'padding': '0'})


app.layout = html.Div([
    dcc.Markdown(md_text, dangerously_allow_html=True),
    fig2, sliders2,
    ###### important for latex ######
    axis_latex_script,
    ###### important for latex ######
    mathjax_script,
])


# update_fig2
@app.callback(
    Output('fig2', 'figure'),
    [Input('fig2_k_slider', 'value'),
     Input('fig2_dk_slider', 'value'),
     Input('fig2_xmax_slider', 'value'),
     ])
def update_fig2(k, dk, xmax):
    fig = getfig2(k=k, dk=dk, xmax=xmax)
    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
