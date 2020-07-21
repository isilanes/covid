import bs4

import plotly.graph_objects as go
from plotly.offline import plot as offplot


PLOTLY_PLOT_ID = "plotly-plot-id"


def get_progress_plot_div():
    """Return <div> of Plotly plot."""

    figure = go.Figure()

    figure.update_layout(
        showlegend=True,
    )

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

    div = offplot(figure, output_type="div", include_plotlyjs=False, config=config)

    return insert_custom_plotly_id(div)


def insert_custom_plotly_id(plotly_div):
    """
    Substitute automatically-generated ID with custom one.
    Return original div if no substitution happened.
    """
    soup = bs4.BeautifulSoup(plotly_div, features="html.parser")
    div = soup.div.div
    if div is not None:
        old_id = soup.div.div["id"]
        return plotly_div.replace(old_id, PLOTLY_PLOT_ID)

    return plotly_div
