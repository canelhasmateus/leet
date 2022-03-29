import java.util.*;

class Solution {
    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public List< Integer > findDuplicates( int[] nums ) {
        return sfindDuplicates( nums );
    }

    public static List< Integer > sfindDuplicates( int[] nums ) {


        List< Integer > result = new ArrayList<>();
        Set< Integer >  seen   = new HashSet<>();
        for ( int num : nums ) {
            boolean novel = seen.add( num );
            if ( !novel ) {
                result.add( num );
            }
        }

        return result;
    }


    public static void main( String[] args ) {

        int[] a   = { 4, 3, 2, 7, 8, 2, 3, 1 };
        int[] res = { 2, 3 };
        compare( sfindDuplicates( a ), Arrays.stream( res ).boxed().toList() );

    }

}