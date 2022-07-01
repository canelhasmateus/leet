<h1>Logios</h1>

<input type="image" height="100px" width="100px" title="edit" src="assets/gear.png" alt="config" on:click={ () => showPopup()}/>


{#if doShowPopup}
	<GithubPopup on:submit={() => doShowPopup = false}>
	</GithubPopup>
{/if}

<input type="image" title="save" src="assets/pencil.png" alt="save" on:click={ () => handleSave()}/>
<input type="image" title="load" src="assets/pencil.png" alt="save" on:click={ () => handleLoad()}/>

<GraphEditor bind:setData={ saveGraph } bind:getData={getGraph}>
</GraphEditor>

<script lang="ts">

	import GraphEditor from "./component/graph/GraphEditor.svelte";
	import GithubPopup from "./component/config/GithubPopup.svelte";
	import { fromGithub, getGithubAuth, loadObject, PersistenceKey, toGithub } from "./component/persistence/persistence";

	let doShowPopup = false;

	let saveGraph;
	let getGraph

	function log( rest ) {
		console.log( rest );
		return rest
	}

	function showPopup() {
		doShowPopup = !doShowPopup
		// console.log( "showPopup" );
	}

	function handleSave() {
		let auth = getGithubAuth()
		let data = JSON.stringify( getGraph(), null, 2 )
		console.log( data );
		toGithub( {
					  auth:    auth,
					  message: "Logios Update",
					  files:   [ { path: "graph.json", contents: data } ]
				  } )
				.then( _ => alert( "saved!" ) )

	}

	function handleLoad() {
		let auth     = getGithubAuth()
		let response = fromGithub( auth )

		alert( response )
		response.then( log )
				.then( massageResponse )
				.then( log )
				.then( JSON.parse )
				.then( log )
				.then( saveGraph )
		alert( "Loaded!" )
	}

	function massageResponse( response ) {

		return response.filter( obj => obj.name == "graph.json" )
				.map( obj => obj.content )[ 0 ]


	}
</script>


<style>

</style>

