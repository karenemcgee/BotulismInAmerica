
//building both state charts
function buildStateCharts(state) {

    var dropdown = d3.select("#stateSelect")
    var state = dropdown.property("value");
    
    var url = `/statecharts/${state}`;

    d3.json(url).then(function(data) {

        var years = data.years;
        var foodborne = data.foodborne;
        var infant = data.infant;
        var wound = data.wound;
        var other = data.other;
        var unknownTox = data.unknownTox;
        var ETox = data.ETox;
        var BTox = data.BTox;
        var ATox = data.ATox;
        var FTox = data.FTox;
        var ABTox = data.ABTox;
        var BaTox = data.BaTox;
        var BfTox = data.BfTox;
        var EFTox = data.EFTox; 
        var ABETox = data.ABETox;
        var AbTox = data.AbTox;
        var BFTox = data.BFTox;
        
        var traceBot = {
            x: years,
            y: foodborne,
            mode: 'markers',
            marker: {
                color: 'OliveDrab'
            },
            name: 'Foodborne',
            type: 'scatter'
          };
        
        var traceBot1 = {
            x: years,
            y: infant,
            mode: 'markers',
            marker: {
                color: 'LightSalmon'
            },
            name: 'Infant',
            type: 'scatter'
          };

        var traceBot2 = {
            x: years,
            y: wound,
            mode: 'markers',
            marker: {
                color: 'Gray'
            },
            name: 'Wound',
            type: 'scatter'
          };

        var traceBot3 = {
            x: years,
            y: other,
            mode: 'markers',
            marker: {
                color: 'Black'
            },
            name: 'Other',
            type: 'scatter'
          };


        var stateBot = [traceBot, traceBot1, traceBot2, traceBot3];
        var layoutBot = {
            title:'Botulism Types',
            xaxis: {
                title: 'Years'
              },
              yaxis: {
                title: 'Number of Cases'
              }
          };
        Plotly.newPlot("stateBot", stateBot, layoutBot)

        var traceTox = {
            x: years,
            y: unknownTox,
            mode: 'markers',
            marker: {
                color: 'DarkOliveGreen'
            },
            name: 'Unknown',
            type: 'scatter'
          };

        var traceTox1 = {
            x: years,
            y: ETox,
            mode: 'markers',
            marker: {
                color: 'Gray'
            },
            name: 'E',
            type: 'scatter'
          };

        var traceTox2 = {
            x: years,
            y: BTox,
            mode: 'markers',
            marker: {
                color: 'LightSalmon'
            },
            name: 'B',
            type: 'scatter'
          };

        var traceTox3 = {
            x: years,
            y: ATox,
            mode: 'markers',
            marker: {
                color: 'Black'
            },
            name: 'A',
            type: 'scatter'
          };

        var traceTox4 = {
            x: years,
            y: FTox,
            mode: 'markers',
            marker: {
                color: 'CadetBlue'
            },
            name: 'F',
            type: 'scatter'
          };

        var traceTox5 = {
            x: years,
            y: ABTox,
            mode: 'markers',
            marker: {
                color: 'DarkGoldenRod'
            },
            name: 'AB',
            type: 'scatter'
          };

        var traceTox6 = {
            x: years,
            y: BaTox,
            mode: 'markers',
            marker: {
                color: 'Coral'
            },
            name: 'Ba',
            type: 'scatter'
          };

        var traceTox7 = {
            x: years,
            y: BfTox,
            mode: 'markers',
            marker: {
                color: 'DarkKhaki'
            },
            name: 'Bf',
            type: 'scatter'
          };

        var traceTox8 = {
            x: years,
            y: EFTox,
            mode: 'markers',
            marker: {
                color: 'IndianRed'
            },
            name: 'EF',
            type: 'scatter'
          };

        var traceTox9 = {
            x: years,
            y: ABETox,
            mode: 'markers',
            marker: {
                color: 'Turquoise'
            },
            name: 'ABE',
            type: 'scatter'
          };

        var traceTox10 = {
            x: years,
            y: AbTox,
            mode: 'markers',
            marker: {
                color: 'YellowGreen'
            },
            name: 'Ab',
            type: 'scatter'
          };

        var traceTox11 = {
            x: years,
            y: BFTox,
            mode: 'markers',
            marker: {
                color: 'Silver'
            },
            name: 'BF',
            type: 'scatter'
          };

        var stateTox = [traceTox, traceTox1, traceTox2, traceTox3, traceTox4, traceTox5, traceTox6, traceTox7, traceTox8, traceTox9, traceTox10, traceTox11];
        var layoutTox = {
            title:'Toxin Types',
            xaxis: {
                title: 'Years'
              },
              yaxis: {
                title: 'Number of Cases'
              }
          };
        Plotly.newPlot("stateTox", stateTox, layoutTox)
    });

}

//build initial state charts
function stateInit() {

    var selector = d3.select("#stateSelect");

    d3.json("/states").then((stateNames) => {
        stateNames.forEach((state) => {
            selector
                .append("option")
                .text(state)
                .property("value", state);
        });

        const firstState = stateNames[0];
        buildStateCharts(firstState);

        console.log(firstState);
    });
}

//Fetch new data each time a new state is selected
function stateChange(newState) {

    buildStateCharts(newState);
    
}

//Initialize the state section
stateInit();

