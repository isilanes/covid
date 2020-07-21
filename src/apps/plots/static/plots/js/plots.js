$(document).ready(function() {
    let graph = document.getElementById("plotly-plot-id");
    if (graph != null) {
        plot_country(graph);
    };
});

function plot_country(graph) {
    let x = [1, 2, 3];
    let y = [1, 4, 9];

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