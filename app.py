from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import psutil
import speedtest
import plotly.graph_objs as go
from datetime import datetime

# Inicializa o app Dash
app = Dash(__name__)

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Monitoramento de Servidor e Internet'),
    
    # Gráfico de uso da CPU
    dcc.Graph(id='cpu-usage-graph', style={'width': '49%', 'display': 'inline-block'}),
    
    # Gráfico de uso de Memória
    dcc.Graph(id='memory-usage-graph', style={'width': '49%', 'display': 'inline-block'}),
    
    # Gráfico de velocidade da Internet
    dcc.Graph(id='internet-speed-graph', style={'width': '49%', 'display': 'inline-block'}),
    
    # Intervalo para atualizar os gráficos a cada 5 segundos
    dcc.Interval(id='interval-component', interval=5*1000, n_intervals=0)
])

# Função para testar a velocidade da internet
def testar_velocidade_internet():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convertendo para Mbps
    upload_speed = st.upload() / 1_000_000  # Convertendo para Mbps
    return download_speed, upload_speed

# Callback para atualizar os gráficos periodicamente
@app.callback(
    [Output('cpu-usage-graph', 'figure'),
     Output('memory-usage-graph', 'figure'),
     Output('internet-speed-graph', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    # Dados de CPU e Memória
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    # Testa a velocidade da internet
    download_speed, upload_speed = testar_velocidade_internet()

    # Hora atual
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Gráfico de uso da CPU
    cpu_fig = go.Figure(data=[go.Scatter(x=[timestamp], y=[cpu_usage], mode='lines+markers', name='Uso de CPU')])
    cpu_fig.update_layout(title='Uso de CPU (%)', xaxis_title='Tempo', yaxis_title='%')

    # Gráfico de uso de Memória
    memory_fig = go.Figure(data=[go.Scatter(x=[timestamp], y=[memory_usage], mode='lines+markers', name='Uso de Memória')])
    memory_fig.update_layout(title='Uso de Memória (%)', xaxis_title='Tempo', yaxis_title='%')

    # Gráfico de velocidade da Internet
    internet_fig = go.Figure(data=[go.Bar(x=['Download', 'Upload'], y=[download_speed, upload_speed], name='Velocidade da Internet')])
    internet_fig.update_layout(title='Velocidade da Internet (Mbps)', xaxis_title='Tipo', yaxis_title='Mbps')

    return cpu_fig, memory_fig, internet_fig

# Roda a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
