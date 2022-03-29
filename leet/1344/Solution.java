class Solution {

    public static final < T > void compare( T actual, T expected ) {

        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public double angleClock( int hour, int minutes ) {

        return sangleClock( hour, minutes );
    }

    public static double sangleClock( int hour, int minutes ) {


        double fHour    = ( double ) minutes / 60;
        double hDelta   = 5 * fHour;
        double hBase    = 5 * ( hour % 12 );
        double hPointer = hBase + hDelta;


        double angle = Math.abs( hPointer - minutes ) * 6;

        if ( angle > 180 ) {
            return 360 - angle;
        }

        return angle;


    }

    public static void main( String[] args ) {
        compare( sangleClock( 12, 30 ), 165D );
    }
}