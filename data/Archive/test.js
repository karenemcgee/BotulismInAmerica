d3.csv('static/botulism_pivot.csv', function(data) {
// CSV section
  var body = d3.select('#stacey')
  var selectData = [ { "text" : "Foodborne" },
                     { "text" : "Infant" },
                     { "text" : "Wound" },
                   ]

console.log(data)


  // Select X-axis Variable
  var span = body.append('span')
    .text('Select X-Axis variable: ')
  var yInput = body.append('select')
      .attr('id','xSelect')
      .on('change',xChange)
    .selectAll('option')
      .data(selectData)
      .enter()
    .append('option')
      .attr('value', function (d) { return d.text })
      .text(function (d) { return d.text ;})
  body.append('br')

  // Select Y-axis Variable
  var span = body.append('span')
      .text('Select Y-Axis variable: ')
  var yInput = body.append('select')
      .attr('id','ySelect')
      .on('change',yChange)
    .selectAll('option')
      .data(selectData)
      .enter()
    .append('option')
      .attr('value', function (d) { return d.text })
      .text(function (d) { return d.text ;})
  body.append('br')

  // Variables
  var body = d3.select('#stacey')
  var margin = { top: 50, right: 50, bottom: 50, left: 50 }
  var h = 500 - margin.top - margin.bottom
  var w = 500 - margin.left - margin.right
  //var formatPercent = d3.format('.2%')
  // Scales
//  var colorScale = d3.schemeCategory10
  var xScale = d3.scaleLinear()
  .domain([0, 1000])
//  .domain([d3.min(data, d => d.Foodborne), d3.max(data, d => d.Foodborne)])
//    .domain([
//      d3.min([0,d3.min(data,function (d) { return d['Foodborne'] })]),
//      d3.max([0,d3.max(data,function (d) { return d['Foodborne'] })])
//      ])
  .range([0,w])
  var yScale = d3.scaleLinear()
  .domain([0, 1000])
//    .domain([d3.min(data, d => d.Foodborne), d3.max(data, d => d.Foodborne)])
//    .domain([
//      d3.min([0,d3.min(data,function (d) { return d['Foodborne'] })]),
//      d3.max([0,d3.max(data,function (d) { return d['Foodborne'] })])
//      ])
  .range([h,0])
  // SVG
  var svg = body.append('svg')
      .attr('height',h + margin.top + margin.bottom)
      .attr('width',w + margin.left + margin.right)
    .append('g')
      .attr('transform','translate(' + margin.left + ',' + margin.top + ')')
  // X-axis
  var xAxis = d3.axisBottom(xScale)
//    .scale(xScale)
//    .tickFormat(formatPercent)
//   .ticks(5)
//    .orient('bottom')
  // Y-axis
  var yAxis = d3.axisLeft(yScale)
//    .scale(yScale)
//    .tickFormat(formatPercent)
//    .ticks(5)
//    .orient('left')
  // Circles
  var circles = svg.selectAll('circle')
      .data(data)
      .enter()
    .append('circle')
      .attr('cx',function (d) { return xScale(d['Foodborne']) })
      .attr('cy',function (d) { return yScale(d['Foodborne']) })
      .attr('r','10')
      .attr('stroke','black')
      .attr('stroke-width',1)
      .attr('fill',  'pink')   //function (d,i) { return colorScale(i) })
      .on('mouseover', function () {
        d3.select(this)
          .transition()
          .duration(500)
          .attr('r',20)
          .attr('stroke-width',3)
      })
      .on('mouseout', function () {
        d3.select(this)
          .transition()
          .duration(500)
          .attr('r',10)
          .attr('stroke-width',1)
      })
      .append('title') // Tooltip
      .text(function (d) { return d.variable +
                           '\nFoodborne: ' + (d['Foodborne']) +
                           '\nInfant: ' + (d['Infant']) +
                           '\nWound: ' + (d['Wound']) })
  // X-axis
  svg.append('g')
      .attr('class','axis')
      .attr('id','xAxis')
      .attr('transform', 'translate(0,' + h + ')')
      .call(xAxis)
    .append('text') // X-axis Label
      .attr('id','xAxisLabel')
      .attr('y',-10)
      .attr('x',w)
      .attr('dy','.71em')
      .style('text-anchor','end')
      .text('Foodborne')
  // Y-axis
  svg.append('g')
      .attr('class','axis')
      .attr('id','yAxis')
      .call(yAxis)
    .append('text') // y-axis Label
      .attr('id', 'yAxisLabel')
      .attr('transform','rotate(-90)')
      .attr('x',0)
      .attr('y',5)
      .attr('dy','.71em')
      .style('text-anchor','end')
      .text('Foodborne')

  function yChange() {
    var value = this.value // get the new y value
    yScale // change the yScale
    .domain([0,1000])
//      .domain([
//        d3.min([0,d3.min(data,function (d) { return d[value] })]),
//        d3.max([0,d3.max(data,function (d) { return d[value] })])
//        ])
    yAxis.scale(yScale) // change the yScale
    d3.select('#yAxis') // redraw the yAxis
      .transition().duration(1000)
      .call(yAxis)
    d3.select('#yAxisLabel') // change the yAxisLabel
      .text(value)    
    d3.selectAll('circle') // move the circles
      .transition().duration(1000)
      .delay(function (d,i) { return i*100})
        .attr('cy',function (d) { return yScale(d[value]) })
  }

  function xChange() {
    var value = this.value // get the new x value
    xScale // change the xScale
    .domain([0,1000])
//      .domain([
//        d3.min([0,d3.min(data,function (d) { return d[value] })]),
//        d3.max([0,d3.max(data,function (d) { return d[value] })])
//        ])
    xAxis.scale(xScale) // change the xScale
    d3.select('#xAxis') // redraw the xAxis
      .transition().duration(1000)
      .call(xAxis)
    d3.select('#xAxisLabel') // change the xAxisLabel
      .transition().duration(1000)
      .text(value)
    d3.selectAll('circle') // move the circles
      .transition().duration(1000)
      .delay(function (d,i) { return i*100})
        .attr('cx',function (d) { return xScale(d[value]) })
  }
})
