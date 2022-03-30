class Solution {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }


    public long kthSmallestProduct( int[] nums1, int[] nums2, long k ) {

        return skthSmallestProduct( nums1, nums2, k );
    }

    public static long skthSmallestProduct( int[] nums1, int[] nums2, long k ) {

        return 0;
    }

    public static void main( String[] args ) {

        int[] a = { 2, 5 };
        int[] b = { 3, 4 };
        long  k = 2;

        compare( skthSmallestProduct( a, b, k ), 8 );

    }
}