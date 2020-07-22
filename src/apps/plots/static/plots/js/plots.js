$(document).ready(function() {
    let graph = document.getElementById("plotly-plot-id");
    if (graph != null) {
        plot_country(graph);
    };
});

async function plot_country(graph) {
    let x = [1, 2, 3];
    //let y = [1, 4, 9];
    let country_data = await get_country_data();
    let y = country_data.y

    var scatter_points = {
        x: x,
        y: y,
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
    data = graph.data.concat(scatter_points)

    Plotly.react(graph, data, graph.layout, graph.config)
};

async function get_country_data() {
    let payload = {};
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

    return JSON.parse(response_txt)
};