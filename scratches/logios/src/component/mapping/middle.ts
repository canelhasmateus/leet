import type { TextEdge, TextMultiTree, TextNode } from "../text/elements";
import type { EdgeConfig, GraphData, NodeConfig } from "@antv/g6";
import { INode } from "@antv/g6-core/lib/interface/item";

export function textNodeToGraphNode( node: TextNode ): NodeConfig {

	return {
		id:    node.id,
		label: node.content,
		data:  {
			content: node.content
		}

	}

}

export function textEdgeToGraphEdge( edge: TextEdge ): EdgeConfig {
	return {
		source: edge.fromNodeId,
		target: edge.toNodeId
	}
}

export function textTreeToGraphData( textTree: TextMultiTree ): GraphData {
	return {
		nodes: textTree.nodes.map( textNodeToGraphNode ),
		edges: textTree.edges.map( textEdgeToGraphEdge ),
	};
}




export function safely( thunk ) {

	try {

		return thunk();

	} catch ( e ) {

		alert( e );
		return null;

	}

}