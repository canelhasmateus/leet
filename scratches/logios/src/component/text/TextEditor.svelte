<div>
	<button bind:this={button} on:click={ handleClick }>GraphIt</button>
	<textarea bind:this={ textBox } on:keydown={ handleTextKeyDown }></textarea>
</div>

<script lang="ts">

	import type { KeyboardComposite, TextComposite } from "./elements";
	import { createEventDispatcher } from "svelte";

	let textBox: HTMLTextAreaElement
	let button: HTMLButtonElement
	const dispatch = createEventDispatcher();

	export var clickConsumer: ( composite: TextComposite ) => void       = ( textComposite: TextComposite ) => {
	}
	export var keydownConsumer: ( composite: KeyboardComposite ) => void = ( keyboardComposite: KeyboardComposite ) => {

		let event: KeyboardEvent = keyboardComposite.keyboardEvent

		if ( event.key == "Tab" ) {
			textBox.value += "\t"
			event.preventDefault()

		}

		if ( event.key == "Enter" && event.ctrlKey ) {
			button.click()
			event.preventDefault()
		}


	}

	function handleClick( event: PointerEvent ): void {
		dispatch( "graphIt", {
			buttonElement: button,
			textElement:   textBox,
			pointerEvent:  event
		} )


	}

	function handleTextKeyDown( event: KeyboardEvent ) {


		keydownConsumer( {
							 buttonElement: button,
							 textElement:   textBox,
							 keyboardEvent: event
						 } )

	}


</script>

<style>
	textarea {
		width: 100%;
		height: 100%;
		box-sizing: border-box;
	}

	button {
		width: 100%;
	}

	div {
		height: 100%;
		width: 100%;
	}
</style>