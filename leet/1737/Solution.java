class Solution {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public int minCharacters(String a, String b) {
        
    }

    public static void main( String[] args ) {

        compare(  );

    }
}