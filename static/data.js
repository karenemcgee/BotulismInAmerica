function addCell(tr, val) {
    var td = document.createElement('td');

    td.innerHTML = val;

    tr.appendChild(td)
  }


  function addRow(tbl, val_1, val_2, val_3) {
    var tr = document.createElement('tr');

    addCell(tr, val_1);
    addCell(tr, val_2);
    addCell(tr, val_3);

    tbl.appendChild(tr)
  }

  function main() {
    tbl = document.getElementById('datatable');

    addRow(tbl, 'foo', 'bar', 'baz');
    addRow(tbl, 'one', 'two', 'three');
  }


// data = d3.json("/allresults").then(function (data) {

//     //console.log(data)

//     //var myList = data
//     //console.log(myList)


//     function makeatable(selector) {
//         var columns = addAllColumnHeaders(data, selector);

//         for (var i = 0; i < data.length; i++) {
//             var row$ = $('<tr/>');
//             for (var colIndex = 0; colIndex < columns.length; colIndex++) {
//                 var cellValue = data[i][columns[colIndex]];
//                 if (cellValue == null) cellValue = "";
//                 row$.append($('<td/>').html(cellValue));
//             }
//             $(selector).append(row$);
//         }
//     }


//     function addAllColumnHeaders(data, selector) {
//         var columnSet = [];
//         var headerTr$ = $('<tr/>');

//         for (var i = 0; i < data.length; i++) {
//             var rowHash = data[i];
//             for (var key in rowHash) {
//                 if ($.inArray(key, columnSet) == -1) {
//                     columnSet.push(key);
//                     headerTr$.append($('<th/>').html(key));
//                 }
//             }
//         }
//         $(selector).append(headerTr$);

//         return columnSet;
//     }




});





    