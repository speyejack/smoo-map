
function from_pix(point) {
	var adjust = [2048-point[0], point[1]];

	return to_map_pos(adjust)
}

function to_map_pos(point) {
	var bounds = get_bounds()

	return [bounds[1][1] - point[1], bounds[1][0] - point[0]]// Switch points cause leaf is crazy
}

var map = L.map('map', {
	crs: L.CRS.Simple,
	minZoom: -2,
	maxZoom: 4
});

var server = window.location.href;
var matrices = fetchMatrices();

var bounds = get_bounds()
var size = [bounds[1][0] - bounds[0][0], bounds[1][1] - bounds[0][1]]
var image = L.imageOverlay(server + 'map', bounds).addTo(map);
map.fitBounds(bounds);
var group = L.layerGroup([])
group.addTo(map);
var markers = {}

function getMatrix(stage) {
	var matrix = matrices[stage]
	if (matrix === undefined) {
		return [[0,0,0],[0,0,0],[0,0,0]];
	}
	return matrix;
}

async function fetchData() {
	var response = await fetch(server + 'info.json')
	if (response.ok) {
		var json = await response.json()
		var json = json.Players

		var new_markers = {}
		for (playerIndex in json) {
			var player = json[playerIndex]
			var name = player.Name;
			var pos = player.Position;
			var stage = player.Stage
			if (stage == undefined || !stage.includes("Home")){
				var marker = markers[name];
				if (marker !== undefined){
					marker.remove();
					delete markers[name];
				}
				continue;
			}


			last_pos = [pos.X, pos.Z];
			var pos = from_game([pos.X, pos.Z], stage);

			marker = markers[name]
			if (marker == undefined){
				marker = L.marker(pos,
								  {'title': name})
					.addTo(group)
					.bindPopup(name);
			}  else {
				marker.setLatLng(pos);
			}

			delete markers[name];

			new_markers[name] = marker;

		}

		for (var name in markers) {
			markers[name].remove();
		}

		markers = new_markers;
	}
}

setInterval(fetchData, 100);
// fetchData()

function get_bounds() {
	return [[0, 0], [2048, 2048]]
}

async function fetchMatrices() {
	var response = await fetch(server + 'view')
	if (response.ok) {
		var json = await response.json()
		matrices = json
	}
}

function from_game(point, stage) {
	var matrix = getMatrix(stage)

	var out_x = matrix[0][0] * point[0] + matrix[0][1] * point[1] + matrix[0][2]
	var out_y = matrix[1][0] * point[0] + matrix[1][1] * point[1] + matrix[1][2]

	return to_map_pos([out_x, out_y])

}

var gpts = [];
var mpts = [];
var last_pos = null;

function recpt(x,y) {
	mpts.push([x,y])
	gpts.push(last_pos)
}

function prpt() {
	console.log(JSON.stringify(gpts));
	console.log(JSON.stringify(mpts));
	gpts = []
	mpts = []
}
