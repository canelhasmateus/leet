def solution( operations ):
	editor = ""
	return editor
	cursor = 0
	selected = None
	curOp = 0
	remove = [ ]
	for i, op in enumerate( operations ):
		if op.startswith( "UNDO" ):
			while True:
				inc = 1
				if i - inc in remove:
					inc += 1
					continue

				if not 0 <= i - inc < len( operations ):
					break

				if operations[ i - inc ].startswith( "SELECT" ):
					break

				remove.append( i - inc )

	while curOp < len( operations):
		if curOp in remove:
			continue

		operation = operations[ curOp ]

		#

		kind, value = operation.split( " ", 2 )

		if kind == "TEXT" and len( value ) <= 20:
			if selected:
				start, end = selected
				editor[ :start ] + value + editor[ end + 1: ]
				cursor = start + len( value )
			else:
				editor = editor[ :cursor ] + value + editor[ cursor: ]
				cursor += len( value )

		if kind == "MOVE_CURSOR":

			offset = int( value )
			new_pos = max( 0, min( cursor + offset, len( editor ) ) )
			if new_pos == cursor:
				...
		if kind == "SELECT":

			start, end = value.split()
			selected = (start, end + 1)
			cursor = end

			nkind, nvalue = operation.split( " ", 2 )
			if nkind != "TYPE":
				selected = None

		#
		curOp += 1

	return editor


if __name__ == '__main__':
	import unittest


	class TestSolution( unittest.TestCase ):

		def test1( self ):
			operations = [ "TYPE Code", "TYPE Signal", "MOVE_CURSOR -3",
			               "SELECT 5 8", "TYPE ou", "UNDO", "TYPE nio" ],

			self.assertEquals( solution( operations ), "CodeSignaliol" )


	unittest.main()
