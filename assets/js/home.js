$(document).ready(function(){
	console.log('up and running');

	var awardsJSONpath = 'https://api.myjson.com/bins/wecf';
	var popJSONpath = 'https://api.myjson.com/bins/2zeyn';
	var unpopJSONpath = 'https://api.myjson.com/bins/4w03j';

	$.getJSON(awardsJSONpath, function(data){
		var jsonData = data;
		var awards = jsonData.awards
		//console.log(awards);

		$('.awardCount').append(Object.keys(awards).length);
		$('.time').append(jsonData.time);
		$('.tweets').append(jsonData.tweets);

		Object.keys(awards).forEach(function(key){
			if (awards[key].presenters[1] == undefined)
				awards[key].presenters[1] = "";

			//console.log(key, awards[key]);
			$('#awards').append("<div class='col-md-4 mb col-sm-4'><div class='award-panel pn centered'><h2>" + key + "</h2><h3 class='centered winner'>" + awards[key].winner + "</h3><h4 class='presenters'>Presenters:</h4><p>" + awards[key].presenters[0] + "</p><p>" + awards[key].presenters[1] + "</p></div></div>");
		});
	});

	$.getJSON(popJSONpath, function(data){
		var celebs = data;
		Object.keys(celebs).forEach(function(key){
			$('#pop').append("<div class='col-md-4 mb col-sm-4'><div class='fun-panel pn centered'><h1>" + key + "</h1><h4 class='adj'>" + celebs[key][2][0] + "</h4><h4 class='adj'>" + celebs[key][2][1] + "</h4><h4 class='adj'>" + celebs[key][2][2] + "</h4><h3>Popularity: " + Math.round(celebs[key][0]*100) + "%</h3></div></div>");
		});
	});

	$.getJSON(unpopJSONpath, function(data){
		var celebs = data;
		Object.keys(celebs).forEach(function(key){
			$('#unpop').append("<div class='col-md-4 mb col-sm-4'><div class='fun-panel pn centered'><h1>" + key + "</h1><h4 class='adj'>" + celebs[key][2][0] + "</h4><h4 class='adj'>" + celebs[key][2][1] + "</h4><h4 class='adj'>" + celebs[key][2][2] + "</h4><h3>Popularity: " + Math.round(celebs[key][0]*100) + "%</h3></div></div>");
		});
	});

	$('#awards-btn').click(function(event){
		$('#fun').hide('slow');
		$('#awards').show('slow');
	});

	$('#fun-btn').click(function(event){
		$('#awards').hide('slow');
		$('#fun').show('slow');
	});

	/*
	var checked = true;
	$('#toggle').click(function(event){
		checked = !checked;
		$('.check1').each(function(){
			this.checked = checked;
		});
	}); */
	
});