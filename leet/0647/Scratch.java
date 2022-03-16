import java.io.Serializable;
import java.util.Arrays;
import java.util.List;

class Scratch {

    public static final < T > void compare( T actual, T expected ) {


        if ( !expected.equals( actual ) ) {

            throw new RuntimeException( "Error!\nexpected:\n\t\t" +
                                        expected +
                                        "\ngotten:\n\t\t" +
                                        actual );

        }
    }

    public static final String reverse( String s ) {
        return new StringBuilder( s ).reverse().toString();
    }

    public static final boolean isPalidrome( String s ) {
        return s.equals( reverse( s ) );
    }

    public static final List< String > palidromicSubstring( String s ) {
        return Arrays.stream( s.split( "" ) ).toList();
    }

    public static void main( String[] args ) {

        compare( palidromicSubstring( "abc" ),
                 List.of( "a", "b", "c" )
               );



    }
}