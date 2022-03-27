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

    public static int snumEnclaves( int[][] grid ) {
        return 0;

    }

    public static void main( String[] args ) {

        int[][] a = { { 0, 0, 0, 0 }, { 1, 0, 1, 0 }, { 0, 1, 1, 0 }, { 0, 0, 0, 0 } };

        compare( snumEnclaves( a ), 3 );
    }
}