<div>
	<form action="">
		{#each fields as field  }
			<label for="{field}"> {field} </label>
			<input type="text" id="{field}" placeholder={field} bind:value={ values[field] }>
		{/each}
		<input type="submit" value="OK" on:click|preventDefault={ handleSubmit }>
	</form>
</div>

<script>

	import { loadObject, PersistenceKey, writeObject } from "../persistence/persistence";
	import { createEventDispatcher, onMount } from "svelte";

	const dispatch = createEventDispatcher();
	let values = {}
	let fields = [ "owner", "repo", "branch", "token" ];

	onMount( () => {
		values = loadObject( PersistenceKey.GITHUB )
	} )

	function handleSubmit ( e ) {
		writeObject( PersistenceKey.GITHUB, values )
		dispatch( "submit" )
	}

</script>


<style>

	label {
		width: 20%;
		display: inline-block;
	}

	input {
		width: 100%
	}

	input[type=submit] {
		margin-left: 33%;
		margin-right: 33%;
		width: 33%;
		background-color: #00f;
		color: #fff
	}
</style>