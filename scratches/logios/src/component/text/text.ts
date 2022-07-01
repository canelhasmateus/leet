import { MD5 } from "./md5";
import type { Optional, TextEdge, TextMultiTree, TextNode } from "./elements";


export function createTextEdge( from: TextNode, to: TextNode ): TextEdge {
	return {
		fromNodeId: from.id,
		toNodeId:   to.id,
	}
}

export function createTextNode( textlet: string ): TextNode {

	const level: number = scoreTextlet( textlet ),
		  content       = normalize( textlet )

	// todo
	return {
		content: content,
		id:      contentHash( content ),
		level:   level
	}

}

export function parseTextMultiTree( text: string ): TextMultiTree {

	const allNodes  = [],
		  allEdges  = [],
		  rootStack = []

	const constituents = text.split( "\n" ).filter( notEmptyLike )
	for ( const textlet of constituents ) {

		const currentNode: TextNode = createTextNode( textlet )
		allNodes.push( currentNode )


		let currentRoot = head( rootStack )
		if ( currentRoot == null ) {
			rootStack.push( currentNode )
			continue
		}

		if ( currentNode.level > currentRoot.level ) {
			allEdges.push( createTextEdge( currentNode, currentRoot ) )
			rootStack.push( currentNode )
			continue
		}


		while ( currentRoot && currentNode.level <= currentRoot.level ) {
			currentRoot = unwind( rootStack )
		}

		if ( currentRoot != null ) {
			allEdges.push( createTextEdge( currentNode, currentRoot ) )
		}
		rootStack.push( currentNode )
	}

	return {
		nodes: allNodes,
		edges: allEdges
	}
}

type Hash = string
type Refined<T> = T

const scoreMapping: Map<string, number> = new Map<string, number>()
scoreMapping[ " " ]                     = 1
scoreMapping[ "\t" ]                    = 4
scoreMapping[ "\r" ]                    = 0

//region stack
function head<T>( stack: Array<T> ): Optional<T> {

	if ( stack.length == 0 ) {
		return null
	}

	return stack[ stack.length - 1 ]

}

function unwind<T>( stack: Array<T> ): Optional<T> {

	stack.pop()
	return head( stack )

}

//endregion

function contentHash( content: string ): Hash {

	return MD5( normalize( content ) )
}

function scoreTextlet( textlet: string ): number {
	let totalScore = 0
	for ( const character of textlet ) {

		const characterScore = scoreMapping[ character ]

		if ( characterScore === undefined ) {
			return totalScore
		}

		totalScore += characterScore

	}
	return totalScore

}

function normalize( textlet: string ): Refined<string> {

	return textlet.trim().toLowerCase()

}

function notEmptyLike( textlet: string ): boolean {

	return textlet.trim() != ""
}




