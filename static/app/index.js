superagent.get('/writerMetaDataList').end(function(err, res){	
	var source   = $("#entry-template").html();
	var template = Handlebars.compile(source);
	var context = JSON.parse(res.text);
	$("#templatePlaceholder").html(template(context));
});

Handlebars.registerHelper('list',function(items, options){
	var ret = "";
	for(var i = 0; i<items.length; i++) {
		ret = ret + options.fn(items[i])
	}
	return ret;
});


var xAxis;
var yAxis;
superagent.get('/writerTotalViewList').end(function(err, res){
   	var data = JSON.parse(res.text);
	xAxis =  _.map(data, function(item) {
		return item.name;
	});
	yAxis = _.map(data, function(item) {
		return item.viewCount;
	});
	setupHighCharts();
});

var setupHighCharts = function() {
	    $('#chart').highcharts({
	        chart: { type: 'column' },
	        title: { text: 'Total Views per Writer' },
	        subtitle: { text: '' },
	        yAxis: { min: 0, title: { text: 'Views' } },
	        plotOptions: { column: { pointPadding: 0.2, borderWidth: 0 } },
	        xAxis: { 
	        	categories: xAxis
	        },
	        series: [{
	            name: 'Content Views',
	            data: yAxis
	        }]	
	    });
	    // Remove excessive graph info
	   $("svg > text")[1].innerHTML = "January 2010 - " + moment(Date.now()).format("MMMM YYYY");
	   $(".highcharts-legend-item").remove(); 
};

