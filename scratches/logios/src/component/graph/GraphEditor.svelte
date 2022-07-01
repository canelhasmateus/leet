<div id="holder">
	<GraphCanvas
			id="canvas"
			bind:setData={setData}
			bind:getData={getData}/>

	<TextEditor on:graphIt={ ( data ) => handleTextParsing( data  ) } id="editor"></TextEditor>
</div>

<script lang="ts">


	import { createEventDispatcher, onMount } from "svelte";
	import { TextComposite } from "../text/elements.d.ts";
	import { parseTextMultiTree } from "../text/text";
	import { safely, textTreeToGraphData } from "../mapping/middle";
	import GraphCanvas from "./GraphCanvas.svelte";
	import TextEditor from "../text/TextEditor.svelte";
	import { createFakeData } from "./graph";
	import { toGithub } from "../persistence/persistence";
	import GithubPopup from "../config/GithubPopup.svelte";

	export let setData
	export let getData

	const dispatch = createEventDispatcher();

	onMount( () => {
	} )

	function handleTextParsing( event: CustomEvent<TextComposite> ) {

		let composite = event.detail
		let textTree  = parseTextMultiTree( composite.textElement.value )
		let graphData = textTreeToGraphData( textTree )

		setData( graphData )

	}

</script>
<style>
	#holder {
		display: flex;
		height: 100%;
	}

	#canvas {
		height: 100%;
		width: 100%;
	}

</style>