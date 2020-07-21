import plotly.graph_objects as go
from plotly.offline import plot as offplot


def get_progress_plot_div():
    """Return <div> of Plotly plot."""

    figure = go.Figure()

    figure.update_layout(
        showlegend=True,
    )

    for country in ["Spain"]:
        x_country = [1, 2, 3, 4]
        y_country = [1, 4, 9, 16]

        country_trace = go.Scatter(
            x=x_country,
            y=y_country,
            mode='lines+text',
            marker={
                "size": 10,
                "color": 'rgba(0, 0, 200, 1.0)',
            },
            line={
                "color": 'green',
                "dash": "dash",
            },
            textposition="top right",
            hoverinfo='x+y',
        )
        figure.add_trace(country_trace)

    config = {
        "displayModeBar": True,
        "modeBarButtons": [
            ["resetScale2d"],
            ["zoom2d"],
            ["lasso2d"],
            ["pan2d"],
        ],
        "scrollZoom": False,
    }

    return offplot(figure, output_type="div", include_plotlyjs=False, config=config)
