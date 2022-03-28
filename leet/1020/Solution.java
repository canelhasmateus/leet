class Solution {


    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public int numEnclaves( int[][] grid ) {
        return snumEnclaves( grid );
    }

    public static void depthFirst( int row, int col, int[][] grid ) {

        //region Edge Checking
        if ( row < 0 || row >= grid.length ) {
            return;
        }

        if ( col < 0 || col >= grid[ 0 ].length ) {
            return;
        }

        //endregion

        // region Action

        grid[ row ][ col ] = 0;

        // endregion

        //region recurse
        depthFirst( row - 1, col, grid );
        depthFirst( row + 1, col, grid );
        depthFirst( row, col - 1, grid );
        depthFirst( row, col + 1, grid );
        //endregion

    }

    public static int snumEnclaves( int[][] grid ) {


//        we need to find the numer of 1 that are not 4-directionally connect to the boundaries.
//        so, we can  find the number of ones, and them subtract the number of ones that ARE connect to the boundaries
//        , by working backwards from the bondaries.
//         A tricky point is to avoid double counting: depending on the way we'll sample the grid, we'll double count entries that are connected
//        to more than one boundary. To avoid doing it like this, we can in-place mutate our input to use it as bookkeeping.


        // Iterate Edges
        int maxRow = grid.length;
        int maxCol = grid[ 0 ].length;
        for ( int row = 0; row < maxRow; row++ ) {
            for ( int col = 0; col < maxCol; col++ ) {
                if ( row == 0 || row == maxRow - 1 ||
                     col == 0 || col == maxCol - 1 ) {
                    depthFirst( row, col, grid );
                }
            }
        }

        int n = 0;
        for ( int[] ints : grid ) {
            for ( int anInt : ints ) {
                n += anInt;
            }
        }

        return n;
    }

    public static void main( String[] args ) {

        int[][] a = { { 0, 0, 0, 0 }, { 1, 0, 1, 0 }, { 0, 1, 1, 0 }, { 0, 0, 0, 0 } };
        int[][] b = { { 0, 1, 1, 0 }, { 0, 0, 1, 0 }, { 0, 0, 1, 0 }, { 0, 0, 0, 0 } };

        compare( snumEnclaves( a ), 3 );
        compare( snumEnclaves( b ), 0 );

    }
}