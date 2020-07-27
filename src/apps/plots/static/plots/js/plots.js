$(document).ready(function() {
});

// See: https://simonwillison.net/2004/May/26/addLoadEvent/
function addLoadEvent(func) {
  var old_onload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (old_onload) {
        old_onload();
      }
      func();
    }
  }
};

function on_plot_view_load() {
    let graph = document.getElementById("plotly-plot-id");
    if (graph != null) {
        plot_country(graph);
    };
};

async function plot_country(graph) {
    let x = [0, 1, 2, 3, 4, 5];

    for (let i = 2; i < 4; i++) {
        let country_data = await get_country_data(i);

        let scatter_points = {
            x: x,
            y: country_data.y,
            mode: 'lines+markers',
            marker: {
                size: 6,
                type: 'scatter',
            },
            line: {
                size: 3,
                dash: "dash",
            }
        };
        graph.data = graph.data.concat(scatter_points)
    };

    Plotly.react(graph, graph.data, graph.layout, graph.config)
};

async function get_country_data(i) {
    let payload = {
        "exponent": i,
    };
    let response = await fetch("/plots/get_country_data",
        {
            method: "POST",
            headers: {
                "Content-Type": 'application/x-www-form-urlencoded',
            },
            body: "payload=" + JSON.stringify(payload),
        }
    );
    response_txt = await response.text();

    return JSON.parse(response_txt);
};