import { createTextEdge, createTextNode, parseTextMultiTree } from "./text";

describe( "Functionality Tests", () => {


	test( "Aligned blocks dont create edges", () => {

		const text = `
		Animal
		Minerals
		`

		const tree = parseTextMultiTree( text )

		const expectedNodes = [ createTextNode( "Animal" ), createTextNode( "Minerals" ) ],
			  expectedEdges = []

		const expectedTree = {
			nodes: expectedNodes.map( removeLevel ),
			edges: expectedEdges
		}

		expect( isSubset( tree, expectedTree ) ).toBe( true )

	} )

	test( "Idented blocks create edges", () => {

		const text = `
		 Animal
			 Vertebrate
			 Invertebrate
		 `

		const tree = parseTextMultiTree( text )

		const animalNode       = createTextNode( "Animal" ),
			  vertebrateNode   = createTextNode( "Vertebrate" ),
			  invertebrateNode = createTextNode( "Invertebrate" ),
			  expectedNodes    = [ animalNode, vertebrateNode, invertebrateNode ],
			  expectedEdges    = [ createTextEdge( vertebrateNode, animalNode ),
								   createTextEdge( invertebrateNode, animalNode ) ],
			  expectedTree     = {
				  nodes: expectedNodes.map( removeLevel ),
				  edges: expectedEdges
			  }


		expect( isSubset( tree, expectedTree ) ).toBe( true )

	} )

	test( "Single dedent creates a branch", () => {

		const text = `
		 Animal
			 Vertebrate
				 Mammal
			 Invertebrate
		 `

		const tree = parseTextMultiTree( text )

		const animalNode       = createTextNode( "Animal" ),
			  vertebrateNode   = createTextNode( "Vertebrate" ),
			  mammalNode       = createTextNode( "Mammal" ),
			  invertebrateNode = createTextNode( "Invertebrate" ),
			  expectedNodes    = [ animalNode, vertebrateNode, mammalNode, invertebrateNode ],
			  expectedEdges    = [ createTextEdge( vertebrateNode, animalNode ),
								   createTextEdge( mammalNode, vertebrateNode ),
								   createTextEdge( invertebrateNode, animalNode ) ]

		const expectedTree = {
			nodes: expectedNodes.map( removeLevel ),
			edges: expectedEdges
		}

		expect( isSubset( tree, expectedTree ) ).toBe( true )


	} )

	test( "Double dedent creates a branch", () => {

		const text = `
		 Animal
			 Vertebrate
				 Mammal
					 Human
			 Invertebrate
		 `

		const tree = parseTextMultiTree( text )

		const animalNode       = createTextNode( "Animal" ),
			  vertebrateNode   = createTextNode( "Vertebrate" ),
			  mammalNode       = createTextNode( "Mammal" ),
			  humanNode        = createTextNode( "Human" ),
			  invertebrateNode = createTextNode( "Invertebrate" ),
			  expectedNodes    = [ animalNode, vertebrateNode, mammalNode, humanNode, invertebrateNode ],
			  expectedEdges    = [ createTextEdge( vertebrateNode, animalNode ),
								   createTextEdge( mammalNode, vertebrateNode ),
								   createTextEdge( humanNode, mammalNode ),
								   createTextEdge( invertebrateNode, animalNode ) ]


		const expectedTree = {
			nodes: expectedNodes.map( removeLevel ),
			edges: expectedEdges
		}

		expect( isSubset( tree, expectedTree ) ).toBe( true )

	} )

	test( "Carriage return doesn't change anything", () => {

		const text         = `Animal\n\tVertebrate\n\tInvertebrate`
		const carriageText = `Animal\n\tVertebrate\n\r\tInvertebrate`

		const tree         = parseTextMultiTree( text )
		const carriageTree = parseTextMultiTree( carriageText )


		expect( tree ).toEqual( carriageTree );

	} )


} )


describe( "Regression Tests", () => {


	test( "Input should create second root", () => {


			  let text = `
			  Human\n
			  \tMammal\n
			  \t\tAnimal\n
			  \t\t\tVertebrate\n
			  aksldalksdj`


			  const tree = parseTextMultiTree( text )

			  const humanNode      = createTextNode( "Human" ),
					mammalNode     = createTextNode( "Mammal" ),
					animalNode     = createTextNode( "Animal" ),
					vertebrateNode = createTextNode( "Vertebrate" ),
					lastNode       = createTextNode( "aksldalksdj" ),
					expectedNodes  = [ humanNode, mammalNode, animalNode, vertebrateNode, lastNode ],
					expectedEdges  = [ createTextEdge( mammalNode, humanNode ),
									   createTextEdge( animalNode, mammalNode ),
									   createTextEdge( vertebrateNode, animalNode ) ]


			  const expectedTree = {
				  nodes: expectedNodes.map( removeLevel ),
				  edges: expectedEdges
			  }

			  expect( isSubset( tree, expectedTree ) ).toBe( true )

		  }
	)


} )


function isSubset( superObj, subObj ) {
	return Object.keys( subObj ).every( subKey => {
		const subEntry   = subObj[ subKey ];
		const superEntry = superObj[ subKey ];
		const objKind    = typeof subEntry

		if ( objKind == 'object' ) {
			return isSubset( superEntry, subEntry );
		}

		return subEntry === superEntry
	} );
}

function removeLevel( obj ) {
	delete obj.level
	return obj
}
