class Solution {

    public static final String reverse( String  s ) {
        return new StringBuilder( s ).reverse().toString();
    }

    public static final boolean isPalidrome(String s) {
        return s.equals( reverse( s) );
    }

    public static void main( String[] args ) {



        assert isPalidrome(  "aba" );

    }
}