<div bind:this={canvasContainer}>
</div>


<script lang="ts">

	import { onMount } from "svelte";
	import type { GraphData, IGraph } from "@antv/g6";
	import { createFakeData, createG6Graph } from "./graph";

	let canvasContainer
	export let componentGraph: IGraph
	export let setData: ( graph: GraphData ) => any = ( graph: GraphData ) => {
		componentGraph.data( graph )
		componentGraph.render()
	}
	export let getData: () => GraphData             = () => {

		return {
			nodes: componentGraph.getNodes().map( node => node.getModel() ),
			edges: componentGraph.getEdges().map( edge => edge.getModel() )
		}
	}

	onMount( () => {
		componentGraph = componentGraph ? componentGraph
										: createG6Graph( canvasContainer )

		componentGraph.data( createFakeData( 10 ) )
		componentGraph.render()
	} )


</script>


<style>
	div {
		height: 100%;
		width: 100%;
	}

</style>