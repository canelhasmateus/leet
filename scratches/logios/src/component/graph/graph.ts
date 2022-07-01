import G6, { GraphData, GraphOptions, IGraph, Item } from '@antv/g6'

let currentMode = "default"

const defaultMode = {
	default: [ 'drag-canvas', "zoom-canvas",
			   'edge-tooltip', 'brush-select',
			   'tooltip', 'click-select', 'drag-node',
	],
	edit:    [ "zoom-canvas", {
		type:       'create-edge',
		trigger:    'drag',
		edgeConfig: {
			type:  'line',
			style: {
				stroke:    "#f00",
				lineWidth: 5
			}

		}
	},

	],

}

export function createG6Graph( container: HTMLElement ): IGraph {

	const graphConfig: GraphOptions = {
		container:    container,
		height:       container.clientHeight,
		width:        container.clientWidth,
		enabledStack: true,
		modes:        defaultMode,
		layout:       {
			gpuEnabled:     false,
			type:           'force',
			preventOverlap: true,

		},
		defaultEdge:  {
			style: {
				endArrow: true
			}

		}

	};
	const graph: IGraph             = new G6.Graph( graphConfig );

	graph.on( 'keydown', ( evt: KeyboardEvent ) => {
		console.log( evt );
		let done = false

		if ( evt.key == 'Escape' ) {
			// if
		}
		if ( evt.key == 'q' && evt.altKey ) {
			done        = true
			currentMode = "default"
			graph.layout()
		}
		if ( evt.key == 'a' && evt.altKey ) {
			done        = true
			currentMode = "view"
			graph.layout()
		}

		if ( evt.key == 'w' && evt.altKey ) {
			done        = true
			currentMode = "edit"
		}

		if ( done ) {
			evt.stopPropagation()
			console.log( `entering ${ currentMode } mode` );

			graph.setMode( currentMode )
		}
	} )
	graph.on( 'canvas:click', ( evt ) => {
		if ( currentMode == "edit" ) {

			const item: Item = evt.item;
			const point      = graph.getPointByClient( evt.clientX, evt.clientY );
			let id           = Math.random().toString()
			graph.addItem( "node", { id: id, x: point.x, y: point.y } )
		}
	} )

	return graph

}


export function createFakeData( n: number ): GraphData {

	let ids   = [ ...Array( n ).keys() ].map( ( i ) => i.toString() )
	let nodes = ids.map( id => ( { id: id, label: id } ) )
	let edges = ids.map( id => {
		let target = Math.round( Math.random() * ( parseInt( id ) ) )
		return {
			source: id,
			target: target.toString()
		}
	} ).filter( edge => edge.source != edge.target )

	return {
		nodes: nodes,
		edges: edges
	}


}




