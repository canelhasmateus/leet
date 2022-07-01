export interface TextComposite {
	buttonElement: HTMLButtonElement,
	textElement: HTMLTextAreaElement,
	pointerEvent: PointerEvent
}

export interface KeyboardComposite {
	buttonElement: HTMLButtonElement,
	textElement: HTMLTextAreaElement,
	keyboardEvent: KeyboardEvent

}

type Optional<T> = T | null | undefined

export interface TextNode {

	id: Hash
	content: string
	level: number

}

export interface TextEdge {

	fromNodeId: string
	toNodeId: string

}

export interface TextMultiTree {

	nodes: Array<TextNode>
	edges: Array<TextEdge>

}

